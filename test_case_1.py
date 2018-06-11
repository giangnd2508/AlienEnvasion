from selenium import webdriver


driver = webdriver.Chrome()
driver.maximize_window()
driver.get('http://www.privataaffarer.se/stock-widgets/telegram-fran-direkt/')

driver.quit()



