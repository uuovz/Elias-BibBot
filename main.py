import login_data  
import model     
from selenium import webdriver 
from selenium.webdriver.common.by import By   
from time import sleep  
import threading            


def process_user_data(user_data):
#for user_data in login_data.peopleArray:
    
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)                         
    driver = webdriver.Chrome(options=options)

    model.loginAnny(driver, username=user_data[0], password=user_data[1])

    model.setDate(driver, model.getDateIn3Days())

    model.setTime(driver, "13:00", "18:00")

    model.choosePlace(driver, place=user_data[2])

    sleep(3)

    driver.close()

    #model.bookButton(driver)

   
threads = []
for user_data in login_data.peopleArray:
    thread = threading.Thread(target=process_user_data, args=(user_data,))
    threads.append(thread)
    thread.start()


for thread in threads:
    thread.join()




