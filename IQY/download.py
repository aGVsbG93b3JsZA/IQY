import m3u8
import asyncio
import aiofile
import aiohttp
import os
from tqdm import tqdm
import shutil

class Downloader:
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'
        }
        self._sem = asyncio.Semaphore(16)
        self.save_path = None

    # 创建ts缓存文件夹
    def _create_buffer(self, save_path):
        if save_path:
            self._buffer = save_path + '/.buffer'
        else:
            self._buffer = '.buffer'
        if not os.path.exists(self._buffer):
            os.mkdir(self._buffer)

    # 导入m3u8字符串
    def loads(self, m3u8_content):
        self.files = m3u8.loads(m3u8_content).files
        self.nums = len(self.files)
    
    # 导入m3u8文件
    def load_file(self, m3u8_file):
        with open(m3u8_file, mode='r') as f:
            self.files = m3u8.loads(f.read()).files
            self.nums = len(self.files)
    
    # 设置协程并发数
    def set_semaphore(self, n):
        self._sem = asyncio.Semaphore(n)

    # 下载单个ts文件
    async def _download_file(self, sq, url):
        async with self._sem:
            async with aiohttp.ClientSession() as session:
                async with session.get(url=url, headers=self.headers) as resp:
                    filename = f'{self._buffer}/{sq}.ts'
                    async with aiofile.async_open(filename, mode='wb') as f:
                        async for chunk in resp.content.iter_chunked(1024):
                            await f.write(chunk)
                    self._bar.update(1)

    # 创建协程任务，下载所有文件
    async def _run(self):
        tasks = []
        for sq, url in enumerate(self.files):
            task = asyncio.create_task(self._download_file(sq, url))
            tasks.append(task)
        await asyncio.wait(tasks)

    # 下载主函数
    def download(self, save_name, save_path=None):
        self._create_buffer(save_path)
        print('正在下载:', save_name)
        with tqdm(total=self.nums) as self._bar:
            loop = asyncio.get_event_loop()
            loop.run_until_complete(self._run())
        self._concat(save_name, save_path)

    # 合并所有ts文件，后缀名为.mp4
    def _concat(self, save_name, save_path):
        if save_path:
            video_name = save_path + '/' + save_name + '.mp4'
        else:
            video_name = save_name + '.mp4'
        with open(video_name, mode='ab') as file:
            for sq in range(self.nums):
                with open(f'{self._buffer}/{sq}.ts', mode='rb') as f:
                    file.write(f.read())
        shutil.rmtree(self._buffer)
