def spirallyTraverse(List,R,C):
    nodesCount=R*C+1

    row=0
    col=0
    ListRet=[]

    Check=1
    visited="visited"



    while nodesCount!=0:

        nodesCount-=1

        if List[row][col] != "visited":
            # print(List[row][col])
            ListRet.append(List[row][col])
            List[row][col] = visited


        if Check==1:
            if col<C-1:
                if (List[row][col+1]!=visited):
                    col+=1
                elif row<R-1:
                    if (List[row+1][col]!=visited):
                        row+=1
                    else:
                        Check=0

            elif row<R-1:
                if (List[row+1][col]!=visited):
                    row+=1
            else:
                Check=0

        if Check==0:
            if col>0:
                if (List[row][col-1]!=visited):
                    col-=1
            elif row>0:
                if (List[row-1][col]!=visited):
                    row-=1
                else:
                    Check=1
            else:
                Check=1

    return ListRet

if __name__ == '__main__':


    Matrix=[[1, 2, 3, 4], [5, 6,7,8], [9, 10, 11, 12], [13,14,15,16]]

    R = 4
    C = 4


    print(spirallyTraverse(Matrix,R,C))

