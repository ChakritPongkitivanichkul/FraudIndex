import pickle
from sys import argv

# with open('dict_data/RK_layer1.pkl', 'rb') as f:
#     loaded_dict = pickle.load(f)

with open(argv[1], 'rb') as f:
    loaded_dict = pickle.load(f)

print(loaded_dict)
print(len(loaded_dict))