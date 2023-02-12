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

