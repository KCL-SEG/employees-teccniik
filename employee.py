"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name, salary, contract_hours, contract_pay, contracts, contracts_commission, bonus_commission):
        self.name = name
        self.salary = salary
        self.contract_pay = contract_pay
        self.contract_hours = contract_hours
        self.contracts = contracts
        self.contracts_commission = contracts_commission
        self.bonus_commission = bonus_commission

    def get_pay(self):
        total_salary = 0
        if (self.salary > 0):
            total_salary+= self.salary
        if (self.contract_pay > 0):
            total_salary += (self.contract_pay * self.contract_hours)
        if (self.contracts > 0):
            total_salary += (self.contracts * self.contracts_commission)
        if (self.bonus_commission > 0):
            total_salary += self.bonus_commission
        return total_salary

    def __str__(self):
        end_string = ""
        end_string += self.name + " works on a "
        if self.salary>0:
            end_string += "monthly salary of "+str(self.salary)
        else:
            end_string += "contract of "+str(self.contract_hours)+" hours at "+str(self.contract_pay)+"/hour"

        if self.contracts>0:
            end_string += " and receives a commission for "+str(self.contracts)+" contract(s) at "+str(self.contracts_commission)+"/contract"
        elif self.bonus_commission > 0:
            end_string += " and receives a bonus commission of "+str(self.bonus_commission)

        end_string += ". Their total pay is " + str(self.get_pay()) +"."


        return end_string


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie', 4000, 0, 0, 0, 0, 0)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie', 0, 100, 25, 0, 0, 0)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee', 3000, 0, 0, 4, 200, 0)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan', 0, 150, 25, 3, 220, 0)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie', 2000, 0, 0, 0, 0, 1500)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel', 0, 120, 30, 0, 0, 600)
