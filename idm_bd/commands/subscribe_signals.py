from .. import utils
from ..objects import dp, Event
from vkapi import VkApiResponseException

@dp.event_handle(dp.Methods.SUBSCRIBE_SIGNALS)
def subscribe_signals(event: Event) -> str:
    message = f"""✅ Беседа распознана

        Ирис чат ID: [{event.chat.iris_id}]
        Имя беседы: [{event.chat.name}]

        """.replace("    ", "")

    event.db.chats[event.chat.iris_id]['installed'] = True
    event.db.save()
    utils.new_message(event.api, event.chat.peer_id, message=message)
    return "ok"