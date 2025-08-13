class Employee :
    Org_Name="TCS"
    def __init__(self,name,age,desg,salary):
        self.name=name
        self.age=age
        self.desg=desg
        self.salary=salary
    def empDisp(self):
        print(f"Name={self.name} Age={self.age} Designation={self.desg} Organization Name={Employee.Org_Name} Salary={self.salary}")
    def empIncSalary(self,perc):
        self.salary=self.salary+(self.salary*perc/100)
        # print(self.salary)
    def empPromotion(self,newdesg):
        self.desg=newdesg
        # print(self.desg)
        
employees=[]
for i in range(3):
    name=input("Enter the name:")
    age=int(input("Enter your age:"))
    salary=float(input("Enter your salary:"))
    desg=input("Enter your Designation:")
    empobj=Employee(name,age,desg,salary)
    employees.append(empobj)

for emp in employees:
    emp.empDisp()
# emp1=Employee("akash",24,"SW Engineer",30000)
# emp1.empIncSalary(25)
# emp1.empPromotion("SW Tester")
