import requests
import json
import os


GRAPH_URL = "https://graph.facebook.com/v2.6"
ACCESS_TOKEN = ""
url = "{0}/me/messages?access_token={1}".format(GRAPH_URL, ACCESS_TOKEN)

def send_text_message(id, text):
    payload = {
        "recipient": {"id": id},
        "message": {"text": text}
    }
    response = requests.post(url, json=payload)

    if response.status_code != 200:
        print("Unable to send message: " + response.text)
    return response

def send_img_message(fb_id, image_url):
    #temp = (os.path.basename(image_url), open(image_url, 'rb'))
    #print(temp)
    response = {
        "attachment": {
            "type": "image",
            "payload": {
                "url": image_url,
                "is_reusable": True
            },
            #"filedata": (os.path.basename(image_url), open(image_url, 'rb'))
        }
    }
    response_msg = json.dumps({"recipient": {"id": fb_id}, "message": response})
    response = requests.post(url, headers={"Content-Type": "application/json"}, data=response_msg)

    if response.status_code != 200:
        print("Unable to send img message")
    return response
"""
def send_image_url(id, img_url):
    pass
"""
def send_button_message(fb_id, text, buttons):
    response = {
        "attachment": {
            "type": "template",
            "payload": {
                "template_type":"button",
                "text": text,
                "buttons": buttons
            },
        }
    }

    response_msg = json.dumps({"recipient": {"id": fb_id}, "message": response})
    response = requests.post(url, headers={"Content-Type": "application/json"}, data=response_msg)
    if response.status_code != 200:
        print("Unable to send message: " + response.text)
    return response

