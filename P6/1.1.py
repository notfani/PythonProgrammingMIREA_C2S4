class MyClass:
    def __init__(self):
        self.field1 = "value1"
        self.field2 = "value2"
        self._private_field = "private_value"
        self.__private_field = "name_mangled_value"

obj = MyClass()
fields = [name for name in dir(obj) if not name.startswith('_')]
print(fields)
