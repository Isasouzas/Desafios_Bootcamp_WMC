# -*- coding: utf-8 -*-
"""Desafio individual - Estatistica WMC - Isabela de Souza Silva.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1YfYPw6evI-gvscJNH6LexRly_ejCZhuq
"""

# Importando minhas bibliotecas do S2:
import pandas as pd
import numpy as np

#Lendo o arquivo js

df = pd.read_json('/content/enem_2023.json')

#Conhecendo o banco de dados que estou lidando
df.head()

df.describe()

df.info()

# Percebi que as tipagens estã ok

# 1. Qual das disciplinas tem a maior amplitude de nota?
#1.1. Calculando a amplitude de cada disciplina:

amplitude_redacao = df['Redação'].max() - df['Redação'].min()
amplitude_matematica = df['Matemática'].max() - df['Matemática'].min()
amplitude_linguagens = df['Linguagens'].max() - df['Linguagens'].min()
amplitude_humanas = df['Ciências humanas'].max() - df['Ciências humanas'].min()
amplitude_natureza = df['Ciências da natureza'].max() - df['Ciências da natureza'].min()

#1.2  Identificando a disciplina com maior amplitude

disciplinas = {
    'Redação': amplitude_redacao,
    'Matemática': amplitude_matematica,
    'Linguagens': amplitude_linguagens,
    'Humanas': amplitude_humanas,
    'Natureza': amplitude_natureza
}

disciplina_maior_amplitude = max(disciplinas, key=disciplinas.get)
print(f"A disciplina com maior amplitude de nota é {disciplina_maior_amplitude} com amplitude de {disciplinas[disciplina_maior_amplitude]:.2f}.")

# 2: Qual é a média e a mediana para cada uma das disciplinas?
# Calculando a média e mediana para cada disciplina
media_mediana = {}
for col in ['Redação', 'Matemática', 'Linguagens', 'Ciências humanas', 'Ciências da natureza']:
    media = df[col].mean()
    mediana = df[col].median()
    media_mediana[col] = {'Média': media, 'Mediana': mediana}

media_mediana_df = pd.DataFrame(media_mediana).T
print(media_mediana_df)

#  3: Qual o desvio padrão e média das notas dos 500 estudantes mais bem colocados considerando os pesos para Ciência da Computação na UFPE?

# Definindo os pesos através de dicinários
pesos = {'Redação': 2, 'Matemática': 4, 'Linguagens': 2,
         'Ciências humanas': 1, 'Ciências da natureza': 1}

# Calculando a média ponderada para cada estudante
df['Média Ponderada'] = (
    df['Redação'] * pesos['Redação'] +
    df['Matemática'] * pesos['Matemática'] +
    df['Linguagens'] * pesos['Linguagens'] +
    df['Ciências humanas'] * pesos['Ciências humanas'] +
    df['Ciências da natureza'] * pesos['Ciências da natureza']
) / sum(pesos.values())

# Ordenando os estudantes pelas maiores médias ponderadas e selecionando os 500 primeiros

top_500 = df.nlargest(500, 'Média Ponderada')

# Calculando o desvio padrão e a média das notas desses 500 estudantes
desvio_padrao = top_500['Média Ponderada'].std()
media_top_500 = top_500['Média Ponderada'].mean()

print(f"Média dos 500 estudantes mais bem colocados: {media_top_500:.2f}")
print(f"Desvio padrão dos 500 estudantes mais bem colocados: {desvio_padrao:.2f}")

# 4: Qual seria a variância e a média da nota dos estudantes que entraram no curso de Ciência da Computação (40 vagas)?

# Selecionando os 40 estudantes com as maiores médias ponderadas
top_40 = top_500.nlargest(40, 'Média Ponderada')

# Calculando a variância e a média das notas desses 40 estudantes
variancia_top_40 = top_40['Média Ponderada'].var()
media_top_40 = top_40['Média Ponderada'].mean()

print(f"Média dos 40 estudantes que entraram no curso: {media_top_40:.2f}")
print(f"Variância das notas dos 40 estudantes que entraram no curso: {variancia_top_40:.2f}")

# 5: Qual o valor do teto do terceiro quartil para as disciplinas de matemática e linguagens?

# Calculando o terceiro quartil para matemática e linguagens
terceiro_quartil_matematica = df['Matemática'].quantile(0.75)
terceiro_quartil_linguagens = df['Linguagens'].quantile(0.75)

print(f"Teto do terceiro quartil para Matemática: {terceiro_quartil_matematica:.2f}")
print(f"Teto do terceiro quartil para Linguagens: {terceiro_quartil_linguagens:.2f}")

#  6: Faça o histograma de Redação e Linguagens, de 20 em 20 pontos. Podemos dizer que são histogramas simétricos? Justifique.

 #Importei as bibliotecas para visualizaçãoide gráficos:

