#line-bot
from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('w3Yoaf/p2AaRfCrmpMkupESO4N92d3QnuCMqAGNqDm1+YaU7jm6fs6zIDxUfPUv7+1YLNaolIXrJgEUUucRDjKm1ck/BWrrbQvEH3sFg2pTicxNa9pwiOOmAysIiyhAelCdEmDNVidJDlVd8OfVHwwdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('807d9f8c34076e8c6aad43dd8afb664a')

#route:路徑
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))


if __name__ == "__main__":
    app.run()