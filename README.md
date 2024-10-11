# AtlassianConfluence-RCE
AtlassianConfluence-RCE批量检测工具
![图片](https://github.com/user-attachments/assets/92d83496-036a-486b-8655-6547210545b9)
```shell
漏洞描述：
Atlassian Confluence是企业广泛使用的wiki系统，其部分版本中存在OGNL表达式注入漏洞。攻击者可以通过这个漏洞，无需任何用户的情况下在目标Confluence中执行任意代码。

fofa搜素语句
fofa：app="Atlassian-Confluence"

影响版本：
    Confluence < 6.13.23
    6.14.0 ≤ Confluence < 7.4.11
    7.5.0 ≤ Confluence < 7.11.6
    7.12.0 ≤ Confluence < 7.12.5
    Confluence < 7.13.0

工具利用：
  -h, --help            获取帮助信息
  -u URL, --url URL     检测指定目标url
  -f FILE, --file FILE  批量检测指定文件中的url
```
