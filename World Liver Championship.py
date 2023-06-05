#World Liver Championship
#مسابقات جهانی کبدی
c=0
n=int(input())
list1 = input().split()
numbers = [int(item) for item in list1]
for i in range(0,len(numbers)):
    if numbers[i] <= 2:
        c=c+1
print(c//3)     
        