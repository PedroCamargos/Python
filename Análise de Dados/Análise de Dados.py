# Passo 1: Importar a base de dados 
import pandas as pd 

tabela = pd.read_csv("clientes.csv", encoding="latin", sep=";")

# Deletar coluna inútil da tabela 
# Axis = 0 -> quando quer deletar uma linha 
# Axis = 1 -> quando quer deletar uma coluna 

tabela = tabela.drop("Unnamed: 8", axis=1)

display(tabela)


# In[ ]:


# Passo 2: Visualizar a base de dados 
    # Entender as informações disponíveis 
    # Procurar as divergências da base de dados  


# In[15]:


# Passo 3: Tratamento de Dados 
    # Valores no formato errado 
tabela["Salário Anual (R$)"] = pd.to_numeric(tabela["Salário Anual (R$)"], errors="coerce")
    
    # Valores vazios (dropna = retira todas as linhas com valores vazios)
tabela = tabela.dropna()    
    
print(tabela.info())       


# In[26]:


# Passo 4: Análise Inicial dos Dados 
pd.set_option('display.float_format', '{:.2f}'.format)
display(tabela.describe())


# In[43]:


# Passo 5: Análise Completa dos Dados 
import plotly.express as px 

# papites: quem ganha mais, é um cliente melhor (com maior nota)
# palpites: cliente que vem por promoção é pior 

# Criação de Gráfico (histfunc = tipo do calculo do eixo y = avg = media)
for coluna in tabela.columns:
    grafico = px.histogram(tabela, x=coluna, y="Nota (1-100)", histfunc="avg", text_auto=True, nbins=10)

# Exibição de Gráfico 
    grafico.show()


# In[ ]:




