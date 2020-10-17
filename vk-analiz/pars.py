import vk_api

groups_name = list()
groups_description = list()
def user_anal(user_id):
    login = '+79185197432'
    password = 'qy.pr.wppw'

    vk = vk_api.VkApi(login,password,token='')
    vk.auth()
    vk = vk.get_api()
    user_ids = user_id
    user_info =vk.users.get(user_ids=user_ids)
    user_groups = vk.groups.get(user_id=user_ids,extended = 1, fields = 'description' )

    groups_bufer = user_groups['items']

    groups_name = []
    for i in groups_bufer:
        groups_name.append(i['name'])

    groups_description = []
    for i in groups_bufer:
        groups_description.append(i['description'])







user_anal(user_id = 216824408)
print(groups_name)
print(groups_description)