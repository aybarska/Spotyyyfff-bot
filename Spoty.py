from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
import random
from time import sleep


#tarayici atama
driver = webdriver.Chrome()
#driver.maximize_window() 
driver.get("https://accounts.spotify.com/tr/login?continue=https://open.spotify.com/playlist/-----------")
#playlist linkiniz buraya gelicek

#zaman

min = 3 #3 saniye
max = 10 #10 saniye
cokmax = 38 #38 saniye



#login islemleri
driver.find_element_by_xpath("//input[@id=\"login-username\"]")\
.send_keys('-----@gmail.com')
sleep(min)

driver.find_element_by_xpath("//input[@id=\"login-password\"]")\
.send_keys('-----')
sleep(min)

#giris bilgileriniz buraya gelecek

driver.find_element_by_xpath("//button[@id=\"login-button\"]").click()
sleep(max)
print('Login basarili.')


#tus atamalari
baslat = ActionChains(driver)
baslat.send_keys(Keys.SPACE)

sonraki = ActionChains(driver)
sonraki.send_keys(Keys.ALT + Keys.ARROW_RIGHT)

onceki = ActionChains(driver)
onceki.send_keys(Keys.ALT + Keys.ARROW_LEFT)

#sesac = ActionChains(driver)
#sesac.send_keys(Keys.ALT + Keys.ARROW_UP)


print('Tus atamalari yapildi.')
sleep(min)
baslat.perform()

#ana dongu
for i in range(300):            
	print('Dongu Basla')
	randomm = random.randint(4, 12)
	print("Rasgle Sayi: ", randomm)
	sleep(min)
	#baslat.perform()
	sonraki.perform()
	print('Sarki1')
	sleep(cokmax + randomm)
	sonraki.perform()
	print('Sarki2')
	sleep(cokmax + randomm)
	sonraki.perform()
	print('Sarki3')
	sleep(cokmax + randomm)
	sonraki.perform()
	print('Sarki4')
	sleep(cokmax + randomm)
	sonraki.perform()
	sleep(min)
	print('Dongu Bit. ')
	print(i)
		
		#bi dongu bosa gidiyor.
		#sarki sayisina gore duzenleyin.

    #yenile.perform()
    

print('1.tur tamam...')


#Random sayi olustur ve classlarla kodu duzenle