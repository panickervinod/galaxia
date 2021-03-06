# Copyright 2016 - Wipro Limited
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Helper for prometheus

from galaxia.gmiddleware.handler import client
from galaxia.common.prometheus import response_parser

import os
import datetime

query_url = "query"

headers = {
        "Accept": "application/json"
    }


def get_all_containers():
        prom_request_url = client.concatenate_url(
        os.getenv("aggregator_endpoint"), query_url)
        current_time = str(datetime.datetime.now().isoformat())+"Z"
        query = "container_last_seen"
        payload = {"query": query, "time": current_time}
        resp = client.http_request("GET", prom_request_url, headers, payload,
                                   None, None)
        names_list, _, _ = response_parser.get_names_list(resp.text)
        return names_list


def get_metrics(expression):
        prom_request_url = client.concatenate_url(
                os.getenv("aggregator_endpoint"), query_url)
        current_time = str(datetime.datetime.now().isoformat())+"Z"
        payload = {"query": expression, "time": current_time}
        resp = client.http_request("GET", prom_request_url, headers, payload,
                                   None, None)
        names_list, metrics_list, _ = response_parser.get_names_list(resp.text)
        return names_list, metrics_list


def get_containers_by_hostname():
        prom_request_url = client.concatenate_url(
        os.getenv("aggregator_endpoint"), query_url)
        current_time = str(datetime.datetime.now().isoformat())+"Z"
        query = "container_last_seen"
        payload = {"query": query, "time": current_time}
        resp = client.http_request("GET", prom_request_url, headers, payload,
                                   None, None)
        names_list, _, hosts_list = response_parser.get_names_list(resp.text)
        return names_list, hosts_list


def get_names_list():

        prom_request_url = client.concatenate_url(os.getenv
                                                  ("aggregator_endpoint"),
                                                  query_url)
        current_time = str(datetime.datetime.now().isoformat())+"Z"
        query = "node_uname_info"
        payload = {"query": query, "time": current_time}
        resp = client.http_request("GET", prom_request_url, headers,
                                   payload, None, None)
        names_list, nodename_list = response_parser.get_node_name_list(resp.text)
        return names_list, nodename_list
