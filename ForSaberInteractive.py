from operator import pow, truediv, mul, add, sub  

operators = {
  '+': add,
  '-': sub,
  '*': mul,
  '/': truediv
}

def calculate(s):
    if s.isdigit():
        return float(s)
    for c in operators.keys():
        left, operator, right = s.partition(c)
        if operator in operators:
            return operators[operator](calculate(left), calculate(right))

calc = input("Type calculation:\n")
print("Answer: " + str(calculate(calc)))

## Еще  нашёл опасный, но короткий вариант
## calc = input("Type calculation:\n")
## print("Answer: " + str(eval(calc)))