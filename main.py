from transformers import pipeline
classifier = pipeline("sentiment-analysis")
res = classifier("I saw a  beautiful flying eagle with a blue beak.")
print(res)