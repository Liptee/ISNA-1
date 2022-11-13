from for_log import *
import vk_api
import json

def getter(group_id):
  """ Функция, которая запишет все посты со стены группы ВК в файл "wall_{groip_id}.csv"""
  vk_session = vk_api.VkApi(login, psswd)
  try:
      vk_session.auth(token_only=True)
  except vk_api.AuthError as error_msg:
      print(error_msg)
      return
  tools = vk_api.VkTools(vk_session)
  wall = tools.get_all('wall.get', 100,
{'owner_id': group_id})
  print('Posts count:', wall['count'])
  with open(r"wall_{}.csv".format(group_id), 'a') as f:
    f.write(str(wall))

  
