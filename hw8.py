from collections import defaultdict
from datetime import datetime, timedelta

def read_users(path):
    user_info = []
    str_l = ''
    with open(path, 'r') as fh:
        while True:
            line = fh.readline()
            if not line:
                break
            str_l = line.split(',')
            user_info.append(dict({'name': str_l[0],'birthday':str_l[1].strip()}))
    return user_info 

def get_birthdays_per_week(dct):
    
    user_dict = defaultdict(list)    
    current_datetime = datetime.today()
    s_w = current_datetime + timedelta(days = 7 - current_datetime.weekday())
    s_p = s_w - timedelta(2)
    e_p = s_w + timedelta(4)
    
    user_date = None
    
    for lst in dct:
        ss = lst['birthday'].split('-')
        user_date = datetime(year = current_datetime.year, month = int(ss[1]), day = int(ss[2]))

        if s_p <= user_date <= e_p:
            if user_date.weekday() in (5,6):
                user_dict['Monday:'].append(lst['name'])
            else:
                user_dict[user_date.strftime('%A:')].append(lst['name'])

    for k,v in user_dict.items():          
         print(k, ', '.join(filter(lambda s: s, v)))
        
        
get_birthdays_per_week(read_users('users.txt'))