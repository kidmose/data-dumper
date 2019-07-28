# Introduction #

Demo of REST API accepting JSON objects and saving them to disk, using Flask.

Work in progress!

Based on: https://codehandbook.org/working-with-json-in-python-flask/

# Setup #

Build and tested on Linux Mint 18.2, with Python 3.5.2.

I use `virtualenv` to make an isolated installation of python 3 for
this project (run once)

	virtualenv -ppython3 env

And everytime I start working on it, I activate it with:

	source env/bin/activate

Tutorial on virtualenv: https://www.pythonforbeginners.com/basics/how-to-use-python-virtualenv


Install additional python libraries with (Run once):

	pip install -r requirements.txt

# Usage #

Start the web server locally:

	python receiver.py
	
Add a new plate to the "database" file with `curl`:

	curl --silent -H "Content-Type: application/json" --request POST --data '{"serial": "9"}' http://127.0.0.1:5000/api/v0/addPlate

Get a list of plates in the "database" file with `curl`:

	curl --silent http://127.0.0.1:5000/api/v0/getPlateList | jq
