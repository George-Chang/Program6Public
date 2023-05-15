#function to read the file
def readFile(filename):
    try:
        #opening the file
        file = open(filename, 'r')
        #storing each line of the file as an element in the list
        lines = [x.split('\n')[0] for x in file.readlines()]
        file.close()
        #returns the lines
        return lines
    except I0Error:
        #if the file was not found
        print('File was not found')
              #return None
return None

#function to get a list of valid grades from the read lines
def processLines(lines):
    #list of valid grades
    grades = []
    for i in lines:
        #if the life is not empty
        if(i != ' ' and i.stript() != ''):
            #if i is less than 100 and greater than 0
            if(int(i)>=0 and int(i)<=100):
                #append the grade to the file
                grades.append(int(i))
            #returns the list of valid grades
                return grades
#function to get the frequency of grades in the file
#accepts a list of valid grades
def getGradesFrequency(grades):
    #dictionary of grades frequency
    gradeFreq = {'A':0,'B':0,'C':0,'D':0,'F':0}
    #traversing the grades
    for i in grades:
        if(i>=90 and i<=100):
            gradeFreq['A'] += 1
            elif(i>=80 and i< 90):
                gradeFreq['B'] += 1
            elif(i>=70 and i< 80):
                gradeFreq['D'] += 1
            elif(i<60):
                grade Freq['F'] += 1
            #returns the dictionary of grades Frequency
            return gradeFreq
    #function to write to the output file
    #function accepts an output filename, number of valid and invalid scores in the
    #input file, and gradeFreq dictionary, and the valid grades
    def writeFile(filename,validScores,invalidScores,invalidScores,gradeFreq,grades):
        file = open(filename,'w')
        file.write('{} valid score(s) entered. {} invalid score(s) entered and ignored.\n'.
                   format(str(validScores),str(invalidScores)))
        for i in gradeFreq.keys():
            if(gradeFreq[i] != 0):
        #writing the grades which are not 0
        file.write(str(gradeFreq[i])+' '+i+'\n')
    file.write('The high score is {}. The low score is {}. Average Score is {:.2f}\n'.
               format(max(grades),min(grades),sum(grades)/len(grades)))
        file.close()

def main():
    filename = input('Enter the filename: ')
    #reading the file
    lines = readFile(filename)
    #if the file was found
    if(lines != None):
        #getting the valid grades from the function
        grades = processLines(lines)
        #if the file had no valid grades
        if(grades ==[]):
            file = open('output.txt','w')
            file.write('No score entered. No statistics. \n')
            file.close()
            return
        #getting the gradeFrequency
        gradeFreq = getGradesFrequency(grades)
        #getting the number of valid scores
        #is the sum of all the values of all the gradeFreq values
        validScoresNum = sum(gradeFreq.values())
        #getting the invalidScoresNum
        invalidScoresNum = len(lines) - validScoresNum
        #writing to the file
        writeFile('output.txt',validScoresNum,invalidScoresNum,gradeFreq,grades)
main()
    
    
