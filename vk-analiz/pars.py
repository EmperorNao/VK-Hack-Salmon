import vk_api

login = '+79185197432'
password = 'qy.pr.wppw'

vk = vk_api.VkApi(login,password,token='')
vk_session = vk.auth()
vk = vk.get_api()
user_ids = 1
user_info =vk.users.get(user_ids=user_ids)

print(user_info)

Dick_dict = dict()