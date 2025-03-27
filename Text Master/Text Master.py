from tkinter import*;
from tkinter.messagebox import askokcancel, WARNING;
from os import path, chdir;

window = Tk();
window.title("Potenad");
window.attributes("-fullscreen", False);
window.config(bg="black");
window.state("zoomed");

# Variables

currentFileName = "";
currentPath = "C:\\";
chdir("C:\\");

isFullscreen = False

### FUNCTIONs ;)

def quitPotenad(event):
    print(f"Events called [For debug only.]>> {event}");    

    askToClose = askokcancel(
            title="Have you saved?",
            message="Please do make sure that you have saved your progress or else...",
            icon=WARNING
        );

    if askToClose:
        window.quit();

def makeNewFile():
    global currentFileName, message;

    newName = NewFName.get();
    if path.exists(newName):
        err = Label(newFileWindow, font=("Consolas", 8), fg="white", bg="black", text="File exists.");
        err.place(x=10, y=64);
    else:
        open(newName, "w");

        currentFileName = newName;

        message.config(text=f"Currently opened file: {newName}");

    newFileWindow.destroy();

def makeNewFileWindow(event):
    print(f"Events called [For debug only.]>> {event}");

    global newFileWindow, NewFName;

    newFileWindow = Tk();

    newFileWindow.title("New../");
    newFileWindow.geometry("400x200");
    newFileWindow.config(bg="black");

    label = Label(newFileWindow, font=("Consolas", 8), fg="white", bg="black", text="Enter filename:");
    label.place(x=10, y=10);

    NewFName = Entry(newFileWindow, bg="gray", fg="white", font=("Consolas", 8), insertbackground="lightblue");
    NewFName.place(x=10, y=26);

    button = Button(newFileWindow, text="Confirm filename", font=("Consolas", 8), command=makeNewFile);
    button.place(x=10, y=46);


def commandlist(event):
    global isFullscreen;

    if event.keysym == "Escape":
        quitPotenad("Escape");
    elif event.keysym == "F11":
        if isFullscreen == False:
            window.attributes("-fullscreen", True);
            isFullscreen = True;
        else:
            window.attributes("-fullscreen", False);
            isFullscreen = False;


def changeDir():
    global currentPath, showCurrentPath;
    
    try:
        newPath = pathName.get();
        chdir(newPath);
        currentPath = newPath;

        showCurrentPath.config(text=f"Current path: {currentPath}");

        changeDirWindow.destroy();
    except Exception as e:
        err = Label(changeDirWindow, font=("Consolas", 8), fg="white", bg="black", text=f":/ There was an error changing the folder.\nErrorCode_:{e}");
        err.place(x=10, y=64);
    return;

def makeChangeDirWindow(event):
    print(f"Events called [For debug only.]>> {event}");

    global pathName, changeDirWindow;

    changeDirWindow = Tk();
    changeDirWindow.title("Changing folder../");
    changeDirWindow.geometry("400x200");
    changeDirWindow.config(bg="black");

    label = Label(changeDirWindow, font=("Consolas", 8), fg="white", bg="black", text="Enter folder path:");
    label.place(x=10, y=10);

    pathName = Entry(changeDirWindow, bg="gray", fg="white", font=("Consolas", 8), insertbackground="lightblue");
    pathName.place(x=10, y=26);

    button = Button(changeDirWindow, text="Confirm filename", font=("Consolas", 8), command=changeDir);
    button.place(x=10, y=46);


def save():
    global currentFileName;

    newfile = open(SaveFName.get(), "w");
    currentFileName = SaveFName.get();

    newfile.write(textbox.get("1.0", END));

    saveWindow.destroy();

def makeSaveWindow(event):
    print(f"Events called [For debug only.]>> {event}");

    global currentFileName;
    if currentFileName == "":
        global SaveFName, saveWindow;

        saveWindow = Tk();
        saveWindow.title("Save../");
        saveWindow.geometry("400x200");
        saveWindow.config(bg="black");

        label = Label(saveWindow, font=("Consolas", 8), fg="white", bg="black", text="Enter filename (enter existing filename to continue editing):");
        label.place(x=10, y=10);

        SaveFName = Entry(saveWindow, bg="gray", fg="white", font=("Consolas", 8), insertbackground="lightblue");
        SaveFName.place(x=10, y=26);

        button = Button(saveWindow, text="Confirm filename", font=("Consolas", 8), command=save);
        button.place(x=10, y=46);
    else:
        newfile = open(currentFileName, "w");
        newfile.write(textbox.get("1.0", END));

