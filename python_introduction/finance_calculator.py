MonthlyIncome = int(input("Enter your monthly income: "))
MonthlyExpenses = int(input("Enter your total monthly expenses "))
MonthlySavings = MonthlyIncome - MonthlyExpenses
print("Your monthly savings are ",MonthlySavings)
Projected_savings =int( MonthlySavings * 12 + (MonthlySavings * 12 * 0.05))
print("Projected savings after one year, with interest, is: ",Projected_savings)

