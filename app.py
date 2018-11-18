import json
import random
from flask import Flask,request

app = Flask(__name__)

def get_random_topic():
    with open('data/topic.json', 'r') as f:
        sentences = json.load(f)
    return sentences

topics = get_random_topic()


@app.route('/', methods=['GET'])
def hello_world(lang='kr'):
    lang = request.args.get('lang','kr')
    topic = random.choice(topics)
    return topic[lang]
    return 'Hello, World!'





