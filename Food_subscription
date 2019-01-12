no_of_eating_days = int(input())
if (no_of_eating_days == 0 ):
	print('0') ## case when no of eating dat is zero.
else:
    ## case when minimum 199 is valid for subscription amount
    eating_days = list(map(int,input().split()))
    low = 0
    dates_covered = 0
    total_amt=0
    while(low<no_of_eating_days):
        if (eating_days[low] > dates_covered):
            high = low + 3
            if (high >= no_of_eating_days):
                total_amt+= 199
                low+=1
            elif (eating_days[high] <= (eating_days[low] + 6)):
                total_amt+= 699
                dates_covered = eating_days[low] + 6;  
                for i in range(low+1,len(eating_days)):
                    if eating_days[i]>dates_covered:
                        low = i
                        break
            else:
                total_amt+= 199
                low+=1
    if total_amt>2499:
        print('2499')   ## case when whole month subscription is beneficial
    else:
        print(total_amt) ## or else, returning the minimum cost for subscriptions required
