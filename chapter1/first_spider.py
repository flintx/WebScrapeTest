from urllib.error import URLError
from urllib.request import urlopen


def download(url, num_retries=2):
    print("Downloading: " + url)
    try:
        html = urlopen(url).read()
    except URLError as e:
        print("error: " + e.reason)
        html = None
        if num_retries > 0:
            if hasattr(e, "code") and 500 <= e.code < 600:
                download(url, num_retries-1)

    return html


if __name__ == '__main__':
    # my_url = "http://example.webscraping.com/"
    my_url = "http://httpstat.us/500"
    res = download(my_url)
    print(res)
