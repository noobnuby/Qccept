import pystray
from PIL import Image
from lcu_driver import Connector
import sys, os, webbrowser, subprocess

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

def exit_program():
    icon.stop()
    sys.exit()

icon = pystray.Icon(
    'Qccept',
    icon=Image.open(resource_path("icon.ico")),
    menu=pystray.Menu(
        pystray.MenuItem('종료', exit_program)
    ),
    title='Qccept'
)

icon.run()