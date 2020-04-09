# Simple Naive Bayes 
# dari materi pdf

# keterangan 
# <=30      = 1
# 31..40    = 2
# >40       = 3

data=[
    [1, "High",     "No",   "Fair",         "No"],
    [1, "High",     "No",   "Excellent",    "No"],
    [2, "High",     "No",   "Fair",         "Yes"],
    [3, "Medium",   "No",   "Fair",         "Yes"],
    [3, "Low",      "Yes",  "Fair",         "Yes"],
    [3, "Low",      "Yes",  "Excellent",    "No"],
    [2, "Low",      "Yes",  "Excellent",    "Yes"],
    [1, "Medium",   "No",   "Fair",         "No"],
    [1, "Low",      "Yes",  "Fair",         "Yes"],
    [3, "Medium",   "Yes",  "Fair",         "Yes"],
    [1, "Medium",   "Yes",  "Excellent",    "Yes"],
    [2, "Medium",   "No",   "Excellent",    "Yes"],
    [2, "High",     "Yes",  "Fair",         "Yes"],
    [3, "Medium",   "No",   "Excellent",    "No"],
]

def matchAllCondition(row,arr):
    tambah=0
    for item in arr:
        a = row[item[0]]
        b = item[1]
        
        if type(a) is str:
            a=a.lower()

        if type(b) is str:
            b=b.lower()

        if( a == b ):
            tambah+=1

    if(tambah == len(arr)):
        return True

    return False

def hitungProbabilitas(data,arr,output="prob",banding=None):
    if banding is 0:
        print("banding adalah 0\ntidak bisa membagi dengan 0")
        return False
    
    if banding is None:
        banding = len(data)
  
    # Params
    # arr= [ 
    #     [idx,condition]
    # ]


    totalMatch=0
    for row in data:
        isMatch = matchAllCondition(row,arr)
        # print(row)
        # print(isMatch)
        if(isMatch):
            totalMatch+=1

    if output is "prob":
        return totalMatch/banding
    else:
        return totalMatch




p1= hitungProbabilitas(data,[[4,"yes"]])
print(p1)


p2= hitungProbabilitas(data,[[4,"no"]])
print(p2)


banyakYes= hitungProbabilitas(data,[[4,"Yes"]],"jumlah")
banyakNo = hitungProbabilitas(data,[[4,"No"]],"jumlah")


p3 = hitungProbabilitas(data,[
        [0,1],
        [4,"Yes"]
    ],"prob",banyakYes)

print(p3)


p4 = hitungProbabilitas(data,[
        [0,1],
        [4,"No"]
    ],"prob",banyakNo)

print(p4)





p5 = hitungProbabilitas(data,[
        [1,"Medium"],
        [4,"Yes"]
    ],"prob",banyakYes)

print(p5)


p6 = hitungProbabilitas(data,[
        [1,"Medium"],
        [4,"No"]
    ],"prob",banyakNo)

print(p6)
        



p7 = hitungProbabilitas(data,[
        [2,"Yes"],
        [4,"Yes"]
    ],"prob",banyakYes)

print(p7)


p8 = hitungProbabilitas(data,[
        [2,"Yes"],
        [4,"No"]
    ],"prob",banyakNo)

print(p8)







p9 = hitungProbabilitas(data,[
        [3,"fair"],
        [4,"Yes"]
    ],"prob",banyakYes)

print(p9)


p10 = hitungProbabilitas(data,[
        [3,"fair"],
        [4,"No"]
    ],"prob",banyakNo)

print(p10)
        
            

ax = p3 * p5 * p7 * p9
bx = p4 * p6 * p8 * p10

print("ax ",ax)
print("bx ",bx)


c = ax*p1
d = bx*p2

print(c)
print(d)