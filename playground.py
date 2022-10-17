import json
from tkinter import messagebox

data = {
    "Twitter": {
        "Email": "whatevere@gmail.com",
        "password": "vnergn@43rcsod",
    }
}

search = input("Enter the search parameter: ")
try:
    with open("test.json","r") as data_file:
        file_data = json.load(data_file)
        #print(type(data))

        if search in file_data:
            print(file_data[search]["Email"])
except FileNotFoundError:
    messagebox.showerror("Whoops", "Damn,No file found")

    with open("test.json", "w") as file:
        json.dump(data,file,indent=4)

else:
    file_data.update(data)

