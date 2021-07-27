import requests
from time import sleep
from secrets import apiKey, myChatId
maxTrials = 5
method = "/sendMessage"
url = "https://api.telegram.org/bot" + apiKey + method

def sendMessage(txt, chatId):
    global url
    try:
        int(chatId)
    except:
        return "Invalid chat id"
    else:
        dataDict = {
        "chat_id": chatId,
        "text": txt
        }
        trials = 0
        while trials < maxTrials:
            response = requests.post(url=url, data=dataDict).json()
            if response["ok"]:
                return "Successfully sent notification"
            else:
                trials += 1
                sleep(5)
        return("Unable to send")

def sendMessageToMe(txt):
    return sendMessage(txt, chatId=myChatId)

while True:
    try:
        print("-"*50)
        print(sendMessageToMe(input("Enter a message to sent. Press CTRL^C to exit\n--> ")))
    except KeyboardInterrupt:
        break
        