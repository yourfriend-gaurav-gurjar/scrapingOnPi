from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import pandas as pd
import time 



options = webdriver.ChromeOptions()
options.add_argument("headless")
options.add_argument('no-sandbox')
#specify the path to chromedriver (download and save on your computer)
#driver = webdriver.Chrome('chromedriver_linux64/chromedriver', chrome_options=options)
driver = webdriver.Chrome('chromedriver_linux64/chromedriver')

input_data = pd.read_csv("input_fourth_slot_data.csv")
print(input_data)
url_link = input_data['url']
driver.get("https://weedmaps.com/brands/all")
location = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[id='global-location-input']")))
location.clear()
location.send_keys("Oklahoma City, Oklahoma, United States")
location.send_keys(Keys.ENTER)
#target the location menu button and click it
location = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[contains(text(), 'Oklahoma City, Oklahoma, United States')]")))
location.click()
time.sleep(5)
df = pd.DataFrame()
df.to_csv('metaData_pages_fourth_slot_data.csv')
df = pd.DataFrame()
df.to_csv('failed_link_fourth_slot_data.csv')
for link in url_link:
    driver.get(link)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
#    wait = WebDriverWait(driver, 10)
    try:
        wait = WebDriverWait(driver, 10)
        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[contains(@class, "sc-kEqXSa ZxMBe dropdown__StyledDropdown-sc-1mtwp7x-0 cWsPSj pagination-styles__PageSelect-sc-1b6a0ck-7 hFqfxF")]/div/button[contains(@class,"sc-iqAclL eKIpLN")]/span')))
        page_location = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Page 1 of')]"))).text        
        link_products_df = pd.DataFrame([page_location], columns=['page_count'])
        link_products_df['link'] = link
        link_products_df.to_csv('metaData_pages_fourth_slot.csv', mode='a', header=False, index=False)
        print(link_products_df)
        wait = WebDriverWait(driver, 10)
    except:
        print("leaked..!")
        failed_df = pd.DataFrame([link], columns=['failed'])
        failed_df.to_csv('failed_link_fourth_slot_data.csv', mode='a', header=False, index=False)
#    finally:
#        print("Server is not serving the requests anymore.")

driver.close()    
#print(failed_df)
#print(link_products_df)
#df_outer.to_csv('data_80plus_products_fourth_slot.csv', index=False)
