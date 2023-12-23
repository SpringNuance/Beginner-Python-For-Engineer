from tracemalloc import start
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import time
import math
def measure_time(func):
    # Decorator that measures and reports the time taken by a given function
    def wrap(*args, **kwargs):
        ################################################################
        # WRITE CODE HERE TO FIX 'start_time' AND 'total_time'
        start_time = time.time()
        result = func(*args, **kwargs)  # This line does not need fixing
        total_time = time.time() - start_time
        ################################################################
        print("Function '{}' took approximately {:.5f} seconds.".format(func.__name__, total_time))
        return result
    return wrap

@measure_time
def calculate_mean_manually(column):
    # Gets parameter 'column' as a list, returns its arithmetic mean
    # Calculations are done manually / "by hand" (not using external libraries)
    ###############################
    # WRITE CODE HERE TO FIX 'mean'
    
    mean = calc_average(column)
    ###############################
    return mean

@measure_time
def calculate_sd_manually(column):
    # Gets parameter 'column' as a list, returns its standard deviation
    # Calculations are done manually / "by hand" (not using external libraries)
    #############################
    # WRITE CODE HERE TO FIX 'sd'
    sd = calc_std(column)
    #############################
    return sd
@measure_time
def calculate_linreg_manually(column1, column2):
    # Gets parameters 'column1' and 'column2' as lists, returns the intercept and slope of their OLS regression
    # Calculations are done manually / "by hand" (not using external libraries)
    ################################################
    # WRITE CODE HERE TO FIX 'intercept' AND 'slope'
    sumX = sum(column1)
    sumY = sum(column2)
    sumX2 = sum(list(map(lambda x: x * x, column1)))
    sumXY = sum([column1[i] * column2[i] for i in range(len(column1))])
    n = len(column1)
    intercept = ((sumY * sumX2) - (sumX * sumXY)) / ((n * sumX2) - (sumX * sumX))
    slope = ((n * sumXY) - (sumX * sumY)) / ((n * sumX2) - (sumX * sumX))
    ################################################
    return intercept, slope
@measure_time
def calculate_mean_automatically(column):
    # Gets parameter 'column' as a Pandas Series object (i.e. DataFrame column), returns its arithmetic mean
    # Calculations are done using external libraries
    ###############################
    # WRITE CODE HERE TO FIX 'mean'
    mean = column.mean()
    ###############################
    return mean
@measure_time
def calculate_sd_automatically(column):
    # Gets parameter 'column' as a Pandas Series object (i.e. DataFrame column), returns its standard deviation
    # Calculations are done using external libraries
    #############################
    # WRITE CODE HERE TO FIX 'sd'
    sd = column.std(ddof=0)
    #############################
    return sd
@measure_time
def calculate_linreg_automatically(column1, column2):
    # Gets parameters 'column1' and 'column2' as separate Pandas DataFrame objects,
    # returns the intercept and slope of their OLS regression
    # Calculations are done using external libraries
    ################################################
    # WRITE CODE HERE TO FIX 'intercept' AND 'slope'
    linearRegression = LinearRegression(fit_intercept = True)
    linearRegression.fit(column1.to_numpy().reshape(-1, 1), column2.to_numpy())
    intercept = linearRegression.intercept_
    slope = linearRegression.coef_
    ################################################
    return intercept, slope

def calc_average(grades):
    sum_grade = 0
    for grade in grades:
        sum_grade += grade
    avg = sum_grade / len(grades)
    return avg

def calc_std(grades):
    avg = calc_average(grades)
    squareSum = 0
    for grade in grades:
        gradeDiff = grade - avg
        squareSum += gradeDiff*gradeDiff
    temp = squareSum / len(grades)
    std = math.sqrt(temp)
    return(std)

def main():
    print("Comparison of processing times between manual calculations and libraries")
    # Generates a semi-random DataFrame with two columns and between 500 000 and 2 000 000 rows
    # Some level of covariance between the two columns is randomly created
    seed = int(input('\nEnter a seed for generating the random DataFrame:\n'))
    np.random.seed(seed)
    means = np.array([np.random.randint(0, 100), np.random.randint(0, 100)])
    covariance = np.random.rand() * 2 - 1
    covariance_matrix = np.array([[1, covariance], [covariance, 1]])
    df = pd.DataFrame(np.random.multivariate_normal(means, covariance_matrix, size=np.random.randint(500000, 2000000)),
                      columns=['A', 'B'])
    print("Created a DataFrame of {} columns and {} rows.".format(df.shape[1], df.shape[0]))
    print('\nCalculating statistics manually...')
    manual_results = {}
    manual_results['mean'] = calculate_mean_manually(df['A'].tolist())
    manual_results['sd'] = calculate_sd_manually(df['A'].tolist())
    manual_results['intercept'], manual_results['slope'] = calculate_linreg_manually(df['A'].tolist(), df['B'].tolist())
    print('\nCalculating statistics using the libraries...')
    library_results = {}
    library_results['mean'] = calculate_mean_automatically(df['A'])
    library_results['sd'] = calculate_sd_automatically(df['A'])
    library_results['intercept'], library_results['slope'] = calculate_linreg_automatically(df[['A']], df[['B']])
    for key in manual_results:
        if not math.isclose(manual_results[key], library_results[key], rel_tol=0.001):
            print("\nDifferences found between the '{}' results – at least one calculation is incorrect.".format(key))
            break
    else:
        print("\nThe arithmetic mean of Column A is {:.4f}.".format(manual_results['mean']))
        print("The standard deviation of Column A is {:.4f}.".format(manual_results['sd']))
        print("The linear regression relationship between Columns A and B is roughly 'B = {:.4f} + {:.4f} × A'."
              .format(manual_results['intercept'], manual_results['slope']))

if __name__ == "__main__":
    main()