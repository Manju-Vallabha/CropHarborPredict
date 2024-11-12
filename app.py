import joblib
import pandas as pd
import json
import streamlit as st
from streamlit_lottie import st_lottie

# Load the model from the file
loaded_model = joblib.load('model.joblib')
st.set_page_config(layout='wide')

# Animation files load function
def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)

# Load the animation file
logo = load_lottiefile("Animation - 1709974787811.json")
predicted_crop = ''
title = st.container()
logo1 = st.container()
description1 = st.container()
# Add description about the model in the sidebar
st.sidebar.title("CropHarbor")
st.sidebar.markdown("This is a crop suitability prediction model. Enter the required input features and click the 'Predict' button to get the predicted crop.")

# Assuming you have the same feature names used during training
# Take user input for features
#st.sidebar.title("Crop Suitability Prediction")
ph = st.sidebar.number_input("Enter pH value:")
max_temperature_avg = st.sidebar.number_input("Enter max temperature average:")
humidity_avg = st.sidebar.number_input("Enter humidity average:")
precip_avg = st.sidebar.number_input("Enter precipitation average:")
area_slope = st.sidebar.number_input("Enter area slope:")
soil_type_mapping = {'sandy soil': 0, 'loamy soil': 1, 'clay soil': 2, 'loamy Soil': 3, 'clay Soil': 4}
soil_type = st.sidebar.selectbox("Select soil type:", list(soil_type_mapping.keys()))
soil_type_encoded = soil_type_mapping[soil_type]
drainage = st.sidebar.selectbox("Select drainage encoded:", ['Yes', 'No'])
drainage_mapping = {'Yes': 1, 'No': 0}
drainage_encoded = drainage_mapping[drainage]

# Create a DataFrame from the user input
user_input_df = pd.DataFrame([[ph, max_temperature_avg, humidity_avg, precip_avg, area_slope, soil_type_encoded, drainage_encoded]],
                              columns=['ph', 'max_temperature_avg', 'humidity_avg', 'precip_avg', 'area_slope', 'soil_type_encoded', 'drainage_encoded'])
predict_button = st.sidebar.button("Predict")
# Add a predict button
if predict_button:
    # Make predictions using the loaded model
    prediction = loaded_model.predict(user_input_df)

    # Display or use the prediction as needed
    #st.write("Predicted Class:", prediction[0])
    crop_mapping = {0: 'cassava', 1: 'corn', 2: 'oil palm', 3: 'rice', 4: 'sugar cane'}
    predicted_crop = crop_mapping[prediction[0]]
    #st.write("Predicted Crop:", predicted_crop)
    st.sidebar.success(f"The predicted crop is {predicted_crop}")
    #st.sidebar.empty()
    #st.experimental_rerun()
with title:
    c1, c2, c3 = st.columns([1,3,1])
    with c2:
        st.markdown(
        """
            <style>
            .title{
                text-align: center;
                font-family: monospace;
                font-weight: bold;
            }
            .mainheading{
                text-align: center;
                font-family: monospace;
                font-size: 25px;
            }
            .mainheading1{
                text-align: center;
                font-family: monospace;
                font-size: 20px;
            }
            </style>
        """,
        unsafe_allow_html=True
        )
        st.markdown('<h1 class="title">CropHarbor</h1>',unsafe_allow_html=True)
        st.markdown('<h2 class="mainheading">Welcome to AI Driven Crop Suitability Prediction App! </h2>',unsafe_allow_html=True)
        st.write("<br>",unsafe_allow_html=True)
with logo1:
    c_1, c_2, c_3 = st.columns([1,1,1])
# Add a logo
    with c_2:
        st_lottie(logo, speed=1, width=400, height=400)
        if predict_button == False:
            st.warning("👈Experience the magic of AI in agriculture!")

with description1:
    c_11, c_22, c_33 = st.columns([1,5,1])
    with c_22:
        if predict_button:
            if predicted_crop == 'cassava':
                t = 'Cassava'
                text = "Cassava is a perennial woody shrub with an edible root, which grows in tropical and subtropical areas of the world. Cassava is a major source of carbohydrates in the diets of people in these areas. The crop is a major source of food in the developing world, providing a basic diet for over half a billion people. It is one of the most drought-tolerant crops, capable of growing on marginal soils. Nigeria is the world's largest producer of cassava, while Thailand is the largest exporter of cassava starch."
                days_to_harvest = "Cassava typically takes about 8-12 months to reach harvest maturity."
                diseases = "Common diseases that can occur during cassava harvest include Cassava Mosaic Disease, Cassava Brown Streak Disease, and Cassava Bacterial Blight."
            elif predicted_crop == 'corn':
                t = 'Corn'
                text = "Corn is a cereal grain that is widely grown throughout the world. It is a staple food in many countries and is used for various purposes, including human consumption, animal feed, and industrial uses. Corn is known for its versatility and can be found in a wide range of products, such as cornmeal, corn oil, corn syrup, and cornstarch."
                days_to_harvest = "Corn typically takes about 60-100 days to reach harvest maturity."
                diseases = "Common diseases that can occur during corn harvest include Corn Smut, Northern Corn Leaf Blight, and Gray Leaf Spot."
            elif predicted_crop == 'oil palm':
                t = 'Oil Palm'
                text = "The oil palm is a tropical palm tree. Palm oil is extracted from the pulp of the fruit of the oil palm. The palm is native to West Africa, but it is cultivated in several tropical countries. The main exporting countries are Indonesia, Malaysia, and Nigeria. The oil palm is a very efficient crop in terms of oil production. It is also a very versatile crop, as every part of the tree can be used for economic purposes."
                days_to_harvest = "Oil palm typically takes about 2-3 years to reach harvest maturity."
                diseases = "Common diseases that can occur during oil palm harvest include Ganoderma Basal Stem Rot, Fusarium Wilt, and Bud Rot."
            elif predicted_crop == 'rice':
                t = 'Rice'
                text = "Rice is a staple food for more than half of the world's population, particularly in Asia. It is a cereal grain that is cultivated extensively in irrigated paddies. Rice is a versatile crop and can be used in various dishes, such as stir-fries, sushi, and rice pudding. It is also an important crop for global food security."
                days_to_harvest = "Rice typically takes about 3-6 months to reach harvest maturity."
                diseases = "Common diseases that can occur during rice harvest include Rice Blast, Sheath Blight, and Brown Spot."
            elif predicted_crop == 'sugar cane':
                t = 'Sugar Cane'
                text = "Sugar cane is a tropical, perennial grass that forms lateral shoots at the base to produce multiple stems, typically 3 to 4 meters high. It is primarily grown for sugar production, but it is also used for the production of ethanol, molasses, and other by-products. Sugar cane is an important cash crop in many countries and plays a significant role in the global sugar industry."
                days_to_harvest = "Sugar cane typically takes about 12-24 months to reach harvest maturity."
                diseases = "Common diseases that can occur during sugar cane harvest include Sugarcane Smut, Red Rot, and Yellow Leaf Syndrome."
            html_code = f"""
            <div style='
                background-color: #2A2937;
                border-radius: 5px;
                padding: 20px;
                font-family: Arial;
                font-size: 20px;
                '><h4>{t}</h4>
                <P>{text}</P>
                <p> - {days_to_harvest}</p>
                <p> - {diseases}</p>
                </div>
            """
            st.markdown(html_code, unsafe_allow_html=True)

            st.sidebar.empty()
