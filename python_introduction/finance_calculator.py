monthly_income = float(input("Enter your monthly income: "))
monthly_expenses = float(input("Enter your total monthly expenses: "))
annual_interest = 0.05
monthly_savings = monthly_income - monthly_expenses
projected_savings = (monthly_savings * 12) + (monthly_savings*12* annual_interest)
print(f'''
    Your monthly savings are ${monthly_savings}
    Projected savings after one year, with interest, is: ${projected_savings}
    ''')