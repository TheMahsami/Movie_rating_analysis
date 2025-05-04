#we want to try numpy so:
import numpy as np
from numpy import genfromtxt
import pandas as pd


Datasetfile = 'movie_ratings.csv'
Dataset = np.genfromtxt(Datasetfile , delimiter=',' , dtype=str , skip_header=1)


#task no.1.1
#extract just ratings for statistic
numeric_datas = np.genfromtxt(Datasetfile , delimiter=',' , skip_header=1 , usecols=2)
def Get_Mean():
    return np.mean(numeric_datas)

def Get_Median():
   return np.median(numeric_datas)

def Get_Standard_Deviation():
    return np.std(numeric_datas)

def Get_calc():
   print(f"mean: {Get_Mean()}")
   print(f"median: {Get_Median()}")
   print(f"standard deviation: {Get_Standard_Deviation()}")
   
Get_calc()

#task no1.2
# the function prints name of any movie that rated more than 5
def Filter_Based_Rate():
    for index in Dataset:
        if float(index[2]) >= 5:
            print(index[0])
            
Filter_Based_Rate()

#the function print a list of action movies
def Filter_Based_Genere():
    for index in Dataset:
        if index[1] == 'Action':
            print(index[0])
            
print("lists of 'Action' movies")        
Filter_Based_Genere()

#task no.2.1

Dataframe = pd.read_csv(Datasetfile)
# print(Dataframe)
#checking for missing data
MissedCheck = Dataframe.isnull()
# NotMissed = Dataframe.notnull()
print(MissedCheck)

def Filtred_DataFrame_Based_Rate():
    print(Dataframe[Dataframe['CriticRating'] > 5])

Filtred_DataFrame_Based_Rate()