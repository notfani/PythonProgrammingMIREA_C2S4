def hadamard_product( A, B ) :
    # Проверяем, что размеры матриц совпадают
    if len( A ) == 0 or len( B ) == 0 or len( A ) != len( B ) or len( A[ 0 ] ) != len( B[ 0 ] ) :
        raise ValueError( "Матрицы должны иметь одинаковые размеры и не быть пустыми." )

    # Получаем размеры матриц
    rows = len( A )
    cols = len( A[ 0 ] )

    # Создаем матрицу для результата
    C = [ [ 0 ] * cols for _ in range( rows ) ]

    # Вычисляем поэлементное произведение
    for i in range( rows ) :
        for j in range( cols ) :
            C[ i ][ j ] = A[ i ][ j ] * B[ i ][ j ]

    return C


def input_matrix( rows, cols ) :
    matrix = [ ]
    for i in range( rows ) :
        row = list( map( int, input( f"Введите элементы {i + 1}-й строки через пробел: " ).split( ) ) )
        if len( row ) != cols :
            raise ValueError( "Количество элементов в строке должно соответствовать количеству столбцов." )
        matrix.append( row )
    return matrix


def main() :
    # Ввод размеров матриц
    rows = int( input( "Введите количество строк: " ) )
    cols = int( input( "Введите количество столбцов: " ) )

    print( "Введите матрицу A:" )
    A = input_matrix( rows, cols )

    print( "Введите матрицу B:" )
    B = input_matrix( rows, cols )

    # Вычисляем произведение Адамара
    result = hadamard_product( A, B )

    # Выводим результат
    print( "Результат поэлементного произведения матриц A и B:" )
    for row in result :
        print( " ".join( map( str, row ) ) )


if __name__ == "__main__" :
    main( )
