### 传入iqiyi播放页url，解析出视频m3u8文件

***
非登陆式：

```python
from iqiyi import Iqiyi

iqiyi = Iqiyi()

# 传入视频播放页url
url = '' 

# 在本地生成m3u8文件
iqiyi.get(url)
 
```
***
登陆式

* 在浏览器上手动登陆[`iqiyi`](https://www.iqiyi.com/)账号

* 导出cookie，推荐使用浏览器插件[`EditThisCookie`](https://chrome.google.com/webstore/detail/editthiscookie/fngmhnnpilhplaeedifhccceomclgfbg)

* （推荐）修改`cookie.conf`文件，将导出的 json 的格式覆盖保存

* （推荐）调用 iqiyi.set_cookie()

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

m3u8下载（如下为可选方案）

```python
from download import Downloader

downloader = Downloader(m3_file)
# 要求m3_file为m3u8文件的绝对路径，路径名为mac的方式
# Windows可能需要对代码做相应的更改
# 基于协程下载
downloader.download()

```
