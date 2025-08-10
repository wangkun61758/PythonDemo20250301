#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Author ：kw
@IDE    ：PyCharm
@Date   ：2025/4/3 23:19
=================================================='''
import pytest

from test_cases.cases_china_railwany.utils.create_url_data import export
from test_cases.cases_china_railwany.utils.get_request_data import ReadJsonFileUtils
from test_cases.cases_china_railwany.utils.send_email import SendMail
from test_cases.cases_china_railwany.utils.send_request import HttpUtils


def setup_module():
    export()


@pytest.mark.parametrize('tests_unitest', ReadJsonFileUtils.get_request_data('request_data.json')["cases"])
def test_api(case):
    interface = case["interface"]
    method = case["method"]
    expected_code = case["expected_code"]
    headers = case.get("headers")
    data = case.get("data")
    res, status_code = HttpUtils.send_request(interface, method, headers, data)
    print('\n获取到的返回值：' + str(res))
    print("返回值中的状态码：" + str(status_code))
    assert status_code == expected_code


def teardown_module():
    email = SendMail(host="smtp.163.com", port=25, user="18325961727@163.com", passwd="HVtbqZRrxFCDwNUc")
    email.send_email(From='h(18325961727@163.com)',
                     To="wk1-18210958030@163.com,wk2-13552790590@163.com,wk3-h18210958030@163.com", Subject="邮件主题",
                     Context="邮件正文", to_addrs="18210958030@163.com,13552790590@163.com,h18210958030@163.com")
