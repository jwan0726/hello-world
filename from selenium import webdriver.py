from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait #wait thingy
from selenium.webdriver.support import expected_conditions as EC # element for wait
from selenium.webdriver.common.by import By # samesame
from selenium.webdriver.common.keys import Keys #controls the keys of the keyboard
from selenium.webdriver.chrome.options import Options #cookieee
import time
import pyperclip


PATH= "C:\Program Files (x86)\chromedriver.exe"
#F_Prof=r"C:\Users\jason\AppData\Local\Google\Chrome\User Data\Profile 1"


options = webdriver.ChromeOptions()
options.add_argument("profile-directory=") #+ F_Prof)

driver=webdriver.Chrome(PATH)#, chrome_options=options)
driver.maximize_window()
driver.get('https://web.whatsapp.com/')


with open('contacts.txt','r',encoding='utf8') as f:
    groups=[group.strip() for group in f.readlines()]

# Mass messaging in Whatsapp,list is ready
with open('msg.txt','r', encoding='utf8') as f:
    msgs=[msg.strip() for msg in f.readlines()]

for group in groups:  
    search_xpath='//*[@id="side"]/div[1]/div/label/div/div[2]' #searchbox xpath
#Use the Wait element fx
    
    search_box = WebDriverWait(driver, 500).until(
        EC.presence_of_element_located((By.XPATH, search_xpath))
    )
#     chee_xpath='//*[@id="pane-side"]/div[1]/div/div/div[1]/div/div/div[2]/div[1]/div[1]/span/span'
#     chee_title=driver.find_element_by_xpath(chee_xpath)


# chee_title.click()
for hehehaha in groups:
    # newchat_xpath='//*[@id="side"]/header/div[2]/div/span/div[2]/div/span' # need click this icon
    # '//*[@id="app"]/div[1]/div[1]/div[2]/div[1]/span/div[1]/span/div[1]/div[2]/div[2]/div/div/div[10]/div/div/div[2]/div[1]/div/span'
    # driver.find_element_by_xpath(search_box).click()
    # driver.find_element_by_xpath(search_box).send_keys(hehehaha)
    # time.sleep(1)
    driver.find_element_by_xpath("//*[@title='"+ hehehaha+ "']").click() # change @Title='xxx'to the name u want


#type something in textbox and click the send button, then loop the next line untill the document is finished

    textbox_xpath='/html/body/div[1]/div[1]/div[1]/div[4]/div[1]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]'
    click_button_xpath='//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button'

    for msg in msgs:
        driver.find_element_by_xpath(textbox_xpath).send_keys(msg)
        driver.find_element_by_xpath(click_button_xpath).click()
        time.sleep(2)
    time.sleep(5)


driver.close()