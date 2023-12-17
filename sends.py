import requests
def send_message(url:str,chat_id,text,reply_markup,parse_mode=False):
    endpoint = "/sendMessage"
    url += endpoint
    data = {
        "chat_id":chat_id,
        "text":text,
        "reply_markup":reply_markup
    }
    if parse_mode:
        data['parse_mode'] = "HTML"
    requests.post(url,json=data)
def send_contact(url,chat_id,phone_number,first_name,last_name,parse_mode=False):
    endpoint = "/sendContact"
    url += endpoint
    payload = {
        "chat_id":chat_id,
        "phone_number":phone_number,
        "first_name":first_name,
        "last_name":last_name
    }
    if parse_mode:
        payload['parse_mode'] = "HTML"
    requests.get(url,params=payload)
def send_photo(url,chat_id,photo,text,parse_mode=False):
    endpoint = "/sendPhoto"
    url += endpoint
    payload = {
        "chat_id":chat_id,
        "caption":text,
        
    }
    file = {
        "photo":open(photo,"rb")
    }
    if parse_mode:
        payload['parse_mode'] = "HTML"
    requests.get(url,params=payload,files=file)





