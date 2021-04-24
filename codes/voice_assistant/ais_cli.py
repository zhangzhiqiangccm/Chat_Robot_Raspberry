"""
This is the client to public AIs' API for voice_assistant.
"""

import requests

class tuling123(object):
    def __init__(self, user_id, api_key, base_url='http://openapi.tuling123.com/openapi/api/v2'):
        self._session = requests.Session()

        self._base_url = base_url
        self._base_data = { 'reqType': 0,
                            'userInfo': {
                                'apiKey': api_key,
                                'userId': user_id
                                },
                            'perception': {
                                'inputText': {
                                    'text': ''
                                    }
                                }
                            }


    def command1(self, input_sentence):
        data = self._base_data
        data['perception']['inputText']['text'] = input_sentence

        r = self._session.post(url=self._base_url, json = data)
        output = r.json()
        # print(output)

        ouput_sentence = ['node','url']
        for result in output['results']:
            if result['resultType']=='text':
                ouput_sentence[0] = result['values']['text']
                # print('@@@',ouput_sentence[0])
                continue
            if result['resultType']=='url':
                ouput_sentence[1] = '相关酒店信息：' + result['values']['url']
                continue

        return(ouput_sentence)

    def command(self, input_sentence):
        data = self._base_data
        data['perception']['inputText']['text'] = input_sentence

        r = self._session.post(url=self._base_url, json = data)
        output = r.json()

        ouput_sentence = []
        for result in output['results']:
            if result['resultType']=='text':
                ouput_sentence = result['values']['text']
                break

        return(ouput_sentence)

    def report(self, input_sentence):
        data = self._base_data
        data['perception']['inputText']['text'] = input_sentence

        r = self._session.post(url=self._base_url, json = data)
        output = r.json()
        # print('@@@',output)

        ouput_sentence = ['title','content','url']
        list_news = []
        content_list = []
        content_str = [' ']
        for result in output['results']:
            if result['resultType'] == 'text':
                # ouput_sentence[2] 列表第1个元素
                ouput_sentence[0] = result['values']['text']
                # print('text@@@', ouput_sentence[0])
                # continue
            if result['resultType'] == 'news':
                # ouput_sentence[2] 列表第1个元素，选择前几条新闻
                for i in result['values']['news'][0:3]:
                    list_news.append(i)
                for i in list_news:
                    content_list.append(i['info'])
                    content_list.append(i['name'])
                for i in content_list:
                    content_str[0] += i
                    content_str[0] += '  '
                ouput_sentence[1] = content_str[0]
                # print(ouput_sentence[1])

                # ouput_sentence[2] 列表第3个元素
                ouput_sentence[2] = list_news[0]['name'] + list_news[0]['detailurl']
                # print(ouput_sentence[2])
                continue

        return(ouput_sentence)
