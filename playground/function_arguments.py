# functions with multiple values in a list
def capitalize(names=[]):
    # names_copy=names.copy()
    names.sort()
    # names_copy.sort()
    final_list = ''
    
    for name in names:
        final_list += name.upper()  + ', '
    
    final_list = final_list[:-2]
    print(final_list)

capitalize(['Riaz', 'Sarah', 'Fiaz'])

# functions with arbitrary values
def sort_any(*args):
    newlist = list(args)
    newlist.sort()
    print(newlist)

sort_any(1, 0.01, 1000, -900, 2)
