Totaltest = 500
# mylist has all the numbers to be used in the Binary Multiplication Test
mylist=[2,2,5,4,5,7,8,4,3,2,8,5,7,20,8,3,9,10]
print(mylist)
# Init binlist based on the length of mylist
binlist = [0]*len(mylist)
print(binlist)
total=1
binindex=0
while sum(binlist) < len(binlist):
    binindex=0
    total = 1
    for num in mylist:
        if binlist[binindex] == 1:
            # print(num)
            binindex = binindex + 1
            total = total*num
            # print(total)
        else:
            binindex = binindex +1
    if total == Totaltest:
        print(f"TOTAL = {total} - {binlist} {mylist}")
    n=0            
    for binnum in binlist:
        # print(binnum)
        if binnum==0:
            binlist[n]=1
            break
        else:
            binlist[n]=0
            n=n+1
        # print(binlist)
print(binlist)
