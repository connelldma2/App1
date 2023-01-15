
import PySimpleGUI as gui

label1 = gui.Text("Select file(s) to compress: ")
input_box1 = gui.InputText(tooltip="Chosen file paths are displayed here.")
select_button1 = gui.FilesBrowse("Choose")

label2 = gui.Text("Select destination folder: ")
input_box2 = gui.InputText(tooltip="Chosen file paths are displayed here.")
select_button2 = gui.FolderBrowse("File Destination")

compress_button = gui.Button("Compress")

window = gui.Window("File Compression", layout=[[label1], [input_box1, select_button1],
                                                [label2], [input_box2, select_button2],
                                                [compress_button]
                                                ])

window.read()

window.close()
