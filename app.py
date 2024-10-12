from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import *
import os

app = Flask(__name__)

# Line API Token and Secret
line_bot_api = LineBotApi('CHANNEL_ACCESS_TOKEN')
handler = WebhookHandler('CHANNEL_SECRET')

# TemplateSendMessage - ImageCarouselTemplate (旋轉木馬按鈕訊息介面)
def Carousel_Template():
    message = TemplateSendMessage(
        alt_text='一則旋轉木馬按鈕訊息',
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    thumbnail_image_url='https://github.com/EthanChu890515/linebot-murder/blob/main/%E5%A5%B3%E5%82%AD.png?raw=true',
                    title='女傭',
                    actions=[
                        PostbackTemplateAction(
                            label='她是兇手',
                            data='correct'  # 女傭為正確答案
                        ),
                        MessageTemplateAction(
                            label='用戶發送訊息',
                            text='兇手是女傭'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://github.com/EthanChu890515/linebot-murder/blob/main/AI%E6%A9%9F%E5%99%A8%E4%BA%BA.png?raw=true',
                    title='AI機器人',
                    actions=[
                        PostbackTemplateAction(
                            label='它是兇手',
                            data='correct'  # AI機器人為正確答案
                        ),
                        MessageTemplateAction(
                            label='用戶發送訊息',
                            text='兇手是AI機器人'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://github.com/EthanChu890515/linebot-murder/blob/main/%E5%BB%9A%E5%B8%AB.png?raw=true',
                    title='廚師',
                    actions=[
                        PostbackTemplateAction(
                            label='他是兇手',
                            data='correct'  # 廚師為正確答案
                        ),
                        MessageTemplateAction(
                            label='用戶發送訊息',
                            text='兇手是廚師'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://github.com/EthanChu890515/linebot-murder/blob/main/%E9%86%AB%E7%94%9F.png?raw=true',
                    title='醫生',
                    actions=[
                        PostbackTemplateAction(
                            label='它是兇手',
                            data='wrong'  # 醫生為錯誤答案
                        ),
                        MessageTemplateAction(
                            label='用戶發送訊息',
                            text='兇手是醫生'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://github.com/EthanChu890515/linebot-murder/blob/main/%E5%9C%92%E4%B8%81.png?raw=true',
                    title='園丁',
                    actions=[
                        PostbackTemplateAction(
                            label='他是兇手',
                            data='wrong'  # 園丁為錯誤答案
                        ),
                        MessageTemplateAction(
                            label='用戶發送訊息',
                            text='兇手是園丁'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://github.com/EthanChu890515/linebot-murder/blob/main/%E9%8B%BC%E7%90%B4%E5%AE%B6.png?raw=true',
                    title='鋼琴家',
                    actions=[
                        PostbackTemplateAction(
                            label='它是兇手',
                            data='wrong'  # 醫生為錯誤答案
                        ),
                        MessageTemplateAction(
                            label='用戶發送訊息',
                            text='兇手是鋼琴家'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://github.com/EthanChu890515/linebot-murder/blob/main/%E5%87%BA%E7%89%88%E7%A4%BE%E8%80%81%E9%97%86.png?raw=true',
                    title='出版社老闆',
                    actions=[
                        PostbackTemplateAction(
                            label='它是兇手',
                            data='wrong'  # 醫生為錯誤答案
                        ),
                        MessageTemplateAction(
                            label='用戶發送訊息',
                            text='兇手是出版社老闆'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://github.com/EthanChu890515/linebot-murder/blob/main/%E7%AE%A1%E5%AE%B6.png?raw=true',
                    title='管家',
                    actions=[
                        PostbackTemplateAction(
                            label='它是兇手',
                            data='wrong'  # 醫生為錯誤答案
                        ),
                        MessageTemplateAction(
                            label='用戶發送訊息',
                            text='兇手是管家'
                        )
                    ]
                )
            ]
        )
    )
    return message

# Flask webhook callback route
@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']

    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'

# Handling postback event to check answer
@handler.add(PostbackEvent)
def handle_postback(event):
    if event.postback.data == 'correct':
        reply_text = "答案正確，恭喜過關！"
    else:
        reply_text = "答案錯誤，失敗！"
    
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=reply_text)
    )

# Handling follow event when user adds bot as friend
@handler.add(FollowEvent)
def handle_follow(event):
    welcome_message = TextSendMessage(text="歡迎加入！這是一個偵探遊戲，選擇誰是兇手來過關！")
    carousel_message = Carousel_Template()
    
    # 發送歡迎訊息和旋轉木馬訊息
    line_bot_api.reply_message(
        event.reply_token,
        [welcome_message, carousel_message]
    )

if __name__ == "__main__":
    app.run()
