import json, datetime
from time import mktime


menu = \
{
"breakfast": {
    "hours": "7-11",
    "items": {
        "breakfast burritos": "$6.00",
        "pancakes": "$4.00"
        }
    },
"lunch" : {
    "hours": "11-3",
    "items": {
        "hamburger": "$5.00"
        }
    },
"dinner": {
    "hours": "3-10",
    "items": {
        "spaghetti": "$8.00"
        }
    }
}


menu_json = json.dumps(menu)
menu_json
menu2 = json.loads(menu_json)
menu2

now = datetime.datetime.utcnow()
now_str = str(now)
json.dumps(now_str)

now_epoch = int(mktime(now.timetuple()))
json.dumps(now_epoch)

class DTEncoder(json.JSONEncoder):
    def default(self, o):
        # isinstance() checks the type of obj
        if isinstance(o, datetime.datetime):
            return int(mktime(o.timetuple()))
        #else it's something the normal decoder knows:
        return json.JSONEncoder.default(self, o)

json.dumps(now, cls=DTEncoder)
json.dumps(now, default=str)