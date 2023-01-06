import pandas as pd
import numpy as np
import csv
# import csv

# data = pd.read_csv('CWE758.csv') 

# # one line split 
# train, validation, test = np.split(data.sample(frac=1), [int(.6*len(data)),
# int(.8*len(data))])

# print(len(train))
# print(len(validation))
# print(len(test))

# train.to_csv('train.csv')
# validation.to_csv('val.csv')
# test.to_csv('test.csv')

# from tokenizer import Tokenizer
# tokenizer = Tokenizer(c_str='''
#               for (int i=0; i<200; i++){
#                 cout<<i;
#               }''')
# print(tokenizer.full_tokenize())
# print(tokenizer.full_tokenize_compressed())
if __name__ == '__main__':
  path_file = 'something.txt'
  path_result = 'related_func.csv'
  f = open(path_file, "r")
  func_name = f.read().split(",")
  f = open(path_result, 'w')
  writer = csv.writer(f)
  writer.writerow(["function", "label"])
  for func in func_name:
    writer.writerow([func, "1"])