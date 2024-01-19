from typing import Optional
from pydantic import BaseModel
# from datetime import date

class chatsM(BaseModel):
    mas_users: Optional[str] = None
    mas_messages: Optional[str] = None

class usersM(BaseModel):
    f_name:str
    s_name: str
    password: str
    email: str
    avatar: Optional[str] = None

    mas_friends: Optional[str] = None
    mas_chats: Optional[str] = None

class LoginM(BaseModel):
    email: str
    password: str 

# import json
# mas_id_friends = [1, 2, 3, 4, 5]
# mas_id_friends_str = json.dumps(mas_id_friends)
# INSERT INTO users (mas_id_friends) VALUES (?)', (mas_id_friends_str,)

# import json
# SELECT mas_id_friends FROM users WHERE id = ?', (1,)
# result = cursor.fetchone()
# if result:
#   mas_id_friends_str = result[0]
#   mas_id_friends = json.loads(mas_id_friends_str)