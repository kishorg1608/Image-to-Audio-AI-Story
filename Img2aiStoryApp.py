# Use a pipeline as a high-level helper
from transformers import pipeline
from dotenv import find_dotenv, load_dotenv
import requests


# This is a function to take in the image and generate a caption first. 
# We then put that caption in another model to generate a story around that caption.
# We can give more prompts in the second model to make according to our script. #
def img2txt(url):
    # First model to give the caption
    image_to_text= pipeline("image-to-text", model = "Salesforce/blip-image-captioning-base")
    text= image_to_text(url)[0]["generated_text"]
    print(text)

    # Second model to reate a story from that caption, it also includes custom prompts.
    textgenerator = pipeline("text-generation", model= "distilgpt2")
    story = textgenerator("Here is a kids story about " + text, 
        max_length=400)
    print(story)
    return story





#txt2audio for converting the created story in a format to listen
def text2speech(message):
    API_URL = "https://api-inference.huggingface.co/models/espnet/kan-bayashi_ljspeech_vits"
    headers = {"Authorization": "Bearer <put a hugging face api key>"}
    payloads={"inputs":message}

    response = requests.post(API_URL, headers=headers, json=payloads)
    with open('baudio.mp3', 'wb') as file:
        file.write(response.content)



#################################################
#final call of all function to make a coherent system from image to audio story.

audio= img2txt("ASNF.png")   #it is the name of an image present in my folder, you can put any path to image 
text2speech(audio)