def load():
    global currentFileName;

    if path.exists(LoadFName.get()):
        filepath = open(LoadFName.get(), "r");
        filedata = filepath.read();
        textbox.delete("1.0", END);
        textbox.insert("1.0", filedata);
        currentFileName = LoadFName.get();

        loadWindow.destroy();
    else:
        err = Label(loadWindow, font=("Consolas", 8), fg="white", bg="black", text=f":/ File doesn't exist.");
        err.place(x=10, y=64);

def makeLoadWindow(event):
    print(f"Events called [For debug only.]>> {event}");

    global LoadFName, loadWindow;

    loadWindow = Tk();
    loadWindow.title("Load../");
    loadWindow.geometry("400x200");
    loadWindow.config(bg="black");

    label = Label(loadWindow, font=("Consolas", 8), fg="white", bg="black", text="Enter filename:");
    label.place(x=10, y=10);

    LoadFName = Entry(loadWindow, bg="gray", fg="white", font=("Consolas", 8), insertbackground="lightblue");
    LoadFName.place(x=10, y=26);

    button = Button(loadWindow, text="Confirm filename", font=("Consolas", 8), command=load);
    button.place(x=10, y=46);

    loadWindow.mainloop();

def makeCreditsWindow():
    creditWindow = Tk();
    creditWindow.title("Credits");
    creditWindow.geometry("600x200");
    creditWindow.config(bg="black");

    credittext = """
    Made by DwagonBos for editing text, with Python 3.13.0 and Tkinter. (Yeah.. You can't scroll.)

    -v.1.2-
    """

    label = Label(creditWindow, font=("Consolas", 8), fg="white", bg="black", text=credittext);
    label.place(x=10, y=10);

### Text box code :DD

textbox = Text (
    window,
    bg="black",
    font=("Aptos", 16),
    fg="white",
    insertbackground="lightblue",
    width=1500,
    height=1060,
    bd=4,
    relief=RAISED,
);

textbox.place(x=0, y=106);

### test button (it will go) :( PRESS F TO PAY RESPECT (it didn't.)
newButton = Button (
    window,
    text="New",
    bg="black",
    command=lambda: makeNewFileWindow("button"),
    fg="lightblue",
    activebackground="lightblue",
    activeforeground="black",
    border=0,
    cursor="hand2",
);
newButton.place(x=10, y=36);

saveButton = Button (
    window,
    text="Save", 
    command=lambda: makeSaveWindow("button"), 
    bg="black",
    fg="lightblue",
    activebackground="lightblue",
    activeforeground="black",
    border=0,
    cursor="hand2"
);
saveButton.place(x=54, y=36);

loadButton = Button (
    window,
    text="Load",
    command=lambda: makeLoadWindow("button"),
    border=0,
    fg="lightblue",
    bg="black",
    activebackground="lightblue",
    activeforeground="black",
    cursor="hand2"
)
loadButton.place(x=98, y=36);

changePathButton = Button (
    window,
    text="Change directory",
    border=0,
    fg="lightblue",
    bg="black",
    activebackground="lightblue",
    activeforeground="black",
    command=lambda: makeChangeDirWindow("button"),
    cursor="hand2"
);
changePathButton.place(x=142, y=36);

creditButton = Button (
    window,
    text="Credits",
    command=makeCreditsWindow,
    border=0,
    bg="black",
    fg="lightblue",
    activebackground="lightblue",
    activeforeground="black",
    cursor="hand2"
);
creditButton.place(x=279, y=36);

message = Label(window, font=("Consolas", 8, "italic"), fg="white", bg="black", text="Press F11 to enter fullscreen!");
message.place(x=10, y=10);

showCurrentPath = Label (
    window,
    font=("Consolas", 12),
    fg="white",
    bg="black",
    text=f"Current path: {currentPath}"
);
showCurrentPath.place(x=10, y=66);

# Bindings

window.bind("<Key>", commandlist);

window.bind("<Control-s>", makeSaveWindow);
window.bind("<Control-S>", makeSaveWindow);

window.bind("<Control-l>", makeLoadWindow);
window.bind("<Control-L>", makeLoadWindow);

window.bind("<Control-d>", makeChangeDirWindow);
window.bind("<Control-D>", makeChangeDirWindow);

window.bind("<Control-n>", makeNewFileWindow);
window.bind("<Control-N>", makeNewFileWindow);

# Loop

window.mainloop();