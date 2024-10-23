from utils.extractText import TextExtractor
from utils.generate_store_embeddings import Embeding_DB
from flask import Flask, request, jsonify
from flask import Flask, jsonify
from src.Log import logger
import os
import pickle
from pinecone import Pinecone, ServerlessSpec
c = ""

# Create a Flask app instance
app = Flask(__name__)

@app.route('/', methods=['GET'])
def greet():
    return jsonify({"hellow":f"greate to meet you,"})

# Define the route /run
@app.route('/build_chat', methods=['GET'])
def run():
    # # Get JSON data from the request
    # data = request.get_json()
    
    # # Get the 'url' key from the JSON data
    # url = data.get('url') if data else None
    # output_file = data.get("output_file") if data else None
    
    # # Check if a URL was provided
    # if url:
    #     text = TextExtractor(url,output_file)
    #     logger.info(">>>>>> Created TextExtractor Object <<<<<<")
    #     c = text.extract_entire_content()
    #     logger.info(">>>>>> Compleated TextExtractor Process <<<<<<")
    #     return jsonify({"message": f"URL received and processed: {url} "})
    # else:
    #     return jsonify({"error": "No URL provided"}), 400

       # Get JSON data from the request
    data = request.get_json()
    
    # Get the 'url' key from the JSON data
    url = data.get('url') if data else None
    output_file = data.get("output_file") if data else None
    
    # Check if a URL was provided
    if url:
        text = TextExtractor(url,output_file)
        logger.info(">>>>>> Created TextExtractor Object <<<<<<")
        c = text.extract_entire_content()
        logger.info(">>>>>> Compleated TextExtractor Process <<<<<<")
    else:
        logger.error("Url does not exist")

    #performing embeding and storing in pinecode vector store:
    # 1)defining the index
    index = "triluxo"
    # getting the api key
    api_key = os.getenv("PINECONE")
    
    

@app.route("/test1", methods=['GET'])
def connect_database():
    obj =Embeding_DB()
    print("created the object >>>>>>>>>>>>>>>")
    retriver = obj.Embed_Save()
    with open('retriever.pkl', 'wb') as f:
        pickle.dump(retriver, f)

    return jsonify({"retriver object serialised":f"{retriver}"})

@app.route("/get_chat", methods=['GET'])
def getCaht():
    pickle_file = 'retriever.pkl'  # Replace with the actual pickle file path

    # Open the pickle file in 'rb' mode (read binary)
    with open(pickle_file, 'rb') as f:
        # Load the object from the pickle file
        data = pickle.load(f)
    print("the content of the retriver file are : ")
    content = data.invoke("7 LessonsView Details$22per sessionThe AI Writer")
    return jsonify({"retriver content":f">>. {content}"})





# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)