
import os
import time
import request
from lxml import html


def get_page_url(pid):
    if pid == 1:
        return "http://www.imeitou.com/nvsheng/mnns/index.html"
    else:
        return "http://www.imeitou.com/nvsheng/mnns/index_{}.html".format(pid)


def main():
    page = request.get_url('http://www.imeitou.com/nvsheng/mnns/index.html')
    root = html.document_fromstring(page)
    ele = root.xpath('/html/body/div[5]/div[2]/ul/div/div/span[3]/strong[1]')
    page_number = int(ele[0].text)
    for pid in range(1, page_number+1):
        page_url = get_page_url(pid)
        page = request.get_url(page_url)

        page_root = html.document_fromstring(page)

        eles = page_root.xpath('/html/body/div[5]/div[2]/ul/li/a/img')
        for ele in eles:
            image_url = ele.attrib['src']
            img = request.get_url(image_url)
            local_path = os.path.join(os.getcwd(), 'images', image_url.split('/')[-1])
            with open(local_path, 'wb') as f:
                f.write(img)
            time.sleep(0.1)
        time.sleep(0.2)


if __name__ == '__main__':
    main()
