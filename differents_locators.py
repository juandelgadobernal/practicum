from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get('https://about.google/')

# Locate the logo by XPATH
g_logo_xpath = driver.find_element(By.XPATH, '//*[@id="glue-drawer"]/div/div[1]/div/div/a/div/img')
if g_logo_xpath.is_displayed():
    print(f"Locator logo by XPATH exist".format())

# By CLASS
g_logo_CLASS = driver.find_elements(By.CLASS_NAME, "glue-header__logo-svg")
if g_logo_CLASS[1].is_displayed():
    print(f"Locator logo by CLASS exist".format())

# Locate the logo by CSS
g_logo_css_01 = driver.find_element(By.CSS_SELECTOR, '.glue-header__logo-link .glue-header__logo-container img.glue-header__logo-svg')
if g_logo_css_01.is_displayed():
    print(f"Locator logo by CSS 01 exist".format())

g_logo_css_02 = driver.find_element(By.CSS_SELECTOR, '.glue-header__logo-container img.glue-header__logo-svg')
if g_logo_css_01.is_displayed():
    print(f"Locator logo by CSS 02 exist".format())

g_logo_css_03 = driver.find_element(By.CSS_SELECTOR, '.glue-header__logo-container img.glue-header__logo-svg')
if g_logo_css_03.is_displayed():
    print(f"Locator logo by CSS 03 exist".format())
