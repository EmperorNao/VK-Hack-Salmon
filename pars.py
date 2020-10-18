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
    user_info = vk.users.get(user_ids = user_ids , extended = 1,fields = ['bdate','quotes'])
    user_info = user_info[0]

    

    try: user_bdate = user_info['bdate']
    except: user_bdate = 0

    try: user_quotes = user_info['quotes']
    except: user_quotes = 0

    user_groups = vk.groups.get(user_id=user_ids,extended = 1, fields = 'description' )

    groups_bufer = user_groups['items']
    x=0
    groups_name = []
    try:
        for i in groups_bufer:
            word = str(i['name'])
            if word[0]<='z' and word[0]>='A':
                word = trans(word)
            groups_name.append(word)
            if x<25:
                x+=1
            else:
                break
    except: groups_name = 0

    x = 0
    groups_description = []
    try:
        for i in groups_bufer:
            groups_description.append(i['description'])
            if x<25:
                x+=1
            else:
                break
    except: groups_description = 0


    return user_bdate,groups_name,groups_description,user_quotes