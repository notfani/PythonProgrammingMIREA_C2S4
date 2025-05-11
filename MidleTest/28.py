# Заданные значения
x = 3
y = 4

# Левое поддерево: (if (y <= 5) then x else y % 4) + y
left_subtree = (x if y <= 5 else x % 4) + y

# Правое поддерево: if (y >= 7) then (y % 4) else (x >> 3)
right_subtree = y if y >= 7 else (x >> 3)

# Корень дерева: левое поддерево + правое поддерево
result = left_subtree + right_subtree + 7

# Вывод результата
print(result)
