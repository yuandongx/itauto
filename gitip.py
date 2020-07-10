import lxml.etree as etree
import re
import urllib.request
import os
import sys

# 140.82.114.4 github.com
# 199.232.5.194 github.global.ssl.fastly.net
# 140.82.112.9 codeload.github.com
# 52.216.237.203 github-cloud.s3.amazonaws.com
regex = re.compile(r"\<li\>(\d+\.\d+\.\d+\.\d+)\<\/li\>")
regex_etc = re.compile(r"\d+\.\d+\.\d+\.\d+\s+(.+)")
HOTS = ("github.com", "github.global.ssl.fastly.net", "codeload.github.com",
        "github-cloud.s3.amazonaws.com")
GITHUB_HOST = {
    "github.com":
    "https://github.com.ipaddress.com",
    "github.global.ssl.fastly.net":
    "https://fastly.net.ipaddress.com/github.global.ssl.fastly.net",
    "codeload.github.com":
    "https://github.com.ipaddress.com/codeload.github.com",
    "github-cloud.s3.amazonaws.com":
    "https://amazonaws.com.ipaddress.com/github-cloud.s3.amazonaws.com",
}


def fetch_url(url='https://github.com.ipaddress.com/'):
    with urllib.request.urlopen(url) as f:
        text = f.read()
        html = etree.HTML(text)
        a = html.xpath("//ul[@class='comma-separated']")
        for b in a:
            tmp = etree.tostring(b[0]).decode('utf-8')
            m = regex.search(tmp)
            if m is not None:
                ip = str(m.group(1))
                print(ip, url)
                return str(m.group(1))


def do_work(etc_host="/etc/host"):
    result = {}
    lines = []
    poped = []
    with open(etc_host, "r") as f:
        lines = f.readlines()
    for key in GITHUB_HOST:
        ip = fetch_url(GITHUB_HOST[key])
        result[key] = ip
    tmp_lines = lines[:]
    for index, line in enumerate(lines):
        if not line.startswith("#"):
            m = regex_etc.search(line)
            if m is not None:
                host_name = str(m.group(1))
                if host_name in HOTS:
                    ip = result.get(host_name)
                    if ip is not None:
                        tmp_lines[index] = "%s %s\n" % (ip, host_name)
                        poped.append(host_name)
    print(result)
    for key in result:
        if result.get(key) is not None and key not in poped:
            tmp_lines.append("%s %s\n" % (result[key], key))
    with open(etc_host, "w") as f:
        f.writelines(tmp_lines)


if __name__ == "__main__":
    # if sys.platform == "win32":
    #     do_work(etc_host=r"C:/Windows/System32/drivers/etc/hosts")
    #     print(os.system("ipconfig /flushdns"))
    # else:
    #     do_work(etc_host=r"/etc/hosts")
        # print(os.system("service networking restart"))
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    print(BASE_DIR)