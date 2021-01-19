# Assessment fo reading files in python
# Download the weather data
import urllib.request
url = " https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%204/ex4.csv"
filename = "Weather_data.txt"
urllib.request.urlretrieve(url, filename)

# make a function that calculate the moving avaerage precipitation in June
# make a plot of the moving average over number of days
import matplotlib.pyplot as plt

statData = "Weather_data.txt"

def getNAvg(file, N):
    with open (file, 'r') as rawdata:
        File = rawdata.read()
        sep_lines = File.split('\n')
        formattedText = []
        for i in sep_lines:
            formattedText.append(i.split(',')[1])
        formattedText.remove('ONE_DAY_PRECIPITATION')
        Precipitations = [float(Prep) for Prep in formattedText]
        File = Precipitations
        print(File)
        print(len(File))
    m = len(File)
    k = N
    n = Precipitations
    s = 0
    M = [None] * m
    for day in range(k):
        s = s + Precipitations[day]
    M[k-1] = s / k
    print(M[k-1])
    for i in range(k, m):
        prec_sub = (n[i] - n[i-k])/k
        M[i] = M[i-1] + prec_sub
    M = [M[x] for x in range(k-1,m)]
    return(M)    


       
getNAvg(statData, 6)  

## Review Questions 
# What do the following lines of code do?

with open("Example1.txt","r") as file1:
    FileContent=file1.readlines()
    print(FileContent)
    
