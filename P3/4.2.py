def transpose_matrix( matrix ) :
    # Проверяем, что матрица не пустая
    if len( matrix ) == 0 :
        raise ValueError( "Матрица не должна быть пустой." )

    # Получаем количество строк и столбцов
    rows = len( matrix )
    cols = len( matrix[ 0 ] )

    # Создаем новую матрицу для транспонированного результата
    transposed = [ [ 0 ] * rows for _ in range( cols ) ]

    # Заполняем транспонированную матрицу
    for i in range( rows ) :
        for j in range( cols ) :
            transposed[ j ][ i ] = matrix[ i ][ j ]

    return transposed


def input_matrix( rows, cols ) :
    matrix = [ ]
    for i in range( rows ) :
        row = list( map( int, input( f"Введите элементы {i + 1}-й строки через пробел: " ).split( ) ) )
        if len( row ) != cols :
            raise ValueError( "Количество элементов в строке должно соответствовать количеству столбцов." )
        matrix.append( row )
    return matrix


def main() :
    # Ввод размеров матрицы
    rows = int( input( "Введите количество строк: " ) )
    cols = int( input( "Введите количество столбцов: " ) )

    print( "Введите матрицу:" )
    matrix = input_matrix( rows, cols )

    # Транспонируем матрицу
    transposed = transpose_matrix( matrix )

    # Выводим результат
    print( "Транспонированная матрица:" )
    for row in transposed :
        print( " ".join( map( str, row ) ) )


if __name__ == "__main__" :
    main( )
