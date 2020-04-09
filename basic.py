print("Naive bayes algorithm")
import csv

import matplotlib.pyplot as plt

def getData():
    # Buka File CSV lalu return kan menjadi array
    with open('datasets/iris.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        return list(csv_reader)


# Step 1: Separate By Class.

def separate_by_class(dataset):
	separated = dict()
	for i in range(len(dataset)):
		vector = dataset[i]
		class_value = vector[-1]
		if (class_value not in separated):
			separated[class_value] = list()
		separated[class_value].append(vector)
	return separated


# data = getData()
data = [
    [3.393533211, 2.331273381,0],
    [3.110073483, 1.781539638,0],
    [1.343808831, 3.368360954,0],
    [3.582294042, 4.67917911,0],
    [2.280362439, 2.866990263,0],
    [7.423436942, 4.696522875,1],
    [5.745051997, 3.533989803,1],
    [9.172168622, 2.511101045,1],
    [7.792783481, 3.424088941,1],
    [7.939820817, 0.791637231,1],
    [3.393533211, 2.331273381,0],
    [3.110073483, 1.781539638,0],
    [1.343808831, 3.368360954,0],
    [3.582294042, 4.67917911,0],
    [2.280362439, 2.866990263,0],
    [7.423436942, 4.696522875,1],
    [5.745051997, 3.533989803,1],
    [9.172168622, 2.511101045,1],
    [7.792783481, 3.424088941,1],
    [7.939820817, 0.791637231,1]
]

separated = separate_by_class(data)
for label in separated:
    print(label)
    for row in separated[label]:
        if(label==1):
            plt.plot(row[0],row[1],"bo")
        else:
            plt.plot(row[0],row[1],"ro")
        print(row)

plt.show()

# Step 2: Summarize Dataset.

def mean(numbers):
	return sum(numbers)/float(len(numbers))

from math import sqrt
 
# Calculate the standard deviation of a list of numbers
def stdev(numbers):
	avg = mean(numbers)
	variance = sum([(x-avg)**2 for x in numbers]) / float(len(numbers)-1)
	return sqrt(variance)

# Calculate the mean, stdev and count for each column in a dataset
def summarize_dataset(dataset):
	summaries = [(mean(column), stdev(column), len(column)) for column in zip(*dataset)]
	del(summaries[-1])
	return summaries

summary = summarize_dataset(data)
# print(summary)

# Step 3: Summarize Data By Class.
 

# # Split dataset by class then calculate statistics for each row
# def summarize_by_class(dataset):
# 	separated = separate_by_class(dataset)
# 	summaries = dict()
# 	for class_value, rows in separated.items():
# 		summaries[class_value] = summarize_dataset(rows)
# 	return summaries
 
# # Test summarizing by class
# dataset = [[3.393533211,2.331273381,0],
# 	[3.110073483,1.781539638,0],
# 	[1.343808831,3.368360954,0],
# 	[3.582294042,4.67917911,0],
# 	[2.280362439,2.866990263,0],
# 	[7.423436942,4.696522875,1],
# 	[5.745051997,3.533989803,1],
# 	[9.172168622,2.511101045,1],
# 	[7.792783481,3.424088941,1],
# 	[7.939820817,0.791637231,1]]
# summary = summarize_by_class(dataset)
# for label in summary:
# 	print(label)
# 	for row in summary[label]:
# 		print(row)


# # Step 4: Gaussian Probability Density Function.

# # Example of Gaussian PDF
# from math import sqrt
# from math import pi
# from math import exp
 
# # Calculate the Gaussian probability distribution function for x
# def calculate_probability(x, mean, stdev):
# 	exponent = exp(-((x-mean)**2 / (2 * stdev**2 )))
# 	return (1 / (sqrt(2 * pi) * stdev)) * exponent
 
# # Test Gaussian PDF
# print(calculate_probability(1.0, 1.0, 1.0))
# print(calculate_probability(2.0, 1.0, 1.0))
# print(calculate_probability(0.0, 1.0, 1.0))


# # Step 5: Class Probabilities.

# # Example of calculating class probabilities
# from math import sqrt
# from math import pi
# from math import exp

 
# # Calculate the probabilities of predicting each class for a given row
# def calculate_class_probabilities(summaries, row):
# 	total_rows = sum([summaries[label][0][2] for label in summaries])
# 	probabilities = dict()
# 	for class_value, class_summaries in summaries.items():
# 		probabilities[class_value] = summaries[class_value][0][2]/float(total_rows)
# 		for i in range(len(class_summaries)):
# 			mean, stdev, _ = class_summaries[i]
# 			probabilities[class_value] *= calculate_probability(row[i], mean, stdev)
# 	return probabilities
 
# # Test calculating class probabilities
# dataset = [[3.393533211,2.331273381,0],
# 	[3.110073483,1.781539638,0],
# 	[1.343808831,3.368360954,0],
# 	[3.582294042,4.67917911,0],
# 	[2.280362439,2.866990263,0],
# 	[7.423436942,4.696522875,1],
# 	[5.745051997,3.533989803,1],
# 	[9.172168622,2.511101045,1],
# 	[7.792783481,3.424088941,1],
# 	[7.939820817,0.791637231,1]]
# summaries = summarize_by_class(dataset)
# probabilities = calculate_class_probabilities(summaries, dataset[0])
# print(probabilities)