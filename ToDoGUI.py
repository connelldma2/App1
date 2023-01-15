
import ToDoFunctions
import PySimpleGUI as gui

label = gui.Text("Enter a module: ")
input_box = gui.InputText(tooltip="Enter a module name.")
add_button = gui.Button("Add Module")

window = gui.Window("Module Repository", layout=[ [label], [input_box, add_button]])

window.read()

window.close()

