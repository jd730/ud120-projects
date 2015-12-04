#!/usr/bin/python

""" 
    starter code for exploring the Enron dataset (emails + finances) 
    loads up the dataset (pickled dict of dicts)

    the dataset has the form
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person
    you should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""
import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))
c = 0
d = 0
maxi = -1
mini = 1000000000
import math
print len(enron_data)
for each in enron_data :
	c = enron_data[each]["salary"]
	if "TOTAL" in each :
		continue
	if  c!= 'NaN' :
		if maxi < c :
			maxi = c
		elif mini > c :
			mini = c
print maxi, mini
#print enron_data["SKILLING JEFFREY K"]
#print enron_data["LAY KENNETH L"]
