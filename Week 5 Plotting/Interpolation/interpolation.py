# Template code for Exercise "Interpolation"
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
def parse_nans(df):
    ##########################################################
    # WRITE CODE HERE TO EXTRACT 'complete_rows' and 'na_rows'
    complete_rows = df  
    na_rows = df
    ##########################################################
    return complete_rows, na_rows
def fit_parabola(x, y):
    #############################################
    # WRITE CODE HERE TO CALCULATE 'coefficients'
    coefficients = []
    #############################################
    return coefficients
def estimate_parabola(x, coefs):
    ##################################
    # WRITE CODE HERE TO CALCULATE 'y'
    y = []
    ################################## 
    return y
def estimate_parabola_inverse(y, coefs):
    ##################################
    # WRITE CODE HERE TO CALCULATE 'x'
    x = []
    ################################## 
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