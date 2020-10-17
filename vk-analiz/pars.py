import vk_api

login = '+79185197432'
password = 'qy.pr.wppw'

vk = vk_api.VkApi(login,password,token='')
vk_session = vk.auth()
vk = vk.get_api()
user_ids = 584194604
user_info =vk.users.get(user_ids=user_ids)

print(user_info)

Dick_dict = dict()

##user_subscribe = vk.users.getSubscriptions(user_ids=user_ids)
#print((user_subscribe))
#array_keys = user_subscribe['groups']
#array_keys = array_keys['items']
#print(array_keys)


user_groups = vk.groups.get(user_id=user_ids,extended = 1, fields = ['name','description'] )


print(user_groups)

x = user_groups['items']
for i in x:
    print('Название:',i['name'],'\n','Описание',i['description'])
    print('_______________')




#for i in array_keys:
#    tag_list = vk.groups.getByld(groups_id=1,fields ='name')
#    print(tag_list)


#for i in range(len(array_keys)):
 #   otsos_group(array_keys[i])