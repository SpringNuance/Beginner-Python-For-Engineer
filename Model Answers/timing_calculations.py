import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import time
from math import isclose


def measure_time(func):
    # Decorator that measures and reports the time taken by a given function
    def wrap(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        total_time = time.perf_counter() - start_time
        print("Function '{}' took approximately {:.5f} seconds.".format(func.__name__, total_time))
        return result

    return wrap


@measure_time
def calculate_mean_manually(column):
    mean = sum(column) / len(column)
    return mean


@measure_time
def calculate_sd_manually(column):
    mean = sum(column) / len(column)
    sum_of_squared_deviations = 0
    for number in column:
        sum_of_squared_deviations += (number - mean) ** 2
    sd = (sum_of_squared_deviations / len(column)) ** 0.5
    return sd


@measure_time
def calculate_linreg_manually(column1, column2):
    length = len(column1)
    sum1 = sum(column1)
    sum2 = sum(column2)
    squared_sum1 = 0
    squared_sum2 = 0
    multiplied_sum = 0
    for i in range(len(column1)):
        squared_sum1 += column1[i] ** 2
        squared_sum2 += column2[i] ** 2
        multiplied_sum += column1[i] * column2[i]
    intercept = ((sum2 * squared_sum1) - (sum1 * multiplied_sum)) / ((length * squared_sum1) - sum1 ** 2)
    slope = (length * multiplied_sum - sum1 * sum2) / (length * squared_sum1 - sum1 ** 2)
    return intercept, slope


@measure_time
def calculate_mean_automatically(column):
    mean = column.mean()    # Alternatively np.mean(column)
    return mean


@measure_time
def calculate_sd_automatically(column):
    sd = column.std(ddof=0) # Alternatively np.std(column)
    return sd


@measure_time
def calculate_linreg_automatically(column1, column2):
    model = LinearRegression().fit(column1, column2)
    intercept = model.intercept_.item()
    slope = model.coef_.item()
    return intercept, slope


def main():
    print("Comparison of processing times between manual calculations and libraries")
    seed = int(input('\nEnter a seed for generating the random DataFrame:\n'))
    np.random.seed(seed)
    means = np.array([np.random.randint(0, 100), np.random.randint(0, 100)])
    covariance = np.random.rand() * 2 - 1
    covariance_matrix = np.array([
        [1, covariance],
        [covariance, 1]
    ])
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
        if not isclose(manual_results[key], library_results[key], rel_tol=0.001):
            print("\nDifferences found between the '{}' results – at least one calculation is incorrect.".format(key))
            break
    else:
        print("\nThe arithmetic mean of Column A is {:.4f}.".format(manual_results['mean']))
        print("The standard deviation of Column A is {:.4f}.".format(manual_results['sd']))
        print("The linear regression relationship between Columns A and B is roughly 'B = {:.4f} + {:.4f} × A'."
              .format(manual_results['intercept'], manual_results['slope']))


if __name__ == "__main__":
    main()
