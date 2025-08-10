import requests


def get_cookiejar():
    cookie_dict = {'PHPSESSID': 'htvoegt7rgb27fadl6d22calic',
                   'SERVERID': '7349dbf5589746919266ccf2e3cd1162|1680399216|1680399216',
                   'ingress_user_id': '1680399217.479.24061.806845|d8c6d8cb6c73f72f411c4a27f7a6674a'}
    # 1、dict转成cookiejar
    # <RequestsCookieJar[<Cookie PHPSESSID=b2n58milhcv5bt9ng1sqna8j9u for gamma-vms.56.cool/>, <Cookie SERVERID=7349dbf5589746919266ccf2e3cd1162|1680398478|1680398478 for gamma-vms.56.cool/>, <Cookie ingress_user_id=1680398479.08.20538.276188|d8c6d8cb6c73f72f411c4a27f7a6674a for gamma-vms.56.cool/>]>
    cookies_jar = requests.utils.cookiejar_from_dict(cookie_dict, cookiejar=None, overwrite=True)

    print('dict转成cookiejar：' + str(cookies_jar), type(cookies_jar))

    # 2、cookiejar转成dict
    cookies_dict2 = requests.utils.dict_from_cookiejar(cookies_jar)
    print('cookiejar转成dict：' + str(
        cookies_dict2))  # {'PHPSESSID': 'htvoegt7rgb27fadl6d22calic', 'SERVERID': '7349dbf5589746919266ccf2e3cd1162|1680399216|1680399216', 'ingress_user_id': '1680399217.479.24061.806845|d8c6d8cb6c73f72f411c4a27f7a6674a'}


