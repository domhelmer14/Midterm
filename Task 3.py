input_string = input("Input numbers: ")
list = input_string.split()

for i in range(len(list)):
       list[i] = int(list[i])
       
out = []
       
for num in list:
       
       if num % 2 == 0:
           out.append(num)
       
       
print("Your even numbers add up to: ")
       
print("Sum = ", sum(out))       