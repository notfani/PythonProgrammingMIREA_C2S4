class VM:
    def __init__(self, code):
        self.code = code      # список байт (чисел)
        self.stack = []       # стек для операций
        self.pc = 0           # счётчик команд
        
        # Библиотека операций для 'op' (упорядоченный набор)
        # Индекс операции (operand) соответствует позиции в этом списке.
        self.LIB = [
            '+', '-', '*', '/', '%',
            '&', '|', '^', '<', '>', '=',
            '<<', '>>', 'if', 'for', '.'
        ]
    
    def run(self):
        """Запускает исполнение байткода с текущего pc."""
        while self.pc < len(self.code):
            byte = self.code[self.pc]
            self.pc += 1
            
            # Младшие 3 бита — это код операции
            opcode = byte & 7
            # Старшие 5 бит — это операнд
            operand = byte >> 3
            
            if opcode == 0:
                # push operand
                self.stack.append(operand)
            
            elif opcode == 1:
                # op <index_in_LIB>
                if operand >= len(self.LIB):
                    raise RuntimeError(f"Неизвестная операция с индексом {operand}")
                op_name = self.LIB[operand]
                
                if op_name == '+':
                    # Сложение двух верхних элементов стека
                    b = self.stack.pop()
                    a = self.stack.pop()
                    self.stack.append(a + b)
                
                elif op_name == '.':
                    # Вывод верхнего элемента стека на экран
                    val = self.stack.pop()
                    print(val)
                
                else:
                    # Для остальных операций пока заглушка
                    raise RuntimeError(f"Операция '{op_name}' не реализована")
            
            elif opcode == 5:
                # exit
                break
            
            else:
                # Заглушка для остальных (call/is/to и т.д.)
                raise RuntimeError(f"Opcode {opcode} не реализован в этой VM")

        # После выхода (exit или конец байткода) можно вернуть стек, если нужно
        return self.stack


if __name__ == "__main__":
    # Тот самый байткод, соответствующий фортиковому "2 2 + .":
    #   2 2 + .
    # Компилятор Фортика выдал [0,16,16,1,121,5].
    # Расшифровка:
    #   byte=0   => (opcode=0, operand=0)  push 0   (иногда используется как 'entry' — зависит от компилятора)
    #   byte=16  => (opcode=0, operand=2)  push 2
    #   byte=16  => (opcode=0, operand=2)  push 2
    #   byte=1   => (opcode=1, operand=0)  op '+'   (LIB[0] = '+')
    #   byte=121 => (opcode=1, operand=15) op '.'   (LIB[15] = '.')
    #   byte=5   => (opcode=5, operand=0)  exit
    
    code = [0, 16, 16, 1, 121, 5]
    
    vm = VM(code)
    vm.run()  # При корректной работе выведет 4
