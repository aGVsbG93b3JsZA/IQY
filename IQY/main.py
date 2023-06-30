from iqiyi import Iqiyi
from download import Downloader


if __name__ == '__main__':

    iqiyi = Iqiyi()
    iqiyi.set_cookie()
    url = 'https://www.iqiyi.com/v_xkt6z3z798.html'
    iqiyi.get(url)

    downloader = Downloader()
    downloader.load_file(iqiyi.file)
    downloader.download(save_name=iqiyi.title, save_path=iqiyi.save_path)
