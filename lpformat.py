#!/bin/python3

#TODO:
#vyresit cely prevadeni textoveho souboru

import sys
from os import _exit

def exit0():
    _exit(0)

def exit1():
    _exit(1)

def err_print(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

def print2(str):
    print("  "+str)

def print4(str):
    print("    "+str)

def print_usage():
    print("lpformat - transform inequalities into the form of Ax <= b or Ax >= b or Ax = b")
    print("USAGE:")
    print2("-h, --help:   print detailed help")
    print2("-i, --input:  input file with inequalities")
    print2("-o, --output: output file with A,x,b matrices")

def print_help():
    print_usage()
    print()
    print("Everything is printed to stderr except the A, x, b matrices")
    print("(which are printed to stdin) if no output file is specified.")
    print()
    print("INPUT FILE FORMAT:")
    print2("VN = variable name")
    print2("You don't have to declare variables, this script gets their names.")
    print2("The input file must include min/max statement with a linear expression,")
    print4("e.g. max/min 2*VN1 - 5*VN2")
    print()
    print2("An inequality must look something like this:")
    print4("2*VN1+3*VN2-4*VN3 = 5 (or >= 5 or <= 5)")
    print4("This scripts finds 3 variables - VN1, VN2, VN3 with corresponding coeffs.")
    print4("A variable mustn't start with a number, e.g. 3VN2 won't work!")
    print("If no input file is specified, this script exits with the 1 exit code.")
    print()
    print("OUTPUT FILE:")
    print2("If no output file is specified, it prints the A, x, b matrices to stdin.")

ARGS = ["--help", "-h", "--input", "-i", "--output", "-o", "-m", "--mode",\
        "-c", "--constraint"]

def ne_to_other_args(s):
    for arg in ARGS:
        if s == arg:
            return False
    return True

def getent():
    if len(sys.argv) == 1:
        print_usage()
        exit1()
    in_file = ""
    out_file = ""
    mode = ""
    constraint = ""
    args = sys.argv
    ln = len(args)
    for i in range(ln):
        if args[i] == "--help" or args[i] == "-h":
            print_help()
            exit1()
        elif (args[i] == "-i" or args[i] == "--input") and \
           i != ln-1 and ne_to_other_args(args[i+1]):
            in_file = args[i+1]
        elif (args[i] == "-o" or args[i] == "--output") and \
           i != ln-1 and ne_to_other_args(args[i+1]):
            out_file = args[i+1]
        elif (args[i] == "-m" or args[i] == "--mode") and \
           i != ln-1 and ne_to_other_args(args[i+1]):
           mode = args[i+1]
        elif (args[i] == "-c" or args[i] == "--constraint") and \
           i != ln-1 and ne_to_other_args(args[i+1]):
           constraint = args[i+1]
    if in_file == "":
        err_print("Input file not specified, exitting.")
        exit1()
    if out_file == "":
        err_print("Output file not specified.")
    if mode == "":
        err_print("Optimization not specified.")
    if constraint == "":
        err_print("Type of constraint not specified.")
    return in_file, out_file, mode, constraint

def op_choice(mode, constraint):
    load_mode = True
    load_constraint = True
    if mode == "max" or mode == "min":
        load_mode = False
    if constraint == ">=" or constraint == "<=" or constraint == "=":
        print("")
        load_constraint = False
    while load_mode:
        err_print("Optimization: ? f:")
        mode = input("\'min\' or \'max\': ")
        if mode != "min" and mode != "max":
            err_print("Wrong choice.")
        else:
            load_mode = False
    while load_constraint:
        err_print("Constraints: Ax ? b:")
        constraint = input("\'>=\' or \'<=\' or \'=\': ")
        if constraint != ">=" and constraint != "<=" and constraint != "=":
            err_print("Wrong choice.")
        else:
            load_constraint = False
    return mode, constraint
    
class Constraint():
    def __init__(self, var_coeff, var_id, op_code, val):
        self.var_coeff = var_coeff
        self.var_id = var_id
        self.op_code = op_code
        self.val = val

def handle_constraint(constraint):
    print("AAAAA")

def transform_lp(f_in, f_out, mode, constraint):
    lp = f_in.readlines()
    max_min = ""
    max_min_found = 0
    first_max_min = True

    variables = []
    constraints = []
    for l in lp:
        if max_min_found >= 2:
            break
        # mezery dulezite!!
        if "max " in l:
            max_min_found += 1
            max_min = "max"
            line = l.split() 
            if line[0] != "max":
                first_max_min = False
        if "min " in l:
            max_min_found += 1
            max_min = "min"
            line = l.split() 
            if line[0] != "min":
                first_max_min = False
        
    if not first_max_min:
        err_print("Wrong optimization format (max/min first).")
        exit1()
    if max_min_found != 1:
        err_print("I don't have a clue what you want minimize/maximize.")
        exit1()
    if not constraints_found:
        err_print("You haven't specified any constraints.")
        exit1()

if __name__ == "__main__":
    in_file, out_file, mode, constraint = getent()
    try:
        f_in = open(in_file, "rt")
    except FileNotFoundError:
        err_print("Input file not found, exitting.")
        exit1()
    if out_file == "":
        f_out = None
    else:
        f_out = open(out_file, "wt")
    mode, constraint = op_choice(mode, constraint)
    transform_lp(f_in, f_out, mode, constraint)