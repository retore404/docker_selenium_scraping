import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

if __name__ == '__main__':
    # Selenium サーバーへ接続する。
    driver = webdriver.Remote(
        command_executor=os.environ["SELENIUM_URL"],
        desired_capabilities=DesiredCapabilities.FIREFOX.copy()
    )  

    # 任意のHTMLの要素が特定の状態になるまで待つ
    # ドライバとタイムアウト値を指定
    wait = WebDriverWait(driver, 10)
    # Googleにアクセス
    driver.get('https://www.iijmio.jp/campaign/mio.html')

    #device_lineup_elem = driver.find_element(By.CSS_SELECTOR, "#device_lineup")    
    #oppo_a73_elems = device_lineup_elem.find_element(By.xpath("//a[@href='/device/detail.html?key=OPPO_A73PD']"))
    oppo_a73_elems = driver.find_element_by_xpath("//a[@href='/device/detail.html?key=OPPO_A73PD']")
    print(oppo_a73_elems)

    driver.quit()