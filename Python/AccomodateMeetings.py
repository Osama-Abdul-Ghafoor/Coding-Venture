def activityselection(TimeS,TimeF,N):

    TimeS, TimeF = zip(*sorted(zip(TimeS, TimeF)))

    Last=TimeF[0]
    count=0
    for iterator in range(1, len(TimeS)):
        if TimeS[iterator] > Last:
            Last = TimeF[iterator]
            count = count + 1


    return count+1

if __name__ == '__main__':
    start = [1, 3, 2, 5]
    finish = [2, 4, 3, 6]
    N=4
    print(activityselection(start,finish,N))