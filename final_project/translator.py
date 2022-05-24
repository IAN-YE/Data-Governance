import http.client
import urllib.parse, urllib.request
import hashlib
import urllib
import random
import json


appid = '20220522001225178'
secretKey = 'QvxN7YrBRNjZSi0It0uO'
url_baidu = 'http://api.fanyi.baidu.com/api/trans/vip/translate'


def translate(text, f='auto', t='zh'):
    salt = random.randint(32768, 65536)
    sign = appid + text + str(salt) + secretKey
    sign = hashlib.md5(sign.encode()).hexdigest()
    url = url_baidu + '?appid=' + appid + '&q=' + urllib.parse.quote(text) + '&from=' + f + '&to=' + t + \
          '&salt=' + str(salt) + '&sign=' + sign

    try:
        httpClient = http.client.HTTPConnection('api.fanyi.baidu.com')
        httpClient.request('GET', url)
        response = httpClient.getresponse()
        result_all = response.read().decode("utf-8")
        result = json.loads(result_all)

    except Exception as e:
        print(e)
    finally:
        if httpClient:
            httpClient.close()

    return str(result['trans_result'][0]['dst'])
