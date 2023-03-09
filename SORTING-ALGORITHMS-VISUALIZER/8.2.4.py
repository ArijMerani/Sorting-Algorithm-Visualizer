def countingSort(array,max,a,b):
    size = len(array) 
    output = [0] * size

    # Initialize count array
    count = [0] * max

    # Store the count of each elements in count array
    for i in range(0, size):
        count[array[i]] += 1

    # Store the cummulative count
    for i in range(1, max):
        count[i] += count[i - 1]

    print("cummulative count array" )    
    print(count) 
    
    print("Numbers that lie in range",a,'...',b)
    if a==0:
        print(count[b]) 
    else:
        print(count[b]-count[a-1])

    i = size - 1
    while i >= 0:
        output[count[array[i]] - 1] = array[i]
        count[array[i]] -= 1
        i -= 1

    for i in range(0, size):
        array[i] = output[i]    

data = []
file_array = open('data.txt' , "r")
for i in file_array:
    data.append(int(i))

max = max(data)
#print(max);
print("a and b must be in range 0 to", max)
a = int(input("Enter a: "))
b = int(input("Enter b: "))

while (a<0 or a>b or a>max):
    a = int(input("Enter correct value of a: "))
while (b<a or b>max):
    b = int(input("Enter correct value of b: "))   

countingSort(data,max+1,a,b)
print("Sorted array")
print(data)