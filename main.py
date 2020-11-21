import algorithms.notations as nt

# TEST DRIVERS

# Postfix to infix
print(nt.postfix_to_infix('a b c - d + / e a - * c *'))

# Infix to postfix
print(nt.infix_to_prefix('1 + ( 2 + ( 4  + 34 ) / 2 ) + 6'))
print(nt.infix_to_prefix('a / d - ( b + c ) * e'))
