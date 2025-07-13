income = int(input("Enter your monthly income: "))
expenses = int(input("Enter your total monthly expenses: "))
annual_interest = 0.05
monthly_savings = expenses - income
projected_savings = (monthly_savings * 12) + (monthly_savings*12*0.05)
print(f'''
    Your monthly savings are ${monthly_savings}
    Projected savings after one year, with interest, is: ${projected_savings}
    ''')