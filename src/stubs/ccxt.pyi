# Copyright 2022 macanudo527
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from typing import Any, Dict, List, Optional, Union

class ccxt:
    def __init__(self, config: Dict[str, str]) -> None: ...

class Exchange:
    def fetch_deposits(  # type: ignore
        self, code: Optional[str] = ..., since: Optional[int] = ..., limit: Optional[int] = ..., params: Optional[Dict[str, Union[int, str, None]]] = ...
    ) -> Any: ...
    def fetch_markets(self, params: Optional[Dict[str, Union[int, str, None]]] = ...) -> Any: ...  # type: ignore
    def fetch_my_dust_trades(  # type: ignore
        self, symbol: Optional[str] = ..., since: Optional[int] = ..., limit: Optional[int] = ..., params: Optional[Dict[str, Union[int, str, None]]] = ...
    ) -> Any: ...
    def fetch_my_trades(  # type: ignore
        self, symbol: Optional[str] = ..., since: Optional[int] = ..., limit: Optional[int] = ..., params: Optional[Dict[str, Union[int, str, None]]] = ...
    ) -> Any: ...
    def fetch_withdrawals(  # type: ignore
        self, symbol: Optional[str] = ..., since: Optional[int] = ..., limit: Optional[int] = ..., params: Optional[Dict[str, Union[int, str, None]]] = ...
    ) -> Any: ...

class binance(Exchange):
    def __init__(self, config: Dict[str, str]) -> None: ...
    options: Dict[str, str]
    def sapiGetAssetAssetDividend(self, params: Dict[str, Union[int, str, None]] = ...) -> Any: ...  # type: ignore
    def sapiGetFiatOrders(self, params: Dict[str, Union[int, str, None]] = ...) -> Any: ...  # type: ignore
    def sapiGetFiatPayments(self, params: Dict[str, Union[int, str, None]] = ...) -> Any: ...  # type: ignore
    def sapiGetMiningPaymentList(self, params: Dict[str, Union[int, str, None]] = ...) -> Any: ...  # type: ignore
    def sapiGetMiningPubAlgoList(self, params: Dict[str, Union[int, str, None]] = ...) -> Any: ...  # type: ignore

class coinbase(Exchange):
    def __init__(self, config: Dict[str, str]) -> None: ...

class coinbasepro(Exchange):
    def __init__(self, config: Dict[str, str]) -> None: ...
