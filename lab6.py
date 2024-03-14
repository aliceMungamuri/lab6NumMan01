'''
Author:Alice Mungamuri
KUID: 3117704
Date:03/05/2024
Lab: Lab 4 exercise 2
Last modified: 03/05/2024
Purpose: List Comparisons
''''
list1 = []
list2=[]
done = 'N'
done2 = 'N'
num = 0
while done == 'N':
  num = input("Enter an value for the first list:  ")
  list1.append(int(num))
  done = input('Are you done? (y|Y): ').upper()
while done2 == 'N':
  num = input("Enter an value for the second list:  ")
  list2.append(int(num))
  done2 = input('Are you done? (y|Y): ').upper()

sumList1 = sum(list1)
sumList2 = sum(list2)
avgList1 = sumList1 / len(list1) 
avgList2 = sumList2 / len(list2) 
numSame = 0

for i in list1:
  for j in list2:
    if list2[j] == list1[i]:
      numSame +=1
backwardList1 = []
backwardList2=[]
index1 = len(list1)-1
index2 = len(list2)-1
pal1 = False
pal2 = False
while index1>=0:
    backwardList1.append(list1[index1])
    index1-=1

if backwardList1 == list1:
  pal1 = True

while index2>=0:
    backwardList2.append(list2[index2])
    index2-=1

if backwardList2 == list2:
  pal2 = True


print("List Statistics:")
if sumList1 > sumList2:
  print(f"The first list has the larger sum of {sumList1}")
elif sumList1 < sumList2:
  print(f"The second list has the larger sum of {sumList2}")
elif sumList1 == sumList2:
  print(f"They both have the sum of {sumList1}")
if avgList1 > avgList2:
  print(f"The first list has the larger average of {avgList1}")
elif avgList1 < avgList2:
  print(f"The second list has the larger average of {avgList2}")
elif avgList1 == avgList2:
  print(f"They both have the average of {avgList1}")
print(f"Count of values that appear in both lists: {numSame}")
if list1 == backwardList1 and list2 == backwardList2:
  print('Both lists are palindromes')
elif list1 == backwardList1 or list2 == backwardList2:
  if list1 == backwardList1:
   print('The first list is a palindrome')
  if list2 == backwardList2:
    print('The second list is a palindrome')
else:
  print('The lists are not palindromes')
