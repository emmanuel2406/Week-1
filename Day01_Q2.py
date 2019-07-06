def ft_print_numbers(n):
    array = list(str(n))
    array = list(map(int,array))
    output = ''
    while array != '':
        mn = min(array)
        output += str(mn)
        array.remove(mn)
    return output
    
