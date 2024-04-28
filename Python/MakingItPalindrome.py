def countMin(str):
    Check=0
    Counter=0
    midpoint=0
    SoFarLength=0
    for iterator in range(len(str)):
        if  iterator>1 and Check==0:
            if str[iterator]==str[iterator-2]:
                Check=1
                Counter+=1
                SoFarLength=iterator-2
                midpoint=iterator-2
                midpoint-=1
        elif Check==1 and str[iterator]==str[midpoint]:
            Counter+=1
            midpoint-=1
        else:
            Check=0
            Counter=0
            midpoint=0
            SoFarLength=0

    if SoFarLength>0:
        return (SoFarLength-Counter+1)
    else:
        if len(str)<=2:
            if str[0]!=str[1]:
                return (1)
            else:
                return (0)
        else:
            return (len(str)-1)




if __name__ == '__main__':
    str = "aa"


    print(countMin(str))
