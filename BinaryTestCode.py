# the purpose of this copde is to identify if ANY combination of the numbers in my list
# can be multiplied together to total the number in Totaltest
# if so, it will print out the binlist and mylist LIST to verify 
Totaltest = 20
# mylist has all the numbers to be used in the Binary Multiplication Test
mylist=[2,3,4,5,6,2,4,6,8,7,3,2,2]
print(mylist)
# Init binlist based on the length of mylist
binlist = [0]*len(mylist)
print(binlist)
total=1
binindex=0
while sum(binlist) <= len(binlist):
    binindex=0
    # if first iteration Then No numbers will be used, and Total must = 0 to ensure it does not match "1"
    if sum(binlist)==0:
        total = 0
    else:
        total =1
 
    n=0            
    for num in mylist:
        if binlist[binindex] == 1:
            # print(num)
            if num == 0:
                total = 0 
            else: 
                total = total*num
            binindex = binindex + 1
            
            # print(total)
        else:
            binindex = binindex +1
    
    # Test Print for Debug - all iterations 
    # print(f"TOTAL-TEST = {total} - {binlist} {mylist}")
    
    # Printout if Test is true
    if total == Totaltest:
        print(f"TOTAL = {total} - {binlist} {mylist}")
    
    if sum(binlist)==len(binlist):
        break       
        # Stop While Loop once binlist is all '1's 

    for binnum in binlist:
        # print(binnum)
        if binnum==0:
            binlist[n]=1
            break
        else:
            binlist[n]=0
            n=n+1
        
# Final Print of binlist - should be all "1"s
print(binlist)
