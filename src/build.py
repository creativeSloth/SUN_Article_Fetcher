import os

from qtpy import uic

current_script_path = os.path.abspath(os.path.dirname(__file__))
uic.compileUiDir(current_script_path + "/ui/windows")
print("DONE!")
