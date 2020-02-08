# 宣言部分
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from time import sleep

options = Options()
options.add_argument('--headless')
driver = webdriver.Chrome('/Users/zuomujiangyi/work/auto_tin_manipulater/tool/chromedriver', chrome_options=options)

driver.get("https://www.yahoo.co.jp")

assert 'Yahoo' in driver.title

input_elem = driver.find_element_by_name('p')
input_elem.clear()
driver.save_screenshot("test.png")
input_elem.send_keys('Python')
driver.save_screenshot("test2.png")
input_elem.send_keys(Keys.RETURN)
sleep(1)
driver.save_screenshot("test3.png")

print(driver.title)
assert 'Python' in driver.title

counter = 1
# for a in driver.find_elements_by_css_selector('.w .hd a'):
for a in driver.find_elements_by_css_selector('.sw-CardBase'):
    print(counter)
    print(a.text)
    b = a.find_element_by_css_selector('a')
    print(b.get_attribute('href'))
    counter += 1
# 終了処理
driver.close()