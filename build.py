from qtpy import uic
import os
current_script_path = os.path.abspath(os.path.dirname(__file__))
uic.compileUiDir(current_script_path+"/ui")
print("DONE!")
