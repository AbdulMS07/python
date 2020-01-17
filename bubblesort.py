def sort1(n):
    for i in range(len(n)-1,0,-1):
        for j in range(i):
            if n[j]>n[j+1]:
                n[j],n[j+1]=n[j+1],n[j]

n=[23,56,12,34,89,6,2,4,72]
sort1(n)
print(n)
print("Enter the list to sort:")

a=[int(i) for i in input().split()]
print(a)

def bubsort(a):
    b=len(a)-1
    for x in range(b):
        for y in range(b-x):
            if a[y]>a[y+1]:
                a[y],a[y+1]=a[y+1],a[y]
    return a

print(bubsort(a))
c=bubsort(a)
print(c)