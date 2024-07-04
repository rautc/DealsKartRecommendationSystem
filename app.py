import streamlit as st
import pandas as pd
from fuzzywuzzy import process

from model import get_recommendations

# Load your dataset
data = pd.read_csv('data/Dealskarts.csv')
product_names = data['Product Name'].tolist()

st.title('Product Recommendation System')

# Autocomplete or suggest product names
product_name = st.selectbox('Enter a partial product name:', product_names)


if st.button('Recommend'):
    recommendations = get_recommendations(product_name)
    st.write('Top Recommendations:')
    for _, row in recommendations.iterrows():
        st.image(row['Image URL'], width=150)
        st.write(f"*Product Name:* {row['Product Name']}")
        st.write(f"*Selling Price:* ₹{row['Selling Price']:.2f}")
        st.write(f"*Original Price:* ₹{row['Original Price']:.2f}")
        st.write(f"*Discount:* {row['Discount']}% ")
        st.write(f"*Description:* {row['Description']}")
        st.write("---")
