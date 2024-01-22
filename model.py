from selenium import webdriver 
from selenium.webdriver.common.by import By 
from time import sleep   
from datetime import datetime, timedelta
import locale 


#options = webdriver.ChromeOptions()
#options.add_experimental_option("detach", True)                         
#driver = webdriver.Chrome(options=options)

#method opens Chrome an logs into Anny
def loginAnny(driver, username, password):
    
    driver.get("https://auth.anny.eu/start-session?entityId=https%3A%2F%2Fidp.scc.kit.edu%2Fidp%2Fshibboleth")

    sleep(1)

    driver.find_element(By.NAME, "j_username").send_keys(username)
    driver.find_element(By.NAME, "j_password").send_keys(password)
    driver.find_element(By.ID, "sbmt").click()

    sleep(1)

    driver.get("https://anny.eu/b/de-formal/book/2-lesesaal-naturwissenschaften-2-og-und-empore?from=community-kit-bibliothek-OTNRQaXc&fromName=KIT-Bibliothek&step=calendar")

    sleep(2)

#method presses the Button in 3 days in Anny   
def setDate(driver, date):
    sleep(2)
    driver.find_element(By.XPATH,'//*[@title="{}"]'.format(date)).click()
    sleep(2)

#method sets Time
def setTime(driver, startTime, endTime):
   
    container = driver.find_elements(By.CLASS_NAME, "eb-scroll-wheel-container")
    sleep(1)
    startelement = container[0].find_elements(By.CLASS_NAME, "eb-scroll-wheel-item")
    sleep(1)
    desired_starttime = [element for element in startelement if startTime in element.text]
    sleep(3)
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", desired_starttime[0])

    sleep(4)

    endelement = container[1].find_elements(By.CLASS_NAME, "eb-scroll-wheel-item")
    desired_endtime = [element for element in endelement if endTime in element.text]
    sleep(3)
    driver.execute_script("arguments[0].scrollIntoView();", desired_endtime[0])

    sleep(2)


#method clicks book button
def bookButton(driver):

    sleep(3)
    bookButtons = driver.find_elements(By.CLASS_NAME, "eb-btn")
    bookButton = [element for element in bookButtons if "Jetzt buchen" in element.text]
    bookButton[0].click()


def choosePlace(driver, place):

    places = driver.find_elements(By.CLASS_NAME, "fa-angle-down")

    places[4].click()

    input_field = driver.find_element(By.ID, "input_208")
    input_field.send_keys(place)
   
        

#method returns date in 3 days in special format
def getDateIn3Days():
    
    current_locale = locale.getlocale()

    try:
        locale.setlocale(locale.LC_TIME, "de_DE")

        current_date = datetime.now()
        date_in_3_days = current_date + timedelta(days=3)

        weekday = date_in_3_days.strftime("%A")
        month = date_in_3_days.strftime("%B")
        day = date_in_3_days.day
        year = date_in_3_days.year

        formatted_date = f"{weekday}, {month} {day}, {year}"

        return formatted_date

    finally:
        
        locale.setlocale(locale.LC_TIME, current_locale)

        

