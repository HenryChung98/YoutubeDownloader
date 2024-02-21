from pytube import YouTube
from tkinter import *
from tkinter.messagebox import *
from tkinter import ttk

class MyGUI:

    def __init__(self):
        self.mainWindow = Tk()
        self.mainWindow.geometry(f"250x300+700+200")
        self.frame1 = Frame(self.mainWindow, width=480, height=480)
        self.frame1.place(x=10, y=10)
        
        self.urlLabel = Label(self.frame1, text="URL", font=14)
        self.urlLabel.place(x=10, y=10)
        self.url = Entry(self.frame1)
        self.url.place(x=10, y=30)
        
        self.streams = ["video/mp4, res=360p", "video/mp4, res=720p", "audio/mp4, abr=48kbps",
                   "audio/mp4, abr=128kbps", "audio/webm, abr=50kbps", "audio/webm, abr=70kbps",
                   "audio/webm, abr=160kbps",]
        self.stream_box = ttk.Combobox(self.frame1, values=self.streams, width=17, state="readonly")
        self.stream_box.set("video/mp4, res=360p")
        self.stream_box.place(x=10, y=150)
       
        
        self.titleLabel = Label(self.frame1, text="Title(optional)", font=14)
        self.titleLabel.place(x=10, y=80)
        self.title = Entry(self.frame1)
        self.title.place(x=10, y=100)
        
        self.downBtn = Button(self.frame1, text="Download", font=14, command=self.do_this)
        self.downBtn.place(x=10, y=200)
        
    def do_this(self):
        itag_map = {
            "video/mp4, res=360p": 18,
            "video/mp4, res=720p": 22,
            "audio/mp4, abr=48kbps": 139,
            "audio/mp4, abr=128kbps": 140,
            "audio/webm, abr=50kbps": 249,
            "audio/webm, abr=70kbps": 250,
            "audio/webm, abr=160kbps": 251
            }
        try:
            get_url = self.url.get()
            get_title = self.title.get()
            get_selected_stream = self.stream_box.get()
            yt = YouTube(get_url)
            
        except:
            showerror("Error", "Invalid URL")
            
        else:
            itag = itag_map.get(get_selected_stream) 
            
            # if title is set, use the title
            if get_title:
                yt.title = get_title
                
            if itag is not None:
                stream = yt.streams.get_by_itag(itag)
                
                # slice after a = to get selected stream quality
                split_stream_elements = get_selected_stream.split("=")
                
                # check whether it is video or audio using slice
                selected_type = split_stream_elements[0][:5]
                selected_qual = split_stream_elements[1]
                
                stream.download()
                showinfo("Result", f"{selected_type}({selected_qual}) was successfully download")
    
        mainloop()
        
my_gui = MyGUI()

