                                            #Exercice 3

# 1. on importe tout le module
import operators

print(operators.addOperator(10, 5))
print(operators.divideOperator(10, 5))

# 2. on importe seulement les fonctions dont on a besoin
from operators import addOperator, divideOperator

print(addOperator(20, 4))
print(divideOperator(20, 4))

# 3. avec un alias
import operators as op

print(op.addOperator(9, 3))
print(op.divideOperator(9, 3))
