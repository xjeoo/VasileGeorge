from employee import Employee 
#Vasile George
X=6; Y=6

class Manager(Employee):
    mgr_count=0
    def __init__(self, name, salary,department):
        self.name=name
        self.salary=salary
        self.department="F24 "+department
        Manager.mgr_count+=1
    
    def display_employee(self):
        print("Name : ", self.name, " ")

X = 6; Y=6
manageri = []
for i in range(Y//3):
    manageri.append(Manager(f"mgr{i+1}",5*i,f"dep{i+1}"))

emoloyees = []
emoloyees.append(Employee("angajat1",6969))



for i, manager in enumerate(manageri):
    print(f"Manager {i + 1}:")
    manager.display_employee()

for i, angajat in enumerate(emoloyees):
    print(f"angajat {i + 1}:")
    angajat.display_employee()


print(Manager.mgr_count, Employee.empCount)



    




