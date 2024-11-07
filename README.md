
# Taylor Series Sine Function Calculator

This Python program calculates the Taylor series approximation of the sine function, \(\sin(x)\), around \(x_0 = 0\). It also visualizes the sine function calculated for different values of \(N\) (the maximum exponent in the Taylor series), allowing you to see the convergence of the Taylor series to the actual sine function as \(N\) increases.

## Project Overview

The Taylor series approximation of \(\sin(x)\) is calculated up to a specified number of terms \(N\). By calculating and plotting the series for multiple values of \(N\), the project demonstrates how the Taylor series increasingly resembles the sine function as more terms are added. The program also computes and prints the difference between the calculated Taylor series approximation and Python's `math.sin` function for a given angle.

## Key Features

- **Taylor Series Approximation**: Calculates the sine of an angle \(x\) using the Taylor series formula:
  \[
  \sin(x) \approx \sum_{n=0}^{N} \frac{(-1)^n}{(2n+1)!}x^{(2n+1)}
  \]
- **Graphical Comparison**: Plots the true sine function and the Taylor series approximation for various values of \(N\), illustrating the accuracy of the approximation.
- **Error Calculation**: Compares the result of the Taylor series approximation with Python’s `math.sin` function and prints the difference.

## Requirements

- Python 3.x
- NumPy
- Matplotlib

To install the required packages, run:

```bash
pip install numpy matplotlib
```

## Usage

1. Run the program and input:
   - The angle (in radians) for which you want to calculate the sine.
   - The number \(N\), which determines the maximum exponent in the Taylor series (note that \(N = 2n + 1\), where \(n\) is the number of terms).
   
2. The program will output:
   - The sine calculated using the Taylor series.
   - The sine calculated by Python's `math.sin` function.
   - The difference between the two values.

3. A graph will display the true sine function and Taylor series approximations for different values of \(N\) (3, 5, 7, 9).

## Project Structure

- **taylor_sine(x, N)**: Function to calculate the Taylor series approximation for \(\sin(x)\).
- **Main Code**: Takes user inputs, calculates the sine, compares with `math.sin`, and plots the sine function for varying values of \(N\).

## Example

To calculate \(\sin(x)\) for \(x = \pi/4\) and \(N = 9\):

```plaintext
Enter the value of the angle you want to know the sine of (in radians): 0.785
Enter the value of N: 9
Sine calculated by the created function: 0.7071067811865475
Math module sine function: 0.7071067811865475
Difference between calculated and math module result: 0.0
```

## Visualization

The program plots the sine function for values of \(N\) from 3 to 9, allowing you to see how the Taylor series approximation improves with more terms.

## License

This project is open-source and free to use.

