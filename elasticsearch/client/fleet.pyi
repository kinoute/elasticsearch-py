#  Licensed to Elasticsearch B.V. under one or more contributor
#  license agreements. See the NOTICE file distributed with
#  this work for additional information regarding copyright
#  ownership. Elasticsearch B.V. licenses this file to you under
#  the Apache License, Version 2.0 (the "License"); you may
#  not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
# 	http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing,
#  software distributed under the License is distributed on an
#  "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
#  KIND, either express or implied.  See the License for the
#  specific language governing permissions and limitations
#  under the License.

from typing import (
    Any,
    Collection,
    Dict,
    Mapping,
    MutableMapping,
    Optional,
    Sequence,
    Tuple,
    Union,
)

from .utils import NamespacedClient

class FleetClient(NamespacedClient):
    def global_checkpoints(
        self,
        *,
        index: Any,
        checkpoints: Optional[Any] = ...,
        timeout: Optional[Any] = ...,
        wait_for_advance: Optional[bool] = ...,
        wait_for_index: Optional[bool] = ...,
        pretty: Optional[bool] = ...,
        human: Optional[bool] = ...,
        error_trace: Optional[bool] = ...,
        format: Optional[str] = ...,
        filter_path: Optional[Union[str, Collection[str]]] = ...,
        request_timeout: Optional[Union[int, float]] = ...,
        ignore: Optional[Union[int, Collection[int]]] = ...,
        opaque_id: Optional[str] = ...,
        http_auth: Optional[Union[str, Tuple[str, str]]] = ...,
        api_key: Optional[Union[str, Tuple[str, str]]] = ...,
        params: Optional[MutableMapping[str, Any]] = ...,
        headers: Optional[MutableMapping[str, str]] = ...,
    ) -> Dict[str, Any]: ...
    def msearch(
        self,
        *,
        body: Union[Sequence[Mapping[str, Any]], bytes, str],
        index: Optional[Any] = ...,
        pretty: Optional[bool] = ...,
        human: Optional[bool] = ...,
        error_trace: Optional[bool] = ...,
        format: Optional[str] = ...,
        filter_path: Optional[Union[str, Collection[str]]] = ...,
        request_timeout: Optional[Union[int, float]] = ...,
        ignore: Optional[Union[int, Collection[int]]] = ...,
        opaque_id: Optional[str] = ...,
        http_auth: Optional[Union[str, Tuple[str, str]]] = ...,
        api_key: Optional[Union[str, Tuple[str, str]]] = ...,
        params: Optional[MutableMapping[str, Any]] = ...,
        headers: Optional[MutableMapping[str, str]] = ...,
    ) -> Dict[str, Any]: ...
    def search(
        self,
        *,
        index: Any,
        body: Optional[Mapping[str, Any]] = ...,
        allow_partial_search_results: Optional[bool] = ...,
        wait_for_checkpoints: Optional[Any] = ...,
        wait_for_checkpoints_timeout: Optional[Any] = ...,
        pretty: Optional[bool] = ...,
        human: Optional[bool] = ...,
        error_trace: Optional[bool] = ...,
        format: Optional[str] = ...,
        filter_path: Optional[Union[str, Collection[str]]] = ...,
        request_timeout: Optional[Union[int, float]] = ...,
        ignore: Optional[Union[int, Collection[int]]] = ...,
        opaque_id: Optional[str] = ...,
        http_auth: Optional[Union[str, Tuple[str, str]]] = ...,
        api_key: Optional[Union[str, Tuple[str, str]]] = ...,
        params: Optional[MutableMapping[str, Any]] = ...,
        headers: Optional[MutableMapping[str, str]] = ...,
    ) -> Dict[str, Any]: ...