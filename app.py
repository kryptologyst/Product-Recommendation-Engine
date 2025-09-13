# app.py

from flask import Flask, render_template, request
from recommendation_engine import RecommendationEngine

app = Flask(__name__)

# Initialize the recommendation engine
ratings_file = 'data/ratings.csv'
engine = RecommendationEngine(ratings_file)

@app.route('/', methods=['GET', 'POST'])
def index():
    recommendations = None
    selected_product = None
    if request.method == 'POST':
        selected_product = request.form.get('product')
        if selected_product:
            recommendations = engine.recommend_products(selected_product)
            if isinstance(recommendations, str):
                recommendations = None # Product not found

    products = engine.ratings_df.columns.tolist()
    return render_template('index.html', 
                           products=products, 
                           selected_product=selected_product,
                           recommendations=recommendations)

if __name__ == '__main__':
    app.run(debug=True)
