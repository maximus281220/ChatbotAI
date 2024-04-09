from transformers import pipeline
chatbot = pipeline(task="conversational", model = "facebook/blenderbot-400M-distill")
user_message= "What are some fun activities we can do on our birthday?"
from transformers import Conversation
conversation= Conversation(user_message)
conversation= chatbot(conversation)
print(conversation)