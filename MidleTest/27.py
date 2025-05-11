# Заданные значения
x = 4
y = 4

# Левое поддерево: (if (x < 1) then 5 else y * 10) + y
left_subtree = ((5 if x < 1 else y * 10) + 10) + y

# Правое поддерево: if (x < 5) then (y >> 2) else 9
right_subtree = (y >> 2) if x < 5 else 9

# Корень дерева: левое поддерево + правое поддерево
result = left_subtree + right_subtree

# Вывод результата
print(result)