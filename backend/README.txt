# ReadMe - Backend for SearchQuest

This application allows users to ask about a topic and answers any questions pertaining to the topic based on search results from the  internet.
It uses Google Custom Search API and the Hugging Face Transformers library.

## Prerequisites

 Dependencies to be installed:

- Python 3.x
- requests
- transformers
- flask

Steps to run the application:
1. Clone the repository or download the source code.
2. Open a terminal and navigate to the project directory.
3. Run the following command to start the application: python server.py
4. The Flask application will start running on `http://localhost:5000`.

Working:

1. Send a POST request to the `/searchQuery` endpoint with the following example JSON payload:

{
  "query": "leaves",
  "question": "what is the function?"
}

The application will search the internet using the Google Custom Search API and retrieve relevant search results which will ne used to answer question.

NOTE:
You can modify the engine_id and api_key variables in the server.py file to use your own Google Custom Search Engine ID and API key.
