from selenium import webdriver
import time 

options = webdriver.ChromeOptions()
options.add_argument("--headless")

options.add_argument("--remote-debugging-port=9222")
options.add_experimental_option("useAutomationExtension", False)
options.add_experimental_option("excludeSwitches",["enable-automation"])

driver = webdriver.Chrome(options=options)

def handle_urls(file_name):
    with open(file_name,"r",encoding="utf-8") as file : 
        list_of_urls = file.readlines()
        for i,url in enumerate(list_of_urls) :
            name_file = f"code_source_of_urls/url_{i+1}.txt"
            scrap_website(url,name_file)
          
def scrap_website(url,name_file):
    global driver
    driver.get(url)
    driver.implicitly_wait(15)

    page_source = driver.page_source
    if "ShieldSquare Captcha" in page_source : 
        '''
        you can increase the amout of time as you want to solve the captcha manually , only once , then you won't face it again 
        '''
        time.sleep(25)
        driver.get(url)
        driver.implicitly_wait(15)

        page_source = driver.page_source
    


    with open(name_file,"w",encoding="utf-8") as file :
        file.write(page_source)
        file.close()


file_name = "urls_28.txt"
handle_urls(file_name)
driver.quit()