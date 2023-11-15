# TESTs

不知道这样写是否符合规范，但是还是想到了一些可能潜在的漏洞需要测试。

## TFT0001-ParentPathTest

路径```/name/the/path```会被映射为```/realPathParentDir/the/path```。

如果```the/path```为```../otherDir```，那么是否会映射到```realPathParentDir```同级的文件夹```otherDir```从而返回用户不期望共享的文件夹呢？

### TFT0001-01

直接在浏览器中访问```http://narc.letmefly.xyz/日常共享/..```，一回车就自动跳转到了```http://narc.letmefly.xyz/```，相当于在浏览器中已经“转到上级目录”了。

### TFT0001-02

直接在浏览器中访问```http://narc.letmefly.xyz/日常共享/../..```，一回车还是自动跳转到了```http://narc.letmefly.xyz/```。

### TFT0001-03

直接在浏览器中访问不行，那么使用Py脚本试一试：

```python
import requests

response = requests.get('http://narc.letmefly.xyz/日常共享/..')
print(response)
print(response.text)
```

运行结果：

```xml
<Response [200]>
<html><body><a href="日常共享/">日常共享</a><hr></body></html>
```

和直接请求```http://narc.letmefly.xyz/```效果相同。

### TFT0001-04

使用Py脚本访问一下[TFT0001-02](#tft0001-02)中所构建的试试：

```python
import requests

response = requests.get('http://narc.letmefly.xyz/日常共享/../..')
print(response)
print(response.text)
```

运行结果：

```xml
<Response [200]>
<html><body><a href="日常共享/">日常共享</a><hr></body></html>
```

和直接请求```http://narc.letmefly.xyz/```效果相同。

### TFT0001-05

使用Py脚本访问一个真实存在的server根目录的同级文件夹：

```python
import requests

response = requests.get('http://narc.letmefly.xyz/日常共享/../TongJi/')
print(response)
print(response.text)
```

运行结果：

```xml
<Response [500]>
<!doctype html>
<html lang=en>
<title>500 Internal Server Error</title>
<h1>Internal Server Error</h1>
<p>The server encountered an internal error and was unable to complete your request. Either the server is overloaded or there is an error in the application.</p>
```

在服务终端中看到```10.112.175.237 - - [15/Nov/2023 18:44:01] "GET /TongJi/ HTTP/1.1" 500 -```。

和直接在浏览器中访问```http://narc.letmefly.xyz/TongJi/```效果相同。

### TFT0001-Result

测试结果认为程序具有一定的健壮性，不存在[此](#tft0001-parentpathtest)潜在的漏洞。
