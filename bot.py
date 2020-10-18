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


def get_button(mode):

    if mode == 0:

        return 'keyboard/button_assist.json'

    else:

        return 'keyboard/default.json'


def get_date(msg):

    date = dateparser.parse(msg)
    diff = str(date-datetime.datetime.now())
    t = int(diff.split()[0])
    if t < 0:
        date = date + datetime.timedelta(days = abs(t))
    return date

# send message to user_id in vk with button mode
def vk_send(user_id, message, mode):

    #keyboard = get_button(mode)

    if message == ' ':

        vk.messages.send(peer_id=user_id,
                         random_id=get_random_id())

    else:

        vk.messages.send(peer_id=user_id,
                         message=message,
                         random_id=get_random_id())

while True:

    for event in longpoll.listen():

        if event.type == VkBotEventType.MESSAGE_NEW:

            if event.from_user:

                user_id = event.object.message['peer_id']
                message = event.message['text']

                if message.lower() == "привет":

                    vk_send(user_id, "Привет!", 0)

                else:

                    date = get_date(message)

                    bdate, groups_name, interesting = pars.user_anal(user_id)

                    print(bdate)
                    if (bdate) :
                        age = (datetime.datetime.now() - datetime.datetime.strptime(bdate,"")).total_seconds()/3600/24/365

                    else:
                        age = 100

                    print(age)

                    sql = "SELECT * from name where Agerestr <= %s"

                    
