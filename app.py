import streamlit as st
from model import get_recommendations

st.title('Product Recommendation System')

product_name = st.text_input('Enter a product name:')

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