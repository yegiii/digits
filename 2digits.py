# Q : multiple choice question

# How many 3-digit numbers can be made using only 2 different digits from 1 - 9?
# (Repetition of digits are allowed)

counter = 0

def hasCondition (n): 
   s = set()
   for _ in range(3):   
      digit = n % 10
      s.add(int(digit))
      n = n / 10
      # print(s)

   if not(0 in s) and len(s) == 2 :
      print (s)
      return True
      

for i in list(range(111,999)):
    if hasCondition(i) :
        counter = counter + 1
        print(i)

print(counter)