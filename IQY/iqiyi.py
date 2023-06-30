import json
import os
import re
import time
from urllib.parse import urlencode

import execjs
import requests
from requests.cookies import cookiejar_from_dict


class Iqiyi:
    def __init__(self) -> None:
        self.domin = 'https://cache.video.iqiyi.com/dash'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
        }
        self.session = requests.Session()
        self.session.headers = self.headers
        self.save_path = None

    def set_cookie(self, file='cookie.json'):
        with open(file) as f:
            cookies = json.load(f)
        cookie_dict = {}
        for cookie in cookies:
            name = cookie["name"]
            value = cookie["value"]
            cookie_dict[name] = value
        cookie_jar = cookiejar_from_dict(cookie_dict)
        self.session.cookies = cookie_jar

    def get(self, url, save_path=None):
        if save_path:
            self.save_path = save_path
        with self.session.get(url) as resp:
            page = resp.text
        self.__parse_page(page)
        self.__get_m3u8()

    def __get_authKey(self, tvid, tm):
        with open('authKey.js') as f:
            js = execjs.compile(f.read())
            return js.call('main', tvid, tm)

    def __get_vf(self, vf_input):
        with open('vf.js') as f:
            js = execjs.compile(f.read())
            return js.call('main', vf_input)

    def __parse_page(self, page):
        pattern = r'window.QiyiPlayerProphetData=(.*?)</script>'
        player = re.search(pattern, page)[1]
        player = json.loads(player)
        self.title = player['a']['data']['originRes']['vdi']['tl']
        # uid = '1418541118'
        # k_uid = '98c3a3df9dc475ce2cc800bba4eef561'
        # dfp = 'a07ab0e922cc00416d9f95e509d8bc758caaa04b7972b203d4f003e22b8a937fec'
        # pck = 'f42Rr6dwjIIrFL5wdjPY2s89ConayQYNpRMyoqqfBfDfZSzXvdpYHcMXRBNfT37lm3m2b9'
        uid = ''
        k_uid = ''
        dfp = ''
        tm = round(time.time() * 1000)
        tvid = player['a']['_params']['episodeId']
        vidl = player['v']['vidl'][-1]
        bid = vidl['bid']
        vid = vidl['vid']
        src = player['a']['_params']['ptid']
        pck = player['a']['_params']['passportCookie']
        params = {
            'tvid': tvid,
            'bid': bid,
            'vid': vid,
            'src': src,
            'vt': '0',
            'rs': '1',
            'uid': uid,
            'ori': 'pcw',
            'ps': '1',
            'k_uid': k_uid,
            'pt': '0',
            'd': '0',
            's': '',
            'lid': '',
            'cf': '',
            'ct': '',
            'authKey': self.__get_authKey(tvid, tm),
            'k_tag': '1',
            'dfp': dfp,
            'locale': 'zh_cn',
            'prio': '{"ff":"f4v","code":2}',
            'pck': pck,
            'k_err_retries': '0',
            'up': '',
            'sr': '1',
            'qd_v': '5',
            'tm': tm,
            'qdy': 'u',
            'qds': '0',
            'k_ft1': '706436220846084',
            'k_ft4': '1161084347621380',
            'k_ft5': '134217729',
            'k_ft7': '4',
            'bop': '{"version":"10.0","dfp":"' + dfp + '","b_ft1":8}',
            'ut': '1',
        }
        vf_input = '/dash?' + urlencode(params)
        vf = self.__get_vf(vf_input)
        params['vf'] = vf
        self.params = params

    def __get_m3u8(self):
        with self.session.get(self.domin, params=self.params) as resp:
            result = resp.json()
        videos = result['data']['program']['video']
        for video in videos:
            if 'm3u8' in video:
                if self.save_path:
                    self.file = self.save_path + '/' + self.title + '.m3u8'
                else:
                    self.save_path = self.title
                    if not os.path.exists(self.save_path):
                        os.mkdir(self.save_path)
                    self.file = self.save_path + '/' + self.title + '.m3u8'
                with open(self.file, mode='w') as f:
                    f.write(video['m3u8'])
                break