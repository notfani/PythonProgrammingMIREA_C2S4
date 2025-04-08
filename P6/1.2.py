class MyClass:
    def my_method(self):
        print("Method called!")

obj = MyClass()
method_name = "my_method"

# Вызов метода по имени
getattr(obj, method_name)()
