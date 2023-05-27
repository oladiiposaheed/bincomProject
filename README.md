"# bincomProject" 

count = 0

lst = []

num = int(input('Enter a positive integer for iteration: '))

if num == 0:

  print('The integer cannot be {}'.format(num))
  
elif num < 0:

  print('You entered a negative number')
  
else:

  for i in range(num):
  
    n = int(input('Enter an integer: '))
    
    count += 1
    
    lst.append(n)
    
    Sum = sum(lst)
    
average = Sum / count

print('The Average of {} is {}'.format(lst, average))
