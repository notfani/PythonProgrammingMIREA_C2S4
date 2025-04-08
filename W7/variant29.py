def main(data):
    tree = {
        1967: {
            'JFLEX': {
                'EQ': 4,
                'FORTH': 5,
                'REBOL': 3
            },
            'ASP': {
                'FORTH': 0,
                'REBOL': {
                    'HLSL': 7,
                    'STAN': 8,
                    'EQ': 9
                }
            }
        },
        1977: {
            'ASP': 6,
            'JFLEX': {
                'HLSL': 7,
                'STAN': 8,
                'EQ': 9
            }
        }
    }

    if data[4] == 'IOKE':
        return 10

    current_node = tree.get(data[0], {})
    for i in [1, 2, 3]:
        if isinstance(current_node, int):
            return current_node
        current_node = current_node.get(data[i], {})

    return current_node if isinstance(current_node, int) else 0

# Тестовые случаи
print(main([1967, 'JFLEX', 'EQ', 'EQ', 'TCL']))        # 4
print(main([1977, 'ASP', 'REBOL', 'HLSL', 'TCL']))     # 6
print(main([1967, 'JFLEX', 'FORTH', 'HLSL', 'IOKE']))  # 10
print(main([1967, 'JFLEX', 'REBOL', 'HLSL', 'TCL']))   # 3
print(main([1967, 'ASP', 'FORTH', 'HLSL', 'TCL']))     # 0
print(main([1967, 'ASP', 'EQ', 'EQ', 'TCL']))          # 0