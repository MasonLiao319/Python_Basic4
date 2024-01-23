#Program 1 – The A-Team
#Description: Design and write a program that reads the text from a provided text file into a list, displays the 
# text on-screen, makes some alterations to the text and outputs the changed text to the screen, then saves the 
# altered text as a new file. 

#Student #:    W0424837 
#Student Name:  Mason Liao


# YOUR CODE STARTS HERE, each line must be indented (one tab)

import random

# Function to print a line of a given character and length
def printALine(p_char,p_length):
    print(p_char * p_length)


# Function to pick a random number within a specified range
def pickARandomNum(p_lowerBound,p_upperBound):
    theNumber = random.randint(p_lowerBound, p_upperBound)
    return theNumber


# Function to read data from a file into a list of lines
def readDataFromFilesToLines(p_fileName):
    """Read data from the specified file path, into a list"""
    fileLines = []
    myFile = open(p_fileName, "r")
    for line in myFile:
        content = line.replace("\n", "")
        fileLines.append(content)       
    return fileLines


# Function to alter lines based on specified conditions and write to a new file
def alterLinesAndWrite(p_lines, p_outputFileName):
    """Process lines based on specified conditions and print the result"""
    # Pick a random line to omit
    randomLineIndex = pickARandomNum(1,len(p_lines))

    lineNumber = 1
    #Try these code except File Not Found Error
    try:
        with open(p_outputFileName, "w") as omittedFile:
            # Convert to lowercase if longer than 20 characters, else to uppercase 
            for line in p_lines:
                charLimit = 20
                if len(line) > charLimit:
                        alteredLine = line.lower()
                elif len(line) < charLimit:
                        alteredLine = line.upper()

                if lineNumber == randomLineIndex:
                # Write the omitted line to the new file
                    omittedFile.write("{0}: {1}\n".format(lineNumber,alteredLine))
                    print("")
                    lineNumber += 1
                    continue  
                

                # Print the line number and altered line
                print("{0}: {1}".format(lineNumber,alteredLine))
                lineNumber += 1
    except FileNotFoundError:
        print("File not found!")  


def main():
   
    printALine("-",70)
    print("Original Text")
    printALine("-",70)

    # Read and print original text from the file
    lines = readDataFromFilesToLines("ateam_Original.txt")
    for line in lines:
        content = line.replace("\n", "")
        print(content)

    printALine("-",70)
    print("Altered Text")
    printALine("-",70)

    # Alter lines and write omitted line to a new file
    alterLinesAndWrite(readDataFromFilesToLines("ateam_Original.txt"), "Omitted_lines.txt")
    


    # YOUR CODE ENDS HERE

main()