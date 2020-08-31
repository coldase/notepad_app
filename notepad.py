#Notepad 2.0
from tkinter import *
from tkinter.filedialog import asksaveasfile

def save_to_file(text):
    with open("file.txt", "w") as file:
        file = asksaveasfile()
        file.write(text)
        print("File Saved")
   
def main():
    def get_from_text_entry():
        data = new_entry.get("1.0", END)
        save_to_file(data)
    root = Tk()
    root.geometry("300x400")
    root.title("Notepad 2.0")

    header = Label(root, text="Notepad 2.0")
    new_entry = Text(root, height=20, width=33)
    make_file_btn = Button(root, text="Save", command=get_from_text_entry)

    header.pack(pady=2)
    new_entry.pack(pady=5)
    make_file_btn.pack(pady=5)
    mainloop()

if __name__ == "__main__":
    main()