import matplotlib.pyplot as plt
import seaborn as sns

# Plotando os histogramas de Redação e Linguagens
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.hist(df['Redação'].dropna(), bins=range(0, 1001, 20), edgecolor='black')
plt.title('Histograma de Redação')
plt.xlabel('Nota')
plt.ylabel('Frequência')

plt.subplot(1, 2, 2)
plt.hist(df['Linguagens'].dropna(), bins=range(0, 1001, 20), edgecolor='black')
plt.title('Histograma de Linguagens')
plt.xlabel('Nota')
plt.ylabel('Frequência')

plt.tight_layout()
plt.show()

#Percebi que as formas das barras é uniformemente distribuída ao redor do centro, dessa forma o histograma apresenta simetria.

# 7: Agora, coloque um range fixo de 0 até 1000. Você ainda tem a mesma opinião quanto à simetria?

# Plotando os histogramas com range fixo de 0 a 1000
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.hist(df['Redação'].dropna(), bins=range(0, 1001, 20), range=(0, 1000), edgecolor='black')
plt.title('Histograma de Redação (Range Fixo)')
plt.xlabel('Nota')
plt.ylabel('Frequência')

plt.subplot(1, 2, 2)
plt.hist(df['Linguagens'].dropna(), bins=range(0, 1001, 20), range=(0, 1000), edgecolor='black')
plt.title('Histograma de Linguagens (Range Fixo)')
plt.xlabel('Nota')
plt.ylabel('Frequência')

plt.tight_layout()
plt.show()

# 8: Faça um boxplot do quartil de todas as disciplinas de Ciências da Natureza e Redação. É possível enxergar outliers? Utilize o método IQR.

# Plotando o boxplot para Ciências da Natureza e Redação
plt.figure(figsize=(8, 6))
sns.boxplot(data=df[['Ciências da natureza', 'Redação']].dropna())
plt.title('Boxplot de Ciências da natureza e Redação')
plt.show()

# Calculando o IQR e os outliers :)
def calcular_outliers(coluna):
    Q1 = df[coluna].quantile(0.25)
    Q3 = df[coluna].quantile(0.75)
    IQR = Q3 - Q1
    limite_inferior = Q1 - 1.5 * IQR
    limite_superior = Q3 + 1.5 * IQR
    outliers = df[(df[coluna] < limite_inferior) | (df[coluna] > limite_superior)]
    return outliers

outliers_redacao = calcular_outliers('Redação')
outliers_natureza = calcular_outliers('Ciências da natureza')

print(f"Número de outliers em Redação: {len(outliers_redacao)}")
print(f"Número de outliers em Ciências da Natureza: {len(outliers_natureza)}")

# 9: Remova todos os outliers e verifique se eles são passíveis de alterar a média nacional significativamente (considerando significativamente um valor acima de 5%).

# Removendo os outliers "abençoados"
df_sem_outliers = df[~df.index.isin(outliers_redacao.index.union(outliers_natureza.index))]

# Calculando a média nacional antes e depois de remover os outliers
media_nacional_antes = df[['Redação', 'Ciências da natureza']].mean()
media_nacional_depois = df_sem_outliers[['Redação', 'Ciências da natureza']].mean()

# Verificando a diferença percentual
diferenca_percentual = ((media_nacional_depois - media_nacional_antes) / media_nacional_antes).abs() * 100

print(f"Alteração percentual nas médias após remover outliers:\n{diferenca_percentual}")

#  10: Substituir os valores nulos pelas medidas de tendência central (média, moda, mediana) e verificar qual delas altera menos a média geral e o desvio padrão

# Substituindo valores nulos por média, moda e mediana
df_media = df.fillna(df.mean(numeric_only=True))  # Substitui valores nulos pela média
df_moda = df.fillna(df.mode(numeric_only=True).iloc[0])  # Substitui valores nulos pela moda (primeiro valor de moda)
df_mediana = df.fillna(df.median(numeric_only=True))  # Substitui valores nulos pela mediana

# Calculando a média geral e desvio padrão para cada método
media_geral_media = df_media.mean(numeric_only=True).mean()
media_geral_moda = df_moda.mean(numeric_only=True).mean()
media_geral_mediana = df_mediana.mean(numeric_only=True).mean()

desvio_padrao_media = df_media.std(numeric_only=True).mean()
desvio_padrao_moda = df_moda.std(numeric_only=True).mean()
desvio_padrao_mediana = df_mediana.std(numeric_only=True).mean()

print(f"Média geral após substituir por média: {media_geral_media:.2f}, Desvio padrão: {desvio_padrao_media:.2f}")
print(f"Média geral após substituir por moda: {media_geral_moda:.2f}, Desvio padrão: {desvio_padrao_moda:.2f}")
print(f"Média geral após substituir por mediana: {media_geral_mediana:.2f}, Desvio padrão: {desvio_padrao_mediana:.2f}")