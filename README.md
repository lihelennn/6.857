# 6.857

## Local Implementation
Our local implementation can see how the messages are stored and encrypted in the API.

#### Dependencies
- Python3
- Virgil Security's Virgil Crypto Python API

#### Instructions
- In terminal, run ```pip install virgil-crypto```, ```python basic.py```.

## Slack Integration
We created a Slack workspace called and created a channel to insert our slash commands. 

#### Dependecies
- Python3, Flask
- Virgil Security's Virgil Crypto Python API

#### Instructions
- Create and run a virtual environment: ```python3 -m venv env```, ```source venv/bin/activate```.
- In terminal, run ```pip install virgil-crypto```, ```pip install flask```.
- Create a new Slack app.
- Insert token ID and team ID from Slack into the beginning of ```slack_python.py``` code.
- In terminal, run ```export FLASK_APP=slack_python.py```.
- Run the Flask app with ```python -m flask run```.
- Our Flask app should now run on localhost:5000.
- Create a ngrok server that will process the forward request from local port 5000 with ```ngrok http 5000```.
- Input that forwarding link into the Slack application for the Slack channel.
- Test with slash command ```/e2ee <messages>```.



## Sources
https://renzo.lucioni.xyz/serverless-slash-commands-with-python/
