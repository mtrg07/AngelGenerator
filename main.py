from threading import Thread
from time import sleep
from random import choice
from itertools import cycle
from hbypass import bypass

from get_headers import get_headers

import os 
import subprocess
import sys
import string
import time
import requests

clear = lambda: subprocess.call(
    'cls' if os.name == 'nt' else 'clear', shell=True
)


def TitleTask():
    while True:
        os.system('title [AngelGenerator]'); sleep(1.5)
        os.system('title [TrolledTooMuch]'); sleep(1.5)


class Generate:
    def __init__(self):
        self.proxies = []
        self.tokens  = []

        self.request = requests.Session()

        self.purple  = '\033[38;5;56m'
        self.pmix    = '\033[38;5;57m'
        self.white   = '\033[38;5;7m'


        self.ascii()
        print('                                   ' +
              self.purple + '[' + self.white + time.strftime('%H:%M:%S', time.localtime()) +
              self.purple + ']' + ' Would you like to use proxies? (y/n): ', end=f'{self.white}')
        proxy=input()

        if proxy.upper() == 'Y':
            for _ in open('proxies.txt'):
                if(':' in _ and len(_.replace('\n', '').split(':')[-1]) <= 5):

                    self.proxies.append(_.replace('\n', ''))



    def start(self):
        self.ascii()
        
        print('                                         ' + 
              self.purple + '[' + self.white + time.strftime('%H:%M:%S', time.localtime()) +
              self.purple + ']' + ' Enter Amount of Threads: ', end=f'{self.white}')
        amount=input(); self.ascii()

        if amount.isdigit():
            threads = []

            for x in range(int(amount)):
                thread = Thread(target=self.main)
                threads.append(thread)
                thread.start()

            for x in threads:
                x.join()
            print('\n' + '                    ' + 
                  self.purple + '[' + self.white + time.strftime('%H:%M:%S', time.localtime()) + self.purple + ']' + ' ' +
                  self.white + 'All tokens can be found in tokens.txt, Press enter to exit...' + '\n', end='')

            input(); os._exit(0)
        
        else : self.start()


    def main(self):
        try:
            cookie      = get_headers().cookie()
            fingerprint = get_headers().fingerprint()

            print('                     ' + 
                  self.purple + '[' + self.white + time.strftime('%H:%M:%S', time.localtime()) +
                  self.purple + ']' + ' Grabbed Fingerprint: ' + self.white + fingerprint)

            headers = {
                'authority'        : 'discord.com',
                'method'           : 'POST',
                'path'             : '/api/v9/auth/register',
                'scheme'           : 'https',
                'accept'           : '*/*',
                'accept-encoding'  : 'gzip, deflate, br',
                'accept-language'  : 'en-US',
                'authorization'    : 'undefined',
                'content-type'     : 'application/json',
                'cookie'           : cookie,
                'origin'           : 'https://discord.com',
                'referer'          : 'https://discord.com/register',
                'sec-fetch-dest'   : 'empty',
                'sec-fetch-mode'   : 'cors',
                'sec-fetch-site'   : 'same-origin',
                'user-agent'       : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36',
                'x-fingerprint'    : fingerprint
            }
            
            payload = {
                'captcha_key'      : bypass('f5561ba9-8f1e-40ca-9b5b-a0b3f719ef34', 'discord.com', proxy=choice(self.proxies)),
                'consent'          : True,
                'date_of_birth'    : '2000-05-05',
                'email'            : ''.join(choice(string.digits) for x in range(10)) + '@gmail.com',
                'fingerprint'      : fingerprint,
                'gift_code_sku_id' : None,
                'invite'           : None,
                'password'         : 'xth&*#7juds8',
                'username'         : '﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽'
            }

            proxies = {
                'http'  : f'http://{choice(self.proxies)}',
                'https' : f'http://{choice(self.proxies)}'
            }


            create_account = requests.Session().post('https://discord.com/api/v9/auth/register', headers=headers, json=payload, proxies=proxies)

            if create_account.status_code in (200, 201, 203, 204):
                token = create_account.json()['token']
                self.tokens.append(token)

                open('tokens.txt', 'a').write(f'{token}\n')
                print('                     ' + 
                      self.purple + '[' + self.white + time.strftime('%H:%M:%S', time.localtime()) + 
                      self.purple + ']' + ' Generated Token: ' + self.white + token[:30] + '...')
                
                if requests.get('https://discord.com/api/v9/users/@me', headers={'authorization' : token}).json()['discriminator'] in ['0001', '9999', '1337', '1338', '6666', '0666', '1000', '2000', '1500', '1800', '1400', '0999']:
                    open('rare.txt', 'a').write(f'{token}\n')
            else:
                if 'retry_after' in create_account.json():
                    ratelimit = create_account.json()['retry_after']

                    print('                     ' + 
                      self.purple + '[' + self.white + time.strftime('%H:%M:%S', time.localtime()) + 
                      self.purple + ']' + ' Ratelimit: ' + self.white + f'{ratelimit}')

                if 'captcha_key' in create_account.json():
                    fail = create_account.json()['captcha_key']

                    print('                     ' +
                          self.purple + '[' + self.white + time.strftime('%H:%M:%S', time.localtime()) + 
                          self.purple + ']' + ' Captcha Fail: ' + self.white + f'{fail}')

        except requests.exceptions.ProxyError: return None


    def ascii(self):
        clear()

        ascii_text = self.purple + '''\n
                                      ▄▄▄·  ▐ ▄  ▄▄ • ▄▄▄ .▄▄▌     ▄▄ • ▄▄▄ . ▐ ▄ 
                                     ▐█ ▀█ •█▌▐█▐█ ▀ ▪▀▄.▀·██•    ▐█ ▀ ▪▀▄.▀·•█▌▐█
                                     ▄█▀▀█ ▐█▐▐▌▄█ ▀█▄▐▀▀▪▄██ ▪   ▄█ ▀█▄▐▀▀▪▄▐█▐▐▌
                                     ▐█▪ ▐▌██▐█▌▐█▄▪▐█▐█▄▄▌▐█▌ ▄  ▐█▄▪▐█▐█▄▄▌██▐█▌
                                      ▀  ▀ ▀▀ █▪·▀▀▀▀  ▀▀▀ .▀▀▀   ·▀▀▀▀  ▀▀▀ ▀▀ █▪''' + '\n\n'

        
        text = ascii_text.replace('•', f'{self.white}•{self.purple}').replace('·', f'{self.white}·{self.purple}'
                        ).replace('▪', f'{self.white}▪{self.purple}').replace('.', f'{self.white}.{self.purple}')

        
        print(text)




if __name__ == '__main__':
    Thread(target=TitleTask).start()
    Generate().start()
