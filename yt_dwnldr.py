## Youtube Video Downloader
## By Brer D.
import tkinter
import customtkinter
from pytube import YouTube

## Video Download Function
def startDownload():
    try:
        ytLink = link.get()
        save_path = filedialog.askdirectory(ytLink)
        ytObject = YouTube(ytLink, on_progress_callback=on_progress)
        video = ytObject.streams.filter(progressive=True).get_highest_resolution().last()
        #video = ytObject.streams.filter(progressive=True).last()
        title.configure(text=ytObject.title, text_color="white")
        finishLabel.configure()
        video.download(output_path=str(save_path), filename=ytObject.title)
        finishLabel.configure(text="Downloaded!")
    except:
        finishLabel.configure(text="Youtube link is invalid", text_color="red")


## Progress Bar Function
def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize()
    bytes_downloaded = total_size - bytes_remaining
    per_of_com = bytes_downloaded / total_size * 100
    per = str(int(per_of_com))
    proBar.configure(text= per + '%')
    proBar.update()

    ## Update progress Bar
    proBar.set(float(per_of_com) / 100 )


## System Settings
customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("blue")

## Application Frame
app = customtkinter.CTk()
app.geometry("500x200")
app.title("Youtube Downloader by Brer D.")
app.minsize(250,100)
app.maxsize(2000,800)

## Adding UI Elements
title = customtkinter.CTkLabel(app,text="Insert Youtube Link Here")
title.pack(padx=10,pady=10)

## Link Input
url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=400, height=40, textvariable=url_var)
link.pack()

## Finished Download
finishLabel = customtkinter.CTkLabel(app, text="")
finishLabel.pack()

## Progress Percentage
pPer = customtkinter.CTkLabel(app, text="0%")
pPer.pack()

proBar = customtkinter.CTkProgressBar(app, width=400, height=25)
proBar.set(0)
proBar.pack()

## Download Button
download = customtkinter.CTkButton(app, text="Download", command=startDownload)
download.pack(padx=10, pady=5)

## Run Application
app.mainloop()
