#Central Tendency Analysis
import pandas as pd #library for data sets - allow for use of functions such as .readcsv()

database = pd.read_csv("dataset.csv") #accesses csv file

#re-usable function that finds mean, median & mode
def calculations(variable):
    mean = database[variable].mean() #calculates mean
    median = database[variable].median() #calculates median
    mode = database[variable].mode() #calculates mode
    return f"Variable:{variable}\nMean:{mean}\nMedian:{median}\nMode:{mode}\n" #returns all values

print(calculations("traffic_flow")) #passes string/column "traffic_flow" through function calculations, variable = "traffic_flow"
print(calculations("pm25")) #passes string/column "pm25" through function calculations, variable = "pm25"