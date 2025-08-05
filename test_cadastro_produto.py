""" from selenium import webdriver 
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("file:///C:/Users/jamilly_froes/Downloads/testesdeSistemas/cadProd.html")

#Preenche o campo Id Produto
id_produto_input= driver.find_element(By.ID, "id")
id_produto_input.send_keys("1")

#Preenche o campo Descrição
descricao_textarea= driver.find_element(By.ID, "descricao")
descricao_textarea.send_keys("Produto de Teste")

#Preenche o campo Marca
marca_input = driver.find_element(By.ID, "marca")
marca_input.send_keys("Marca Teste")

#Preenche o campo Quantidade
quantidade_input= driver.find_element(By.ID, "quantidade")
quantidade_input.send_keys("10")

#Preenche o campo Preço
preco_input = driver.find_element(By.ID, "preco")
preco_input.send_keys("29.99")

time.sleep(8)

driver.quit() """
