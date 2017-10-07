def iterCombi(upNumber, iterDeep, frozeList, dimension):
    combiList=[]
    for dec in range(0,dimension):
        if dec not in frozeList:
            version = upNumber + iterDeep*(10**dec)
            if iterDeep < dimension:
                frozeListLok=frozeList[:]
                frozeListLok.append(dec)
                lowerList = iterCombi(version, iterDeep + 1, frozeListLok, 7)
                for num in lowerList:
                    combiList.append(num)
            else:
                combiList.append(version)
    return(combiList)

def listSorter(unsortedList):
    sortedList = {}
    for num in unsortedList:
        left=0
        right=0
        wiev=0
        numRew = ""
        i = 0
        for dig in str(num):
            numRew = dig + numRew
            if wiev<int(dig):
                left+=1
                wiev =int(dig)
            try:
                sortedList[("byDigit",int(dig),i)].append(int(num))
            except:
                sortedList[("byDigit",int(dig),i)]=[]
                sortedList[("byDigit",int(dig),i)].append(int(num))
            i+=1
        wiev=0
        for dig in numRew:
            if wiev<int(dig):
                right+=1
                wiev =int(dig)
        try:
            sortedList[(left,right)].append(int(num))
        except:
            sortedList[(left,right)]=[]
            sortedList[(left,right)].append(int(num))
        try:
            sortedList[(0,right)].append(int(num))
        except:
            sortedList[(0,right)]=[]
            sortedList[(0,right)].append(int(num))
        try:
            sortedList[(left,0)].append(int(num))
        except:
            sortedList[(left,0)]=[]
            sortedList[(left,0)].append(int(num))
        try:
            sortedList[(0,0)].append(int(num))
        except:
            sortedList[(0,0)]=[]
            sortedList[(0,0)].append(int(num))
    return(sortedList)
    
print(listSorter(iterCombi(0,1,[],7))[("byDigit",2,1)])
