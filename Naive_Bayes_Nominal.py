import pandas as pd
import numpy as np

#read data from csv file from each attribute into a list of the same name
df = pd.read_csv("path_to_data.csv")
feature1 = df['feature1'].tolist()
feature2 = df['feature2'].tolist()
feature3 = df['feature3'].tolist()
feature4 = df['feature4'].tolist()
labels = df['labels'].tolist()
#calculate the num of yes and no in the labels and calculate their probabilities
num_yes = labels.count(1)
num_no = labels.count(0)
probability_yes = num_yes / len(labels)
probability_no = num_no / len(labels)
#get user data for testing
print("Enter the test data : ")
f1 = int(input("Enter the value of feature 1 : "))
f2 = int(input("Enter the value of feature 2 : "))
f3 = int(input("Enter the value of feature 3 : "))
f4 = int(input("Enter the value of feature 4 : "))
#to calculate probability of x given yes
f1_yes = 0
f2_yes = 0
f3_yes = 0
f4_yes = 0
for i in range(0, len(label)):
  if feature1[i] == f1 and label[i] == 1:
    f1_yes += 1
  if feature2[i] == f2 and label[i] == 1:
    f2_yes += 1
  if feature3[i] == f3 and label[i] == 1:
    f3_yes += 1
  if feature4[i] == f4 and label[i] == 1:
    f4_yes += 1
p_x_yes = (f1_yes * f2_yes * f3_yes * f4_yes) / ((num_yes)**4)
#to calculate probability of x given no
f1_no = 0
f2_no = 0
f3_no = 0
f4_no = 0
for i in range(0, len(label)):
  if feature1[i] == f1 and label[i] == 0:
    f1_no += 1
  if feature2[i] == f2 and label[i] == 0:
    f2_no += 1
  if feature3[i] == f3 and label[i] == 0:
    f3_no += 1
  if feature4[i] == f4 and label[i] == 0:
    f4_no += 1
p_x_no = (f1_no * f2_no * f3_no * f4_no) / ((num_no)**4)
#to calculate probability of yes given x and no given x
p_yes_x = p_x_yes * probability_yes
p_no_x = p_x_no * probability_no
#predict the label
if p_yes_x > p_no_x:
  print("Yes")
else:
  print("No")
