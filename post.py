from for_log import *
import vk_api
# При выполнении данного кода на вашей странице в ВК появится пост со словами 'Hello World'

def auth_handler():
    """Функция для двухэтапной аутентификации"""
    key = input("code::: ")
    remember_device = True
    return key, remember_device

def stop_f(items):
    print(items)

def poster(for_post):
    vk_session = vk_api.VkApi(
        login, psswd,
        auth_handler=auth_handler
    )

    try:
        vk_session.auth()
    except vk_api.AuthError as error_msg:
        print(error_msg)

    tools = vk_api.VkTools(vk_session)
    vk_app = vk_session.get_api()
    print(vk_app.wall.post(message=for_post))

if __name__ == "__main__":
    poster("Hello World")