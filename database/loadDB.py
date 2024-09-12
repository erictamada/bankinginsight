import psycopg2
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()

conn = psycopg2.connect(
    dbname=os.getenv("DB_NAME"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    host=os.getenv("DB_HOST"),
    port=os.getenv("DB_PORT")
)
cursor = conn.cursor()

# Inserindo os dados na tabela customers
def insert_customers():
    customers_df = pd.read_csv('data_gen/customers.csv')
    for _, row in customers_df.iterrows():
        cursor.execute("""
        INSERT INTO customers (id, name, email, telefone, age, monthly_income, monthly_expense, risk_taken, investment_duration, financial_goal)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        ON CONFLICT (id) DO NOTHING
        """, tuple(row))
    conn.commit()
    print("Customers data inserted successfully.")

# Inserindo os dados na tabela investments
def insert_investments():
    investments_df = pd.read_csv('data_gen/investments.csv')
    for _, row in investments_df.iterrows():
        cursor.execute("""
        INSERT INTO investments (id, name, type, risk_level, expected_return, duration)
        VALUES (%s, %s, %s, %s, %s, %s)
        ON CONFLICT (id) DO NOTHING
        """, tuple(row))
    conn.commit()
    print("Investments data inserted successfully.")

if __name__ == "__main__":
    insert_customers()
    insert_investments()
    cursor.close()
    conn.close()
