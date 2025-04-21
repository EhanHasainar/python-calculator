print("""
 _____________________
|  _________________  |
| |              0  | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | ÷ | |
| |___|___|___| |___| |
|_____________________|
""")
print()

def plus(fn, sn):
  print(fn, '+', sn, '=', fn + sn)

def sub(fn, sn):
  print(fn, '-', sn, '=', fn - sn)

def multi(fn, sn):
  print(fn, 'x', sn, '=', fn * sn)

def div(fn, sn):
  print(fn, '/', sn, '=', fn / sn)

again = True
while again is True:
  fn = float(input("What is your first number: "))
  print()
  op = str(input("What operation: (+, -, *, /): "))
  print()
  sn = float (input("What is your second number: "))
  print()

  if op == '+':
    result = plus(fn, sn)
    print()
  elif op == '-':
    result = sub(fn, sn)
    print()
  elif op == '*':
    result = multi(fn,sn)
    print()
  elif op == '/':
    result = div(fn, sn)
    print()
  else:
    print("Sorry didn't get that!")
    print()
  
  ask = input("Type 'y' to go again and 'n' to stop: ")
  print()
  if ask == 'y':
    again = True
  elif ask == 'n':
    again = False
  else:
    again = False
    print("Sorry didn't get that!")
    print()

