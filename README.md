# Product Recommendation Engine

This project is a simple product recommendation engine that uses collaborative filtering to suggest items to users based on their past behavior. The engine is built with Python, Pandas, and Scikit-learn, and it uses a Flask web interface to provide an interactive user experience.

## Features

- **Collaborative Filtering**: Recommends products based on user-item interaction data.
- **Cosine Similarity**: Calculates the similarity between products to find the best recommendations.
- **Web Interface**: A simple and intuitive UI built with Flask to interact with the recommendation engine.
- **Modular Code**: The project is structured with a clear separation of concerns, making it easy to understand and extend.

## How to Run the Project

1.  **Clone the repository**:

    ```bash
    git clone <repository-url>
    cd 0047_Product_recommendation_engine
    ```

2.  **Install the dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

3.  **Run the Flask application**:

    ```bash
    python3 app.py
    ```

4.  **Open your browser** and navigate to `http://127.0.0.1:5000` to use the recommendation engine.

## Project Structure

- `app.py`: The main Flask application file.
- `recommendation_engine.py`: Contains the `RecommendationEngine` class with the core recommendation logic.
- `data/ratings.csv`: The mock database with user-product ratings.
- `templates/index.html`: The HTML template for the web interface.
- `requirements.txt`: A list of the project's Python dependencies.
- `.gitignore`: Specifies which files and directories to ignore in the Git repository.
# Product-Recommendation-Engine
