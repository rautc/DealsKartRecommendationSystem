import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load dataset
data = pd.read_csv('data/CleanData.csv')

# Data preprocessing
data = data.dropna(subset=['Product_Name', 'Description', 'Category_Name'])
data['Description'] = data['Description'].astype(str)

# Combine relevant features into a single string
data['combined_features'] = data['Product_Name'] + ' ' + data['Description'] + ' ' + data['Category_Name']
# print(data)

# TF-IDF Vectorizer
tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(data['combined_features'])
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)


def get_recommendations(product_name, cosine_sim=cosine_sim, data=data):
    idx = data.index[data['Product_Name'] == product_name] .tolist()
    if not idx:
        return "Product not found."
    idx = idx[0]

    product_category = data.iloc[idx]['Category_Name']

    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    recommended_indices = [i[0] for i in sim_scores if data.iloc[i[0]]['Category_Name'] == product_category]
    recommended_indices = recommended_indices[1:6]  # Skip the first one as it is the queried product itself

    return data.iloc[recommended_indices]


if __name__ == "_main_":
    # Example usage
    print(get_recommendations("Example Product Name"))