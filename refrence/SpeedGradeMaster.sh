#!/bin/bash
declare -A comp_scores
declare -A correct_scores
declare -a input_files
declare -A run_scores
declare -A exceeded_limit

# This script is designed to aid in the manual grading of student c programs.
# Author: Amanda Strate, April 2020

# Get file paths.
echo "Please enter the path (likely starting with C:/) of the student files: "
read student_path
echo "Please enter the path of the input files (in the form Input***.txt): "
read input_path
echo "Please indicate the compiler you would like to use (1 = CygWin and gcc, \
2 = VisualStudio and cl)"
read compiler_type

# Get the list of input files.
cd $input_path
if [ $? -ne 0 ]
then
	echo "Path for input files is invalid."
	exit
fi

for f in Input*.txt; do
    input_files[${#input_files[@]}+1]=$(echo "$f");
done

# Go to the student files directory for the rest of the script.
cd $student_path
if [ $? -ne 0 ]
then
	echo "Student files path is invalid."
	exit
fi

# Get rid of spaces in the names of files.
for f in *.c; do
	mv "$f" "${f// /_}"
done
	
# Loop through the student files.
for f in *.c; do
    # Compile the student file.
	if [ "$compiler_type" = "1" ]
	then
		gcc "$f"
		name="a.exe"
	elif [ "$compiler_type" = "2" ]
	then
		cl "$f"
		name="${f:0:-2}.exe"
	else
		echo "You entered an invalid compiler type."
		break
	fi
		
	# Print the filename for student's name reference.
    echo " "
    echo "$f"
	wc_results=$(wc -L "$f")
	line_length=$(echo $wc_results|cut -d' ' -f1)
	if [ "$line_length" -gt 80 ]
	then
		exceeded_limit[${f:0:-2}]="Longest line length: $line_length"
	else
		exceeded_limit[${f:0:-2}]="Didn't exceed character limit"
	fi
	
	# Run the student's program with each of the input files.
	for input in "${input_files[@]}"; do
		# Note that sending the output of the program to a file allows you to
		# see the prompts from their program. You will not see the input values,
		# but doing this and then cat output.txt will allow you to at least see
		# everything their program outputs.
		# 
		# Note also that timeout 2 gives the program 2 seconds to execute and
		# then interrupts it to prevent getting held up on infinite loop 
		# programs.
        eval "timeout 2 ./${name} < ${input_path}/${input} > output.txt"
		echo " "
		cat output.txt
		echo " "
	done
	
	# Get and store the scores for this student's program.
	echo "Scores and comments:"
    echo "compilation without errors:"
    read x
    comp_scores[${f:0:-2}]=$x
	echo "running without errors:"
    read x
    run_scores[${f:0:-2}]=$x
    echo "operation: "
    read x
    correct_scores[${f:0:-2}]=$x
	
	# Remove any executables so that a program that doesn't compile
	# doesn't use the previous student's compiled program.
    rm *.exe
done

# Output the recorded scores
echo " "
echo "SCORES:"
echo "  filename"
echo "    compile"
echo "    run"
echo "    operation"
echo "    80 character limit information"
echo " "
for f in *.c; do
    echo "${f:0:-2}"
    echo "${comp_scores[${f:0:-2}]}"
    echo "${run_scores[${f:0:-2}]}"
    echo "${correct_scores[${f:0:-2}]}"
    echo "${exceeded_limit[${f:0:-2}]}"
	echo " "
done
echo " "

# This is simply here so the program doesn't exit automatically.
echo "Hit <Enter> to exit."
read x