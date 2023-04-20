import requests
import time
from pprint import pprint

API_URL: str = ' https://api.thecatapi.com/v1/images/search'
BOT_TOKEN: str = '6231595283:AAFg23Zeg8gHZbRRjNt1zgmJBI7RLZDXs0U'
TEXT: str = 'Я звоню маме!'
MAX_COUNTER: int = 200

offset: int = -2
counter: int = 0
chat_id: int
text: str
if __name__ == '__main__':
    while counter < MAX_COUNTER:

        print('attempt =', counter)  # Чтобы видеть в консоли, что код живет

        updates = requests.get(f'{API_URL}{BOT_TOKEN}/getUpdates?').json()
        updates1 = requests.get(f'{API_URL}{BOT_TOKEN}/getUpdates?offset={offset + 1}').json()

        #if updates['result']:
            #for result in updates['result']:
                #offset = result['update_id']
                #chat_id = result['message']['from']['id']
                #requests.get(f'{API_URL}{BOT_TOKEN}/sendMessage?chat_id={chat_id}&text={TEXT}')

        time.sleep(1)
        counter += 1
        pprint(updates)
        print()
        pprint(updates1)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
