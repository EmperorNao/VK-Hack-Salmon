import json
import re
from datetime import datetime
path = '/Users/Mr_Ocean_Man/Downloads/Хакатон/events.txt'
data = open(path,'r')
f = open('for_vladuk.txt','w')
s = 0
for i in data:
    tags = []
    s+=1
    data_json = json.loads(i)
    name = data_json.get('name')
    age_restriction = data_json.get('ageRestriction')
    category = data_json.get('category').get('name')
    description = data_json.get('description')
    text = re.sub('[^а-яА-Я0-9 ]','',(data_json.get('content')[0]).get('text'))
    for j in data_json.get('tags'):
        tags.append(j.get('name'))
    is_free = data_json.get('isFree')


    try:
        place = data_json.get('schedules')[0].get('venue').get('place').get('name')
        start_time = datetime.fromtimestamp((data_json.get("schedules")[0]).get('start')/1000)
        end_time = datetime.fromtimestamp((data_json.get("schedules")[0]).get('end')/1000)
        min_price = (data_json.get("schedules")[0]).get('ticketsInfo').get('minPrice')
        max_price = (data_json.get("schedules")[0]).get('ticketsInfo').get('maxPrice')
    except:
        pass

