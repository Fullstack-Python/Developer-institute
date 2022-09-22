import operators

operators.addOperator(2, 3)
operators.divideOperator(5, 4)


# Importing Specific Functions

from operators import addOperator

addOperator(2, 3)

from operators import divideOperator

divideOperator(4, 5)

# Using Alias

from operators import addOperator as Junior

Junior(4, 5)

from operators import divideOperator as Junior

Junior(5, 4)