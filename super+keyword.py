class A:
    def method1(self):
        print("I'm calling parent class")

class B(A):
    def method1(self): 
        super().method1()
        print("I'm calling child class")
        super().method1()

c=B()
c.method1()