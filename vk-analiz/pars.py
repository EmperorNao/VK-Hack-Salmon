import vk_api
from googletrans import Translator


def trans(en_word):
    translator = Translator()
    word = (translator.translate(en_word, dest='ru')).text
    return word


def user_anal(user_id):
    login = '+79185197432'
    password = 'qy.pr.wppw'

    vk = vk_api.VkApi(login,password,token='')
    vk.auth()
    vk = vk.get_api()
    user_ids = user_id
    user_info = vk.users.get(user_id=user_ids,fields = ['bdata','quotes'])
    print(user_info)






    user_groups = vk.groups.get(user_id=user_ids,extended = 1, fields = 'description' )

    groups_bufer = user_groups['items']
    x=0
    groups_name = []
    for i in groups_bufer:
        word = str(i['name'])
        if word[0]<='z' and word[0]>='A':
            word = trans(word)
        groups_name.append(word)
        if x<25:
            x+=1
        else:
            break
    x = 0
    groups_description = []
    for i in groups_bufer:
        groups_description.append(i['description'])
        if x<25:
            x+=1
        else:
            break
    return groups_name,groups_description

print(user_anal(216824408))
