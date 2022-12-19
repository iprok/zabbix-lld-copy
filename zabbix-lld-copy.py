#!/usr/bin/python3
from zabbix_api import ZabbixAPI, ZabbixAPIException

server="https://zabbix.example.com"
api_token="123....aaa890"

params={
        "discoveryids": [
            "224582"
        ],

        "hostids": [
            "11438"
        ]     
    }

zapi = ZabbixAPI(server)

try:
    zapi.login(api_token=api_token)
except ZabbixAPIException as e:
    sys.stderr.write(str(e) + '\n')

try:
    print(zapi.discoveryrule.copy(params))
except ZabbixAPIException as e:
    sys.stderr.write(str(e) + '\n')
