# iqiyi视频逆向解析下载

### 依赖项
* Python依赖项：```pip install -r requirements.txt```
* 其他：需安装好 [`NodeJs`](https://nodejs.org/en) 环境


***
### 非登陆式：

```python
from iqiyi import Iqiyi

iqiyi = Iqiyi()

# 传入视频播放页url
url = '' 

# 在本地生成m3u8文件
iqiyi.get(url)
 
```
***
### 登陆式

* 在浏览器上手动登陆[`iqiyi`](https://www.iqiyi.com/)账号

* 导出 cookie，推荐使用Chrome浏览器插件[`EditThisCookie`](https://chrome.google.com/webstore/detail/editthiscookie/fngmhnnpilhplaeedifhccceomclgfbg)

* 清空`cookie.json`文件，将导出的 cookie 覆盖保存

* 调用 `iqiyi.set_cookie()`

```python
from iqiyi import Iqiyi

iqiyi = Iqiyi()

iqiyi.set_cookie()

iqiyi.get(url=url)

```
* 其他方法

  1. 打开浏览器开发者工具，刷新后得到请求头里的cookie
  2. 修改文件`self.headers`,添加一行`'Cookie': 'your_cookie'`
***

### m3u8下载

```python
from download import Downloader

downloader = Downloader()

# 导入m3u8文件路径
downloader.load_file(filepath)

# 基于协程下载
downloader.download(save_name)

```
