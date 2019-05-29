from time import sleep

from selenium import webdriver

doubandriver = webdriver.Chrome()

url = 'https://www.douban.com/'

doubandriver.get(url)

doubandriver.implicitly_wait(5)

doubandriver.maximize_window()

# 进入子页面
doubandriver.switch_to.frame(doubandriver.find_element_by_xpath('//*[@id="anony-reg-new"]/div/div[1]/iframe'))

doubandriver.find_element_by_class_name('account-tab-account').click()

doubandriver.find_element_by_id('username').send_keys('手机号')

doubandriver.find_element_by_id('password').send_keys('密码')

doubandriver.find_element_by_css_selector('a.btn:nth-child(1)').click()  # 因为是复合类，所以不可以用类名

# 切出来
doubandriver.switch_to.default_content()

doubandriver.save_screenshot('douban.png')
print('screenshot success')




