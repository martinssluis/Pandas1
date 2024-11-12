import pandas as pd

#Read the file 
df = pd.read_excel('testWorkbook.xlsx')

# Split the columns
df_splited = df.iloc[:, 0].str.split(',', expand=True)
df_splited.columns = ['account', 'name', 'ssn', 'date_birth', 'account_balance']

#Convertions 
df_splited['account_balance'] = pd.to_numeric(df_splited['account_balance'], errors='coerce')
df_splited['date_birth'] = pd.to_datetime(df_splited['date_birth'], errors='coerce')

#Query

deadline = pd.to_datetime('1990-01-01')
results = df_splited[df_splited['date_birth']> deadline]
premium_customers = df_splited[df_splited['account_balance'] > 2500.00]
total_value = df_splited['account_balance'].sum()
query_ssn = df_splited[df_splited['ssn'] == '678.901.234-05']

#Output
print(query_ssn[['name', 'ssn']])
#print(results[['name', 'date_birth']])
#print(f"The premium costumers,those who have more than R$2500.00 in their account: {premium_customers[['name', 'account_balance']]}")
#print(f"Total amount in the bank is: {total_value}")
#print(df_splited)
