import streamlit as st
import joblib

st.set_page_config(page_title="Multi Model Prediction System", page_icon="🤖", layout="centered")
st.title("🤖 Multi Model Prediction System")
option=st.sidebar.selectbox("Select Prediction Model",["Heart Disease Prediction","Ford Car Price Prediction"])
if option=="Heart Disease Prediction":
    model=joblib.load("heart_model.pkl")
    scaler=joblib.load("heart_scaler.pkl")
    st.header("❤️ Heart Disease Prediction")
    age=st.number_input("Age",1,100,40)
    sex=1 if st.selectbox("Sex",["M","F"])=="M" else 0
    chest={"ATA":0,"NAP":1,"ASY":2,"TA":3}[st.selectbox("Chest Pain Type",["ATA","NAP","ASY","TA"])]
    bp=st.number_input("Resting Blood Pressure",80,250,120)
    chol=st.number_input("Cholesterol",0,700,200)
    fasting=st.selectbox("Fasting Blood Sugar",[0,1])
    ecg={"Normal":0,"ST":1,"LVH":2}[st.selectbox("Resting ECG",["Normal","ST","LVH"])]
    hr=st.number_input("Maximum Heart Rate",60,220,150)
    angina=1 if st.selectbox("Exercise Angina",["N","Y"])=="Y" else 0
    oldpeak=st.number_input("Old Peak",0.0,10.0,0.0)
    slope={"Down":0,"Flat":1,"Up":2}[st.selectbox("ST Slope",["Up","Flat","Down"])]
    if st.button("Predict Heart Disease"):
        p=model.predict(scaler.transform([[age,sex,chest,bp,chol,fasting,ecg,hr,angina,oldpeak,slope]]))
        st.success("Heart Disease Detected" if p[0]==1 else "No Heart Disease")
else:
    model=joblib.load("ford_model.pkl")
    scaler=joblib.load("ford_scaler.pkl")
    st.header("🚗 Ford Car Price Prediction")
    year=st.number_input("Year",2000,2025,2018)
    mileage=st.number_input("Mileage",0,300000,50000)
    tax=st.number_input("Tax",0,500,150)
    mpg=st.number_input("MPG",0.0,100.0,50.0)
    engine=st.number_input("Engine Size",0.8,6.0,1.5)
    if st.button("Predict Car Price"):
        p=model.predict(scaler.transform([[year,mileage,tax,mpg,engine]]))
        st.success(f"Predicted Price: £{p[0]:,.2f}")
