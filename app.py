import os
from datetime import datetime

from flask import Flask, abort, request

# https://github.com/line/line-bot-sdk-python
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

app = Flask(__name__)

line_bot_api = Mexp3AdQdl+UiGz2lW3Tr+CBM88O3EGle1l1NUo7AbKD1cRpWokByxfq+z1A9LkJCtm+hW2VmPaPWUwhXhIQ8U6Zqi5Q/DfhV6q/onuZS10f6upRJz+TYn7WbAQobMX5GHDr5r1CmRU6G8cnbe4vNAdB04t89/1O/w1cDnyilFU=
handler = c01c2737f06a8a2e5f8ea0aeb6ff5c2c


@app.route("/", methods=["GET", "POST"])
def callback():

    if request.method == "GET":
        return "Hello Heroku"
    if request.method == "POST":
        signature = request.headers["X-Line-Signature"]
        body = request.get_data(as_text=True)

        try:
            handler.handle(body, signature)
        except InvalidSignatureError:
            abort(400)

        return "OK"


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    get_message = event.message.text

    # Send To Line
    reply = TextSendMessage(text=f"{get_message}")
    line_bot_api.reply_message(event.reply_token, reply)
