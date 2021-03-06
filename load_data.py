import csv 
import numpy as np


# return a np.array of the data, and a list of the attribute names
def load_data(cvsfilename, csv_delimiter=','): 
    # import data, include encoding to ommit BOM  
    data = []
    with open(cvsfilename, 'r', encoding='utf-8-sig') as csvfile:
        reader = csv.reader(csvfile, delimiter=csv_delimiter)
        for row in reader:
            if len(row) != 0: # skip empty lines
                data.append(row)
            
    # drop the attribute row from the list
    attributes = data.pop(0)
    data = np.array(data).astype(float)

    return (data, attributes)



# return a np.array of the data, and a list of the attribute names
def load_data_category_string(cvsfilename, attr_type, csv_delimiter=',', dropID=False, nameToPrefix=False): 
    # import data, include encoding to ommit BOM  
    data = []
    with open(cvsfilename, 'r', encoding='utf-8-sig') as csvfile:
        reader = csv.reader(csvfile, delimiter=csv_delimiter)
        for row in reader:
            if len(row) != 0: # skip empty lines
                if dropID:
                    row = row[1:]
                if nameToPrefix:
                    row[2] = row[2].split()[0]
                data.append(row)
        
    # drop the attribute row from the list
    attributes = data.pop(0)
    data = np.array(data)
    for col in range(len(data.T)):
        if attr_type[col] == "categorical" or attr_type[col] == "class":
            possible_category = list(set(data.T[col]))
            # if col == 2:
            #     print(possible_category)
            encode_dict = { possible_category[i] : i for i in range(len(possible_category)) }
            # encode the data
            for row in range(len(data)):
                data[row][col] = encode_dict[data[row][col]]
        else:
            for row in range(len(data)):
                data[row][col] = data[row][col]
    data = data.astype(float)
    return (data, attributes)




# if the attribute is categorical, return a list of all possible options
# if the attribute is numerical, return a list mid-point
def get_possible_options(data, attr_type):
    options = []
    for i in range(len(attr_type)):
        opt = []
        if attr_type[i] == "numerical":
            # opt = [0, 1] # 0: <=, 1: >
            val = list(sorted(set(data.T[i])))
            opt = [float(val[i]) + float(val[i+1])/2 for i in range(len(val)-1)]
        else: # if the attribute is categorical or a class
            opt = list(set(data.T[i]))
        options.append(opt)
    return options


# return a dictionary of the attribute names and their types
# be careful when access with index, like dict.key()[index]
# since a python dict is not ordered
# for wang san's nn input
def build_attribute_dict(attributes, attribute_type):
    attribute_dict = {}
    for i in range(len(attributes)):
        attribute_dict[attributes[i]] = attribute_type[i]
    return attribute_dict
