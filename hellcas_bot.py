from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument('user-data-dir=C:\\Users\\iago\\AppData\\Local\\Google\\Chrome\\User Data')

driver = webdriver.Chrome(executable_path='D:\chromedriver.exe',chrome_options=options)


def exbot():
    

    driver.get('https://hellcase.com/es/dailyfree')
    print ("Cargando la pagina")

    daily = driver.find_element_by_xpath('//*[@id="btnOpening"]')
                                            
    daily.click()

    driver.close()

exbot()
