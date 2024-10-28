# def solve(n, k):
#     return 0 if n%2==0 else  1

# t = int(input())
# for i in range(t):
#     arr = input()
#     n , k = int(arr.split(" ")[0]) , int(arr.split(" ")[1])
#     print(solve(n,k))


import pandas as pd
import numpy as np

Card_Master  = pd.DataFrame({
    'Card_no': np.arange(1, 1000001),
    'Customer_name': ['Customer']*1000000,
    'Card_limit': [10000]*1000000,
    'Billing_date': pd.to_datetime('2019-01-01') + pd.to_timedelta(np.random.randint(0, 24*30, size=1000000), unit='D'),
    'Due_date': pd.to_datetime('2019-01-10') + pd.to_timedelta(np.random.randint(0, 24*30, size=1000000), unit='D'),
    'Interest_rate': [0.02]*1000000
})


Transaction_Master = pd.DataFrame({
    'Card_no': np.random.randint(1, 1000001, 5000000),
    'Date_of_transaction': pd.to_datetime('2019-01-01') + pd.to_timedelta(np.random.randint(0, 24*30, size=5000000), unit='D'),
    'Value_of_transaction': np.random.uniform(10, 1000, 5000000),
    'Merchant': ['Merchant']*5000000
})


Paynment_Master = pd.DataFrame({
    'Card_no': np.random.randint(1, 1000001, 3000000),
    'Date_of_payment': pd.to_datetime('2019-01-01') + pd.to_timedelta(np.random.randint(0, 24*30, size=3000000), unit='D'),
    'Value_of_payment': np.random.uniform(10, 1000, 3000000)
})

# Initialize a matrix of shape 1,000,000 x 24 with NaN
Rolling_Matrix = pd.DataFrame(np.nan, index=Card_Master['Card_no'], columns=pd.date_range('2019-01-01', '2020-12-01', freq='MS').strftime('%Y-%m'))


# Calculate rolling balance
for month in Rolling_Matrix.columns:
    month_start = pd.to_datetime(month)
    month_end = month_start + pd.DateOffset(months=1)

    # Get transactions and payments within the month for each card
    transactions_month = Transaction_Master[(Transaction_Master['Date_of_transaction'] >= month_start) &
                                            (Transaction_Master['Date_of_transaction'] < month_end)]
    payments_month = Paynment_Master[(Paynment_Master['Date_of_payment'] >= month_start) &
                                    (Paynment_Master['Date_of_payment'] < month_end)]
    
    # Group by card and calculate total transaction amount and payment amount
    transactions_sum = transactions_month.groupby('Card_no')['Value_of_transaction'].sum()
    payments_sum = payments_month.groupby('Card_no')['Value_of_payment'].sum()
    
    # Calculate rolling balance
    for card_no in Card_Master['Card_no']:
        # Previous month's balance (or 0 if starting from Jan 2019)
        previous_balance = Rolling_Matrix.loc[card_no, pd.date_range(start='2019-01-01', end=month_start, freq='MS').strftime('%Y-%m')].dropna().iloc[-1] if month != '2019-01' else 0
        total_due = previous_balance + transactions_sum.get(card_no, 0)
        minimum_due = 0.1 * total_due  # Assuming minimum due is 10% of total
        paid_amount = payments_sum.get(card_no, 0)
        rolling_balance = total_due - min(total_due, paid_amount)  # Deduct the payment, capped at total due
        Rolling_Matrix.loc[card_no, month] = rolling_balance

# Save the matrix to a file (optional)
Rolling_Matrix.to_csv('rolling_balance_matrix.csv')