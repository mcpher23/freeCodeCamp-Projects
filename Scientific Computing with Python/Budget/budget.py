# import math library to be able to use the floor method
import math


# Create the class named Category
class Category:
    
    
    # Initilze the object and create the variables seen below including taking the argument name and assigning it to the variable name   
    def __init__(self,name):
        self.name = name
        self.ledger = []
        self.funds = 0
        self.spent = 0
    
    
    # Add to the list the amount input and add to the list the description
    def deposit(self, amount, description=''):
        self.ledger.append({'amount': amount, 'description':description})
        self.funds += amount
        return
    
    
    # Add to the list the -(amount) input and add to the list the description
    def withdraw(self, amount, description=''):
        if self.check_funds(amount):
            self.ledger.append({'amount': -amount, 'description':description})
            self.funds -= amount
            self.spent += amount
            return True
        else: return False
    
    
    # Return the current funds amount
    def get_balance(self):
        return self.funds
    
    
    # Treat the transfer like a withdrawal so perform the withdraw method but then also treat as a deposit in the desitnation so perform the deposit method for the desitnation
    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category.name}")
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        else: return False
    
    
    # Method to check the amount is never more than the current total funds
    def check_funds(self, amount):
        if amount > self.funds:
            return False
        else: return True
     
    
    # Create the output string requested. Capatalizes and centers the name to 30 characters. Performs formatting including string slicing, setting significant figures and more text alignment
    def __str__(self):
        output = f"{self.name.capitalize():*^30}\n"
        final = ""
        for entry in self.ledger:
            fdescription = f"{entry['description'][:23]:<23}"
            famount = f"{entry['amount']:>7.2f}"
            final += f"{fdescription}{famount}\n" 
        
        final += f"Total: {self.funds}"
        
        return output + final
    

# Creates the desired chart in a string format
def create_spend_chart(categories):
    
    total = 0
    spent = []
    
    for category in categories:
        total += category.spent
    
    # By performing floor(x/10)*10 we are able to round down to the nearest 10    
    for category in categories:   
        spent.append({category.name: (math.floor(((category.spent / total * 100) / 10)) * 10)})
    
    spends = []
    for category in categories:   
        spends.append((math.floor(((category.spent / total * 100) / 10)) * 10))
              
    final = ""
    
    # Iterates through the 100 - 0 chart and checks if the amount spent in the category matches or is lower and marks with the "o" character 
    for i in range(100, -10, -10):
        
        k = (str(i)).rjust(3) + "|"
        
        for item in spent:
            for key in item:
                if  item[key] >= i:
                    k += " o "
                else: k += "   "
                        
        final += k + " \n"
     
    dashes = "    -" + "---" * len(categories)
    
    final += dashes + "\n"
    
    names = []
    
    for item in spent:
        for key in item.keys():
            names.append(key)
    
    # Finds the maximum length between the items in the names list
    maxlength = len(max(names, key=len))
    
    # Iterates through the names list and prints character by charcter. If the name is finished then instead prints a " "   
    for i in range(maxlength):
        line = "    "
        for name in names:
            if len(name) > i:
                if i == 0:
                    line += f" {name[i].upper()} "
                else: line += f" {name[i]} "
            else:
                line += "   "
        if i == maxlength - 1:
            final += line + " "        
        else: final += line + " \n"
        
    
    final = "Percentage spent by category" + "\n" + final
    return final

 
# Test Case 
food = Category('food')
entertainment = Category('entertainment')
business = Category('business')

categories = [business, food, entertainment]

food.deposit(900, "deposit")
entertainment.deposit(900, "deposit")
business.deposit(900, "deposit")
food.withdraw(105.55)
entertainment.withdraw(33.40)
business.withdraw(10.99)

final = create_spend_chart(categories)

print(food)
print()
print((final))

# Expected Response
#*************Food*************
#deposit                 900.00
#                       -105.55
#Total: 794.45

#Percentage spent by category
#100|          
# 90|          
# 80|          
# 70|    o     
# 60|    o     
# 50|    o     
# 40|    o     
# 30|    o     
# 20|    o  o  
# 10|    o  o  
#  0| o  o  o  
#    ----------
#     B  F  E  
#     u  o  n  
#     s  o  t  
#     i  d  e  
#     n     r  
#     e     t  
#     s     a  
#     s     i  
#           n  
#           m  
#           e  
#           n  
#           t