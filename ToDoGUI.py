
import ToDoFunctions
import PySimpleGUI as gui

label = gui.Text("Enter a module: ")
input_box = gui.InputText(tooltip="Enter a module name.", key="Item")
add_button = gui.Button("Add Module")

list_box = gui.Listbox(values=ToDoFunctions.get_file_todos(),
                       key="ListItems",
                       enable_events=True,
                       size=[40,10])

edit_button = gui.Button("Edit")

window = gui.Window("Module Repository",
                    layout=[[label], [input_box, add_button], [list_box, edit_button]],
                    font=("Arial", 20))

while True:
    event, values = window.read()
    print(event)
    print(values)

    if event == "Add Module":
        todos_list = ToDoFunctions.get_file_todos()
        new_todo = values["Item"] + "\n"
        todos_list.append(new_todo)
        ToDoFunctions.write_file_todos(todos_list)
        window["ListItems"].update(values=todos_list)
    elif event == "Edit":
        todo_for_edit = values["ListItems"][0]
        new_todo = values["Item"] + "\n"

        todos_list = ToDoFunctions.get_file_todos()
        index = todos_list.index(todo_for_edit)

        todos_list[index] = new_todo
        ToDoFunctions.write_file_todos(todos_list)
        window["ListItems"].update(values=todos_list)
    elif event == "ListItems":
        window["Item"].update(value=values["ListItems"][0])

    elif event == gui.WIN_CLOSED:
        break

window.close()

