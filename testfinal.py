import subprocess
import time
import difflib
import datetime
import socket
import uuid
import hashlib


def testingwin():
    with open('actualresults.txt', 'w') as f:
        f.write("Winning Test\n")
        p = subprocess.Popen(['python', 'final.py'], stdin=subprocess.PIPE, stdout=f)
        try:
            p.stdin.write(b'Kos\n')
            p.stdin.flush()
            p.stdin.write(b'Kay\n')
            p.stdin.flush()
            p.stdin.write(b'5\n')
            p.stdin.flush()
            p.stdin.write(b'5\n')
            p.stdin.flush()
            p.stdin.write(b'1\n')
            p.stdin.flush()
            p.stdin.write(b'2\n')
            p.stdin.flush()
            p.stdin.write(b'4\n')
            p.stdin.flush()
            p.stdin.write(b'7\n')
            p.stdin.flush()
            p.stdin.write(b'8\n')
            p.stdin.flush()
            p.stdin.write(b'3\n')
            p.stdin.flush()
        except Exception as e:
            f.write (e)
    f.close()

def testingnowin():
    with open('actualresults.txt', 'a') as f:
        f.write("Not Winning Test")
        p = subprocess.Popen(['python', 'final.py'], stdin=subprocess.PIPE, stdout=f)
        try:
            p.stdin.write(b'Kos\n')
            p.stdin.flush()
            p.stdin.write(b'Kay\n')
            p.stdin.flush()
            p.stdin.write(b'5\n')
            p.stdin.flush()
            p.stdin.write(b'1\n')
            p.stdin.flush()
            p.stdin.write(b'4\n')
            p.stdin.flush()
            p.stdin.write(b'6\n')
            p.stdin.flush()
            p.stdin.write(b'A\n')
            p.stdin.flush()
            p.stdin.write(b'7\n')
            p.stdin.flush()
            p.stdin.write(b'3\n')
            p.stdin.flush()
            p.stdin.write(b'9\n')
            p.stdin.flush()
            p.stdin.write(b'8\n')
            p.stdin.flush()
            p.stdin.write(b'2\n')
            p.stdin.flush()
        except Exception as e:
            f.write (e)
    f.close()

def calculatemscore():
    file1 = open('actualresults.txt', 'r').readlines()
    file2 = open('expected_results.txt', 'r').readlines()

    # Calculate the differences between the two files
    d = difflib.Differ()
    diff = list(d.compare(file1, file2))

    # Count the number of different lines
    diff_count = sum([1 for line in diff if line.startswith('+') or line.startswith('-')])

    # Calculate the percentage difference
    percentage_diff = (diff_count / float(len(file1))) * 100

    return percentage_diff

def calculatepoints():
    diff = calculatemscore()
    score = 0
    if (diff == 0):
        score = 15
    elif(0 < diff < 5):
        score = 13 
    elif(5 < diff < 10):
        score = 11
    elif(10 < diff < 15):
        score = 9
    elif(15 < diff < 20):
        score = 7
    elif(20 < diff < 25):
        score = 5
    elif(25 < diff < 30):
        score = 4
    elif(30 < diff < 40):
        score = 3
    elif(40 < diff < 50):
        score = 2
    elif(50 < diff < 80):
        score = 1 
    else: 
        score = 0
    return score 

def getactualresulthash():
    filename = 'actualresults.txt'
    hash_md5 = hashlib.md5()
    hash_sha = hashlib.sha256()

    with open(filename, 'rb') as f:
        for chunk in iter(lambda: f.read(4096), b''):
            hash_md5.update(chunk)
            hash_sha.update(chunk)
    return (hash_sha.hexdigest())

def markmytest():
    testingwin()
    time.sleep(10)
    testingnowin()

    studentnumber = input("Enter your student number: ")
    firstname = input("Enter your first name: ")
    lastname = input("Enter your lastname: ")
    email = input("Enter your email: ")

    academicintegrity = input("I hereby authorize I fully understand the Seneca Academic Integrity Policies and the work I submit here is completly my own (Y/N)")

    if (str(academicintegrity).lower() != 'y'):
        print ("Please review Seneca Academic Integrity Policies. You can only submit your own work for this final exam")
        return

    today = datetime.datetime.now()
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)

    actualresultfilehash = getactualresulthash()

    percentage = calculatemscore()

    points = calculatepoints()

    with open('finalsubmission.txt', 'w') as f: 
        f.write("**************************************\n")
        f.write("Student Number: %s\n" %studentnumber)
        f.write("First Name: %s\n" %firstname)
        f.write("Last Name: %s\n" %lastname)
        f.write("Email: %s\n" %email)
        f.write("Academic integrity confirmation: Y\n")
        f.write("Time: %s\n" %today)
        f.write("I understand, that I still have to meet the blackbord submission timeline to get credit for my work\n")
        f.write("Computer Name: %s\n" %hostname)
        f.write("IP Address: %s\n" %ip_address)
        f.write("Result File Hash: %s\n" %actualresultfilehash)
        f.write("**************************************\n")
        f.write("\n")
        f.write("\n")
        f.write("**************************************\n")
        f.write("**************************************\n")
        f.write("Percentage Difference %s\n" %percentage)
        f.write("**************************************\n")
        f.write("**************************************\n")
        f.write("\n")
        f.write("\n")
        f.write("**************************************\n")
        f.write("**************************************\n")
        f.write("Points Earned: %s\n" %points)
        f.write("**************************************\n")
        f.write("**************************************\n")
    
    print ("Please check the finalsubmission.txt file")
    print ("If you are happy with the points you have made submit the files below for Part 2 submission")
    print ("Completed final_<studentnumber>.py")
    print ("finalsubmission_<studentnumber>.txt")
    print ("actualresults_<studentnumber>.txt")
    print ("flowchart_<studentnumber>.pdf")
    print ("If the above key files are not submitted there you will loose points from your overall grade")

if __name__ == "__main__":
    markmytest()