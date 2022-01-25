from tkinter import *
from turtle import width
from tkinter import ttk, filedialog
import os, shutil
from xml.dom.minidom import Document



class Sorting_App:
    def __init__(self, root):
        self.root = root
        self.root.title("Sorting Application | Developed by Nabeel | Webcode")
        self.root.geometry("1440x900+0+0")
        self.root.config(bg="white")
        self.logo_icon=PhotoImage(file="images/folder.png")
        title = Label(self.root, text="Files Sorting Application",padx=10, image = self.logo_icon,compound=LEFT, font = ("Arial", 30), bg="#023548", fg="white", anchor="w").place(x=0, y=0, relwidth=1)


    #====Section1==============
        
        self.var_foldername=StringVar()
        
        lbl_select_folder = Label(self.root,text="Select Folder",font=("Arial", 25, "bold"), bg="white").place(x=70,y=140)
        txt_folder_name=Entry(self.root, textvariable=self.var_foldername, font=("times new roman", 15),state= 'readonly', bg="lightyellow").place(x=300, y=140, height=35, width=600)
        btn_browse=Button(self.root, command=self.browse_function, text="BROWSE", font=("times new roman", 15, "bold"), bg="#262626", fg="white", activebackground="#262626", cursor="hand2",activeforeground="white").place(x=920, y=135, height=45, width=150)
        hr = Label(self.root, bg="lightgrey").place(x=50, y=190, height=2, width=1250)


    #======Section 2=======
    #=====All extensions
        self.image_extensions=["Image Extensions",".png",".jpg"]
        self.audio_extensions=["Audio Extensions",".amr",".mp3"]
        self.video_extensions=["Video Extensions",".mp4",".avi",".mpeg4",".3gp"]
        self.doc_extensions=["Document Extensions",".doc",".xlsx",".ppt",".pptx",".xls",".pdf",".zip",".rar",".csv",".docx",".txt"]

        self.folders={
            'videos':self.video_extensions,
            'audios':self.audio_extensions,
            'images':self.image_extensions,
            'documents':self.doc_extensions,
            }

        lbl_support_ext = Label(self.root,text="Various Supported Extension",font=("Arial", 25, "bold"), bg="white").place(x=70,y=200)
        self.image_box = ttk.Combobox(self.root,values=self.image_extensions, font=("Arial", 15), state='readonly', justify=CENTER)
        self.image_box.place(x=65, y=260, width= 270, height=35)
        self.image_box.current(0)

        self.video_box = ttk.Combobox(self.root,values=self.video_extensions, font=("Arial", 15), state='readonly', justify=CENTER)
        self.video_box.place(x=385, y=260, width= 270, height=35)
        self.video_box.current(0)

        self.audio_box = ttk.Combobox(self.root,values=self.audio_extensions, font=("Arial", 15), state='readonly', justify=CENTER)
        self.audio_box.place(x=705, y=260, width= 270, height=35)
        self.audio_box.current(0)

        self.doc_box = ttk.Combobox(self.root,values=self.doc_extensions, font=("Arial", 15), state='readonly', justify=CENTER)
        self.doc_box.place(x=1025, y=260, width= 270, height=35)
        self.doc_box.current(0)

        #==========Section 3================
        #=========All imageicons============ 
        self.image_icon = PhotoImage(file="images/img.png")
        self.audio_icon = PhotoImage(file="images/audio.png")
        self.video_icon = PhotoImage(file="images/video.png")
        self.document_icon = PhotoImage(file="images/doc.png")
        self.other_icon = PhotoImage(file="images/q.png")

        Frame1=Frame(self.root, bd=2, relief=RIDGE, bg="white")
        Frame1.place(x=65, y=320, width=1230, height=350)
        self.lbl_total_files=Label(Frame1, bd=2, relief=RAISED, text="Total Files : 150",font=("Arial", 25, "bold"), bg="white")
        self.lbl_total_files.place(x=10,y=10)

        self.lbl_total_image=Label(Frame1, bd=2, relief=RAISED, text="Total Images\n250", image=self.image_icon, compound=TOP, font=("times new roman", 20, "bold"), bg="#0875B7", fg="white")
        self.lbl_total_image.place(x=20, y=90, width=200, height=230)

        self.lbl_total_audio=Label(Frame1,  bd=2, relief=RAISED, text="Total audio\n250", image=self.audio_icon, compound=TOP, font=("times new roman", 20, "bold"), bg="#0875B7", fg="white")
        self.lbl_total_audio.place(x=270, y=90, width=200, height=230)

        self.lbl_total_video=Label(Frame1,  bd=2, relief=RAISED, text="Total video\n250", image=self.video_icon, compound=TOP,font=("times new roman", 20, "bold"), bg="#0875B7", fg="white")
        self.lbl_total_video.place(x=520, y=90, width=200, height=230)

        self.lbl_total_document=Label(Frame1,  bd=2, relief=RAISED, text="Total document\n250", image=self.document_icon, compound=TOP,font=("times new roman", 20, "bold"), bg="#0875B7", fg="white")
        self.lbl_total_document.place(x=770, y=90, width=200, height=230)

        self.lbl_total_other=Label(Frame1, text="Total other files\n250", image=self.other_icon, compound=TOP,font=("times new roman", 20, "bold"), bg="#0875B7", fg="white")
        self.lbl_total_other.place(x=1000, y=90, width=200, height=230)

        #==================Section4=======================

        lbl_status = Label(self.root,text="STATUS",font=("times new roman", 20, "bold"), bg="white").place(x=75,y=690)
        self.lbl_st_total = Label(self.root,text="TOTAL: 250",font=("times new roman", 20, "bold"), bg="white", fg="blue")
        self.lbl_st_total.place(x=270,y=690)

        self.lbl_st_moved = Label(self.root,text="MOVED: 150",font=("times new roman", 20, "bold"), bg="white", fg="blue")
        self.lbl_st_moved.place(x=500,y=690)

        self.lbl_st_left = Label(self.root,text="LEFT: 182",font=("times new roman", 20, "bold"), bg="white", fg="blue")
        self.lbl_st_left.place(x=730,y=690)

        #==========Buttons=========
        self.btn_clear=Button(self.root, text="CLEAR", font=("times new roman", 15, "bold"), bg="#262626", fg="white", activebackground="#262626", cursor="hand2",activeforeground="white")
        self.btn_clear.place(x=940, y=685, height=45, width=150)

        self.btn_start=Button(self.root, text="START", font=("times new roman", 15, "bold"), bg="#262626", fg="white", activebackground="#262626", cursor="hand2",activeforeground="white")
        self.btn_start.place(x=1140, y=685, height=45, width=150)

    def Total_count(self):
        images=0
        audios=0
        videos=0
        documents=0
        others=0
        for file in self.all_files:  
            if os.path.isfile(os.path.join(self.directory, file)) == True:   # os.path.join(self.directory, i) == (self.directory + "/" +i)
                ext = "." + file.split(".")[-1]
                for folder_name in self.folders.items():
                    #print(folder_name)
                    if ext in folder_name[1] and folder_name[0]=="images":
                        images+=1
                    if ext in folder_name[1] and folder_name[0]=="audios":
                        audios+=1
                    if ext in folder_name[1] and folder_name[0]=="videos":
                        videos+=1
                    if ext in folder_name[1] and folder_name[0]=="documents":
                        documents+=1
        self.lbl_total_image.config(text="Total Images\n"+str(images))
        self.lbl_total_image.config(text="Total Images\n"+str(videos))
        self.lbl_total_image.config(text="Total Images\n"+str(audios))
        self.lbl_total_image.config(text="Total Images\n"+str(documents))
        

    def browse_function(self):
        op = filedialog.askdirectory(title="SELECT FOLDER FOR SORTING")
        if op!=None:
            #print(op)
            self.var_foldername.set(str(op))
            self.directory = self.var_foldername.get()
            self.other_files = "others"
            self.all_files = os.listdir(self.directory)
            length=len(self.all_files)
            count = 1
            self.Total_count() 
            self.rename_folder()


            # for file in self.all_files:  
            #     if os.path.isfile(os.path.join(self.directory, file)) == True:   # os.path.join(self.directory, i) == (self.directory + "/" +i)
                    # extension = file.split(".")[-1]
                    # self.create_move(extension, file)
                    #pass
                # print(f"Total Files: {length}| Done: {count} | Left:{length-count}")
                # count += 1

    def rename_folder(self):
        for folder in os.listdir(self.directory):
            if os.path.isdir(os.path.join(self.directory, folder)) == True:
                os.rename(os.path.join(self.directory, folder), os.path.join(self.directory, folder.lower()))

    def create_move(self, ext, file_name):
        find = False
        for folder_name in self.folders:
            if "."+ext in self.folders[folder_name]:
                if folder_name not in os.listdir(self.directory):
                    os.mkdir(os.path.join(self.directory, folder_name)) #(src(path,filename),dst(path,dest folder))
                shutil.move(os.path.join(self.directory, file_name), os.path.join(self.directory,folder_name))#(src,dst)
                find = True
                break
        if find != True:
            if self.other_files not in os.listdir(self.directory):
                os.mkdir(os.path.join(self.directory, self.other_files))
            shutil.move(os.path.join(self.directory, file_name), os.path.join(self.directory, self.other_files))



root = Tk()
obj = Sorting_App(root)
root.mainloop() #hold screen

