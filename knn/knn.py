import csv
import math

with open('movie.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    list = list(readCSV)

    list2=[]


    for i in  range(1,len(list)):
        list2.append(list[i])


    slice1 = []
    slice2 = []

    slice1 = list2[:24]
    slice2 =list2[24:len(list2)]



    print(type(slice1[2][4]))

    print("Enter a Movie ID : ")

    input=input()



    inputlist=[]


    for i in range(0,len(slice2)):



        var=slice2[i][0]


        if(input==var):
            inputlist=slice2[i]

    result=[]


    for j in range(0,len(slice1)):
        result.append([])

        sum = 0
        for k in range(2, 10):
            sub=0
            val1=float(inputlist[k])
            val2=float(slice1[j][k])
            sub=pow((val1-val2),2)
            sum +=sub
        rootover=math.sqrt(sum)
        for l in range(2):
            if l==0:
                result[j].append(slice1[j][1])
            else:
                result[j].append(rootover)



    def takeSecond(elem):
        return elem[1]

    result.sort(key=takeSecond)
    print("Topmost 5 movies are ")

    print(result)

    print(" ")
    print(">>")
    print(" ")
    for m in range(5):
        print(result[m][0])



