import requests
import os
# import psutil
from transformers import pipeline
from flask import Flask, request, jsonify

app = Flask(__name__)
# process = psutil.Process()



#Google Custom Search Engine ID
engine_id = os.environ.get('ENGINE_ID')
# engine_id = '02545075c61a24321'
#Google API key
api_key = os.environ.get('API_KEY')
# api_key = 'AIzaSyChfaN-id-IAkInxkPoLwx49YfHgF4krsY'



# question-answering pipeline initialized
pipeline_search = pipeline("question-answering", model="distilbert-base-uncased-distilled-squad")

# memory_usage = get_memory_usage()
# print(f"Memory Usage Pipeline: {memory_usage} MB")


# def get_memory_usage():
#     mem_info = process.memory_info()
#     memory_usage = mem_info.rss / (1024 * 1024)  # Convert to megabytes
#     return memory_usage

@app.route('/')
def indicator():
    return "My Flask Application is running!"






#Path that accepts requests
@app.route('/searchQuery', methods=['POST'])
def perform_search():
    data = request.get_json()
    topic = data.get('query')
    question = data.get('question')

    results = search_internet(topic, question)
    answer = result_questions(results, question)

    response = {
        'answer': answer
    }

    # Check memory usage
    # memory_usage = get_memory_usage()
    # print(f"Memory Usage: {memory_usage} MB")

    return jsonify(response)


#Method that answers questions to given topic using distilbert-base-cased-distilled-squad model
def result_questions(results, question):
    if results:
#Empty list created to store snippets 
        snippets_lst = []

# Iterate over each result in the 'results' list
        for result in results:
    # Access the 'snippet' key
            snippets_lst.append(result['snippet'])

        page_content = ' '.join(snippets_lst)

        #  question-answering using the Hugging Face model
        answer = pipeline_search(question=question, context=page_content)

        return answer['answer']
    else:
        return "No search results found."


# Function to search Google for given topic
def search_internet(topic, question):
    # Make a request to the Google Custom Search API
    url = f'https://www.googleapis.com/customsearch/v1?key={api_key}&cx={engine_id}&q={topic}+{question}'
    res = requests.get(url)
    res.raise_for_status()

    # Extract the search results
    data = res.json()
    results = data.get('items', [])

    return results


if __name__ == '__main__':
    app.run()
