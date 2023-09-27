print("enter the elements in the list")
list1=list(map(int,input().split()))
list1.sort()
target=int(input("enter number to be searched"))
def binary_search(list1,target):
    start=0
    end=len(list1)
    while(start<=end):
        mid=(start+end)//2
        if(list1[mid]==target):
            print(f"{target} found at {mid}")
            break
        elif list1[mid]<target:
            start=mid+1
        else:
            end=mid-1
    return -1
    
binary_search(list1,target)
