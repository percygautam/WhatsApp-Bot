# Note: For proper working of this Script Good and Uninterepted Internet Connection is Required
# Or else increase the time duration between commands


# Import required packages
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
# Declare global variables
global gpmembers
global gpname
gpmembers=[]
gpname=[]

def mainfun():
    # Driver to open a browser
    # different drivers are used for different web browsers
    # download the driver of your browser and specify the path directory of where executable 
    # file is stored
    #use if firefox is used
    #driver = webdriver.Firefox()# Enter the path of driver in bracket as string 
    driver = webdriver.Chrome("/Enter/the/path/of/driver")# Enter the path of chrome driver in bracket as string
    #link to open the WhatsApp web site
    driver.get("https://web.whatsapp.com/")
    # 10 sec wait time to load, if good internet connection is not good then increase the time
    # units in seconds
    # note this time is being used below also
    wait = WebDriverWait(driver, 10)
    wait5 = WebDriverWait(driver, 5)
    input("Scan the QR code and then press Enter")

    # utility variables to tract count of success and fails
    success=0
    sNo = 1
    failList = []

    # Click the add new group option in the whatsapp web
    driver.find_element_by_xpath('//*[@id="side"]/header/div[2]/div/span/div[3]/div').click()
    driver.find_element_by_xpath('//*[@id="side"]/header/div[2]/div/span/div[3]/span/div/ul/li[1]/div').click()
    # Iterate over selected contact
    for target in gpmembers:
        print(sNo, ". Target is: " + target)
        sNo+=1
        # Selecting the search box
        inp_xpath = "//*[@id='app']/div/div/div[2]/div[1]/span/div/span/div/div/div[1]/div/div/input"
        input_box = wait.until(EC.presence_of_element_located((By.XPATH, inp_xpath)))
        #Entering the participant name in the search box
        input_box.send_keys(target)
        time.sleep(1)
        target = "\"" + target + "\""
        # Selecting the name from list
        x_arg = '//span[contains(@title,' + target + ')]'
        # To check if the name is in your contact list
        try:
            #wait5.until(EC.presence_of_element_located(( By.XPATH, x_arg )))
            input_box.send_keys(Keys.ENTER)
            print(target + " successfully added")
            success += 1
            time.sleep(1)
        except:
            # Adds name to fail list if not found in contact list
            print(target + " is not found in your contact list")
            input_box.clear()
            failList.append(target)
    # To check if all the names are not found in contact list       
    if(len(failList) != len(gpmembers)):
        driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[1]/span/div/span/div/div/span/div/span').click()
        time.sleep(1)
        inp_xpath = "//*[@id='app']/div/div/div[2]/div[1]/span/div/span/div/div/div[2]/div/div[2]/div/div[2]"
        input_box = wait.until(EC.presence_of_element_located((By.XPATH, inp_xpath)))
        time.sleep(1)
        input_box.send_keys(gpname[0] + Keys.ENTER)
        time.sleep(3)
        print("Group successfully created")
    # Print all the details of extraction
    print('\n')
    print("Number of participants added in the group : " + str(success))
    print("Number of Failed participants : " + str(len(failList)))
    print("Failed participants are : ")
    for i in range(1, len(failList)+1):
        print(str(i) + " : " + failList[i-1])
    print('\n')
    driver.quit()

