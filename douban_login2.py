from time import sleep
from selenium import webdriver

doubandriver = webdriver.Firefox()
url = 'https://accounts.douban.com/passport/login'

doubandriver.get(url)
sleep(6)

doubandriver.find_element_by_class_name('account-tab-account').click()

doubandriver.find_element_by_id('username').send_keys('手机号')
doubandriver.find_element_by_id('password').send_keys('密码')
sleep(1)

doubandriver.find_element_by_partial_link_text('登录豆瓣').click()
print("已经click")
sleep(3)

doubandriver.save_screenshot('douban.png')
print('已经截图')
sleep(3)

doubandriver.close()
