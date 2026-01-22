def add(num1, num2):
    answer = num1 + num2
    return answer
def subtract(num1, num2):
    answer = num1 - num2
    return answer
def multiply(num1, num2):
    answer = num1 * num2
    return answer
def divide(num1, num2):
    if num2 == 0 or num1 == 0:
        answer = 0
        return answer
    answer = num1 / num2
    return answer
def power(num1, num2):
    answer = num1 ** num2
    return answer