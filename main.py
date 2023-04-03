 
from flask import Flask, request, jsonify
import GenrePredictor

# Define the app
app = Flask(__name__)
genrePredictor = GenrePredictor.GenrePredictor()

# Define the route for making predictions
@app.route('/predict', methods=['POST'])
def predict():
    # Get the uploaded file
    file = request.files['file']
    print("Starting prediction")
    genre_predictions = []
    try:
        genre_predictions = genrePredictor.predict_genre(file)
    except:
        print("WHOAH, something went wrong!")
    
    print(f'Got genre predictions: {genre_predictions}') 
    # Return the result as a JSON object
    return jsonify(genre_predictions)

# Start the app
if __name__ == '__main__':
    app.run(debug=False)
