import requests


def get_cookiejar():
    cookie_dict = {'PHPSESSID': 'htvoegt7rgb27fadl6d22calic',
                   'SERVERID': '7349dbf5589746919266ccf2e3cd1162|1680399216|1680399216',
                   'ingress_user_id': '1680399217.479.24061.806845|d8c6d8cb6c73f72f411c4a27f7a6674a'}
    # 1、dict转成cookiejar
    # <RequestsCookieJar[<Cookie PHPSESSID=b2n58milhcv5bt9ng1sqna8j9u for gamma-vms.56.cool/>, <Cookie SERVERID=7349dbf5589746919266ccf2e3cd1162|1680398478|1680398478 for gamma-vms.56.cool/>, <Cookie ingress_user_id=1680398479.08.20538.276188|d8c6d8cb6c73f72f411c4a27f7a6674a for gamma-vms.56.cool/>]>
    cookies_jar = requests.utils.cookiejar_from_dict(cookie_dict, cookiejar=None, overwrite=True)

    print('dict转成cookiejar：' + str(cookies_jar),type(cookies_jar))

    # 2、cookiejar转成dict
    cookies_dict2 = requests.utils.dict_from_cookiejar(cookies_jar)
    print('cookiejar转成dict：' + str(cookies_dict2))#{'PHPSESSID': 'htvoegt7rgb27fadl6d22calic', 'SERVERID': '7349dbf5589746919266ccf2e3cd1162|1680399216|1680399216', 'ingress_user_id': '1680399217.479.24061.806845|d8c6d8cb6c73f72f411c4a27f7a6674a'}



get_cookiejar()


###########################################################
def get_cookie():
    cookie_dict = {'PHPSESSID': 'htvoegt7rgb27fadl6d22calic',
                   'SERVERID': '7349dbf5589746919266ccf2e3cd1162|1680399216|1680399216',
                   'ingress_user_id': '1680399217.479.24061.806845|d8c6d8cb6c73f72f411c4a27f7a6674a'}
    cookie_jars = requests.utils.cookiejar_from_dict(cookie_dict, cookiejar=None, overwrite=True)
    print(cookie_jars)
    cookie_jars2 = requests.utils.dict_from_cookiejar(cookie_jars)
    print(cookie_jars2,type(cookie_jars2))

    cookie_jars3 = requests.utils.cookiejar_from_dict(cookie_jars2)
    print(cookie_jars3)


get_cookie()


def test1():
    cookie_dict = {'PHPSESSID': 'htvoegt7rgb27fadl6d22calic',
                   'SERVERID': '7349dbf5589746919266ccf2e3cd1162|1680399216|1680399216',
                   'ingress_user_id': '1680399217.479.24061.806845|d8c6d8cb6c73f72f411c4a27f7a6674a'}
    cookie_jar = requests.utils.cookiejar_from_dict(cookie_dict)
    print(cookie_jar,'\d',type(cookie_jar))
    cookie_dict1 = requests.utils.dict_from_cookiejar(cookie_jar)
    print(cookie_dict1)


def test2():
    cookie_dict = {'PHPSESSID': 'htvoegt7rgb27fadl6d22calic',
                   'SERVERID': '7349dbf5589746919266ccf2e3cd1162|1680399216|1680399216',
                   'ingress_user_id': '1680399217.479.24061.806845|d8c6d8cb6c73f72f411c4a27f7a6674a'}
    jar = requests.utils.cookiejar_from_dict(cookie_dict)
    print(jar)

def test3():
    cookie_dict = {'PHPSESSID': 'htvoegt7rgb27fadl6d22calic',
                   'SERVERID': '7349dbf5589746919266ccf2e3cd1162|1680399216|1680399216',
                   'ingress_user_id': '1680399217.479.24061.806845|d8c6d8cb6c73f72f411c4a27f7a6674a'}
    cookie_jar=requests.utils.cookiejar_from_dict(cookie_dict)
    print(cookie_jar)
    cookie=requests.utils.dict_from_cookiejar(cookie_jar)
    print(cookie)

def test4():
    cookie_dict = {'PHPSESSID': 'htvoegt7rgb27fadl6d22calic',
                   'SERVERID': '7349dbf5589746919266ccf2e3cd1162|1680399216|1680399216',
                   'ingress_user_id': '1680399217.479.24061.806845|d8c6d8cb6c73f72f411c4a27f7a6674a'}
    cookie1=requests.utils.cookiejar_from_dict(cookie_dict)
    print(cookie1)
    cookie2=requests.utils.dict_from_cookiejar(cookie1)
    print(cookie2)

def test5():
    cookie_dict = {'PHPSESSID': 'htvoegt7rgb27fadl6d22calic',
                   'SERVERID': '7349dbf5589746919266ccf2e3cd1162|1680399216|1680399216',
                   'ingress_user_id': '1680399217.479.24061.806845|d8c6d8cb6c73f72f411c4a27f7a6674a'}
    cookie1=requests.utils.cookiejar_from_dict(cookie_dict)
    cookie2=requests.utils.dict_from_cookiejar(cookie1)

