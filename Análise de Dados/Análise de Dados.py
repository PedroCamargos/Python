# Passo 1: Importar a base de dados 
import pandas as pd 

tabela = pd.read_csv("clientes.csv", encoding="latin", sep=";")

# Deletar coluna inútil da tabela 
# Axis = 0 -> quando quer deletar uma linha 
# Axis = 1 -> quando quer deletar uma coluna 

tabela = tabela.drop("Unnamed: 8", axis=1)

print(tabela)

      ClienteID    Origem  Idade Salário Anual (R$)  Nota (1-100)  
0             1    Normal     19              15000            39   
1             2    Normal     21              35000            81   
2             3  Promoção     20              86000             2   
3             4  Promoção     23              59000            73   
4             5  Promoção     31              38000            48   
...         ...       ...    ...                ...           ...   
1995       1996  Promoção     71             184387            48   
1996       1997  Promoção     91              73158            28   
1997       1998    Normal     87              90961            14   
1998       1999    Normal     77             182109             4   
1999       2000    Normal     90             110610            64

           Profissão  Experiência Trabalho  Tamanho Família  
0              Saúde                     1                4  
1         Engenheiro                     3                3  
2         Engenheiro                     1                1  
3           Advogado                     0                2  
4     Entretenimento                     2                6  
...              ...                   ...              ...  
1995         Artista                     8                7  
1996          Doutor                     7                7  
1997           Saúde                     9                2  
1998       Executivo                     7                2  
1999  Entretenimento                     5                2  

[2000 rows x 8 columns]

# Passo 2: Visualizar a base de dados 
    # Entender as informações disponíveis 
    # Procurar as divergências da base de dados  
    
# Passo 3: Tratamento de Dados 
    # Valores no formato errado 
tabela["Salário Anual (R$)"] = pd.to_numeric(tabela["Salário Anual (R$)"], errors="coerce")
    
    # Valores vazios (dropna = retira todas as linhas com valores vazios)
tabela = tabela.dropna()    
    
print(tabela.info())        

<class 'pandas.core.frame.DataFrame'>
Int64Index: 1965 entries, 0 to 1999
Data columns (total 8 columns):
 #   Column                Non-Null Count  Dtype  
---  ------                --------------  -----  
 0   ClienteID             1965 non-null   int64  
 1   Origem                1965 non-null   object 
 2   Idade                 1965 non-null   int64  
 3   Salário Anual (R$)    1965 non-null   float64
 4   Nota (1-100)          1965 non-null   int64  
 5   Profissão             1965 non-null   object 
 6   Experiência Trabalho  1965 non-null   int64  
 7   Tamanho Família       1965 non-null   int64  
dtypes: float64(1), int64(5), object(2)
memory usage: 138.2+ KB
None

# Passo 4: Análise Inicial dos Dados 
pd.set_option('display.float_format', '{:.2f}'.format)
display(tabela.describe())

       ClienteID   Idade  Nota (1-100)  Experiência Trabalho  Tamanho Família
count    2000.00 2000.00       2000.00               2000.00          2000.00
mean     1000.50   48.96         52.17                  3.69             3.77
std       577.49   28.43         28.58                  3.91             1.97
min         1.00    0.00          1.00                  0.00             1.00
25%       500.75   25.00         29.00                  0.00             2.00
50%      1000.50   48.00         52.00                  1.00             4.00
75%      1500.25   73.00         76.00                  7.00             5.00
max      2000.00   99.00        100.00                 17.00             9.00

# Passo 5: Análise Completa dos Dados 
import plotly.express as px 

# papites: quem ganha mais, é um cliente melhor (com maior nota)
# palpites: cliente que vem por promoção é pior 

# Criação de Gráfico (histfunc = tipo do calculo do eixo y = avg = media)
for coluna in tabela.columns:
    grafico = px.histogram(tabela, x=coluna, y="Nota (1-100)", histfunc="avg", text_auto=True, nbins=10)

# Exibição de Gráfico 
    grafico.show()

# Perfil ideal de cliente 
# Clientes acima de 10 anos 
# Entretenimento, Artista, e Marketing, são as profissões ideais para os nossos clientes, (evitar construção) 
# Clientes entre 10 e 15 anos de experiencia de trabalho são os melhores 
# Familias com até 7 pessoas 

# Obs Final 
# O salário não parece fazer muita diferença. Clientes de promoção parecem ter uma leve nota menor, mas não tanto
