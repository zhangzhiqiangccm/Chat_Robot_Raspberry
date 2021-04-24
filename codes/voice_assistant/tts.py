from aip import AipSpeech
import os

def run(text):
    try:
        app_id = '15396738'
        api_key = 'tNSgctsOolIEr40DRV4MeaOv'
        secret_key = 'dlPK65O5BeWCfFerfqtGZOfNl8vqNBj6'
        client = AipSpeech(app_id,api_key,secret_key)

        result = client.synthesis(text,'zh','123456',
                                 {"vol": 5,
                                  "spd": 5,
                                  "pit": 5,
                                  "per": 4,
                                 })

        with open("/home/pi/voice_assistant/audio.wav","wb") as f:
            f.write(result)
        os.popen("mplayer /home/pi/voice_assistant/audio.wav")
        print("[INFO] 播放完成")
    except:
        print("[INFO] 语言播报错误，检查网络或参数")
