from tkinter import*
from tkinter import ttk, filedialog, messagebox
import os
import shutil


class Sorting_App:
    def __init__(self, root):
        self.root = root
        self.root.title(
            " Distributing Files Application | Developed By Akshat srivastava | mr_cs.coder ")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")
        self.logo_icon = PhotoImage(file="images/logo.png")
        title = Label(self.root, text="FILES DISTRIBUTING APPLICATION", padx=20, image=self.logo_icon, compound="left", font=(
            "Algerian", 40,), bg="#151B54", fg="#FFD801", anchor="s").place(x=0, y=0, relwidth=1)

# -----section-1--------

        self.var_foldername = StringVar()
        lbl_Select_folder = Label(
            self.root, text="Select Folder - ", font=("Algerian", 25, "bold"), bg="white").place(x=50, y=100)
        txt_folder_name = Entry(self.root, textvariable=self.var_foldername, font=(
            "Cambria (Headings)", 15, "bold"), state='readonly', bg="#FFF8C6").place(x=337, y=102, height=40, width=600)
        btn_browse = Button(self.root, command=self.browse_function, text="BROWSE", bd=5, font=(
            "Cambria (Headings)", 15, "bold"), bg="#2B1B17", fg="white", activebackground="#E5E4E2", cursor="hand2", activeforeground="black").place(x=955, y=101, height=40, width=150)
        hr = Label(self.root, bg="lightgray").place(
            x=50, y=160, height=2, width=1260)

# --------Section-2---------
# -----All extentions----------

        self.image_extentions = ["Image Extentions", ".png", ".jpg", ".jpeg"]
        self.audio_extentions = [
            "Audio Extentions", '.mp3', '.wav', '.amr', '.m4a']
        self.video_extentions = ["Video Extentions",
                                 ".mkv", ".avi", ".3gp", ".mpeg4", ".mp4"]
        self.doc_extentions = ["Document Extentions", '.doc', '.xlsx',
                               '.pdf', '.zip', '.rar', '.xls', '.docx', '.pptx', '.txt']
        self.folders = {
            'videos': self.video_extentions,
            'audios': self.audio_extentions,
            'images': self.image_extentions,
            'documents': self.doc_extentions,

        }

        lbl_Support_ext = Label(
            self.root, text="Various supported extentions :-", font=("Algerian", 25), bg="white").place(x=50, y=170)
        self.image_box = ttk.Combobox(
            self.root, values=self.image_extentions, font=("Cambria (Headings)", 15), state='readonly', justify="center")
        self.image_box.place(x=60, y=230, width=220, height=30)
        self.image_box.current(0)

        self.video_box = ttk.Combobox(
            self.root, values=self.video_extentions, font=("Cambria (Headings)", 15), state='readonly', justify="center")
        self.video_box.place(x=380, y=230, width=220, height=30)
        self.video_box.current(0)

        self.audio_box = ttk.Combobox(
            self.root, values=self.audio_extentions, font=("Cambria (Headings)", 15), state='readonly', justify="center")
        self.audio_box.place(x=720, y=230, width=220, height=30)
        self.audio_box.current(0)

        self.doc_box = ttk.Combobox(
            self.root, values=self.doc_extentions, font=("Cambria (Headings)", 15), state='readonly', justify="center")
        self.doc_box.place(x=1050, y=230, width=220, height=30)
        self.doc_box.current(0)

# --------Section-3---------
# --------All-Image-Icons---------
        self.image_icon = PhotoImage(file="images/image.png")
        self.audio_icon = PhotoImage(file="images/audio.png")
        self.video_icon = PhotoImage(file="images/video.png")
        self.document_icon = PhotoImage(file="images/doc.png")
        self.other_icon = PhotoImage(file="images/other1.png")

        Frame1 = Frame(self.root, bd=2, relief=RIDGE, bg="white")
        Frame1.place(x=50, y=300, width=1250, height=280)
        self.lbl_total_files = Label(
            Frame1, text="Total Files :- ", font=("Algerian", 18, "bold"), bg="white")
        self.lbl_total_files.place(x=10, y=8)

        self.lbl_total_image = Label(
            Frame1, bd=3, relief=RAISED, image=self.image_icon, compound="top", font=("Algerian", 18), bg="#800000", fg="#FFD801")
        self.lbl_total_image.place(x=25, y=55, width=230, height=200)

        self.lbl_total_video = Label(
            Frame1, bd=3, relief=RAISED,  image=self.video_icon, compound="top", font=("Algerian", 18), bg="#E4287C", fg="#FFD801")
        self.lbl_total_video.place(x=267, y=55, width=230, height=200)

        self.lbl_total_audio = Label(
            Frame1, bd=3, relief=RAISED,  image=self.audio_icon, compound="top", font=("Algerian", 18), bg="#728C00", fg="#FFD801")
        self.lbl_total_audio.place(x=507, y=55, width=230, height=200)

        self.lbl_total_document = Label(
            Frame1, bd=3, relief=RAISED,  image=self.document_icon, compound="top", font=("Algerian", 18), bg="#7D0552", fg="#FFD801")
        self.lbl_total_document.place(x=747, y=55, width=230, height=200)

        self.lbl_total_other = Label(
            Frame1, bd=3, relief=RAISED, image=self.other_icon, compound="top", font=("Algerian", 18), bg="#4B0082", fg="#FFD801")
        self.lbl_total_other.place(x=987, y=55, width=230, height=200)

