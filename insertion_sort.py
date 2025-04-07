

def insertion_sort(list):
    n=len(list)
    for j in range (1,n-1):
        item=arr[i]
        while list[j-1]>item and j>0:
            arr[j]=arr[j-1]
            j-=1
        
       arr[j+1] =item














list=[5,4,3,2,1]
insertion_sort(list)
print(list)