def test6():
    cookie_dict = {'PHPSESSID': 'htvoegt7rgb27fadl6d22calic',
                   'SERVERID': '7349dbf5589746919266ccf2e3cd1162|1680399216|1680399216',
                   'ingress_user_id': '1680399217.479.24061.806845|d8c6d8cb6c73f72f411c4a27f7a6674a'}
    cookie1=requests.utils.cookiejar_from_dict(cookie_dict)
    cookie2=requests.utils.dict_from_cookiejar(cookie1)

def test7():
    cookie_dict = {'PHPSESSID': 'htvoegt7rgb27fadl6d22calic',
                   'SERVERID': '7349dbf5589746919266ccf2e3cd1162|1680399216|1680399216',
                   'ingress_user_id': '1680399217.479.24061.806845|d8c6d8cb6c73f72f411c4a27f7a6674a'}
    cookie1=requests.utils.cookiejar_from_dict(cookie_dict)
    cookie2=requests.utils.dict_from_cookiejar(cookie1)

def test8():
    cookie_dict = {'PHPSESSID': 'htvoegt7rgb27fadl6d22calic',
                   'SERVERID': '7349dbf5589746919266ccf2e3cd1162|1680399216|1680399216',
                   'ingress_user_id': '1680399217.479.24061.806845|d8c6d8cb6c73f72f411c4a27f7a6674a'}
    cookie1=requests.utils.cookiejar_from_dict(cookie_dict)
    cookie2=requests.utils.dict_from_cookiejar(cookie1)

def test9():
    cookie_dict = {'PHPSESSID': 'htvoegt7rgb27fadl6d22calic',
                   'SERVERID': '7349dbf5589746919266ccf2e3cd1162|1680399216|1680399216',
                   'ingress_user_id': '1680399217.479.24061.806845|d8c6d8cb6c73f72f411c4a27f7a6674a'}
    cookie1=requests.utils.cookiejar_from_dict(cookie_dict)
    cookie2=requests.utils.dict_from_cookiejar(cookie1)

def test10():
    cookie_dict = {'PHPSESSID': 'htvoegt7rgb27fadl6d22calic',
                   'SERVERID': '7349dbf5589746919266ccf2e3cd1162|1680399216|1680399216',
                   'ingress_user_id': '1680399217.479.24061.806845|d8c6d8cb6c73f72f411c4a27f7a6674a'}
    cookie1=requests.utils.cookiejar_from_dict(cookie_dict)
    cookie2=requests.utils.dict_from_cookiejar(cookie1)

def test11():
    cookie_dict = {'PHPSESSID': 'htvoegt7rgb27fadl6d22calic',
                   'SERVERID': '7349dbf5589746919266ccf2e3cd1162|1680399216|1680399216',
                   'ingress_user_id': '1680399217.479.24061.806845|d8c6d8cb6c73f72f411c4a27f7a6674a'}
    cookie1=requests.utils.cookiejar_from_dict(cookie_dict)
    cookie2=requests.utils.dict_from_cookiejar(cookie1)

def test12():
    cookie_dict = {'PHPSESSID': 'htvoegt7rgb27fadl6d22calic',
                   'SERVERID': '7349dbf5589746919266ccf2e3cd1162|1680399216|1680399216',
                   'ingress_user_id': '1680399217.479.24061.806845|d8c6d8cb6c73f72f411c4a27f7a6674a'}
    cookie1=requests.utils.dict_from_cookiejar(cookie_dict)
    cookie2=requests.utils.dict_from_cookiejar(cookie1)
def test13():
    dict1={'name':'兰兰','性别':'male'}
    cookie1=requests.utils.cookiejar_from_dict(dict1)
    print(cookie1)
    cookie2=requests.utils.dict_from_cookiejar(cookie1)
    print(cookie2)

def test14():
    dict1={'name':'兰兰','性别':'male'}
    c1=requests.utils.cookiejar_from_dict(dict1)
    print(c1)
    c2=requests.utils.dict_from_cookiejar(c1)
    print(c2)
def test15():
    dict1 = {'name': '兰兰', '性别': 'male'}
    c1=requests.utils.cookiejar_from_dict(dict1)
    c2=requests.utils.dict_from_cookiejar(c1)
'''
练习：2025/3/20（1）
'''
def test16():
    dict1 = {'name': '兰兰', '性别': 'male'}
    c1=requests.utils.cookiejar_from_dict(dict1)
    c2=requests.utils.dict_from_cookiejar(c1)

def test17():
    dict1={'name': '兰兰', '性别': 'male'}
    c1=requests.utils.cookiejar_from_dict(dict1)
    c2=requests.utils.dict_from_cookiejar(c1)

def test18():
    dict1 = {'name': '兰兰', '性别': 'male'}
    c1=requests.utils.cookiejar_from_dict(dict1)
    c2=requests.utils.dict_from_cookiejar(c1)
    print(c1)
    print(c2)



