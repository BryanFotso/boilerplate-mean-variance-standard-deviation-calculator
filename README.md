# Mean-Variance-Standard Deviation Calculator

This is the boilerplate for the Mean-Variance-Standard Deviation Calculator project. Instructions for building your project can be found at https://www.freecodecamp.org/learn/data-analysis-with-python/data-analysis-with-python-projects/mean-variance-standard-deviation-calculator

This project implements a Python function calculate() that uses the Numpy library to compute various statistical indicators for a 3x3 matrix. It is part of an educational project forked from freeCodeCamp.

## Features

The calculate() function returns the following statistics for a 3x3 matrix, along the row and column axes, as well as for the entire matrix:

Mean
Variance
Standard Deviation
Maximum Value
Minimum Value
Sum

## Output Dictionary Structure
The function’s output is a dictionary containing each statistic as a list for all three dimensions:

{
  'mean': [by_columns, by_rows, flattened],
  'variance': [by_columns, by_rows, flattened],
  'standard deviation': [by_columns, by_rows, flattened],
  'max': [by_columns, by_rows, flattened],
  'min': [by_columns, by_rows, flattened],
  'sum': [by_columns, by_rows, flattened]
}
