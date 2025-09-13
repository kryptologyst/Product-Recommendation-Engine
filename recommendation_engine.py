# recommendation_engine.py

import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

class RecommendationEngine:
    def __init__(self, ratings_file):
        self.ratings_df = self._load_ratings(ratings_file)
        self.similarity_matrix = self._calculate_similarity()

    def _load_ratings(self, ratings_file):
        """Load user-product ratings from a CSV file."""
        df = pd.read_csv(ratings_file, index_col='user_id')
        print("User-Product Ratings:\n")
        print(df)
        return df

    def _calculate_similarity(self):
        """Calculate cosine similarity between products."""
        product_user_matrix = self.ratings_df.T
        similarity_matrix = pd.DataFrame(
            cosine_similarity(product_user_matrix),
            index=product_user_matrix.index,
            columns=product_user_matrix.index
        )
        print("\nProduct Similarity Matrix:\n")
        print(similarity_matrix.round(2))
        return similarity_matrix

    def recommend_products(self, product_name, top_n=3):
        """Recommend similar products based on a given product."""
        if product_name not in self.similarity_matrix:
            return f"Product '{product_name}' not found."
        
        sorted_similar_products = self.similarity_matrix[product_name].sort_values(ascending=False)
        recommendations = sorted_similar_products[1:top_n+1]  # Exclude the product itself
        return recommendations

if __name__ == "__main__":
    # Path to the ratings data
    ratings_file = 'data/ratings.csv'

    # Initialize the recommendation engine
    engine = RecommendationEngine(ratings_file)

    # Example: Recommend similar products to "Product A"
    product_to_recommend = "Product A"
    recommendations = engine.recommend_products(product_to_recommend)

    print(f"\nRecommended products for '{product_to_recommend}':\n")
    print(recommendations)
