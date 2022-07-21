from datetime import datetime


def log(msg: str, pnt: bool):
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    DebgMsg = f'[{dt_string}] {msg}'
    if pnt:
        print(DebgMsg)
        return
    else:
        return DebgMsg
