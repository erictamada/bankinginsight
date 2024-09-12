from faker import Faker
import random
import pandas as pd

fake = Faker("pt-br")

# Gerando clientes sintéticos

def generate_customers(qtd_customers):
    customers = []
    for i in range(qtd_customers):
        monthly_income = round(random.uniform(1500, 20000), 2)

        # Regra para gasto mensal com base na renda
        if monthly_income <= 5000:
            monthly_expense = round(random.uniform(1000, 0.8 * monthly_income), 2)
            risk_taken = random.choice(['Low', 'Medium'])
        elif monthly_income <= 15000:
            monthly_expense = round(random.uniform(0.5 * monthly_income, 0.7 * monthly_income), 2)
            risk_taken = random.choice(['Medium', 'High'])
        else:
            monthly_expense = round(random.uniform(0.5 * monthly_income, 0.7 * monthly_income), 2)
            risk_taken = 'High'


        customer = {
            'id': fake.uuid4(),
            'name': fake.name(),
            'email': fake.email(),
            'telefone': fake.phone_number(),
            'age': random.randint(18, 80),
            'monthly_income': monthly_income,
            'monthly_expense': monthly_expense,
            'risk_taken': risk_taken,
            'investment_duration': random.choice(['Short Term', 'Medium Term', 'Long Term']),
            'financial_goal': random.choice(['Retirement', 'Home Purchase', 'Car Purchase', 'Education', 'Emergency Fund', 'Entrepreneurship']) 
        }

        customers.append(customer)
    return pd.DataFrame(customers)
    
if __name__ == "__main__":
    customer_df = generate_customers(1000)
    customer_df.to_csv('data_gen/customers.csv', index=False)


