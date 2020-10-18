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

        return 'keyboard/start.json'


def get_date(msg):

    return dateparser.parse(msg)

# send message to user_id in vk with button mode
def vk_send(user_id, message, mode):

    # keyboard = get_button(mode)

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

                if message.lower() == "помощь":

                    vk_send(user_id, "ТЫ", -1)

                else:

                    date = get_date(msg)

                    bdate, groups_name, interesting = user_anal(user_id)

                    if (bdate) :
                        age = (datetime.datetime.now() - bdate).total_seconds()/3600/

                    else:
                        age = 100




                    sql = "SELECT * from name where Agerestr <= %s"

                    
