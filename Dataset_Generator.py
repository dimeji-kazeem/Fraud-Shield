import pandas as pd
import numpy as np
from faker import Faker

# Initialize Faker for generating fake customer information
fake = Faker()

# Set random seed for reproducibility
np.random.seed(42)

# Generate 10,000 records of financial transactions
num_records = 10000

# Create an empty DataFrame to store the transaction data
data = pd.DataFrame(columns=['transaction_id', 'customer_id', 'transaction_amount', 'transaction_timestamp', 'region', 'state', 'customer_category', 'account_balance'])

# Generate the transaction data
for i in range(num_records):
    transaction_id = i + 1
    customer_id = fake.uuid4()
    transaction_amount = round(np.random.uniform(1, 10000), 2)
    transaction_timestamp = fake.date_time_between(start_date='-1y', end_date='now')
    
    # Generate region
    region = np.random.choice(['Europe (UK)', 'Europe (Germany)', 'Europe (Sweden)', 'Europe (Ireland)',
                              'South America (Mexico)', 'South America (Brazil)',
                              'Africa (Nigeria)', 'Africa (South Africa)', 'Africa (Kenya)', 'Africa (Ghana)',
                              'North America (USA)', 'North America (Canada)'])
    
    # Generate state based on the region
    if 'Europe' in region:
        state = np.random.choice(['UK', 'Germany', 'Sweden', 'Ireland'])
    elif 'South America' in region:
        state = np.random.choice(['Mexico', 'Brazil'])
    elif 'Africa' in region:
        state = np.random.choice(['Nigeria', 'South Africa', 'Kenya', 'Ghana'])
    elif 'North America' in region:
        state = np.random.choice(['USA', 'Canada'])
    
    # Generate customer category
    customer_category = np.random.choice(['High-Profile', 'Medium-Profile', 'Low-Profile'])
    
    # Generate account balance based on customer category
    if customer_category == 'High-Profile':
        account_balance = round(np.random.uniform(10000, 100000), 2)
    elif customer_category == 'Medium-Profile':
        account_balance = round(np.random.uniform(5000, 10000), 2)
    elif customer_category == 'Low-Profile':
        account_balance = round(np.random.uniform(0, 5000), 2)
    
    # Append the transaction record to the DataFrame
    data = data.append({
        'transaction_id': transaction_id,
        'customer_id': customer_id,
        'transaction_amount': transaction_amount,
        'transaction_timestamp': transaction_timestamp,
        'region': region,
        'state': state,
        'customer_category': customer_category,
        'account_balance': account_balance
    }, ignore_index=True)

# Export the DataFrame to a CSV file
data.to_csv('financial_transactions.csv', index=False)
