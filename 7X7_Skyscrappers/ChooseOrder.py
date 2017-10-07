stepList=[]
neededClue=2



def chooseSteps(clue, dimension):
    x=0
    y=0
    neededClueVertikal = 2
    neededClueGorizontal = 2
    while len(stepList)<dimension*2:
        verticalIsntChoosen = True
        gorisontalIsntChoosen = True
        while verticalIsntChoosen:
            if neededClueVertikal==2 and clue[x]!=0 and clue[dimension*2+x]!=0:
                stepList.append((x,neededClueVertikal,(clue[x],clue[dimension*2+x]),"vert"))
                verticalIsntChoosen = False
            elif neededClueVertikal==1 and ((clue[x]!=0 and clue[dimension*2+x]==0) or (clue[x]==0 and clue[dimension*2+x]!=0)):
                stepList.append((x,neededClueVertikal,(clue[x],clue[dimension*2+x]),"vert"))
                verticalIsntChoosen = False
            elif  neededClueVertikal==0 and clue[x]==0 and clue[dimension*2+x]==0:
                stepList.append((x,neededClueVertikal,(clue[x],clue[dimension*2+x]),"vert"))
                verticalIsntChoosen = False
            if x < dimension-1 :
                x+=1
            else:
                x=0
                neededClueVertikal+=-1
        while gorisontalIsntChoosen:
            if neededClueGorizontal==2 and clue[dimension+y]!=0 and clue[dimension*3+y]!=0:
                stepList.append((y,neededClueGorizontal,(clue[dimension+y],clue[dimension*3+y]),"gori"))
                gorisontalIsntChoosen = False
            elif neededClueGorizontal==1 and ((clue[dimension+y]!=0 and clue[dimension*3+y]==0) or (clue[dimension+y]==0 and clue[dimension*3+y]!=0)):
                stepList.append((y,neededClueGorizontal,(clue[dimension+y],clue[dimension*3+y]),"gori"))
                gorisontalIsntChoosen = False
            elif  neededClueGorizontal==0 and clue[dimension+y]==0 and clue[dimension*3+y]==0:
                stepList.append((y,neededClueGorizontal,(clue[dimension+y],clue[dimension*3+y]),"gori"))
                gorisontalIsntChoosen = False
            if y < dimension-1 :
                y+=1
            else:
                y=0
                neededClueGorizontal+=-1

    return(stepList)

print(chooseSteps([0,0,2,0,1,0,0,0,0,0,1,0,0,0,0,0,2,0,0,0,1,1,0,0,0,1,0,0],7))
