import numpy as np
import pickle 
import streamlit as st 

loaded_model = pickle.load(open('diabetes model.sav','rb'))

def diabetes_prediction(input):
    input = (1,1,1,40,1,0,0,0,0,1,0,1,0,5,18,15,1,0,9)
    inp_arr = np.asarray(input)
    inp_arr_reshaped  = inp_arr.reshape(1,-1)
    prediction = loaded_model.predict(inp_arr_reshaped)
    print(prediction)
    if (prediction[0]== 0):
        return "The person is not diabetes"
    else :
        return "The person is diabetic"
    
def main():
    st.title("Diabetes prediction")

    HighBp  = st.text_input("Enter 1 if you have High BP")
    HighCholestrol = st.text_input("Enter 1 if you have High Cholestrol")
    CholCheck = st.text_input("Enter 1 if you check cholestrol regularly")
    BMI = st.text_input("Enter your BMI")
    Smoker = st.text_input("Enter 1 if you are a Smoker")
    Stroke = st.text_input("Enter 1 if you have previously encountered Stroke")
    HeartDiseaseorAttack = st.text_input("Enter 1 if you have Heart disorder")
    PhysActivity = st.text_input("Enter 1 if you have physical activity")
    Fruits = st.text_input("Enter 1 if you eat fruits")
    Veggies = st.text_input("Enter 1 if you eat vegtables")
    HvyAlcoholConsump = st.text_input("Enter 1 if consume alchohol heavily")
    NoDocbcCost = st.text_input("Enter 1 if you have not visited doctor in the past year")
    GenHlth = st.text_input("how would you rate your health on the scale of 1-5")
    MentHlth = st.text_input("enter the days of poor mental health")
    PhysHlth = st.text_input("enter the days of poor physical health")
    DiffWalk = st.text_input("Enter 1 if you have difficulty walking ")
    Sex = st.text_input("Enter your gender")
    Age = st.text_input("Enter your age")


    diagnostics = " "

    if st.button("Test Result"):
        diagnostics = diabetes_prediction(['HighBp','HighCholestrol','CholCheck','BMI','Smoker','HeartDiseaseorAttack','PhysActivity','Fruits','Veggies','HvyAlcoholConsump','NoDocbcCost','GenHlth','MentHlth','PhysHlth','DiffWalk','Sex','Age'])

    st.success(diagnostics)

if __name__ == '__main__':
    main()