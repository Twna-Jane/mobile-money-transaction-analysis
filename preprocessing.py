import pandas as pd

df = pd.read_csv("synthetic_mobile_money_transaction_dataset.csv")

df_cleaned=df.drop(['initiator','recipient', 'isFraud'], axis=1)

df_cleaned = pd.get_dummies(df_cleaned, columns=['transactionType'], drop_first=True)

df_cleaned.to_csv('cleaned_data.csv', index=False)

print(df_cleaned.head())