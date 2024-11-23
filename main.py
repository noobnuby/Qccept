import pystray
from PIL import Image
from lcu_driver import Connector
import sys, os
import threading


def resource_path(relative_path):
    """Get absolute path to resource, works for dev and for PyInstaller"""
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

def exit_program():
    icon.stop()
    connector.stop()
    sys.exit()

connector = Connector()

@connector.ready
async def connect(connection):
    print("LCU API is ready to be used.")


@connector.close
async def disconnect(connection):
    print("The client was closed")

@connector.ws.register("/lol-matchmaking/v1/ready-check", event_types=("UPDATE",))
async def icon_changed(connection, event):
    await connection.request("post", "/lol-matchmaking/v1/ready-check/accept")
    print(f"{event.data}")


def start_connector():
    connector.start()

threading.Thread(target=start_connector, daemon=True).start()

icon = pystray.Icon(
    "Qccept",
    icon=Image.open(resource_path("icon.ico")),
    title="Qccept",
    menu=pystray.Menu(pystray.MenuItem("종료", exit_program)),
)

icon.run()
