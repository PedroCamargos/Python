
#dados selenium 
#firefox -> geckodriver
# google drive -> chromedriver 

#Passo a Passo 

#Passo 1 Entrar na internet - Abrir o Navegador 
from selenium import webdriver 

navegador = webdriver.Chrome()
navegador.get("https://www.google.com/")

#Passo 2: Importar a base de dados
import pandas as pd 

tabela = pd.read_excel("commodities.xlsx")
display(tabela)

print(list(tabela.index))

#Passo 3: Para cada produto da base de dado
#Passo 4: Pegar o preço atual do produto 
#Passo 5: Atualizar o preço na base de dados 

#comandos xpath
#.send_keys("Pedro Camargos") -> se quiser escrever nesse campo 
#.click() -> se quiser clicar nele 
#.get_attribute() -> pegar a informação dele 

#opção para retirar os carácteres especiais das letras 
#import unicodedata
#link = unicodedata.normalize("NFKD", link).encode("ascci", "ignore")

for linha in tabela.index:
    
    produto = tabela.loc[linha, "Produto"]

    #Entrar no site Melhor Cambio (https://www.melhorcambio.com/milho-hoje)
    link = f"https://www.melhorcambio.com/{produto}-hoje"
    link = link.replace("ó", "o")
    link = link.replace("ã", "a")
    link = link.replace("á", "a")
    link = link.replace("ç", "c")
    link = link.replace("é", "e")
    link = link.replace("ú", "u")
    print(link)
    
    navegador.get(link)

    #Pegar a Cotação atual, (xpath) é o caminho de um elemento seguido pelo código 
    cotacao = navegador.find_element('xpath', '//*[@id="comercial"]').get_attribute('value')
    cotacao = cotacao.replace(".", "")
    cotacao = cotacao.replace(",", ".")
    cotacao = float(cotacao)

    #Na coluna Preço Atual do Milho, preencher a cotação do milho 
    #tabela.loc[linha, coluna ]
    tabela.loc[linha,"Preço Atual"] = cotacao    

#Passo 6: Desidir se irá comprar ou não 
tabela["Comprar"] = tabela["Preço Atual"] < tabela["Preço Ideal"]

display(tabela) 

#Passo 7 - Exportar tabela para excel 

#fechar o navegador 
navegador.quit()

#nome do arquivo em seguida a informação se irá salvar o indice da tabela ou não 
tabela.to_excel("comodities_atualizado.xlsx", index=False)

