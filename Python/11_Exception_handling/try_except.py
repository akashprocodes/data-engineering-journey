
# This is an example of exception handling in Python

try:
  print(x) # x is not defined. Then show error.
except:
  print("Something went wrong") # Then print this message
finally:
  print("The 'try except' is finished") # Also print this message because of finally to confirm.