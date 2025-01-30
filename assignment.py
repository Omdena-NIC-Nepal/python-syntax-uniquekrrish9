def format_string(name, age):
    return f"My name is{name} and I am {age} old."

name =input("Enter your name:")
age = int(input("Enter your age:"))

text = format_string(name,age)
print(text)

def conditional_check(number):
        if number > 10:
            return "Greater"
        elif number < 10:
            return "Lesser"
        else:
            return "Equal"
  

 #take input from user
num = int(input("Enter a number:"))
print(conditional_check(num))
    

def loop_sum(n):
    total = 0
    for i in range(1, n+1):
        total +=i
    return total
num = int(input("Enter a number:"))
print(f"Sum from 1 to {num} is {loop_sum(num)}")

def list_operations(numbers):
    
    if not numbers:
        return (0, None, None)
    return (sum(numbers), max(numbers), min(numbers))

num_list = [3, 7, 2, 8, 5]
result = list_operations(num_list)
print(f"Sum: {result[0]}, Max:{result[1]}, Min:{result[2]}")

def dict_operations(students_dict):
    return [name for name, score in students_dict.items() if score > 80]
students = {
    "krishna": 85,
    "ram": 78,
    "sita": 90,
    "rita": 60,
    "shyam": 95
}

high_scorers = dict_operations(students)
print("Students with scores above 80:", high_scorers)

def set_operations(list1, list2):
    return set(list1) & set(list2)
list_a = [1,2,3,4,5]
list_b = [4,5,6,7,8]
common_elements = set_operations(list_a, list_b)
print("Common elements:", common_elements)

def arithmetic_ops(a, b):
    if b == 0:
        division = None
    else:
        division = a / b
    
    return {
        "Addition": a + b,
        "Subtraction": a - b,
        "Multiplication": a * b,
        "Division": division,
        "Exponentiation": a ** b
    }
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

results = arithmetic_ops(num1,num2)
print("Results:", results)

def logical_ops(x, y):
    return{
        "and": x and y,
        "or": x or y,
        "not_x": not x,
        "not_y": not y,
        "xor": x ^ y
    }
bool1 = bool(int(input("Enter first boolean (0 or 1): ")))
bool2 = bool(int(input("Enter second boolean (0 or 1): ")))

results = logical_ops(bool1, bool2)
print("Results:", results)

def bitwise_ops(a, b):
    return{
        "and": a & b,
        "or": a | b,
        "xor": a ^ b,
        "left_shift_a": a << 1,
        "left_shift_b": b << 1,
        "right_shift_a": a >> 1,
        "right_shift_b": b >> 1
    }
num1 = int(input("Enter first integer: "))
num2 = int(input("Enter second integer: "))

results = bitwise_ops(num1, num2)
print("Results:", results)