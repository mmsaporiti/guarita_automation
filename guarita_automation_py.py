#!/usr/bin/env python
# coding: utf-8

# In[14]:


pip install webdriver-manager


# In[39]:


import pandas as pd
import requests
import os
from time import sleep


# Atualização do webdriver automático - > https://www.youtube.com/watch?v=2EIfXi2-vCI

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


# In[40]:


servico = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service = servico)
driver.get('https://www.mercante.transportes.gov.br/g36127/servlet/serpro.siscomex.mercante.servlet.MercanteController')


# In[41]:


df = pd.read_excel(r'C:\Users\Marcos\Documents\Guarita 0581S.xlsx')


# In[42]:


df.to_csv(r'C:\Users\Marcos\Documents\guarita.csv')


# In[43]:


df.shape


# In[45]:


df.head(3)


# In[46]:


df.columns


# In[81]:


df.dtypes


# In[53]:


lst_ISO = df['ISO'].to_list()
lst_cubagem = []
for item in lst_ISO:
    if item[:2] == '45' or item[:2] == '42':
        lst_cubagem.append('60000')
    elif item[:2] == '22':
        lst_cubagem.append('30000')
    
print(len(lst_cubagem))
df['Cubagem'] = lst_cubagem
df


# In[56]:


df_guarita = df[['ISO', 'Container', 'Tara', 'Peso Bruto', 'NCM', 'Lacre', 'Cubagem' ]]


# In[57]:


df_guarita.head()


# In[85]:


df_guarita.dtypes


# In[58]:


guarita_dict = df_guarita.to_dict(orient = 'index')
guarita_dict


# In[59]:


len(guarita_dict)


# In[113]:


count = 0
while count <= len(guarita_dict):

    for item in guarita_dict[count]:
#ISO        
        # get xpath for ISO
        #e = driver.find_element('xpath', '//*[@id="divCampos"]/fieldset[3]/fieldset[1]/table/tbody/tr[1]/td[2]/input[1]')
        #e.send_keys(guarita_dict[count]['ISO'])
        
        # print confirmação
        print(guarita_dict[count]['ISO'])
        sleep(0.5)

#CONTAINER
        # get xpath for Container 
        #e = driver.find_element('xpath', '//*[@id="divCampos"]/fieldset[3]/fieldset[1]/table/tbody/tr[1]/td[4]/input')
        #e.send_keys(guarita_dict[count]['Container'])

        # print confirmação
        print(guarita_dict[count]['Container'])
        sleep(0.5)

#TARA
        # get xpath for Tara
        #e = driver.find_element('xpath', '//*[@id="divCampos"]/fieldset[3]/fieldset[1]/table/tbody/tr[2]/td[2]/input')
        #e.send_keys(guarita_dict[count]['Tara'])
        
        # print confirmação
        print(guarita_dict[count]['Tara'])
        sleep(0.5)

#PESO_BRUTO
        # get xpath for Peso Bruto
        #e = driver.find_element('xpath', '//*[@id="divCampos"]/fieldset[3]/fieldset[1]/table/tbody/tr[2]/td[4]/input')
        #e.send_keys(guarita_dict[count]['Peso Bruto'])
        
        # print confirmação
        print(guarita_dict[count]['Peso Bruto'])
        sleep(0.5)
        
        
#CUBAGEM
        # startswith
       
        # get xpath for CUBAGEM
        #e = driver.find_element('xpath', '//*[@id="divCampos"]/fieldset[3]/fieldset[1]/table/tbody/tr[3]/td[2]/input')
        #e.send_keys(guarita_dict[count]['Cubagem'])
        
        # print confirmação
        print(guarita_dict[count]['Cubagem'])
        sleep(0.5)
        
# NCM
        ncms = str(guarita_dict[count]['NCM']).split('/')            
        
        # split "/" e loop for para múltiplas inserções
        for item in ncms:
            # get xpath for NCM
            #e = driver.find_element('xpath', '//*[@id="divCampos"]/fieldset[3]/table/tbody/tr/td[1]/fieldset/table/tbody/tr[1]/td[2]/input[1]')
            #e.send_keys(item)
            # get xpath for "incluir"
            #e = driver.find_element('//*[@id="divCampos"]/fieldset[3]/table/tbody/tr/td[1]/fieldset/table/tbody/tr[2]/td/input')
            #e.click()
            print(item)
            sleep(0.5)
        
        
        ##### SE TIVER / INSERIR VÁRIAS VEZES. EX: PRIMEIRA VEZ, ATÉ A BARRA; SEGUNDA VEZ, ATÉ A PRÓXIMA BARRA;
        ### TERCEIRA VEZ, ATÉ A PRÓXIMA BARRA
        
        

        # get xpath for Lacre
        # driver.find_element('xpath', '//*[@id="divCampos"]/fieldset[3]/table/tbody/tr/td[3]/fieldset/table/tbody/tr[1]/td[2]/input')
        
        print(guarita_dict[count]['Lacre'])
        sleep(0.5)
        
        # get xpath for "incluir"
        # driver.find_element('xpath', '//*[@id="divCampos"]/fieldset[3]/table/tbody/tr/td[3]/fieldset/table/tbody/tr[2]/td/input')
        
        print('Click - Clicar em inserir Item.')
        sleep(0.5)
        
        
# ENVIAR ITEM        
        # driver.find_element('xpath', ''=xpath //*[@id="divCampos"]/p[2]/input[1]')
    
# INCLUIR NOVO ITEM - radio button

        # driver.find_element('xpath', '/html/body/form[1]/fieldset[5]/table/tbody/tr/td[1]/input[1]')
        print('marcar inserir novo item')
        sleep(0.5)
        
# ENVIAR
        # driver.find_element('xpath', '/html/body/form[1]/p[2]/input')
        print('clicar em enviar')
        sleep(0.5)

        count += 1

        print('----- next one-----')


# In[ ]:





# In[ ]:





# In[63]:


nnn = "34933223/3243232/1231312"


# In[68]:


nnn = nnn.split('/')


# In[72]:


for item in nnn:
    print(item)


# In[ ]:





# In[ ]:


dict_df = df.to_dict(orient = 'index')


# In[ ]:


dict_df


# In[110]:




