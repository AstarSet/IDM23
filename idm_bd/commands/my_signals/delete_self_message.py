from ...objects import dp, MySignalEvent
from ... import utils
from datetime import datetime
from vkapi import VkApi, VkApiResponseException

from threading import Timer

def delete_msg(api: VkApi, msg_id: int):
    api("messages.delete", message_ids=msg_id, delete_for_all=1)


@dp.my_signal_event_handle('д')

def delete_self_message(event: MySignalEvent) -> str:
    message_id = event.msg['id']
    utils.edit_message(event.api, event.chat.peer_id, message_id, message="Исчезаю..")

    user_id = event.msg['from_id']
    msg_ids = []
    for mmsg in utils.get_all_history_gen(event.api, event.chat.peer_id):
        if datetime.now().timestamp() - mmsg['date'] > 300:
            break
        if mmsg['from_id'] == user_id and mmsg.get('action', None) == None:
            msg_ids.append(str(mmsg['id']))
    message_id = 0
    try:
        event.api("messages.delete", message_ids=",".join(msg_ids), delete_for_all=1)
        message_id = utils.new_message(event.api, event.chat.peer_id, message="✅ Сообщения за 5 минут удалены")
    except VkApiResponseException as e:
        if e.error_code == 924:
            message_id = utils.new_message(event.api, event.chat.peer_id, message="✅ Сообщения за 5 минут удалены")
        else:
            message_id = utils.new_message(event.api, event.chat.peer_id, message=f"❗  удалось удалить сообщения. Ошибка VK {e.error_msg}")
    except:
        message_id = utils.new_message(event.api, event.chat.peer_id, message=f"❗ Произошла неизвестная ошибка.")


    t = Timer(2, delete_msg, (event.api, message_id))
    t.start()
    return "ok"