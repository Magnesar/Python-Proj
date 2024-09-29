def truncate(n):
	return round(n*100,-1)/100

class Category:
	def __init__(self, category):
		self.category = category
		self.ledger = list()
		self.dep_call_count = 0
		
	def deposit(self, amount, description = ''):
		self.dep_call_count += 1
		self.ledger.append({'amount': amount, 'description': description})
		
			
		
	def get_count(self):
		return self.dep_call_count

	
	def __str__(self):
		title = f'{self.category:*^30}\n'  # '*^30' formats the string to be centered in a field of 30 characters wide, and the remaining spaces are filled with the * character. 
		items = ''
		total = ''
		
		for item in self.ledger:
			items += f'{item["description"][:23]:23}' + f'{item["amount"]:>7.2f}' + '\n'
            #':>7.2f' formats as a floating-point number with two decimal places, right-aligned in a field of 7 characters wide. If the number has fewer than 7 characters (including the decimal point and digits), it will be padded with spaces on the left. 	

		total = title + items+ f'Total: {self.get_balance()}' 
		return total

	def withdraw(self, amount, description = ''):
		if self.check_funds(amount):
			self.ledger.append({'amount': -amount, 'description': description})
			return True
		return False


	def withdrawals(self):
		total = 0
		for i in self.ledger:
			if i['amount'] < 0:
				#print(i['amount'])
				total += i['amount']
		#print(f'Spent in {self.category}: {total}')
		return total

		
		
	def get_balance(self):
		bal = 0
		for i in self.ledger:
			bal += i['amount']
		return bal
		
		
	def transfer(self, amount, category):
		if self.check_funds(amount):
			self.withdraw(amount, 'Transfer to '+ category.category)
			category.deposit(amount, 'Transfer from '+ self.category)
			return True
		return False
		
		
	def check_funds(self, amount):
		if amount > self.get_balance():
			return False
		return True

	
	


def total_spent(categories):
		total = 0
		breakdown = []
		for category in categories:
			total += category.withdrawals()	
			breakdown.append(category.withdrawals())
		#print('Total spent: ',-total)
		#print(breakdown)
		rounded = list(map(lambda x: truncate(x/total), breakdown))
		return rounded			#return all of the spent money category-wise
		

def create_spend_chart(categories):
    spent_amounts = []
    # Get total spent in each category
    for category in categories:
        spent = 0
        for item in category.ledger:
            if item["amount"] < 0:
                spent += abs(item["amount"])
        spent_amounts.append(round(spent, 2))

    # Calculate percentage rounded down to the nearest 10
    total = round(sum(spent_amounts), 2)
    spent_percentage = list(map(lambda amount: int((((amount / total) * 10) // 1) * 10), spent_amounts))

    # Create the bar chart substrings
    header = "Percentage spent by category\n"

    chart = ""
    for value in reversed(range(0, 101, 10)):
        chart += str(value).rjust(3) + '|'
        for percent in spent_percentage:
            if percent >= value:
                chart += " o "
            else:
                chart += "   "
        chart += " \n"

    footer = "    " + "-" * ((3 * len(categories)) + 1) + "\n"
    descriptions = list(map(lambda category: category.category, categories))
    max_length = max(map(lambda description: len(description), descriptions))
    descriptions = list(map(lambda description: description.ljust(max_length), descriptions))
    for x in zip(*descriptions):
        footer += "    " + "".join(map(lambda s: s.center(3), x)) + " \n"

    return (header + chart + footer).rstrip("\n")
		
 	
	
food = Category('Food')
food.deposit(900, "deposit")
food.withdraw(45.67, "milk, cereal, eggs, bacon, bread")
entertainment = Category("Entertainment")
food.transfer(20, entertainment)
print(food)
x =f"*************Food*************\ndeposit                 900.00\nmilk, cereal, eggs, bac -45.67\nTransfer to Entertainme -20.00\nTotal: 834.33"
print(x)


if food == x:
	print(True)
else:
	print(False)
print(len(str(food)),len(x))
