from utils.extractText import TextExtractor
from flask import Flask, request, jsonify
from flask import Flask, jsonify

c = ""

# Create a Flask app instance
app = Flask(__name__)

# Define the route /run
@app.route('/get_content', methods=['GET'])
def run():
    # Get JSON data from the request
    data = request.get_json()
    
    # Get the 'url' key from the JSON data
    url = data.get('url') if data else None
    output_file = data.get("output_file") if data else None
    
    # Check if a URL was provided
    if url:
        text = TextExtractor(url,output_file)
        content = text.extract_entire_content()
        return jsonify({"message": f"URL received and processed: {url} "})
    else:
        return jsonify({"error": "No URL provided"}), 400

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)