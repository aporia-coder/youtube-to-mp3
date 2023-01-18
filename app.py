import os
from tkinter import *
from tkinter import messagebox, filedialog
from pytube import YouTube

app = Tk()
app.geometry('520x280')
app.resizable(False, False)
app.title('Youtube to mp3')
app.config(background="PaleGreen1")

download_path = StringVar()
video_link = StringVar()

def init_gui():
    head_label = Label(app, text="YouTube to mp3",
                       padx=15,
                       pady=15,
                       font="SegoeUI 14",
                       bg="palegreen1",
                       fg="red")
    head_label.grid(row=1,
                    column=1,
                    pady=10,
                    padx=5,
                    columnspan=3)
 
    link_label = Label(app,
                       text="YouTube link :",
                       bg="salmon",
                       pady=5,
                       padx=5)
    link_label.grid(row=2,
                    column=0,
                    pady=5,
                    padx=5)
 
    app.linkText = Entry(app,
                          width=35,
                          textvariable=video_link,
                          font="Arial 14")
    app.linkText.grid(row=2,
                       column=1,
                       pady=5,
                       padx=5,
                       columnspan=2)
 
 
    destination_label = Label(app,
                              text="Destination :",
                              bg="salmon",
                              pady=5,
                              padx=9)
    destination_label.grid(row=3,
                           column=0,
                           pady=5,
                           padx=5)
 
 
    app.destinationText = Entry(app,
                                 width=27,
                                 textvariable=download_path,
                                 font="Arial 14")
    app.destinationText.grid(row=3,
                              column=1,
                              pady=5,
                              padx=5)
 
 
    browse_B = Button(app,
                      text="Browse",
                      command=select_dir,
                      width=10,
                      bg="bisque",
                      relief=GROOVE)
    browse_B.grid(row=3,
                  column=2,
                  pady=1,
                  padx=1)
 
    Download_B = Button(app,
                        text="Download Video",
                        command=download,
                        width=20,
                        bg="thistle1",
                        pady=10,
                        padx=15,
                        relief=GROOVE,
                        font="Georgia, 13")
    Download_B.grid(row=4,
                    column=1,
                    pady=20,
                    padx=20)


def select_dir():
    download_dir = filedialog.askdirectory(title="Save mp3")
    download_path.set(download_dir)

def download():
    youtube_link = video_link.get()
    download_folder = download_path.get()
    getVideo = YouTube(youtube_link)
    video_audio = getVideo.streams.filter(only_audio=True).first()
    out_file = video_audio.download(download_folder)
    base, ext = os.path.splitext(out_file)
    mp3_file = base + '.mp3'

    os.rename(out_file, mp3_file)

    messagebox.showinfo('SUCCESS', 'Successfully downloaded and saved in\n' + download_folder)

init_gui()
app.mainloop()