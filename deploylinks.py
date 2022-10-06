from webbrowser import Chrome
from selenium import webdriver
from shutil import which
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options as ChromeOptions
import time
import csv
import scraper_helper
spm_options = Options()
from scrapy import Selector
import pandas as pd
import requests
# import verify
import scraper_helper
from webdriver_manager.firefox import GeckoDriverManager
from zyte_smartproxy_selenium import webdriver
from seleniumrequests import Chrome


df=pd.read_csv('links.csv',index_col=False)
# print(df)
print(df.columns)
# first = df.loc['Name']
# print(first)
mylist = df.Name.values.tolist()
# print(mylist)
# HEADLESS_PROXY = "localhost:3128"
# webdriver.DesiredCapabilities.FIREFOX['proxy'] = {
#     "httpProxy": HEADLESS_PROXY,
#     "sslProxy": HEADLESS_PROXY,
#     "proxyType": "MANUAL",
# }
spm_options.add_argument("--headless")
spm_options.add_argument("--window-size=1920x1080")
spm_options.add_argument('--disable-blink-features=AutomationControlled')

Chrome_path = which('chromedriver')
browser = webdriver.Chrome(executable_path=Chrome_path, options=spm_options)
browser.get('https://linkdeploy.com/start/')    

for webname in mylist:
    # driver.get('https://linkdeploy.com/start/')
    # driver.implicitly_wait(10)
    # import requests
    # headers = { 
    # "apikey": "fe3cda60-28f8-11ed-bdca-3d544305451b"}
    # params = (
    # ("url","https://linkdeploy.com/start/"),
    # ("premium","true"),
    # ("render","true"),
    # );
    # response = requests.get('https://app.zenscrape.com/api/v1/get', headers=headers, params=params);
    # headers = scraper_helper.get_dict(headers,strip_cookie=True)
    # link = 'https://linkdeploy.com/'
    # response = requests.get(link, headers=headers,
    # proxies={
    #     "http": "http://50576354ac11457097dd1a4d74f143d3:@proxy.crawlera.com:8011/",
    #     "https": "http://50576354ac11457097dd1a4d74f143d3:@proxy.crawlera.com:8011/",
    # },
    # verify=r'C:\Users\TOSHIBA\projects\deploylinks\zyte-proxy-ca.crt' 
    # )
    # print(f"response-status-code--------------, {response.status_code}")
    # print('-------------------------')
    # print(response.text)
    # with webdriver.Firefox() as driver:
    #     driver.get("https://linkdeploy.com/start/")
    # spm_options = Options()
    
    browser = webdriver.Chrome(spm_options={'spm_apikey': '50576354ac11457097dd1a4d74f143d3'})
    browser.get('https://linkdeploy.com/start/')
    # browser.save_screenshot('screenshot.png')
    # browser.close()
    browser.implicitly_wait(20)
    print(webname)
    search_input = browser.find_element_by_xpath('//form[@action="/start/"]/input[@name="domain"]')
    browser.implicitly_wait(3)
    search_input.click()
    browser.implicitly_wait(5)
    search_input.send_keys(webname)
    browser.implicitly_wait(3)
    search_input.send_keys(Keys.RETURN)
    time.sleep(10)
    resp = Selector(text=browser.page_source)
    Website_content = resp.xpath('(//div[@class="col-md-2"]/i/@aria-hidden)[1]').get()
    Domain_Authority = resp.xpath('(//div[@class="col-md-2"]/i/@aria-hidden)[2]').get()
    Traffic = resp.xpath('(//div[@class="col-md-2"]/i/@aria-hidden)[3]').get()
    Quality_Check = resp.xpath('(//div[@class="col-md-2"]/i/@aria-hidden)[4]').get()
    data = {
        'website content':Website_content,
        'Domain Authority':Domain_Authority,
        'Traffic': Traffic ,
        'quality check': Quality_Check
    }

browser.quit()
