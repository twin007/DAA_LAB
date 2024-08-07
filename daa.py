import matplotlib.pyplot as plt 
import random 
def bubble_sort(arr):
    n=len(arr)
    step_count=0
    for i in range(n):
        for j in range(0, n-i-1):
            step_count += 1  # Counting the comparison
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
                step_count += 1  # Counting the swap
    return step_count
def selection_sort(arr):
    n=len(arr)
    step_count =0
    for i in range (0,n):
        key = i
        step_count+=1
        for j in range(i+1,n):
            step_count+=1
            if arr[j]< arr[key]:         
                key = j
                step_count+=1
        arr[i],arr[key] = arr[key],arr[i]  
        step_count +=1            #swap the elements
    return step_count


arr = []
arr_sb = []
arr_ss = []
arr_y = [10,20,30,40,50,60,70,80,90,100]
arr_size = 100 
x= 10
while x <= arr_size:
    for i in range(x):
        a = random.randint(1,100)
        arr.append(a)
    sb = bubble_sort(arr)
    ss = selection_sort(arr)
    arr_sb.append(sb)
    arr_ss.append(ss)
    x += 10

plt.plot(arr_y, arr_ss)
plt.plot(arr_y, arr_sb)
plt.xlabel('bubble_sort(orange), selection_sort(blue)')
plt.ylabel('step count')
plt.title('line plot')
plt.show()
