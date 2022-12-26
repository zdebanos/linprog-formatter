# linprog-formatter (lpformat)
A simple Python script which translates the language of inequalities into matrices for computational software
(such as MATLAB, Octave and etc.).
The output is in the form of matrices Ax (>=|<=|=) b.

# Usage
Multiple switches:
## -i
Specify an input text file with a linear optimization problem.
## -o
Specify an output file.
## -m
Specify an optimization mode for the solver (min or max).
## -c
Specify the type of constraint (>= or <= or =).