# --------Section-4---------
        self.lbl_status = Label(
            self.root, text="STATUS :- ", font=("Algerian", 20), bg="white", fg="red")
        self.lbl_status.place(x=50, y=620)

        self.lbl_st_total = Label(
            self.root, text="", font=("Algerian", 20), bg="white", fg="green")
        self.lbl_st_total.place(x=300, y=620)

        self.lbl_st_moved = Label(
            self.root, text="", font=("Algerian", 20), bg="white", fg="#000080")
        self.lbl_st_moved.place(x=510, y=620)

        self.lbl_st_left = Label(
            self.root, text="", font=("Algerian", 20), bg="white", fg="Magenta")
        self.lbl_st_left.place(x=710, y=620)

# -----------Buttons---------------

        self.btn_clear = Button(self.root, text="CLEAR", bd=3, relief=RAISED, command=self.clear, font=(
            "Cambria (Headings)", 15, "bold"), bg="#616D7E", fg="black", activebackground="#25383C", cursor="hand2", activeforeground="white")
        self.btn_clear.place(x=900, y=617, height=40, width=160)

        self.btn_start = Button(self.root, state=DISABLED, command=self.start_function, text="START", bd=3, relief=RAISED, font=(
            "Cambria (Headings)", 15, "bold"), bg="red", fg="black", activebackground="Green", cursor="hand2", activeforeground="white")
        self.btn_start.place(x=1100, y=617, height=40, width=160)

    def Total_count(self):
        images = 0
        videos = 0
        audios = 0
        documents = 0
        others = 0
        self.count = 0
        combine_list = []
        for i in self.all_files:
            if os.path.isfile(os.path.join(self.directry, i)) == True:
                self.count += 1
                ext = "."+i.split(".")[-1]
                for folder_name in self.folders.items():
                    # print(folder_name)
                    for x in folder_name[1]:
                        combine_list.append(x)
                    if ext.lower() in folder_name[1] and folder_name[0] == "images":
                        images += 1
                    if ext.lower() in folder_name[1] and folder_name[0] == "videos":
                        videos += 1
                    if ext.lower() in folder_name[1] and folder_name[0] == "audios":
                        audios += 1
                    if ext.lower() in folder_name[1] and folder_name[0] == "documents":
                        documents += 1

        for i in self.all_files:
            if os.path.isfile(os.path.join(self.directry, i)) == True:
                ext = "."+i.split(".")[-1]
                if ext.lower() not in combine_list:
                    others += 1

        self.lbl_total_image.config(text="Total Images\n"+str(images))
        self.lbl_total_video.config(text="Total Videos\n"+str(videos))
        self.lbl_total_audio.config(text="Total Audios\n"+str(audios))
        self.lbl_total_document.config(text="Total Documents\n"+str(documents))
        self.lbl_total_other.config(text="Others Files\n"+str(others))
        self.lbl_total_files.config(text="Total Files :- "+str(self.count))

    def browse_function(self):
        op = filedialog.askdirectory(title="SELECT FOLDER FOR DISTRIBUTING")
        if op != None:
            # print(op)
            self.var_foldername.set(str(op))
            self.directry = self.var_foldername.get()
            self.other_name = "others"
            self.rename_folder()
            self.all_files = os.listdir(self.directry)
            length = len(self.all_files)
            count = 1
            self.Total_count()
            self.btn_start.config(state=NORMAL)

    def start_function(self):
        if self.var_foldername.get() != "":
            self.btn_clear.config(state=DISABLED)
            c = 0
            for i in self.all_files:
                if os.path.isfile(os.path.join(self.directry, i)) == True:
                    c += 1
                    self.create_move(i.split(".")[-1], i)
                    self.lbl_st_total.config(text="TOTAL :- "+str(self.count))
                    self.lbl_st_moved.config(text="MOVED :- "+str(c))
                    self.lbl_st_left.config(text="LEFT :- "+str(self.count-c))

                    self.lbl_st_total.update()
                    self.lbl_st_moved.update()
                    self.lbl_st_left.update()

            messagebox.showinfo("SUCCESS", "ALL FILES HAS MOVED SUCCESSFULLY")
            self.btn_start.config(state=DISABLED)
            self.btn_clear.config(state=NORMAL)
        else:
            messagebox.showerror("ERROR", "PLEASE SELECT FOLDER")

    def clear(self):
        self.btn_start.config(state=DISABLED)
        self.var_foldername.set("")
        self.lbl_st_total.config(text="")
        self.lbl_st_moved.config(text="")
        self.lbl_st_left.config(text="")

        self.lbl_total_image.config(text="")
        self.lbl_total_video.config(text="")
        self.lbl_total_audio.config(text="")
        self.lbl_total_document.config(text="")
        self.lbl_total_other.config(text="")
        self.lbl_total_files.config(text="TOTAL FILES")

    def rename_folder(self):
        for folder in os.listdir(self.directry):
            if os.path.isdir(os.path.join(self.directry, folder)) == True:
                os.rename(os.path.join(self.directry, folder),
                          os.path.join(self.directry, folder.lower()))

    def create_move(self, ext, file_name):
        find = False
        for folder_name in self.folders:
            if "." + ext in self.folders[folder_name]:
                if folder_name not in os.listdir(self.directry):
                    os.mkdir(os.path.join(self.directry, folder_name))
                shutil.move(os.path.join(self.directry, file_name),
                            os.path.join(self.directry, folder_name))
                find = True
                break
        if find != True:
            if self.other_name not in os.listdir(self.directry):
                os.mkdir(os.path.join(self.directry, self.other_name))
            shutil.move(os.path.join(self.directry, file_name),
                        os.path.join(self.directry, self.other_name))


root = Tk()
obj = Sorting_App(root)
root.mainloop()
