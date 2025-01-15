from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import os
import pandas as pd

options = webdriver.ChromeOptions()
options.add_experimental_option("prefs", {
  "download.default_directory": r"C:\Users\tesch\downloads",
  "download.prompt_for_download": False,
  "download.directory_upgrade": True,
  "safebrowsing.enabled": True
})

servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico, options=options)

caminho = os.getcwd()
arquivo_login = caminho + r'\login.html'
arquivo_emissao = caminho + r'\NotasEmitir.xlsx'
navegador.get(arquivo_login)

navegador.find_element(By.XPATH, '/html/body/div/form/input[1]').send_keys('login')
navegador.find_element(By.XPATH, '/html/body/div/form/input[2]').send_keys('senha')
navegador.find_element(By.XPATH, '/html/body/div/form/button').click()

df_para_emissao = pd.read_excel(arquivo_emissao)

for linha in df_para_emissao.index:

  #nova tela
  navegador.find_element(By.NAME, 'nome' ).send_keys(df_para_emissao.loc[linha,'Cliente'])
  navegador.find_element(By.NAME, 'endereco' ).send_keys(df_para_emissao.loc[linha,'Endereço'])
  navegador.find_element(By.NAME, 'bairro' ).send_keys(df_para_emissao.loc[linha,'Bairro'])
  navegador.find_element(By.NAME, 'municipio' ).send_keys(df_para_emissao.loc[linha,'Municipio'])
  navegador.find_element(By.NAME, 'cep' ).send_keys(str(df_para_emissao.loc[linha,'CEP']))
  navegador.find_element(By.NAME, 'uf' ).send_keys(df_para_emissao.loc[linha,'UF'])
  navegador.find_element(By.NAME, 'cnpj' ).send_keys(str(df_para_emissao.loc[linha,r'CPF/CNPJ']))
  navegador.find_element(By.NAME, 'inscricao' ).send_keys(str(df_para_emissao.loc[linha,'Inscricao Estadual']))
  navegador.find_element(By.NAME, 'descricao' ).send_keys(df_para_emissao.loc[linha,'Descrição'])
  navegador.find_element(By.NAME, 'quantidade' ).send_keys(str(df_para_emissao.loc[linha,'Quantidade']))
  navegador.find_element(By.NAME, 'valor_unitario' ).send_keys(str(df_para_emissao.loc[linha,'Valor Unitario']))
  navegador.find_element(By.NAME, 'total' ).send_keys(str(df_para_emissao.loc[linha,'Valor Total']))
  #navegador.find_element(By.CLASS_NAME, 'registerbtn' ).click()
  navegador.refresh()