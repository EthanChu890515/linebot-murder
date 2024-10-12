from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import *
import os
import random

#TemplateSendMessage - ImageCarouselTemplate(圖片旋轉木馬)
#旋轉木馬按鈕訊息介面

def Carousel_Template():
    message = TemplateSendMessage(
        alt_text='一則旋轉木馬按鈕訊息',
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    thumbnail_image_url='https://github.com/EthanChu890515/linebot-murder/blob/main/%E5%A5%B3%E5%82%AD.png?raw=true',
                    title='女傭',
                    text='一個模板可以有三個按鈕',
                    actions=[
                        PostbackTemplateAction(
                            label='她是兇手',
                            data='將這個訊息偷偷回傳給機器人'
                        ),
                        MessageTemplateAction(
                            label='用戶發送訊息',
                            text='我知道這是1'
                        ),
                        URITemplateAction(
                            label='進入1的網頁',
                            uri='https://upload.wikimedia.org/wikipedia/commons/thumb/8/88/Number_1_in_green_rounded_square.svg/200px-Number_1_in_green_rounded_square.svg.png'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://github.com/EthanChu890515/linebot-murder/blob/main/AI%E6%A9%9F%E5%99%A8%E4%BA%BA.png?raw=true',
                    title='AI機器人',
                    text='副標題可以自己改',
                    actions=[
                        PostbackTemplateAction(
                            label='它是兇手',
                            data='這是ID=2'
                        ),
                        MessageTemplateAction(
                            label='用戶發送訊息',
                            text='我知道這是2'
                        ),
                        URITemplateAction(
                            label='進入2的網頁',
                            uri='https://upload.wikimedia.org/wikipedia/commons/thumb/c/cd/Number_2_in_light_blue_rounded_square.svg/200px-Number_2_in_light_blue_rounded_square.svg.png'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://upload.wikimedia.org/wikipedia/commons/thumb/e/e4/Number_3_in_yellow_rounded_square.svg/200px-Number_3_in_yellow_rounded_square.svg.png',
                    title='廚師',
                    text='最多可以放十個',
                    actions=[
                        PostbackTemplateAction(
                            label='他是兇手',
                            data='這是ID=3'
                        ),
                        MessageTemplateAction(
                            label='用戶發送訊息',
                            text='我知道這是3'
                        ),
                        URITemplateAction(
                            label='uri2',
                            uri='https://upload.wikimedia.org/wikipedia/commons/thumb/e/e4/Number_3_in_yellow_rounded_square.svg/200px-Number_3_in_yellow_rounded_square.svg.png'
                        )
                    ]
                )
            ]
        )
    )
    return message
