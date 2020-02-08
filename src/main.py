from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from time import sleep

options = Options()
options.add_argument('--headless')
driver = webdriver.Chrome('/Users/zuomujiangyi/work/auto_tin_manipulater/tool/chromedriver', chrome_options=options)

url = 'https://tinder.com/app/recs'

driver.get(url)
sleep(3)
assert 'Tinder' in driver.title

buttons = list(filter(lambda button: 'NUMBER' in button.text\
    ,driver.find_elements_by_css_selector('.button')))
if len(buttons):
    buttons[0].click()
sleep(3)
driver.save_screenshot('images/start.png')





