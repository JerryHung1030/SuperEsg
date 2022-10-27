from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import random
from datetime import datetime
import sys
import os

def hover_clear_fillIn( browser, element, value) :
    ActionChains(browser).move_to_element(element).perform()
    element.clear()
    element.send_keys(value)

def validate(date_text):
        try:
            datetime.strptime(date_text, '%Y-%m-%d')
        except ValueError:
            raise ValueError("Incorrect data format, should be YYYY-MM-DD")

# set default value
specifiedDate = False
browser = webdriver.Chrome(ChromeDriverManager().install() )
options = webdriver.ChromeOptions()
options.headless = True
formCount = 0
if (datetime.today().isoweekday() == 1) :
    howManyDaysBeforeShouldBeFillin = 2
else :
    howManyDaysBeforeShouldBeFillin = 0

# set arguments
for i in range(1, len(sys.argv)):
    if (sys.argv[i] == '-daysbefore') :
        howManyDaysBeforeShouldBeFillin = int(sys.argv[i+1])
        i += 1
    elif (sys.argv[i] == '-specify') :
        validate(sys.argv[i+1])
        specifiedDate = True
        i += 1
    else :
        print('Error : Arguments input Error......')
        os._exit()
    '''
    elif (sys.argv[i] == '-browser') :
        if (sys.argv[i+1] == 's')
            browser = webdriver.Safari()
        elif (sys.args[i+1] == 'c') :
            browser = webdriver.Chrome(ChromeDriverManager().install() )
        else :
            print('Error : Brower Setting Error......')
            os._exit()
        i += 1
    '''


# fill in 0-2 form(s)
while (howManyDaysBeforeShouldBeFillin >= 0) :
    print('Open browser...')
    print('Start to fillin form...')

    url = "http://eepsrv/JQWebClient/RWDMainFlowPage.aspx?"
    browser.get(url)

    # log in esp
    loginButton = browser.find_element("xpath", "//*[@id='ok']")
    loginButton.click()
    WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='collapse_0']/div/div/div[10]/a"))).click()
    print('Login Seccussfully...')

    # change iframe into iframe
    esgiframe = browser.find_element(By.CSS_SELECTOR, "#menu_92 > iframe")
    browser.switch_to.frame(esgiframe)

    # get all elements
    date = browser.find_element("id","dfMaster_date")
    plasticBag = browser.find_element("id","dfMaster_e1_1")
    plasticCup = browser.find_element("id","dfMaster_e2_1")
    lunchBox = browser.find_element("id","dfMaster_e3_1")
    chopsticks = browser.find_element("id","dfMaster_e4_1")
    coffee = browser.find_element("id","dfMaster_e5_1")
    drink = browser.find_element("id","dfMaster_e6_1")
    elevator = browser.find_element("id","dfMaster_e7_1")
    papper = browser.find_element("id","dfMaster_e8_1")
    light = browser.find_element("id","dfMaster_e9_1")
    letter = browser.find_element("id","dfMaster_d6_1")
    carton = browser.find_element("id","dfMaster_d6_2")
    foilPack = browser.find_element("id","dfMaster_d8_1")
    receipt = browser.find_element("id","dfMaster_d8_2")
    glassBottle = browser.find_element("id","dfMaster_d7_1")
    bottle = browser.find_element("id","dfMaster_d7_2")

    # get date info
    if ( specifiedDate ) :
        fillInDate = sys.argv[1]
    else :
        now = datetime.now() 
        year = now.strftime("%Y")
        month = now.strftime("%m")
        day = str(int(now.strftime("%d"))-howManyDaysBeforeShouldBeFillin)
        fillInDate = year+'-'+month+'-'+day

    # fill in
    print('Start fillIn random data...')
    hover_clear_fillIn(browser, date, fillInDate)
    hover_clear_fillIn(browser, plasticBag, random.randint(0,1))
    hover_clear_fillIn(browser, plasticCup, random.randint(0,1))
    hover_clear_fillIn(browser, lunchBox, random.randint(0,1))
    hover_clear_fillIn(browser, chopsticks, random.randint(0,1))
    hover_clear_fillIn(browser, coffee, random.randint(0,1))
    hover_clear_fillIn(browser, drink, random.randint(0,1))
    hover_clear_fillIn(browser, elevator, random.randint(0,1))
    hover_clear_fillIn(browser, papper, random.randint(0,2))
    hover_clear_fillIn(browser, light, random.randint(0,1))
    hover_clear_fillIn(browser, letter, random.randint(0,1))
    hover_clear_fillIn(browser, carton, '0')
    hover_clear_fillIn(browser, foilPack, random.randint(0,1))
    hover_clear_fillIn(browser, receipt, random.randint(0,3))
    hover_clear_fillIn(browser, glassBottle, '0')
    hover_clear_fillIn(browser, bottle, random.randint(0,1))
    
    offPower = browser.find_element("id","dfMaster_e10_1")
    walk = browser.find_element("id","dfMaster_e11_1")
    offLight = browser.find_element("id","dfMaster_e12_1")
    
    if ( random.randint(0,1) ) :
        browser.execute_script("arguments[0].click();", offPower)
    if ( random.randint(0,1) ) :
        browser.execute_script("arguments[0].click();", walk)
    if ( random.randint(0,1) ) :
        browser.execute_script("arguments[0].click();", offLight)
    print('finish fillin form...')    

    submitBtn = browser.find_element("xpath", "//*[@id='dfMaster']/div/div/div[3]/button[2]")
    submitBtn.click()
    print('Submit form Seccussfully...')

    time.sleep(10)
    print('Close the browser...')
    browser.quit()
    howManyDaysBeforeShouldBeFillin -= 1