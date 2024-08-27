from faker import Faker
import random
import pandas as pd

fake = Faker()

# Gerando clientes sintéticos

def generate_customers(qtd_customers):
    customers = []
    for i in range(qtd_customers):
        customer = {
            'id': fake.uuid4(),
            'name': fake.name(),
            'email': fake.email(),
            'telefone': fake.phone_number(),
            'age': random.randint(18, 80),
            'monthly_income': round(random.uniform(2000, 50000), 2),
            'account_balance': round(random.uniform(10000, 500000), 2),
        }

        customers.append(customer)
    return pd.DataFrame(customers)

    
if __name__ == "__main__":
    customer_df = generate_customers(100)
    customer_df.to_csv('data/customers.csv', index=False)

