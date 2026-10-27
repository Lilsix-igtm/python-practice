x = 42
y = 0

print()
try:
    print(x / y)
except ZeroDivisionError as e:
    print('Not allowedto divide by Zero')
else:
    print('Something else went wrong')
finally:
    print('this is our cleanup code')
print()

