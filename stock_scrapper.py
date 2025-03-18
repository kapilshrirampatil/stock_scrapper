## Importing the important library
import time
import pandas as pd
import numpy as np
import selenium
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

class StockScrapper:
    def __init__(self,driver,timeout = 10):

        self.driver = driver
        self.wait = WebDriverWait(self.driver,timeout = timeout)
        self.data = []

    def wait_for_page_to_load(self):
        try:
            page = self.driver.title
            self.wait.until(lambda d:d.execute_script("return document.readyState")=='complete')
        except:
            print(f'page {page} is not fully loaded')

        else:
            print(f'page {page} is fully loaded')

    def access_url(self,url):

        self.driver.get(url)
        
        self.wait_for_page_to_load()

    def access_stock(self):

        action = ActionChains(self.driver)
        market_menu = self.wait.until(EC.presence_of_element_located((By.XPATH,'/html[1]/body[1]/div[2]/header[1]/div[1]/div[1]/div[1]/div[4]/div[1]/div[1]/ul[1]/li[3]/a[1]')))
        action.move_to_element(market_menu).perform()

        trending_tickers = self.wait.until(EC.element_to_be_clickable((By.XPATH,'/html[1]/body[1]/div[2]/header[1]/div[1]/div[1]/div[1]/div[4]/div[1]/div[1]/ul[1]/li[3]/div[1]/ul[1]/li[4]/a[1]/div[1]')))
        action.click(trending_tickers).perform()

        self.wait_for_page_to_load()

        most_active = self.wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="nimbus-app"]/section/section/section/article/section[1]/div/nav/ul/li[1]/a/span')))
        action.click(most_active).perform()

        self.wait_for_page_to_load()

    def extract_stocks(self):

        while True:
    
            rows = self.driver.find_elements(By.CSS_SELECTOR, 'table tbody tr')
            
            for row in rows:
                
                values = row.find_elements(By.TAG_NAME,'td')
                stock= {
                    'symbol':values[0].text,
                    'name'  : values[1].text,
                "price"  : values[3].text,
                "change" : values[4].text,
                "pct_cng" : values[5].text,
                "volume" : values[6].text,
                "avg_vol" : values[7].text,
                "mark_cap" : values[8].text,
                "pe_rat" : values[9].text,
                "year_cng" : values[10].text
                }
                self.data.append(stock)
            try:
                next_page = self.wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="nimbus-app"]/section/section/section/article/section[1]/div/div[3]/div[3]/button[3]')))

            except:
                print('Element is not clickable')
                break

            else:
                next_page.click()
                time.sleep(1.5)

    def data_cleaning_excel_op(self,filename):

        stock_df = (pd.DataFrame(self.data).apply(lambda col:col.str.strip() if col.dtype == 'object' else col)
                    .assign(
                        price  = lambda df_:pd.to_numeric(df_['price']),
                        change = lambda df_:pd.to_numeric(df_['change'].str.replace('+','')),
                        volume = lambda df_:pd.to_numeric(df_['volume'].str.replace('M','')),
                        avg_vol= lambda df_:pd.to_numeric(df_['avg_vol'].str.replace('M','')),
                        mark_cap=lambda df_:df_.mark_cap.apply(lambda x:float(x.replace('B','')) if 'B' in x else float(x.replace('T',''))*1000),
                        pe_rat = lambda df_: df_['pe_rat'].replace('-',np.nan).str.replace(',','').pipe(lambda col:pd.to_numeric(col))
                    )
                    .rename(columns = {'price':'price_USD','volume':'Volume M',
                    'avg_vol':'avg_vol M','mark_cap':'mark_cap B'}))

        stock_df.to_excel(filename+'.xlsx',index = False)

if __name__ == "__main__":

    driver = webdriver.Chrome()

    driver.maximize_window()


    url = 'https://finance.yahoo.com/'

    scapper = StockScrapper(driver,5)

    scapper.access_url(url)
    scapper.access_stock()
    scapper.extract_stocks()
    scapper.data_cleaning_excel_op('most active stocks')

    driver.quit()