

import requests


def get_url(url):
    session = requests.Session()
    session.headers.update({
        'Origin': 'http://www.imeitou.com',
        'Referer': 'http://www.imeitou.com/nvsheng/mnns/index.html',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36',
        'Cookie': 'Hm_lvt_1ef6d22326fe2c0f9411d7294ca6d902=1565681953,1565682000; Hm_lpvt_1ef6d22326fe2c0f9411d7294ca6d902=1565950344'
    })
    return session.get(url).content


if __name__=="__main__":
    print(get_url('http://www.imeitou.com/nvsheng/mnns/index.html'))
