from utils.extractText import TextExtractor
from utils.generate_store_embeddings import Embeding_DB
from flask import Flask, request, jsonify
from flask import Flask, jsonify
from src.Log import logger
import os
import dill as pickle
import requests
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
    
    

@app.route("/test1", methods=['GET'])
def connect_database():
    obj =Embeding_DB(index_name="triluxo", api_key=os.getenv("PINECONE"),filename="output.txt" )
    print("created the object >>>>>>>>>>>>>>>")
    global retriver
    retriver = obj.Embed_Save()
    return jsonify({"vivek":"sonal"})

@app.route("/get_chat", methods=['GET'])
def getChat():
    # data = requests.get('http://127.0.0.1:5000/get_retriever')

    content = retriver.invoke("7 LessonsView Details$22per sessionThe AI Writer")
    print("the content of the retriver file are : ")
    return jsonify({"retriver content":f">>. {content}"})





# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)