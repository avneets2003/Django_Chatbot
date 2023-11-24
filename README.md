# Django Chatbot

## Description
This is my attempt to build a chatbot using Django and an API key from Cohere (which uses Command LLM). Using this simplistic chatbot, you can view the past responses and delete your chatting history.  Functionalities include setting a limit on the length of the responses, displaying multiple responses and continuing the previous response.

## Installation

- In your working directory, clone this repository.
```sh
git clone https://github.com/avneets2003/Django_Chatbot.git
```
- Make sure you have Python installed on your computer.
```sh
python --version
```
- Set up a Python virtual environment.
```sh
python -m venv virt
source virt/Scripts/activate
```
- Install the requirements.
```sh
pip install django cohere
```
- Change directory to `Django_Chatbot`.
```sh
cd Django_Chatbot
```
- Obtain an API from Cohere's website.
- In `chat/views.py`, paste your API key.
- Run the Django server.
```sh
python manage.py runserver
```
- Boom! Your chatbot is ready to answer any question.
