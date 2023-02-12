#make a function to calculate the linear regression of a set of data


def linear_regression(x,y): #x and y are lists of data
    n = len(x)
    x_sum = sum(x)
    y_sum = sum(y)
    x_squared_sum = sum([i**2 for i in x])
    xy_sum = sum([x[i]*y[i] for i in range(n)])
    slope = (n*xy_sum - x_sum*y_sum)/(n*x_squared_sum - x_sum**2)
    intercept = (y_sum - slope*x_sum)/n
    return slope, intercept

#make a function that prints in separate rows the mean median and mode of ten values
def mean_median_mode(): #no arguments
    import statistics
    import random
    data = [random.randint(1,100) for i in range(10)]
    print("Mean: ", statistics.mean(data))
    print("Median: ", statistics.median(data))
    print("Mode: ", statistics.mode(data))

#call the functions and print the results   
print(linear_regression([1,2,3,4,5],[1,2,3,4,5]))
mean_median_mode()

# Python program to print
# median of elements
 
# list of elements to calculate median
n_num = [1, 2, 3, 4, 5]
n = len(n_num)
n_num.sort()
 
if n % 2 == 0:
    median1 = n_num[n//2]
    median2 = n_num[n//2 - 1]
    median = (median1 + median2)/2
else:
    median = n_num[n//2]
print("Median is: " + str(median))

#make a function that prints the median of ten values without using statistics
def median(): #no arguments
    import random   
    data = [random.randint(1,100) for i in range(10)]   
    data.sort()
    if len(data) % 2 == 0:
        median1 = data[len(data)//2]
        median2 = data[len(data)//2 - 1]
        median = (median1 + median2)/2
    else:   
        median = data[len(data)//2]
    print("Median is: " + str(median))

#call the function and print the results
median()
