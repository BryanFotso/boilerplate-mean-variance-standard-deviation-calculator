import numpy as np

def calculate(list):
    if len(list) == 9:
        list_array = np.array(list).reshape(3,3)
        calculations = {
                    'mean' : [list_array.mean(axis = 0).tolist(),list_array.mean(axis = 1).tolist(),list_array.mean().tolist()],
                    'variance':[list_array.var(axis = 0).tolist(),list_array.var(axis = 1).tolist(),list_array.var().tolist()],
                    'standard deviation': [list_array.std(axis = 0).tolist(),list_array.std(axis = 1).tolist(),list_array.std().tolist()], 
                    'max':[list_array.max(axis = 0).tolist(),list_array.max(axis = 1).tolist(),list_array.max().tolist()],
                    'min':[list_array.min(axis = 0).tolist(),list_array.min(axis = 1).tolist(),list_array.min().tolist()],
                    'sum':[list_array.sum(axis = 0).tolist(),list_array.sum(axis = 1).tolist(),list_array.sum().tolist()]
                        }
        
    else:
        raise ValueError('List must contain nine numbers.')
    
    return calculations