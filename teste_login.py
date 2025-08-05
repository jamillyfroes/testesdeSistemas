from selenium import webdriver 
from selenium.webdriver.common.by import By
import time

driver= webdriver.Chrome()
driver.get("http://localhost:8080/testesdeSistemas/login.html")
time.sleep(2)

#Preenche os campos
driver.find_element(By.ID,"username").send_keys("admin")
driver.find_element(By.ID,"password").send_keys("123456")
driver.find_element(By.CSS_SELECTOR,"button[type='submit']").click()

time.sleep(5)

if "Cadastro de Cliente" in driver.page_source:
    print("Login realizado com sucesso!")
else:
    print("Falha no login.")

""" #Preenche o campo de usuário
usuario_input= driver.find_element(By.ID, "username")
usuario_input.send_keys("admin")

#Preenche o campo de senha
senha_input= driver.find_element(By.ID, "password")
senha_input.send_keys("123456")

# Clica no botão de login
botao_login= driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
botao_login.click()

time.sleep(8)
if "Cadastro de Cliente" in driver.page_source:
    print("Login realizado com sucesso e redirecionando para index.html!")
else:
    print("Falha no login ou redirecionamento.")

print("Título atual da página:", driver.title)  """   

#encerra o navegador
#driver.quit()