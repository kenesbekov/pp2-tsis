thousand = 'M{0,3}'
hundred = '(C[DM]|D?C{0,3})'
ten = '(X[LC]|L?X{0,3})'
digit = '(I[VX]|V?I{0,3})'
regex_pattern = thousand+hundred+ten+digit +'$'
import re
print(str(bool(re.match(regex_pattern, input()))))