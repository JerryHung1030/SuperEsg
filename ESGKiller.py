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

def hover_clear_fillIn( chrome, element, value) :
    ActionChains(chrome).move_to_element(element).perform()
    element.clear()
    element.send_keys(value)

def validate(date_text):
        try:
            datetime.strptime(date_text, '%Y-%m-%d')
        except ValueError:
            raise ValueError("Incorrect data format, should be YYYY-MM-DD")

# on monday, it will also fillin form on Sunday and Saturday
if (datetime.today().isoweekday() == 1) :
    howManyDaysBeforeShouldBeFillin = 2
else :
    howManyDaysBeforeShouldBeFillin = 0

specifiedDate = False
# check if arg a valid date
if (len(sys.argv) == 2) :
    validate(sys.argv[1])
    howManyDaysBeforeShouldBeFillin = 0
    specifiedDate = True
elif  (len(sys.argv) > 2) :
    print('args count error')
    os._exit()

# fill in 0-2 form(s)
while (howManyDaysBeforeShouldBeFillin >= 0) :
    print('Open chrome...')
    print('Start to fillin form...')
    options = webdriver.ChromeOptions()
    options.headless = True
    url = "http://eepsrv/JQWebClient/RWDMainFlowPage.aspx?"
    chrome = webdriver.Chrome(ChromeDriverManager().install(), options=options )
    chrome.get(url) 

    # log in esp
    loginButton = chrome.find_element("xpath", "//*[@id='ok']")
    loginButton.click()
    WebDriverWait(chrome, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='collapse_0']/div/div/div[10]/a"))).click()
    print('Login Seccussfully...')

    # change iframe into iframe
    esgiframe = chrome.find_element(By.CSS_SELECTOR, "#menu_92 > iframe")
    chrome.switch_to.frame(esgiframe)

    # get all elements
    date = chrome.find_element("id","dfMaster_date")
    plasticBag = chrome.find_element("id","dfMaster_e1_1")
    plasticCup = chrome.find_element("id","dfMaster_e2_1")
    lunchBox = chrome.find_element("id","dfMaster_e3_1")
    chopsticks = chrome.find_element("id","dfMaster_e4_1")
    coffee = chrome.find_element("id","dfMaster_e5_1")
    drink = chrome.find_element("id","dfMaster_e6_1")
    elevator = chrome.find_element("id","dfMaster_e7_1")
    papper = chrome.find_element("id","dfMaster_e8_1")
    light = chrome.find_element("id","dfMaster_e9_1")
    letter = chrome.find_element("id","dfMaster_d6_1")
    carton = chrome.find_element("id","dfMaster_d6_2")
    foilPack = chrome.find_element("id","dfMaster_d8_1")
    receipt = chrome.find_element("id","dfMaster_d8_2")
    glassBottle = chrome.find_element("id","dfMaster_d7_1")
    bottle = chrome.find_element("id","dfMaster_d7_2")

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
    hover_clear_fillIn(chrome, date, fillInDate)
    hover_clear_fillIn(chrome, plasticBag, random.randint(0,1))
    hover_clear_fillIn(chrome, plasticCup, random.randint(0,1))
    hover_clear_fillIn(chrome, lunchBox, random.randint(0,1))
    hover_clear_fillIn(chrome, chopsticks, random.randint(0,1))
    hover_clear_fillIn(chrome, coffee, random.randint(0,1))
    hover_clear_fillIn(chrome, drink, random.randint(0,1))
    hover_clear_fillIn(chrome, elevator, random.randint(0,1))
    hover_clear_fillIn(chrome, papper, random.randint(0,2))
    hover_clear_fillIn(chrome, light, random.randint(0,1))
    hover_clear_fillIn(chrome, letter, random.randint(0,1))
    hover_clear_fillIn(chrome, carton, '0')
    hover_clear_fillIn(chrome, foilPack, random.randint(0,1))
    hover_clear_fillIn(chrome, receipt, random.randint(0,3))
    hover_clear_fillIn(chrome, glassBottle, '0')
    hover_clear_fillIn(chrome, bottle, random.randint(0,1))
    
    offPower = chrome.find_element("id","dfMaster_e10_1")
    walk = chrome.find_element("id","dfMaster_e11_1")
    offLight = chrome.find_element("id","dfMaster_e12_1")
    
    if ( random.randint(0,1) ) :
        chrome.execute_script("arguments[0].click();", offPower)
    if ( random.randint(0,1) ) :
        chrome.execute_script("arguments[0].click();", walk)
    if ( random.randint(0,1) ) :
        chrome.execute_script("arguments[0].click();", offLight)
    print('finish fillin form...')    

    submitBtn = chrome.find_element("xpath", "//*[@id='dfMaster']/div/div/div[3]/button[2]")
    submitBtn.click()
    print('Submit form Seccussfully...')

    time.sleep(10)
    print('Close the chrome...')
    chrome.quit()
    howManyDaysBeforeShouldBeFillin -= 1