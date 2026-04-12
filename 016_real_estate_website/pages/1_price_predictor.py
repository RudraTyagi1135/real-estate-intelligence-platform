import streamlit as st
import pickle
import pandas as pd
import numpy as np
from pathlib import Path

st.set_page_config(page_title="Price Predictor")


PROJECT_ROOT = Path(__file__).resolve().parents[2]
target_path = PROJECT_ROOT / "015_selected_model_and_preprocessor"

# Load the DataFrame
with open(target_path / 'df.pkl', 'rb') as file:
    df = pickle.load(file)

# Load the Pipeline (or Preprocessor)
with open(target_path / 'pipeline.pkl', 'rb') as file:
    pipeline = pickle.load(file)

print("Files loaded successfully!")



st.header('Enter your inputs')

# property_type
property_type = st.selectbox('Property Type', sorted(df['property_type'].unique().tolist()))


# sector
sector = st.selectbox('Sector',sorted(df['sector'].unique().tolist()))

bedrooms = float(st.selectbox('Number of Bedroom',sorted(df['bedRoom'].unique().tolist())))   # type: ignore

bathroom = float(st.selectbox('Number of Bathrooms',sorted(df['bathroom'].unique().tolist())))   # type: ignore

balcony = st.selectbox('Balconies',sorted(df['balcony'].unique().tolist()))

property_age = st.selectbox('Property Age',sorted(df['agePossession'].unique().tolist()))

built_up_area = float(st.number_input('Built Up Area'))

servant_room = float(st.selectbox('Servant Room',[0.0, 1.0]))  # type: ignore
store_room = float(st.selectbox('Store Room',[0.0, 1.0]))   # type: ignore

furnishing_type = st.selectbox('Furnishing Type',sorted(df['furnishing_type'].unique().tolist()))
luxury_category = st.selectbox('Luxury Category',sorted(df['luxury_category'].unique().tolist()))
floor_category = st.selectbox('Floor Category',sorted(df['floor_category'].unique().tolist()))

if st.button('Predict'):

    # form a dataframe
    data = [[property_type, sector, bedrooms, bathroom, balcony, property_age, built_up_area, servant_room, store_room, furnishing_type, luxury_category, floor_category]]
    columns = ['property_type', 'sector', 'bedRoom', 'bathroom', 'balcony',
               'agePossession', 'built_up_area', 'servant room', 'store room',
               'furnishing_type', 'luxury_category', 'floor_category']

    # Convert to DataFrame
    one_df = pd.DataFrame(data, columns=columns)

    #st.dataframe(one_df)

    # predict
    base_price = np.expm1(pipeline.predict(one_df))[0]
    low = base_price - 0.22
    high = base_price + 0.22

    # display
    st.text("The price of the flat is between {} Cr and {} Cr".format(round(low,2),round(high,2)))
