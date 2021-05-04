import numpy as np

def getData(filename):
    datadir = 'MaterialData/'
    with open(datadir + filename, 'r') as f:
        data_in_rows = f.read().split('\n')
        data_in_rows = filter(lambda row: row != '', data_in_rows)
        data_as_matrix = np.array([row.split('\t') for row in data_in_rows])
        H_col = data_as_matrix[:,0]
        B_col = data_as_matrix[:,1]
        return H_col.astype(float), B_col.astype(float)

def calcH(x, H_col, B_col, *args, **kwargs):
    x_data = B_col
    y_data = H_col
    y = interpolate(x, x_data, y_data, *args, **kwargs)
    return y

def calcB(x, H_col, B_col, *args, **kwargs):
    x_data = H_col
    y_data = B_col
    y = interpolate(x, x_data, y_data, *args, **kwargs)
    return y

def interpolate(x, x_data, y_data, *args, **kwargs):
    
    indexes = np.array(nearValues(x,x_data,*args,**kwargs))

    x_data = x_data[indexes]
    y_data = y_data[indexes]
    
    coef = divided_diff(x_data, y_data)[0,:]
    
    return newton_poly(coef, x_data, x)

def divided_diff(x, y):
    '''
    function to calculate the divided
    differences table
    '''
    n = len(y)
    coef = np.zeros([n, n])
    # the first column is y
    coef[:,0] = y
    
    for j in range(1,n):
        for i in range(n-j):
            coef[i][j] = \
           (coef[i+1][j-1] - coef[i][j-1]) / (x[i+j]-x[i])
            
    return coef

def newton_poly(coef, x_data, x):
    '''
    evaluate the newton polynomial 
    at x
    '''
    n = len(x_data) - 1 
    p = coef[n]
    for k in range(1,n+1):
        p = coef[n-k] + (x -x_data[n-k])*p
    return p

def nearValues(x, xi, strategy=0):
    k = len(xi)-1
    i = np.abs(xi - x).argmin()
    i = i if (xi[i] <= x or i==0) else i-1
    if strategy in [0]:
        indexes = [0,1,2,3] if (i==0) else \
            [i-1,i,i+1,i+2] if (i < k-1) else [k-3, k-2, k-1, k]
    elif strategy in [1]:
        indexes = \
            [i,i+1,i+2,i+3] if (i < k-2) else [k-3, k-2, k-1, k]
    elif strategy in [2]:
        indexes = [0,1,2,3,4] if (i<3) else \
            [i-2,i-1,i,i+1,i+2] if (i < k-1) else [k-4,k-3,k-2,k-1,k]
    elif strategy in [3]:
        indexes = [0,1,2,3,4] if (i<2) else \
            [i-1,i,i+1,i+2,i+3] if (i < k-2) else [k-4,k-3,k-2,k-1,k]
    return indexes
