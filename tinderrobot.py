from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
from selenium.common.exceptions import ElementClickInterceptedException

FB_EMAIL = "7739980377"
FB_PASSWORD = "Sexy1994"

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
chrome_driver_path = "/Users/jeffli/Python/chromedriver"
driver = webdriver.Chrome(options=options, executable_path=chrome_driver_path)
driver.get("http://www.tinder.com")

driver.maximize_window()

driver.implicitly_wait(10)
#cookies
element = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div/div/div[1]/div[1]/button')
element.click()

driver.implicitly_wait(10)
#login
login = driver.find_element(By.XPATH, '//*[@id="q888578821"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a/div[2]/div[2]')
login.click()

driver.implicitly_wait(10)
sleep(3)
#-------------Login with Facebook------------#
fb = driver.find_element(By.XPATH, '//*[@id="q-839802255"]/main/div/div[1]/div/div/div[3]/span/div[2]/button/div[2]/div[2]')
fb.click()

sleep(3)
base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
print(driver.title)

driver.implicitly_wait(5)
sleep(3)
#Login and hit enter
email = driver.find_element(By.XPATH, '//*[@id="email"]')
password = driver.find_element(By.XPATH, '//*[@id="pass"]')
email.send_keys(FB_EMAIL)
password.send_keys(FB_PASSWORD)
password.send_keys(Keys.ENTER)

driver.switch_to.window(base_window)
print(driver.title)

#Delay by 5 seconds to allow page to load.
sleep(5)
driver.implicitly_wait(10)


#Allow location
allow_location_button = driver.find_element(By.XPATH, '//*[@id="q-839802255"]/main/div/div/div/div[3]/button[1]/div[2]/div[2]')
allow_location_button.click()

driver.implicitly_wait(10)
#Disallow notifications
notifications_button = driver.find_element(By.XPATH, '//*[@id="q-839802255"]/main/div/div/div/div[3]/button[2]/div[2]/div[2]')
notifications_button.click()


sleep(5)
driver.implicitly_wait(5)
#disable darkmode
dark_button = driver.find_element(By.XPATH, '/html/body/div[2]/main/div/div[2]/button')
dark_button.click()


for n in range(10000):

    #Add a 1 second delay between likes.
    driver.implicitly_wait(3)
    sleep(2)

    try:
        print("called")
        button_like = driver.find_element(By.XPATH, '/html/body')
        button_like.send_keys(Keys.ARROW_RIGHT)


    #Catches the cases where there is a "Matched" pop-up in front of the "Like" button:
    except ElementClickInterceptedException:
        try:
            match_popup = driver.find_element(By.CSS_SELECTOR, ".itsAMatch a")
            match_popup.click()

        #Catches the cases where the "Like" button has not yet loaded, so wait 2 seconds before retrying.
        except NoSuchElementException:
            sleep(2)

driver.quit()