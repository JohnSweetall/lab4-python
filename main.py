# Author: Yanling Wang yuw17@psu.edu
# Collaborator:
# Collaborator:
# Collaborator:
# Section: 1
# Breakout: 12

def num_of_divisors(n):
  
  i = 0
  sumAdd = 0
  while i <= n:
    if (n % i == 0):
      sumAdd = sumAdd + 1
      i = 1 + 1
    else:
      i = i + 1 
  return sumAdd
  

def num_of_primes(n):
   
  numb = 0
  for i in range(n+1):
    if(num_of_divisors(i) == 2):
      numb = numb + 1
  return numb


def sum_n(n):
  
  sumAdd = 0
  i = 1
  while i <= n:
    sumAdd = sumAdd + 1
  i = i + 1
  return sumAdd


def print_n(s, n):
  
  for i in range(n):
    print(s)
  return 0


def run():
  num = int(input("Enter an int: "))
  print(f"sum is {sum_n(num)}.")
  print(f"{num} has {num_of_divisors(num)} divisors.")
  print(f"There are {num_of_primes(num)} primes <= {num}.")
  line = input("Enter a string: ")
  print_n(line, num)

if __name__ == "__main__":
  run()
