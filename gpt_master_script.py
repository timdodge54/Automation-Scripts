import os
import subprocess

comp_scores = {}
correct_scores = {}
input_files = []
run_scores = {}
exceeded_limit = {}

# Get file paths.
student_path = input("Please enter the path (likely starting with C:/) of the student files: ")
input_path = input("Please enter the path of the input files (in the form Input***.txt): ")
compiler_type = input("Please indicate the compiler you would like to use (1 = CygWin and gcc, 2 = VisualStudio and cl)")

# Get the list of input files.
os.chdir(input_path)
if os.getcwd() != input_path:
    print("Path for input files is invalid.")
    exit()

for file in os.listdir():
    if file.startswith("Input") and file.endswith(".txt"):
        input_files.append(file)

# Go to the student files directory for the rest of the script.
os.chdir(student_path)
if os.getcwd() != student_path:
    print("Student files path is invalid.")
    exit()

# Get rid of spaces in the names of files.
for file in os.listdir():
    if file.endswith(".c"):
        os.rename(file, file.replace(" ", "_"))

# Loop through the student files.
for file in os.listdir():
    if file.endswith(".c"):
        # Compile the student file.
        if compiler_type == "1":
            subprocess.run(["gcc", file])
            name = "a.exe"
        elif compiler_type == "2":
            subprocess.run(["cl", file])
            name = f"{file[:-2]}.exe"
        else:
            print("You entered an invalid compiler type.")
            break

        # Print the filename for student's name reference.
        print(" ")
        print(file)
        wc_results = subprocess.run(["wc", "-L", file], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        line_length = int(wc_results.stdout.split()[0])
        if line_length > 80:
            exceeded_limit[file[:-2]] = f"Longest line length: {line_length}"
        else:
            exceeded_limit[file[:-2]] = "Didn't exceed character limit"

        # Run the student's program with each of the input files.
        for input_file in input_files:
            with open(f"{input_path}/{input_file}", "r") as input_data:
                subprocess.run(["timeout", "2", "./"+name], stdin=input_data, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                print(" ")
                with open("output.txt", "r") as output_data:
                    print(output_data.read())
                print(" ")

        # Get and store the scores for this student's program.
        print("Scores and comments:")

