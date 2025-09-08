import pandas as pd
import numpy as np

np.random.seed(42)
n = 5000
df = pd.DataFrame({
    'ID_Transacao': range(1, n+1),
    'Valor': np.random.uniform(10, 10000, n),
    'Tipo_Transacao': np.random.choice(['Compra', 'Transferencia', 'Pagamento'], n),
    'Localizacao': np.random.choice(['SP', 'RJ', 'MG', 'RS', 'BA', 'PR'], n),
    'Horario': np.random.choice(['Manha', 'Tarde', 'Noite', 'Madrugada'], n),
    'Fraude': np.random.choice([0, 1], n, p=[0.7, 0.3])
})

# 1. Amostragem aleatória simples
amostra_aleatoria = df.sample(n=500)

# 2. Amostragem sistemática (cada 10º registro)
amostra_sistematica = df.iloc[::10]

# 3. Amostragem estratificada por localização (80 de cada)
amostra_estratificada_lista = []
for loc in df['Localizacao'].unique():
    linhas = df[df['Localizacao'] == loc]
    amostra = linhas.sample(n=80)
    amostra_estratificada_lista += list(amostra.index)
amostra_estratificada = df.loc[amostra_estratificada_lista]

# 4. Seleção aleatória de transações fraudulentas e não fraudulentas
fraudulentas = df[df['Fraude'] == 1].sample(n=50)
nao_fraudulentas = df[df['Fraude'] == 0].sample(n=50)
comparacao = pd.concat([fraudulentas, nao_fraudulentas])

# 5. Amostragem por julgamento: transações acima de R$5000
amostra_julgamento = df[df['Valor'] > 5000]

# 6. Amostragem por conglomerados: todas de um tipo sorteado
tipo_escolhido = np.random.choice(df['Tipo_Transacao'].unique())
amostra_conglomerado = df[df['Tipo_Transacao'] == tipo_escolhido]

# 7. Amostragem por conveniência: primeiros 300 registros
amostra_conveniencia = df.head(300)

# 8. Amostragem por cotas: 20 de cada tipo em SP
amostra_cotas_lista = []
for tipo in df['Tipo_Transacao'].unique():
    linhas = df[(df['Tipo_Transacao'] == tipo) & (df['Localizacao'] == 'SP')]
    amostra = linhas.sample(n=20)
    amostra_cotas_lista += list(amostra.index)
amostra_cotas = df.loc[amostra_cotas_lista]

# 9. Comparação simples
print("Média valor aleatória:", amostra_aleatoria['Valor'].mean())
print("Média valor estratificada:", amostra_estratificada['Valor'].mean())
print("Localização aleatória:\n", amostra_aleatoria['Localizacao'].value_counts())
print("Localização estratificada:\n", amostra_estratificada['Localizacao'].value_counts())
