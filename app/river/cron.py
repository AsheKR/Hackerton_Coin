import time

from bs4 import BeautifulSoup
from selenium import webdriver

from .models import River


def river_temper_cron():
    url = 'http://www.koreawqi.go.kr/index_web.jsp'
    coptions = webdriver.ChromeOptions()
    coptions.add_argument('headless')
    coptions.add_argument('window-size=1920x1080')
    coptions.add_argument("disable-gpu")
    coptions.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36")
    coptions.add_argument("lang=ko_KR")
    driver = webdriver.Chrome('/usr/sbin/chromedriver', options=coptions)
    print("before get_url")
    driver.get(url)
    print("after get_url")
    driver.switch_to.frame('MainFrame')
    driver.find_element_by_id('container').find_element_by_id('state')
    driver.find_element_by_class_name('tab_container').find_element_by_class_name('timetable')
    td = driver.find_element_by_xpath('//*[@id="div_layer_btn1_r1"]/table/tbody/tr[18]').get_attribute('outerHTML')
    driver.switch_to.default_content()
    soup = BeautifulSoup(td, 'lxml')
    td_list = soup.select('td')
    temperature = td_list[0].get_text(strip=True)

    River.objects.create(
        temperature=temperature,
    )
