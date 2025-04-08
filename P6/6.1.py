# Фрагмент реализации виртуальной машины

OP_NAMES = {
    0: 'push',
    1: 'op',
    2: 'call',
    3: 'is',
    4: 'to',
    5: 'exit'
}

def not_implemented(vm):
    raise RuntimeError('Not implemented!')

# Библиотека операций с сохранением порядка (начиная с Python 3.7 словари сохраняют порядок вставки)
LIB = {
    '+': not_implemented,
    '-': not_implemented,
    '*': not_implemented,
    '/': not_implemented,  # Целочисленный вариант деления
    '%': not_implemented,
    '&': not_implemented,
    '|': not_implemented,
    '^': not_implemented,
    '<': not_implemented,
    '>': not_implemented,
    '=': not_implemented,
    '<<': not_implemented,
    '>>': not_implemented,
    'if': not_implemented,
    'for': not_implemented,
    '.': not_implemented
}

def disasm(bytecode):
    """
    Дизассемблер байткода Фортика.
    
    Код байткоманды имеет следующий формат: каждая команда задаётся одним байтом.
    Младшие 3 бита байта (значение byte & 7) – это код операции (смотрим в OP_NAMES),
    а старшие 5 бит (byte >> 3) – операнд.
    
    При этом первый байт байткода не дизассемблируется, а используется как метка entry.
    
    Для операций:
      - push, call, to, exit – операнд выводится как число;
      - op – операнд интерпретируется как индекс в упорядоченном списке библиотечных операций LIB.
    """
    lines = []
    # Выводим метку entry
    lines.append("entry:")
    
    # Получаем упорядоченный список ключей LIB для последующей индексации в op-инструкциях
    lib_keys = list(LIB.keys())
    
    # Дизассемблируем команды, начиная со второго байта
    for byte in bytecode[1:]:
        opcode = byte & 7        # младшие 3 бита
        operand = byte >> 3      # старшие 5 бит
        op_name = OP_NAMES.get(opcode, f'?.{opcode}')
        
        if op_name == 'op':
            # Если operand выходит за пределы LIB – отобразим как есть
            if operand < len(lib_keys):
                op_symbol = lib_keys[operand]
            else:
                op_symbol = f"?{operand}?"
            line = f"  {op_name} '{op_symbol}'"
        else:
            line = f"  {op_name} {operand}"
        lines.append(line)
    return "\n".join(lines)


if __name__ == "__main__":
    # Пример использования дизассемблера.
    # Согласно примеру задания, вызов:
    #   disasm([0, 16, 16, 1, 121, 5])
    # должен вывести:
    #
    # entry:
    #   push 2
    #   push 2
    #   op '+'
    #   op '.'
    #   exit 0

    code = [0, 16, 16, 1, 121, 5]
    output = disasm(code)
    print(output)
