from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait  
from selenium.webdriver.support import expected_conditions as EC 
import time
from selenium.webdriver.common.action_chains import ActionChains

driver_path = r'C:\Users\pc\Desktop\WebDriver\chromedriver-win64\chromedriver.exe'  #A changer

service = Service(driver_path)

driver = webdriver.Chrome(service=service)

driver.get('http://localhost:4200')

username_field = driver.find_element(By.ID, 'username')
username_field.send_keys('Admin')  

password_field = driver.find_element(By.ID, 'password')
password_field.send_keys('admin')  

connect_button = driver.find_element(By.XPATH, "//button[contains(text(),'Connecter')]")
connect_button.click()


WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.ID, 'nom')))

driver.find_element(By.ID, 'nom').send_keys('alsk')
time.sleep(2)
driver.find_element(By.ID, 'prenom').send_keys('djde')
time.sleep(2)
driver.find_element(By.ID, 'date-naissance').send_keys('01-12-2009')
time.sleep(2)  
driver.find_element(By.ID, 'nss').send_keys('100544')
time.sleep(2)
driver.find_element(By.ID, 'adresse').send_keys('khkhj')
time.sleep(2)
driver.find_element(By.ID, 'telephone').send_keys('07455')
time.sleep(2)
driver.find_element(By.ID, 'mutuelle').send_keys('lsks')
time.sleep(2)
driver.find_element(By.ID, 'email').send_keys('skzz')
time.sleep(2)



# Étape 1: Cliquer sur l'input pour afficher la liste des médecins
medecin_input = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, "medecin"))
)
medecin_input.click()
time.sleep(2)




# Étape 2: Sélectionner un médecin de la liste
doctor_item = driver.find_element(By.XPATH, "//ul/li[contains(text(),'medecin')]")
ActionChains(driver).move_to_element(doctor_item).double_click().perform()
time.sleep(2)



valider_button = driver.find_element(By.XPATH, "//button[contains(text(),'Valider')]")  
valider_button.click()
time.sleep(1)


WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "swal2-popup"))
    )




confirm_button = driver.find_element(By.XPATH, "//button[contains(text(),'Oui, valider')]")
confirm_button.click()




time.sleep(20)  
driver.quit()



