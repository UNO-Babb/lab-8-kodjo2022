#ProcessData.py
#Name:
#Date:
#Assignment:

import random

def main():

  #Open the files we will be using
  inFile = open("names.dat", 'r')
  outFile = open("StudentList.csv", 'w')
  # Write CSV header
  outFile.write("LastName,FirstName,StudentID,Major-Year\n")

  #Process each line of the input file and output to the CSV file

  for line in inFile:
    data = line.split()
    first = data[0]
    last = data[1]
    IdNum = data[3]
    year = data[5]
    major = data [6]
    student_id = makeID(first, last, IdNum)
    major_year = makeMajorYear(major, year)
    output = str(last) + "," + str(first) + "," + student_id + "," + major_year + "\n"
    outFile.write(output)

  #Close files in the end to save and ensure they are not damaged.
  inFile.close()
  outFile.close()
def makeID(first, last, idNum):
  idLen = len(idNum)

  while len(last) < 5:
    last = last + "X"
  
  id = first[0] + last + idNum[idLen - 3: ]
  return id
def makeMajorYear(major, year):
  # Abbreviate the major to the first 3 letters
  major_abbrev = major[:3].upper()

  # Determine the year abbreviation using if statements
  if year == "Freshman":
      year_abbrev = "FR"
  elif year == "Sophomore":
      year_abbrev = "SO"
  elif year == "Junior":
      year_abbrev = "JR"
  elif year == "Senior":
      year_abbrev = "SR"
  else:
      year_abbrev = "??"  # For unknown or invalid year values

  return f"{major_abbrev}-{year_abbrev}"


if __name__ == '__main__':
  main()
