# Scripts

## Purpose
	* Take student submitted code and automate the grading 
	* It compiles the code extracts the input for the files from .txt files and runs the code with the input
	* input is of the form ```./grading <folder of students code> <folder of input files> <compiler options>
	* Compilor options are 1: g++ 2: visual studio
## Example output
```
GRADING SCRIPT


|--------------------------------------------------------------------------------------|

FILENAME = cpp//test1.cpp

COMPILATION OUTPUT ----------------------------

COMPILATION SUCCESSFUL FOR test1.cpp

Line Length Exceeded: 117

STANDARD OUTPUT: -----------------

Test file 20000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
argc = 6
1
2
3
4
5

STANDARD ERROR: ------------------


Recorded Score: ------------------
Compilation without errors: yes
Program ran without errors: yes
Program output correct: yes
|--------------------------------------------------------------------------------------|


|--------------------------------------------------------------------------------------|

FILENAME = cpp//test.cpp

COMPILATION OUTPUT ----------------------------

COMPILATION FAILED FOR test.cpp

Did not exceed line limit.

STANDARD OUTPUT: -----------------


STANDARD ERROR: ------------------

/bin/sh: 1: ./a.out: not found

Recorded Score: ------------------
Compilation without errors: yes
Program ran without errors: yes
Program output correct: yes
|--------------------------------------------------------------------------------------|


||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

Scores and comments:

||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||



|--------------------------------------------------------------------------------------|
        Filename: test1.cpp
|--------------------------------------------------------------------------------------|
                Compilation without errors: yes
                Program ran without errors: yes
                Program output correct: yes
                80 character limit information: Longest Line Length: 117



|--------------------------------------------------------------------------------------|
        Filename: test.cpp
|--------------------------------------------------------------------------------------|
                Compilation without errors: yes
                Program ran without errors: yes
                Program output correct: yes
                80 character limit information: Did not exceed line limit.



Press Enter to exit...
```

