from functions import URLFunctions
import pandas as pd


class Preprocessor:
    @staticmethod
    def preprocess(url):
        df = pd.DataFrame([url], columns=['url'])

        df['ip'] = df['url'].apply(URLFunctions.find_ip)
        df['count.'] = df['url'].apply(URLFunctions.count_dot)
        df['length'] = df['url'].apply(URLFunctions.url_len)
        df['has_https'] = df['url'].apply(URLFunctions.has_https)
        df['subdomain_count'] = df['url'].apply(URLFunctions.count_subdomains)
        df['param_count'] = df['url'].apply(URLFunctions.count_url_params)
        df['www'] = df['url'].apply(URLFunctions.count_www)
        df['@'] = df['url'].apply(URLFunctions.count_atrate)
        df['%'] = df['url'].apply(URLFunctions.count_percentage)
        df['*'] = df['url'].apply(URLFunctions.count_asterisk)
        df['$'] = df['url'].apply(URLFunctions.count_dollar)
        df['#'] = df['url'].apply(URLFunctions.count_hash)
        df['='] = df['url'].apply(URLFunctions.count_equalto)
        df['hostname_length'] = df['url'].apply(URLFunctions.hostname_length)
        df['hostname_length_2'] = df['url'].apply(URLFunctions.hostname_length2)
        df['sus_url'] = df['url'].apply(URLFunctions.suspicious_words)
        df['count_dir'] = df['url'].apply(URLFunctions.no_of_dir)
        df['count_embed_domian'] = df['url'].apply(URLFunctions.no_of_embed)
        df['short_url'] = df['url'].apply(URLFunctions.shortening_service)

        df = df.drop(['url'], axis=1)

        return df
