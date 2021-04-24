#!/usr/bin/env python3

import speech_recognition as sr
from ha_cli import ha_cli
from ais_cli import tuling123
import tts

tuling_user_id = '421096'
tuling_api_key = '1f55700b32a14243a6ea696b1423d511'
ha_token='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJkOTI5MDBiYjMzMjE0MzlhODhlNzBjZWI0ODdkYTRmYiIsImlhdCI6MTYxODQ3MDc0OCwiZXhwIjoxOTMzODMwNzQ4fQ.ciUuKwjEuY2Ik-mz5I7bsoSpiVJqiYekOIidfH0JMPk'
snowboy_location = '/home/pi/voice_assistant/sb/'
snowboy_models = ['/home/pi/voice_assistant/sb/models/snowboy.umdl', '/home/pi/voice_assistant/sb/models/xiaohei.pmdl']
snowboy_config = (snowboy_location, snowboy_models)

import sys
sys.path.append(snowboy_location)
import snowboydecoder
sys.path.pop()

r = sr.Recognizer()
ha = ha_cli(token=ha_token)
tuling = tuling123(user_id=tuling_user_id, api_key=tuling_api_key)

with sr.Microphone(sample_rate=16000) as source:
    while True:
        try:
            print("开始监听……")
            audio = r.listen(source,
                             phrase_time_limit=6,
                             snowboy_configuration=snowboy_config,
                             hot_word_callback=snowboydecoder.play_audio_file
                             )

            print("开始识别……")
            snowboydecoder.play_audio_file(fname=snowboy_location+'resources/dong.wav')
            result = r.recognize_google_cn(audio, language='zh-CN')
        except sr.UnknownValueError:
            result = ''
        except Exception as e:
            print("识别错误：{0}".format(e))
            continue
        print("识别结果：" + result)

        try:
            speech = ha.process(result)
            if speech == "Sorry, I didn't understand that":
                speech = tuling.command(result)
                # ha.note(message=result)
            tts.run(speech)
        except Exception as e:
            print("与HomeAssistant通讯失败：{0}".format(e))
            continue

