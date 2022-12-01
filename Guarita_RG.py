#!/usr/bin/env python
# coding: utf-8

# In[7]:


#!pip install webdriver-manager
#!pip install selenium

import pandas as pd
from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

#def

servico = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service = servico)
driver.get("https://www.mercante.transportes.gov.br/g36127/servlet/serpro.siscomex.mercante.servlet.MercanteController")

try:
    df = pd.read_excel(r'C:\Users\NVG-DSK-RG-06\Desktop\automacao\vazios.xlsx')
    
except:
    df = pd.read_excel(r'C:\Users\NVG-DSK-RG-06\Desktop\automacao\vazios.xls')
    

guarita_rg_dict = df.to_dict(orient = 'index')


# In[6]:


count = 0
frames = driver.find_elements()
driver.switch_to.default_content()
driver.switch_to.frame('Principal')

while count < len(guarita_rg_dict):
    
    driver.switch_to.default_content()
    driver.switch_to.frame('Principal')
    
    e = driver.find_element('xpath', "/html/body/form/table[3]/tbody/tr/td[2]/fieldset/table/tbody/tr[2]/td[1]/input")
    e.send_keys(guarita_rg_dict[count]['Container'])
    print(guarita_rg_dict[count]['Container'])
    sleep(0.3)
    
    e = driver.find_element('xpath', '/html/body/form/table[3]/tbody/tr/td[2]/fieldset/table/tbody/tr[2]/td[2]/input' )
    e.send_keys(guarita_rg_dict[count]['Tara'])
    print(guarita_rg_dict[count]['Tara'])
    sleep(0.3)
    
    e = driver.find_element('xpath', '/html/body/form/table[3]/tbody/tr/td[2]/fieldset/table/tbody/tr[2]/td[3]/input' )
    e.send_keys(guarita_rg_dict[count]['ISO'])
    print(guarita_rg_dict[count]['ISO'])
    
    
    
    e = driver.find_element('xpath', '/html/body/form/table[3]/tbody/tr/td[2]/fieldset/table/tbody/tr[2]/td[5]/input').click()
    
    if count >= len(guarita_rg_dict):
        print('Processo Finalizado')

    else: 
        #input('Aperte enter para prosseguir')

        print('----- next one-----')
    
    count += 1
    
print("PROCESSO FINALIZADO COM ", count, " LINHAS")
    
    
    
    

