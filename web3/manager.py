import logging
from typing import (  # noqa: F401
    TYPE_CHECKING,
    Any,
    Callable,
    Dict,
    List,
    NoReturn,
    Optional,
    Sequence,
    Tuple,
    Union,
    cast,
)

from eth_utils.toolz import (
    pipe,
)
from hexbytes import (
    HexBytes,
)

from web3._utils.threads import (  # noqa: F401
    ThreadWithReturn,
)
from web3.datastructures import (
    NamedElementOnion,
)
from web3.exceptions import (
    BadResponseFormat,
    MethodUnavailable,
)
from web3.middleware import (
    abi_middleware,
    async_attrdict_middleware,
    async_buffered_gas_estimate_middleware,
    async_gas_price_strategy_middleware,
    async_validation_middleware,
    attrdict_middleware,
    buffered_gas_estimate_middleware,
    gas_price_strategy_middleware,
    name_to_address_middleware,
    pythonic_middleware,
    request_parameter_normalizer,
    validation_middleware,
)
from web3.providers import (
    AutoProvider,
)
from web3.types import (  # noqa: F401
    AsyncMiddleware,
    Middleware,
    MiddlewareOnion,
    RPCEndpoint,
    RPCResponse,
)

if TYPE_CHECKING:
    from web3 import Web3  # noqa: F401
    from web3.providers import (  # noqa: F401
        AsyncBaseProvider,
        BaseProvider,
    )


NULL_RESPONSES = [None, HexBytes("0x"), "0x"]


def apply_error_formatters(
    error_formatters: Callable[..., Any],
    response: RPCResponse,
) -> RPCResponse:
    if error_formatters:
        formatted_resp = pipe(response, error_formatters)
        return formatted_resp
    else:
        return response


def apply_null_result_formatters(
    null_result_formatters: Callable[..., Any],
    response: RPCResponse,
    params: Optional[Any] = None,
) -> RPCResponse:
    if null_result_formatters:
        formatted_resp = pipe(params, null_result_formatters)
        return formatted_resp
    else:
        return response


class RequestManager:
    logger = logging.getLogger("web3.RequestManager")

    def __init__(
        self,
        w3: "Web3",
        provider: Optional[Union["BaseProvider", "AsyncBaseProvider"]] = None,
        middlewares: Optional[Sequence[Tuple[Middleware, str]]] = None,
    ) -> None:
        self.w3 = w3

        if provider is None:
            self.provider = AutoProvider()
        else:
            self.provider = provider

        if middlewares is None:
            middlewares = (
                self.async_default_middlewares()
                if self.provider.is_async
                else self.default_middlewares(w3)
            )

        self.middleware_onion: MiddlewareOnion = NamedElementOnion(middlewares)

    w3: "Web3" = None
    _provider = None

    @property
    def provider(self) -> Union["BaseProvider", "AsyncBaseProvider"]:
        return self._provider

    @provider.setter
    def provider(self, provider: Union["BaseProvider", "AsyncBaseProvider"]) -> None:
        self._provider = provider

    @staticmethod
    def default_middlewares(w3: "Web3") -> List[Tuple[Middleware, str]]:
        """
        List the default middlewares for the request manager.
        Leaving ens unspecified will prevent the middleware from resolving names.
        """
        return [
            (request_parameter_normalizer, "request_param_normalizer"),  # Delete
            (gas_price_strategy_middleware, "gas_price_strategy"),
            (name_to_address_middleware(w3), "name_to_address"),  # Add Async
            (attrdict_middleware, "attrdict"),
            (pythonic_middleware, "pythonic"),  # Delete
            (validation_middleware, "validation"),
            (abi_middleware, "abi"),  # Delete
            (buffered_gas_estimate_middleware, "gas_estimate"),
        ]

    @staticmethod
    def async_default_middlewares() -> List[Tuple[Middleware, str]]:
        """
        List the default async middlewares for the request manager.
        """
        return [
            (async_gas_price_strategy_middleware, "gas_price_strategy"),
            (async_attrdict_middleware, "attrdict"),
            (async_validation_middleware, "validation"),
            (async_buffered_gas_estimate_middleware, "gas_estimate"),
        ]

    #
    # Provider requests and response
    #
    def _make_request(
        self, method: Union[RPCEndpoint, Callable[..., RPCEndpoint]], params: Any
    ) -> RPCResponse:
        provider = cast("BaseProvider", self.provider)
        request_func = provider.request_func(self.w3, self.middleware_onion)
        self.logger.debug(f"Making request. Method: {method}")
        return request_func(method, params)

    async def _coro_make_request(
        self, method: Union[RPCEndpoint, Callable[..., RPCEndpoint]], params: Any
    ) -> RPCResponse:
        # type ignored b/c request_func is an awaitable in async model
        request_func = await self.provider.request_func(  # type: ignore
            self.w3, self.middleware_onion
        )
        self.logger.debug(f"Making request. Method: {method}")
        return await request_func(method, params)

    @staticmethod
    def formatted_response(
        response: RPCResponse,
        params: Any,
        error_formatters: Optional[Callable[..., Any]] = None,
        null_result_formatters: Optional[Callable[..., Any]] = None,
    ) -> Any:
        if "error" in response:
            apply_error_formatters(error_formatters, response)

            # guard against eth-tester case - eth-tester returns a string
            # with no code, so can't parse what the error is.
            if isinstance(response["error"], dict):
                resp_code = response["error"].get("code")
                if resp_code == -32601:
                    raise MethodUnavailable(response["error"])
            raise ValueError(response["error"])
        # NULL_RESPONSES includes None, so return False here as the default
        # so we don't apply the null_result_formatters if there is no 'result' key
        elif response.get("result", False) in NULL_RESPONSES:
            # null_result_formatters raise either a BlockNotFound
            # or a TransactionNotFound error, depending on the method called
            apply_null_result_formatters(null_result_formatters, response, params)
            return response["result"]
        elif response.get("result") is not None:
            return response["result"]
        else:
            raise BadResponseFormat(
                "The response was in an unexpected format and unable to be parsed. "
                f"The raw response is: {response}"
            )

    def request_blocking(
        self,
        method: Union[RPCEndpoint, Callable[..., RPCEndpoint]],
        params: Any,
        error_formatters: Optional[Callable[..., Any]] = None,
        null_result_formatters: Optional[Callable[..., Any]] = None,
    ) -> Any:
        """
        Make a synchronous request using the provider
        """
        response = self._make_request(method, params)
        return self.formatted_response(
            response, params, error_formatters, null_result_formatters
        )

    async def coro_request(
        self,
        method: Union[RPCEndpoint, Callable[..., RPCEndpoint]],
        params: Any,
        error_formatters: Optional[Callable[..., Any]] = None,
        null_result_formatters: Optional[Callable[..., Any]] = None,
    ) -> Any:
        """
        Couroutine for making a request using the provider
        """
        response = await self._coro_make_request(method, params)
        return self.formatted_response(
            response, params, error_formatters, null_result_formatters
        )
