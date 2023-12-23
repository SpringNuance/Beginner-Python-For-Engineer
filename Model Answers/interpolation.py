# BPfE SPRING 2022
# Beginner's Python For Engineers
# Author: Visa Mäkeläinen
# Example solution for Exercise "Interpolation"

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def parse_nans(df):
    # Extracts rows without NaN values
    complete_rows = df.dropna()  
    # Extracts rows with NaN values
    na_rows = df[df.isna().any(axis=1)]  
    return complete_rows, na_rows


def fit_parabola(x, y):
    # Calculates coefficients of 2nd degree polynomial
    coefficients = np.polyfit(x, y, 2)  
    return coefficients


def estimate_parabola(x, coefs):
    # Calculates y values corresponding to x values
    y = np.polyval(coefs, x) 
    y = np.around(y, 5) 
    return y


def estimate_parabola_inverse(y, coefs):
    # Creates polyfit object from coefficients
    poly = np.poly1d(coefs)  
    # Calculates x values corresponding to y values
    # These are the maximum roots of vertically-shifted polynomials
    x = [max((poly - y_i).roots) for y_i in y]  
    x = np.around(x, 5) 
    return x  


def main():
    filename = input("Enter the name of the file to be read:\n")

    try:
        # Loading DataFrame and initializing plot
        df = pd.read_csv(filename, index_col="measurement_id")
        fig, ax = plt.subplots()
        
        # Separating complete rows and rows with NaNs; plotting complete data
        df, df_na = parse_nans(df)
        ax.scatter(df['distance'], df['height'], label='Existing data')
        print(f"Loaded data with {len(df)} complete row(s) and {len(df_na)} incomplete row(s).")

        # Finding parabola coefficients; interpolating and plotting NaN rows
        coefs = fit_parabola(df['distance'], df['height'])
        df_na['height'] = estimate_parabola(df_na['distance'], coefs)
        ax.scatter(df_na['distance'], df_na['height'], label='Interpolated data point(s)')
        print(f"Interpolated {len(df_na)} missing height value(s): {list(df_na['height'])}")

        # Extrapolating and plotting maximum distance (y=0)
        y = [0]
        max_distance = estimate_parabola_inverse(y, coefs)
        ax.scatter(max_distance, y, label='Extrapolated maximum distance')
        print(f"Extrapolated maximum distance: {list(max_distance)}")

        # Drawing parabola between 0 and maximum distance
        x_lin = np.linspace(0, max(max_distance))
        y_lin = estimate_parabola(x_lin, coefs)
        ax.plot(x_lin, y_lin, label='Fitted parabola')

        ax.legend()

    except OSError:
        print("Error in reading the file '{:s}'. Program ends.".format(filename))


if __name__ == "__main__":
    main()
