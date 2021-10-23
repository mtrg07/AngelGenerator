import requests
import random

from requests import exceptions

class get_headers:
    def cookie(self) -> str:
        try:
            url = 'https://discord.com/register'
            proxy = open('proxies.txt').read().split('\n')

            headers = {
                'authority'       : 'discord.com',
                'method'          : 'GET',
                'path'            : '/register',
                'scheme'          : 'https',
                'accept'          : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                'accept-encoding' : 'gzip, deflate, br',
                'accept-language' : 'en-US,en;q=0.9',
                'user-agent'      : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36'
            }

            proxies = {
                'http'  : f'http://{random.choice(proxy)}',
                'https' : f'http://{random.choice(proxy)}'
            }

            get_cookie = requests.Session().get(url, headers=headers, proxies=proxies).cookies

            __dcfduid  = get_cookie['__dcfduid']
            __sdcfduid = get_cookie['__sdcfduid']

            return '__dcfduid=' + __dcfduid + '; ' + '__sdcfduid=' + __sdcfduid

        except requests.exceptions.ProxyError: return None


    def fingerprint(self) -> str:
        try:
            url = 'https://discord.com/api/v9/experiments'
            proxy = open('proxies.txt').read().split('\n')

            headers = {
                'authority'       : 'discord.com',
                'method'          : 'GET',
                'path'            : '/api/v9/experiments',
                'scheme'          : 'https',
                'accept'          : '*/*',
                'accept-encoding' : 'gzip, deflate, br',
                'accept-language' : 'en-US,en;q=0.9',
                'connection'      : 'keep-alive',
                'content-type'    : 'application/json',
                'user-agent'      : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36'
            }

            proxies = {
                'http'  : f'http://{random.choice(proxy)}',
                'https' : f'http://{random.choice(proxy)}'
            }

            get_fingerprint = requests.Session().get(url, headers=headers, proxies=proxies)

            if 'fingerprint' in get_fingerprint.json():
                return get_fingerprint.json()['fingerprint']
            else:
                self.fingerprint()

        except requests.exceptions.ProxyError: return None
