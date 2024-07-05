import streamlit as st
from model import get_recommendations
import pandas as pd

# Load dataset
data = pd.read_csv('data/CleanData.csv')

product_names = data['Product_Name'].tolist()

st.title('Product Recommendation System')

# Autocomplete or suggest product names
product_name = st.selectbox('Enter a partial product name:', product_names)
# cat_name = data['Category_Name'][(data['Product_Name'] == product_name)]

cat_name = (data['Product_Name'] == product_name) == True
print(cat_name,33)

# print(product_name['Category_Name'], 111)
if st.button("Get Recommendations"):
    recommendations = get_recommendations(product_name, data=data)
    if isinstance(recommendations, str):
        st.write(recommendations)
    else:
        for index, row in recommendations.iterrows():
            st.image(row['images'], width=150)
            st.write(f"Product Name: {row['Product_Name']}")
            st.write(f"*Selling Price:* ₹{row['Selling_Price']:.2f}")
            st.write(f"*Original Price:* ₹{row['Original_Price']:.2f}")
            st.write(f"*Discount:* {row['Discount']} %")
            st.write(f"Category: {row['Category_Name']}")
            st.write(f"Description: {row['Description']}")


            st.write("---")