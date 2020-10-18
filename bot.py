import vk_api
from vk_api.utils import get_random_id
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import random
import datetime
import pymysql
import dateparser
import pars

vk_session = vk_api.VkApi(token="d0dca2ad6c98fd2cea75c4e9dc844d44a1b44a55040593a6a1d0e80ab1ce639a7ab1d4b04e32269c50ee2")
vk = vk_session.get_api()
longpoll = VkBotLongPoll(vk_session, group_id=199535050)
letter = open('config/letter.txt','r',encoding='UTF-8')
help = open('config/help.txt', 'r', encoding='UTF-8')

def get_connection():

    connection = pymysql.connect(host='localhost',
                                 user='root',
                                 password='qy.pr.wppw',
                                 db='vk_hack',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)

    return connection
connection = get_connection()


def get_button(mode):

    if mode == 0:

        return 'keyboard/button_assist.json'

    if mode == 1:

        return 'keyboard/answer'

    else:

        return 'keyboard/default.json'


def get_date(msg):

    date = dateparser.parse(msg)
    if (date != None):

        diff = str(date-datetime.datetime.now())
        #t = int(diff.split()[0])
        #if t < 0:
            #date = date + datetime.timedelta(days = abs(t))
        return date

    else :

        return None


# send message to user_id in vk with button mode
def vk_send(user_id, message, mode):

   # keyboard = get_button(mode)

    if message == ' ':

        vk.messages.send(peer_id=user_id,
                         random_id=get_random_id())#keyboard=keyboard)

    else:

        vk.messages.send(peer_id=user_id,
                         message=message,
                         random_id=get_random_id())#,keyboard=keyboard)

while True:

    for event in longpoll.listen():

        if event.type == VkBotEventType.GROUP_JOIN:

            user_id = event.obj.user_id
            vk_send(user_id, letter.read(), 0)

        if event.type == VkBotEventType.MESSAGE_NEW:

            if event.from_user:

                user_id = event.object.message['peer_id']
                message = event.message['text']

                if message.lower() == 'помощь':

                    vk_send(user_id, help.read(), 0)

                else:

                    date = get_date(message)

                    if (date == None) :

                        vk_send(user_id,"Я получил не корректную дату! "
                                        "Если возникли вопросы с форматом, напиши 'помощь'",0)
                        continue

                    bdate, groups_name, interesting = pars.user_anal(user_id)

                    if (bdate) :

                        year = bdate.split('.')[2]
                        age = datetime.datetime.now().year - int(year)

                    else:
                        age = 100

                    cursor = connection.cursor()
                    sql = "SELECT name, description, content, tags,mean_price,start_time, place from name where Agerestr" \
                          " <= %s and start_time BETWEEN %s and %s" # добавить текущую дату
                    cursor.execute(sql, (age, date, date + datetime.timedelta(days=1)))

                    t = 0
                    for row in cursor:

                        if (t < 3):

                            vk_send(user_id, 'Название мероприятия: ' + row['name'] +
                                    '\n\n' + 'Описание мероприятия: ' + row['description'] +
                                    '\n\n' +  row['content'] + '\n_________________________________________\n'+
                                    '\n\n' + 'Минимальная стоимость билета: ' + str(row['mean_price']) + " руб."+
                                    '\n\n' + 'Время начала мероприятия: ' + str(row['start_time']) +
                                    '\n\n' + 'Место проведения: ' + row['place'], 0)
                            t += 1

                        else:

                            break

                    cursor.close()