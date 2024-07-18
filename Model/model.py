import numpy as np
import pickle


loaded_model = pickle.load(open('diabetes model.sav','rb'))

input = (1,1,1,40,1,0,0,0,0,1,0,1,0,5,18,15,1,0,9)
inp_arr = np.asarray(input)
inp_arr_reshaped  = inp_arr.reshape(1,-1)
prediction = loaded_model.predict(inp_arr_reshaped)
print(prediction)