
import PySimpleGUI as gui
from ZIPcreator import make_archive

label1 = gui.Text("Select file(s) to compress: ")
input_box1 = gui.InputText(tooltip="Chosen file paths are displayed here.")
select_button1 = gui.FilesBrowse("Choose", key="SelectFiles")

label2 = gui.Text("Select destination folder: ")
input_box2 = gui.InputText(tooltip="Chosen file paths are displayed here.")
select_button2 = gui.FolderBrowse("File Destination", key="DestinationFolder")

compress_button = gui.Button("Compress")

output_text = gui.Text(" ", key="success_message", text_color="blue")

window = gui.Window("File Compression", layout=[[label1], [input_box1, select_button1],
                                                [label2], [input_box2, select_button2],
                                                [compress_button, output_text]
                                                ])
while True:
    event, values = window.read()
    selected_filepaths = values["SelectFiles"].split(";") # create list of selected files
    destination_folder_path = values["DestinationFolder"]

    if event == "Compress":
        make_archive(selected_filepaths, destination_folder_path)
        window["success_message"].update(value="Compression Successful.")
    elif event == gui.WIN_CLOSED:
        break

window.close()
