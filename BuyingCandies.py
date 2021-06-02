def candyStore(List,k,N):
    ListMax=sorted(List,reverse=True)
    ListMin=sorted(List,reverse=False)
    MoneyMax=0
    MoneyMin=0
    for valuesMax,valuesMin in zip(ListMax,ListMin):
        MoneyMax+=valuesMax
        MoneyMin+=valuesMin
        for times in range(k):
            ListMax.pop()
            ListMin.pop()

    # print(MoneyMin)
    # print(MoneyMax)
    return MoneyMin,MoneyMax
if __name__ == '__main__':
    List = [3, 2, 1, 4]
    k = 2
    N = 4
    print(candyStore(List,k,N))
