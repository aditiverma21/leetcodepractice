
class Payrollsystem:
    def calculate_payroll(self,employees):
        print("Calculating Payroll")
        for emp in employees:
            print(f"Payroll for: {emp.id}: {emp.name}")
            print(f" Check amount : {emp.calculate_payroll()}")
            if emp.address:
                print("sent to :")
                print(emp.address)


class Employee:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.address = None

class Salary_emp(Employee):
    def __init__(self,id,name,salary):
        super().__init__(id,name)
        self.salary = salary

    def calculate_payroll(self):
        return self.salary


class Address:
    def __init__(self, street, city, state, zipcode, street2=''):
        self.street = street
        self.street2 = street2
        self.city = city
        self.state = state
        self.zipcode = zipcode

    def __str__(self):
        line = [self.street]
        if self.street2:
            line.append(self.street2)
        line.append(f'{self.city} , {self.state} , {self.zipcode}')
        return '\n'.join(line)


salaryemp = Salary_emp(302111,"Aditi",50000)
'''
addr = Address('Plot 26','Bhilai','Chhattisgarh',490006)
print(addr)
'''
salaryemp.address = Address('Plot 26','Bhilai','Chhattisgarh',490006)
payroll = Payrollsystem()
payroll.calculate_payroll([salaryemp])

'''
Here Employee is the composite class and Address is the component class
Composition allows composite class to resuse the implementation of the components it contains.
Employee class leverage the implementation of the address class without any knowledge of what
an Address object is and how its represented 
'''