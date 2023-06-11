from flask import Flask, render_template, request, jsonify
import json
import os
from datetime import datetime
from google.oauth2 import id_token
from google.auth.transport import requests
import time

app = Flask(__name__, static_url_path='/static')

@app.route('/submit-init-data', methods=['POST'])
def submit_init_data():
    instruction = request.form.get('instruction')
    input_data = request.form.get('input')
    output = request.form.get('output')
    current_time = datetime.now()
    formatted_time = current_time.strftime("%Y%m%d_%H%M%S")

    data = {
        'instruction': instruction,
        'input': input_data,
        'output': output,
        'time': formatted_time,
    }

    # Check if the path contains '/init-closed-qa'
    if '/init-closed-qa' in request.headers.get('Referer'):
        data['task'] = 'ClosedQA'
    elif '/init-open-qa' in request.headers.get('Referer'):
        data['task'] = 'OpenQA'
    elif '/init-extraction' in request.headers.get('Referer'):
        data['task'] = 'Extraction'
    elif '/init-completion' in request.headers.get('Referer'):
        data['task'] = 'Completion'
    elif '/init-summarization' in request.headers.get('Referer'):
        data['task'] = 'Summarization'
    elif '/init-translation' in request.headers.get('Referer'):
        data['task'] = 'Translation'
    elif '/init-rewrite' in request.headers.get('Referer'):
        data['task'] = 'Rewrite'
    elif '/init-classification' in request.headers.get('Referer'):
        data['task'] = 'Classification'
    elif '/init-sentiment-analysis' in request.headers.get('Referer'):
        data['task'] = 'SentimentAnalysis'
    elif '/init-generation' in request.headers.get('Referer'):
        data['task'] = 'Generation'
    elif '/init-brainstorming' in request.headers.get('Referer'):
        data['task'] = 'Brainstorming'

    save_data_as_json(data)

    return jsonify({'message': 'Data submitted successfully!'})

def save_data_as_json(data):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_name = 'collected_data.json'
    file_path = os.path.join(current_dir, file_name)

    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf8') as f:
            file_data = json.load(f)
    else:
        file_data = []
    file_data.append(data)

    with open(file_path, 'w', encoding='utf8') as f:
        json.dump(file_data, f, ensure_ascii=False, indent=4)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/introduction')
def introduction():
    return render_template('introduction.html')

@app.route('/initial-task')
def initial_task():
    return render_template('initial-task.html')

@app.route('/init-closed-qa')
def openClosedQA():
    return render_template('init-closed-qa.html')

@app.route('/init-open-qa')
def openOpenQA():
    return render_template('init-open-qa.html')

@app.route('/init-extraction')
def openExtract():
    return render_template('init-extraction.html')

@app.route('/init-completion')
def openCompletion():
    return render_template('init-completion.html')

@app.route('/init-summarization')
def openSummarization():
    return render_template('init-summarization.html')

@app.route('/init-translation')
def openTranslation():
    return render_template('init-translation.html')

@app.route('/init-rewrite')
def openRewrite():
    return render_template('init-rewrite.html')

@app.route('/init-classification')
def openClassification():
    return render_template('init-classification.html')

@app.route('/init-sentiment-analysis')
def openSentimentAnalysis():
    return render_template('init-sentiment-analysis.html')

@app.route('/init-generation')
def openGeneration():
    return render_template('init-generation.html')

@app.route('/init-brainstorming')
def openBrainstorming():
    return render_template('init-brainstorming.html')

@app.route('/init-further-tasks')
def openFurtherTasks():
    return render_template('init-further-tasks.html')

@app.route('/make-prompt')
def openMakePrompt():
    return render_template('make-prompt.html')

@app.route('/make-completion')
def openMakeCompletion():
    return render_template('make-completion.html')

@app.route('/dashboard')
def openDashboard():
    return render_template('dashboard.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003, debug=True)
