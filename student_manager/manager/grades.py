def calculate_average(a, b, c):
    return (a + b + c) / 3

def check_result(average):
    if average >= 50:
        result = "Passed"
    else:
        result = "Failed"
    print(f"Result: {result}")
