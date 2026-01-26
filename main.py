# # This is a sample Python script.
#
# # Press Shift+F10 to execute it or replace it with your code.
# # Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
#
#
# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')
#
# # See PyCharm help at https://www.jetbrains.com/help/pycharm/

from unicodedata import digit
from collections import Counter

actual_value =[10,501,22,37,100,999,87,351]
#actual_value =[351]

even_list=[]
odd_list=[]
prime_list=[]
# To find odd or Even numbers

for i in actual_value:
    if i%2==0:
        even_list.append(i)


    else:
        odd_list.append(i)
print('\n\n\n******* ODD OR EVEN FROM THE LIST*******\n', actual_value,'\n' )
print("The even number list has ", even_list)
print("The odd number list has ", odd_list)




# To find Prime Numbers
print('\n\n\n******* PRIME NUMBER FORM THE LIST *******\n',actual_value,'\n' )
for i in actual_value:
    if i>1:
        prime = 0
        for j in range(2, i-1):
            if i%j == 0:
                prime = prime + 1
    if prime == 0:
        prime_list.append(i)

print("The prime list has ", prime_list)

#To find Happy numbers
print('\n\n\n TO FIND A HAPPY NUMBERS*****\n')
actual_value =[10,501,22,37,100,999,87,351]
for i in range(len(actual_value)):
    num = actual_value[i]
    while num !=1 and num > 9:
        sum_num = 0
        while num >0:

            end_num = num % 10
            sum_num = sum_num + end_num * end_num
            start_num = num // 10
            num = start_num
        num = sum_num
    if num ==1:
        print('\nThe happy number is ', actual_value[i])



print('\n\n\n ******SUM OF FIRST AND LAST DIGIT OF THE LIST*****\n',actual_value,'\n' )
for k in actual_value:

    digit_1 = k//10
    digit_2 = k%10
    if digit_1 >9:
        digit_1 = digit_1//10
    summation = digit_1 + digit_2
    print('The first digit for ',k, 'is ',int(digit_1), '\nThe last digit is ',int(digit_2))
    print('The sum of first and last digits for ',k, 'is ',summation)


coins = [1, 2, 5, 10]
target = 10

# List to store all combinations
combinations = []


for coin10 in range(target//10 + 1):
    for coin5 in range(target//5 + 1):
        for coin2 in range(target//2 + 1):
            for coin1 in range(target + 1):
                if coin10*10 + coin5*5 + coin2*2 + coin1*1 == target:
                    combinations.append((coin10, coin5, coin2, coin1))
                    # print(combinations)

# Print results
print('\n\n\n****** TO MAKE RD 10 USING 1,2,5 ana 10 RS COINS *****')
print("\nTotal combinations:",len(combinations))
for combo in combinations:
    print("10Rs:",{combo[0]}," 5Rs:",{combo[1]}," 2Rs:",{combo[2]}," 1Rs:",{combo[3]})


print('\n\n\n******* FIND THE DUPLICATES FROM THE THREE LIST *****')
list1 = [1,2,5,8,9]
list2 = [2,3,4,5,6]
list3 = [2,3,6,7,8]
result_list = []

print('\nList 1 has the values ',list1)
print('\nList 2 has the values ',list2)
print('\nList 3 has the values ',list3)
for i in list1:
    if i not in list2 or i not in list3:
        result_list.append(i)
print(result_list)
# #sum =(digit_1)**2+(digit_2)**2+(digit_3)**2
# print(sum)
# sum= sum(digit_1)+sum(digit_2)+sum(digit_3)


# sum of first and last digit of a number
# for i in actual_value:
#     start_num= i/10
#     print(start_num)




print('\n\n\n******* FIND THE DUPLICATES FROM THE THREE LIST *****')
list1 = [1,2,5,8,9]
list2 = [2,3,4,5,6]
list3 = [2,3,6,7,8]
result_list = []
duplicates = []
no_duplicate =[]

print('\nList 1 has the values ',list1)
print('\nList 2 has the values ',list2)
print('\nList 3 has the values ',list3)
all_lists = list1+list2+list3
# j=0
# for i in list1:
#     for j in list2:
#         if i==j:
#             result_list.append(i)
#         elif j in list3:
#             result_list.append(i)
#
#         else :
#             no_duplicate.append(i)
# for i in range(len(list1)):
#         for j in range(len(list2)):
#             for k in range(len(list3)):
#                 if list1[i] == list2[j] == list3[k]:
#                     result_list.append(list1[i])
#                 if list2[i] == list3[j] == list1[k] :
#                     result_list.append(list1[j])
#                 if list3[i] == list1[j] == list2[k]:
#                     result_list.append(list1[k])

for  item,count in Counter(all_lists).items():
    #unpacking the tuples. counter will assign 1) Value , 2) Number of times it appeared
    #assigning item for value and count for number of times
    if count > 1:
        duplicates.append(item)
    else:
        # To find the first non repeating number
        no_duplicate.append(item)

print('\nThe duplicate numbers in the list are ',duplicates)
print('\n The unique numbers in the lists are ',no_duplicate)
#To find the first non repeating number
print('\n\n\n The First non repeating number in the list is ',no_duplicate[0])

# To find the minimium number

all_lists.sort()
print('\n\n\n The minium number in the list is ',all_lists[0])

list4 = [10,20,30,9]
target_value = 59

for i in range (1, len(list4)):
    for j in range (i+1, len(list4)):
        for k in range (j+1, len(list4)):
            if list4[i]+list4[j]+list4[k] == target_value:
                print ('\n\n\n The triplets numbers that are results 59 is ', list4[i], list4[j], list4[k] )



print('\n \n\n\n******* To find a sublist whose sum is 0 ******\n')
list5 = [4,2,-3,1,6]

for i in range(len(list5)):
    sum  = 0
    for j in range(i, len(list5)):
        sum = sum + list5[j]

        if sum == 0:
            print("Sub-list with sum 0 found:", list5[i:j+1])