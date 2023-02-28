import numpy as np

def calculate(list):
   
    if len(list) < 9:
        raise ValueError("List must contain nine numbers.")
       
    nparray = np.array(list).reshape(3,3)

    calculations = {'mean': [(np.mean(nparray, axis = 0)).tolist(), (np.mean(nparray, axis = 1)).tolist(), np.mean(nparray)],
                'variance': [(np.var(nparray, axis = 0)).tolist(), (np.var(nparray, axis = 1)).tolist(), np.var(nparray)],
                'standard deviation': [(np.std(nparray, axis = 0)).tolist(), (np.std(nparray, axis = 1)).tolist(), np.std(nparray)],
                'max': [(np.max(nparray, axis = 0)).tolist(), (np.max(nparray, axis = 1)).tolist(), np.max(nparray)],
                'min': [(np.min(nparray, axis = 0)).tolist(), (np.min(nparray, axis = 1)).tolist(), np.min(nparray)],
                'sum': [(np.sum(nparray, axis = 0)).tolist(), (np.sum(nparray, axis = 1)).tolist(), np.sum(nparray)],
    }      

    return calculations

# Test Case
list = [0,1,2,3,4,5,6,7,8]

calculations = calculate(list)

print(calculations)

# Expected Output
#{'mean': [[3.0, 4.0, 5.0], [1.0, 4.0, 7.0], 4.0],
# 'variance': [[6.0, 6.0, 6.0], [0.6666666666666666, 0.6666666666666666, 0.6666666666666666], 6.666666666666667],
# 'standard deviation': [[2.449489742783178, 2.449489742783178, 2.449489742783178], [0.816496580927726, 0.816496580927726, 0.816496580927726], 2.581988897471611],
# 'max': [[6, 7, 8], [2, 5, 8], 8],
# 'min': [[0, 1, 2], [0, 3, 6], 0],
# 'sum': [[9, 12, 15], [3, 12, 21], 36]}