
    for i in matrix:
        if type(i) != list and type(i) != float:
            raise TypeError('matrix must be a matrix (list of lists) of\
                    integers/floats')
        if type(i) != list and type(i) != int:
            raise TypeError('matrix must be a matrix (list of lists) of\
                    integers/floats')
        if len(i) != len(i):
            raise TypeError('Each row of the matrix must have the same size')
            for j in i:
                if type(j) != int & type(j) != float:
                    raise TypeError('matrix must be a matrix (list of lists)\
                            of integers/floats')

            else:
                if type(div) != int & type(div) != float:
                    raise TypeError('div must be a number')
                    if div == 0:
                        raise TypeError('division by zero')

                    else:
                        return round(list(map(lambda x: x / 2, i)))
