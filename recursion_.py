def recursion(number):
  # Define output.
  output = 1
  
  # Create a list of factorial numbers.
  factorialNumbers = []

  # Reverse list.
  # reverseList = []
 
  # Append numbers within range of what user is giving into factorial no. list
  for num in range(number + 1):
    if num != 0:
      factorialNumbers.append(num)
      # print(factorialNumbers)

  # Reverse list.
  factorialNumbers = factorialNumbers[::-1]
  print(factorialNumbers)

  # Multiply numbers in factorialNumbers list.
  for factorialNumber in factorialNumbers:
    print(output, '*', factorialNumber)
    output = output * factorialNumber
    

  return output


print(recursion(5))
  