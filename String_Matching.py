str1 = list(map(str,input()))
str2 = list(map(str,input()))
total_arrangements = 0

if len(str1) >= len(str2):
    length = len(str1)
else:
    length = len(str2)

for i in range(length):
    ##checking normal cases for the same length strings
    if (len(str1) > i and len(str2) > i):
        if str1[i] != str2[i]:
            if str1[i] == str2[i-1]:
                str2.insert(i,str1[i])
                total_arrangements=total_arrangements+1
            elif str1[i-1] == str2[i]:
                str1.insert(i,str2[i])
                total_arrangements=total_arrangements+1
    else:
        ##checking the case like: 'rebeel' and 'rebeellllll'
        if length == len(str1):
            for leftover_indx in range(i,len(str1)):
                if str1[leftover_indx] == str2[-1:]:
                    str2.insert(i,str2[i-1])
                    total_arrangements=total_arrangements+1
        else:
            for leftover_indx in range(i,len(str2)):
                if str2[leftover_indx] == str1[i-1]:
                    str1.insert(i,str1[i-1])
                    total_arrangements=total_arrangements+1
if str1 == str2:
    print(total_arrangements)
else:
    print('Not possible')
