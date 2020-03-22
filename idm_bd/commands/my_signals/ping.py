from ...objects import dp, MySignalEvent
from ...utils import new_message
from datetime import datetime

@dp.my_signal_event_handle('пинг', 'кыш', 'кинг', 'пиу', 'вадим', 'соня')
def ping(event: MySignalEvent) -> str:

    c_time = datetime.now().timestamp()
    delta = round(c_time - event.msg['date'], 2)

    c_time_str = str(datetime.fromtimestamp(round(c_time)))
    v_time_str = str(datetime.fromtimestamp(round(event.msg['date'])))

    r_type = '\nPONG!' if event.command == "пинг" else "\nМЫШЬ!" if event.command == "кыш" else "\nКОНГ" if event.command == "кинг" else "\nГЕЙ!" if event.command == "вадим" else "\nТРАП!" if event.command == "соня" else "ПАУ!!"


    if delta > 23:r_type += "\n\nНам пиздец."
    elif delta > 15:r_type += "\n\nСильно тормозит."
    elif delta > 10:r_type += "\n\nПодтормаживает."
    elif delta > 5:r_type += "\n\nНачинает чутка подтормаживать."
    else:r_type += "\n\nРаботает вполне стабильно."

    message = f"""{r_type}

    Ответ через: {delta} с.

    Time: {c_time_str}
    """.replace('    ', '')
    new_message(event.api, event.chat.peer_id, message=message)

    return "ok"