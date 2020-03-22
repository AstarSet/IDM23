from ...objects import dp, MySignalEvent, SignalEvent
from ...utils import edit_message, new_message
from datetime import datetime
from idm import __version__
import typing
import threading

@dp.my_signal_event_handle('инфо', 'инфа', '-i', 'info')
def info(event: typing.Union[MySignalEvent, SignalEvent]) -> str:

    owner = event.api('users.get', user_ids=event.db.owner_id)[0]


    message = f"""============ИНФО============

    Владеет Дежурным: [id{owner['id']}|{owner['first_name']} {owner['last_name']}]🥵
    Кол-во чатов:[{len(event.db.chats.keys())}]
    Ирис чат ID: [{event.chat.iris_id}]
    Имя беседы: [{event.chat.name}]

    =======ВЕЧНЫЙ ОНЛАЙН=======
           Выключен
    ==============================


    """.replace('  ', ' ')

    edit_message(event.api, event.chat.peer_id, event.msg['id'],  message=message)
    return "ok"