import m3u8
import asyncio
import aiofile
import aiohttp
import os
from tqdm import tqdm
import shutil

class Downloader:
    def __init__(self, m3_file):
        self.dir, self.filename = m3_file.rsplit('/', 1)
        self.filename = self.filename.split('.')[0]
        self.buffer = self.dir + '/buffer'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'
        }
        self.sem = asyncio.Semaphore(20)
        self.__init_dir()
        self.__parse(m3_file)

    def __init_dir(self):
        if not os.path.exists(self.dir):
            os.mkdir(self.dir)
        if not os.path.exists(self.buffer):
            os.mkdir(self.buffer)

    def __parse(self, m3_file):
        with open(m3_file) as f:
            self.files = m3u8.loads(f.read()).files
            self.nums = len(self.files)

    async def __download_file(self, sq, url):
        async with self.sem:
            async with aiohttp.ClientSession() as session:
                async with session.get(url=url, headers=self.headers) as resp:
                    filename = f'{self.buffer}/{sq}.ts'
                    async with aiofile.async_open(filename, mode='wb') as f:
                        if self.skip_head:
                            await resp.content.readexactly(self.skip_head)
                        # await resp.content.readexactly(471)
                        async for chunk in resp.content.iter_chunked(1024):
                            await f.write(chunk)
                    self.bar.update(1)

    async def __run(self):
        tasks = []
        for sq, url in enumerate(self.files):
            task = asyncio.create_task(self.__download_file(sq, url))
            tasks.append(task)
        await asyncio.wait(tasks)

    def download(self, skip_head=0):
        self.skip_head = skip_head
        with tqdm(total=self.nums) as self.bar:
            loop = asyncio.get_event_loop()
            loop.run_until_complete(self.__run())
        self.__concat()

    def __concat(self):
        with open(f'{self.dir}/{self.filename}.mp4', mode='ab') as file:
            for sq in range(self.nums):
                with open(f'{self.buffer}/{sq}.ts', mode='rb') as f:
                    file.write(f.read())
        shutil.rmtree(self.buffer)
