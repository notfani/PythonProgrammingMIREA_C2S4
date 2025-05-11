# Заданные значения
x = 3
y = 3

# Левое поддерево: (y << 8) - (if (x < 1) then (x % 1) else (x - 7)) + 1
left_subtree = ((y << 8) - ((x % 1) if x < 1 else (x - 7)))

# Правое поддерево: if (x < 6) then 3 else (x >> 1)
right_subtree = 3 if x < 6 else (x >> 1)

# Корень дерева: левое поддерево - правое поддерево
result = left_subtree + right_subtree - 1

# Вывод результата
print(result)