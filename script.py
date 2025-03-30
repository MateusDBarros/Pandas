import pandas as pd
import openpyxl

xlsx_path = 'teste.xlsx'

df = pd.read_excel(xlsx_path)
filial = df[['FILIAL']]
valor = df[df['VALOR_TOTAL'] > 1200]
valor2 = df.get('VALOR_TOTAL')



print(filial)
print('-----------------------------')
print(df.head())
print('-----------------------------')
print(valor)