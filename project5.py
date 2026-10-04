class Person:
    def __init__(self, grno ,name, age):
        self.geno =grno
        self.name = name
        self.age = age

    def show_details(self):
        print(f"person created with name : {self.name}")
        print(f"and age: {self.age}")

class Employee(Person):
    def __init__(self, grno, name, age, employee_id, salary):
        super().__init__(grno,name, age)
        self.employee_id = employee_id
        self.salary = salary

    def details(self):
        print(f"employee created with name: {self.name}")
        print(f"age: {self.age}, ID: {self.employee_id}")
        print(f"and salary: {self.salary}")

class Manager(Employee):
    def __init__(self, grno, name, age, employee_id, salary, department):
        super().__init__(grno,name, age, employee_id, salary)
        self.department = department

    def detail(self):
        print(f"employee created with name: {self.name}")
        print(f"age: {self.age}, ID: {self.employee_id}")
        print(f"and salary: {self.salary}")
        print(f"and department: {self.department}")

per = []
emp = []
man = []

while True:
    print("--- python oop Project: employee management system ---")

    print("choose an operation")
    print("1. create a person")
    print("2. create a employee")
    print("3. create a manager")
    print("4. show detail")
    print("5. exit")

    choice = int(input("enter your choice: "))

    match choice:

        case 1:
            grno = int(input("enter your gr no: "))
            name = input("enter your name: ")
            age = int(input("enter your age: "))

            Per = Person(grno,name,age)
            per.append(Per)

            Per.show_details()

        case 2:
            grno = int(input("enter your gr no: "))
            name = input("enter your name: ")
            age = int(input("enter your age: "))
            employee_id = int(input("enter employee id: "))
            salary = int(input("enter employee salary: "))

            Emp = Employee(grno,name, age, employee_id, salary)
            emp.append(Emp)

            Emp.details()

        case 3:
            grno = int(input("enter your gr no: "))
            name = input("enter your name: ")
            age = int(input("enter your age: "))
            employee_id = int(input("enter employee id: "))
            salary = int(input("enter employee salary: "))
            department = input("enter your department: ")

            Man = Manager(grno,name, age, employee_id, salary, department)
            man.append(Man)

            Man.detail()

        case 4:
            print("\n choose detail to show: ")
            print("1. person")
            print("2. employee")
            print("3. manager")

            choice = int(input("enter your choice: "))

            if choice == 1:
                gr_no = int(input("Enter your gr_no: "))

                if gr_no == grno:
                    Per.show_details()
                else:
                    print("GR number not found.")

            elif choice == 2:
                gr_no = int(input("Enter your gr_no: "))

                if gr_no == grno:
                    Emp.details()
                else:
                    print("GR number not found.")

            elif choice == 3:
                gr_no = int(input("Enter your gr_no: "))

                if gr_no == grno:
                    Man.detail()
                else:
                    print("GR number not found.")

            else:
                print("Invalid choice.")

        case 5:
            print("exiting from program!")
            break

        case _:
            print("invalid choice please enter choice between 1 to 5!")