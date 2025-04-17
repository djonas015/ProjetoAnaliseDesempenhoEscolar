import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('desempenhoescolar.csv')


def classificar(nota):
    if nota == 10:
        return "Excelente"
    elif nota >= 9:
        return "Bom"
    elif nota >= 8:
        return "Ok"
    elif nota >= 6:
        return "Regular"
    elif nota < 6:
        return "Insatisfatório"
     
     
df['desempenho'] = df['nota'].apply(classificar)
print("\nTabela com situação de desempenho:")
print(df[['nome', 'nota', 'disciplina', 'bimestre', 'desempenho']])

notamin = df['nota'].min()
alunomin = df[df['nota'] == notamin]['nome'].tolist()
print(f"Menor nota: {notamin} - Alunos: {', '.join(alunomin)}")

notamax = df['nota'].max()
alunomax = df[df['nota'] == notamax]['nome'].tolist()
print(f"Maior nota: {notamax} - Alunos: {', '.join(alunomax)}")

mediageral = df['nota'].mean()
print(f"Média geral do bimestre: {mediageral:.2f}")

mediadedesempenho = df['desempenho'].mode()[0]
print(f"Média geral de desempenho do bimestre: {mediadedesempenho}")

df['desempenho'].value_counts().plot(kind='bar', color='skyblue', edgecolor='black')
plt.title('Distribuição de desempenho dos Alunos')
plt.xlabel('Desempenho')
plt.ylabel('Número de alunos')
plt.xticks(rotation=45)
plt.tight_layout()
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.savefig('grafico_desempenho.png', dpi=300)
plt.show()

df.to_csv('resultado_final.csv', index=False)
