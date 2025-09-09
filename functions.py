import re
from urllib.parse import urlparse


class URLFunctions:

    @staticmethod
    def find_ip(url):
        ipv6 = r'\b(?:[0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}\b'
        ipv4 = r'\b(?:(?:25[0-5]|2[0-4]\d|1\d{2}|[1-9]?\d)\.){3}(?:25[0-5]|2[0-4]\d|1\d{2}|[1-9]?\d)\b'
        ipv4_hex = r'\b(?:0x[0-9a-fA-F]{1,2}\.){3}0x[0-9a-fA-F]{1,2}\b'
        return int(bool(re.search(ipv6, url) or re.search(ipv4, url) or re.search(ipv4_hex, url)))

    @staticmethod
    def count_dot(url):
        return url.count('.')

    @staticmethod
    def url_len(url):
        return len(url)

    @staticmethod
    def has_https(url):
        return int(url.startswith('https://'))

    @staticmethod
    def count_subdomains(url):
        hostname = urlparse(url).hostname
        if hostname:
            return hostname.count('.')
        return 0

    @staticmethod
    def count_url_params(url):
        parsed = urlparse(url)
        return parsed.query.count('&') + 1 if parsed.query else 0

    @staticmethod
    def count_www(url):
        return url.count('www')

    @staticmethod
    def count_atrate(url):
        return url.count('@')

    @staticmethod
    def count_percentage(url):
        return url.count('%')

    @staticmethod
    def count_asterisk(url):
        return url.count('*')

    @staticmethod
    def count_dollar(url):
        return url.count('$')

    @staticmethod
    def count_hash(url):
        return url.count('#')

    @staticmethod
    def count_equalto(url):
        return url.count('=')

    @staticmethod
    def hostname_length(url):
        return len(urlparse(url).netloc)

    @staticmethod
    def hostname_length2(url):
        try:
            if not url.startswith(('http://', 'https://')):
                url = 'http://' + url
            return len(urlparse(url).netloc)
        except ValueError:
            return 0

    @staticmethod
    def suspicious_words(url):
        return int(bool(re.search(
            r'PayPal|login|signin|bank|account|update|free|lucky|service|bonus|ebayisapi|webscr',
            url, re.IGNORECASE)))

    @staticmethod
    def no_of_dir(url):
        return urlparse(url).path.count('/')

    @staticmethod
    def shortening_service(url):
        pattern = (
            r'bit\.ly|goo\.gl|shorte\.st|go2l\.ink|x\.co|ow\.ly|t\.co|tinyurl|tr\.im|is\.gd|cli\.gs|'
            r'yfrog\.com|migre\.me|ff\.im|tiny\.cc|url4\.eu|twit\.ac|su\.pr|twurl\.nl|snipurl\.com|'
            r'short\.to|BudURL\.com|ping\.fm|post\.ly|Just\.as|bkite\.com|snipr\.com|fic\.kr|loopt\.us|'
            r'doiop\.com|short\.ie|kl\.am|wp\.me|rubyurl\.com|om\.ly|to\.ly|bit\.do|t\.co|lnkd\.in|'
            r'db\.tt|qr\.ae|adf\.ly|bitly\.com|cur\.lv|tinyurl\.com|ow\.ly|bit\.ly|ity\.im|'
            r'q\.gs|is\.gd|po\.st|bc\.vc|twitthis\.com|u\.to|j\.mp|buzurl\.com|cutt\.us|u\.bb|yourls\.org|'
            r'x\.co|prettylinkpro\.com|scrnch\.me|filoops\.info|vzturl\.com|qr\.net|1url\.com|tweez\.me|v\.gd|'
            r'tr\.im|link\.zip\.net'
        )
        return int(bool(re.search(pattern, url, re.IGNORECASE)))
    @staticmethod
    def no_of_embed(url):
        urldir = urlparse(url).path
        return urldir.count('//')




    @staticmethod
    def http(url):
        return int(url.startswith('http://'))
