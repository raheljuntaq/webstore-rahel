from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://google.co.id')
driver.find_element_by_name('q') send keys.('Rahel' + Keys.ENTER )
assert 'Rahel' in driver.title
driver.quit()