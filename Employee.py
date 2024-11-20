class Employee:
    def __init__(self):
        print("Employee created")
    def __del__(self):
        print("Employee destructed/deleted")
def CreateObj():
    print("Making object")
    Obj=Employee()
    print("Function End")
    return Obj
print("Calling Create Object function")
Obj=CreateObj()
print("Programme end")