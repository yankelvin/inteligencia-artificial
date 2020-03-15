# coding=utf8

# Import dos pacotes necessários do Twython
from twython import TwythonStreamer
from twython import Twython

# Import métodos para tratar a data
from datetime import datetime
import pytz

import pickle
from pprint import pprint

# Lê os arquivos e desserializa
tweets = pickle.load(
    open('tweets.pkl', 'rb'))


class MyStreamer(TwythonStreamer):
    def on_success(self, data):
        # Id do twitter
        object_id = data['id']

        # Id do usuário que postou o texto
        user_id = data['user']['id']

        # Usuário que postou o texto
        user_name = data['user']['screen_name']

        # Texto postado em utf-8
        text = data['text'].encode('utf-8')

        # Data que foi publicado
        posted_at_tweet = data['created_at']

        # Data que foi publicado formatada
        fmt = '%Y-%m-%d %H:%M:%S.%f'
        new_date = datetime.strptime(
            posted_at_tweet, '%a %b %d %H:%M:%S +0000 %Y').replace(tzinfo=pytz.UTC)

        published_date = str(new_date.strftime(fmt))

        tweet = {
            'object_id': object_id,
            'user_id': user_id,
            'user_name': user_name,
            'text': text,
            'published_date': published_date,
            'create_date': published_date,
            'last_update': published_date,
        }

        tweets.append(tweet)

        # Grava os arquivos serializados
        pickle.dump(tweets, open('tweets.pkl', 'wb'))

        pprint(tweet)

    def on_error(self, status_code, data):
        print(status_code)

        self.disconnect()


# Definição das chaves da API do Twitter
consumer_key = "atmarKZPN23ATHFLIqZH9Ezfi"
consumer_secret = "S72tbc7WfZN1NffCQxbepeqIWhCmxA6vTR1fENsFqPw9616Txu"
access_token = "3968788457-ZNc77eDdGp8gTlSJzXGpSPCI4ajXwpK3SSg4gw4"
access_token_secret = "gvzMDnf7qKrBIxau6pWB78NWBGouB4zBtfpt8kle4q8UW"


# E criamos nossa instância do coletor
stream = MyStreamer(consumer_key, consumer_secret,
                    access_token, access_token_secret)

stream = MyStreamer(consumer_key, consumer_secret,
                    access_token, access_token_secret)

stream.statuses.filter(
    track="#coronavirusnobrasil, #coronavirusbrasil, #covid19brasil", languages=['pt-br'])
