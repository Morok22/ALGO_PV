import time
from urllib3.connectionpool import xrange


def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

def select_sort(arr):
    i = len(arr)
    while i > 1:
        max = 0
        for j in xrange(i):
            if arr[j][1] > arr[max][1]:
                max = j
            if arr[j][1] == arr[max][1]:
                if arr[j][3] > arr[max][3]:
                    max = j
        swap(arr, i - 1, max)
        i -= 1

def quickSort(alist):
   quickSortHelper(alist,0,len(alist)-1)

def quickSortHelper(alist,first,last):
   if first<last:

       splitpoint = partition(alist,first,last)

       quickSortHelper(alist,first,splitpoint-1)
       quickSortHelper(alist,splitpoint+1,last)


def partition(alist,first,last):
   pivotvalue = alist[first]

   leftmark = first+1
   rightmark = last

   done = False
   while not done:

       while leftmark <= rightmark and alist[leftmark][1] <= pivotvalue[1]:
           leftmark = leftmark + 1

       while alist[rightmark][1] >= pivotvalue[1] and rightmark >= leftmark:
           rightmark = rightmark -1

       if rightmark < leftmark:
           done = True
       else:
           temp = alist[leftmark]
           alist[leftmark] = alist[rightmark]
           alist[rightmark] = temp

   temp = alist[first]
   alist[first] = alist[rightmark]
   alist[rightmark] = temp


   return rightmark


file = open('bd.txt','r') #відкриття файлу

vase = []
vaseGlass = []
vass = []
strVase = ''

for line in file: #цикл по файлу
    strVase = line.rstrip() # видалення спец символів закінчення рядка
    vass = strVase.split(", ") # поділ стрічки на слова
    if vass[2] == 'GLASS': #якщо матеріал вази Glass
        vass[1] = int(vass[1]) #перетворення номера та обєм бака в число
        vass[3] = int(vass[3])
        vaseGlass.append(vass) #запис в масив
    else:
        vass[1] = int(vass[1])  # перетворення висоту та вагу вази в число
        vass[3] = int(vass[3])
        vase.append(vass) #запис в масив

i = 0

arr = []
start_time = time.time() # початкок часу
arr = quickSort(vase) #виклик функції сортування
select_sort(vaseGlass)#виклик функції сортування
print("Time %s seconds" % (time.time() - start_time)) #вивід часу
print ("\n")
for line in vaseGlass: #вивід в циклі
    print (vaseGlass[i])
    i+=1

i=0
for line in vase:  #вивід в циклі
    print (vase[i])
    i+=1


