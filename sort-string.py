def sort_string(input_string)->str:
    """
    Sort input string with following conditions:
    sorted lowercase letters ahead of uppercase letters.
    sorted uppercase letters ahead of digits.
    sorted odd digits are ahead of sorted even digits.
    ----------------------------------------------------------
    Input: string with letters and digits
    Output: Sorted string
    """
    order = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1357902468'
    print("Sorted string is:", *sorted(input_string, key=order.index), sep='')

INPUT = "Stringsorting123"

sort_string(INPUT)