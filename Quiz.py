# MENTAL HEALTH QUIZ IF-B
# Esterlita Nugraheni Praharningtyas	2110511050
# Muhammad Ilham Ramadhan		        2110511078
# Irmaya Salsabila				    2110511080


from cProfile import label
from tkinter import *
from tkinter import messagebox as mb
import json

with open(r'D:\Ngoding\Mental Health Quiz\ini.json') as f: #path tergantung pada masing-masing device
    obj = json.load(f)
account = (obj['account'])
rekomen = (obj['rekomen'])
pengertian = (obj['pengertian'])

# ini quiz
def quiz_dimulai():
    global root
    q = (obj['ques'])
    options = (obj['options'])
    a = (obj['ans'])
    z = zip(q,options,a)
    l = list(z)
    total_score=[]
    global score
    score = []

    q,options,a=zip(*l) 
    root = Tk()
    root.geometry("1280x800")
    root.title("Quiz")
    root["bg"]="#33576B"

    class Quiz:
        def __init__(self):
            t = Label(root, text="ₓ˚. ୭ ˚○◦˚Mental Health Quiz˚◦○˚ ୧ .˚ₓ", width=80, bg="#b2a4d4", fg="#33576B", font=("Helvetica", 20, "bold"))
            #t.place(x=0, y=0)
            t.place(x=0, y=2)
            dis = Label(root, text="Disclaimer!\nTest ini tidak ditujukan untuk self-diagnose", width=100, bg="#33576B", fg="#E3EBEC", font=("Helvetica", 16, "bold", "italic"))
            dis.place(x=0,y=50)
            self.qn = 0 #urutan soal
            self.qno = 1 #nomor soal
            self.quest = StringVar()
            self.ques = self.question(self.qn)
            self.opt_selected = IntVar()
            self.opts = self.radiobtns()
            self.display_options(self.qn)
            self.buttons()
            self.correct = 0

        def question(self, qn): #pertanyaan
            self.quest.set(str(self.qno)+". "+q[qn])
            intruksi = Label(root, text="Jawablah pertanyaan berikut dengan jujur!", width=100, bg="#33576B", fg="light yellow", font=("Helvetica", 12, "bold", "italic"), anchor="w")
            intruksi.place(x=70,y=110)
            qn = Label(root, textvariable = self.quest, width=150, bg="#33576B", fg="#F1DDDB", font=("berlin sans fb demi", 16), anchor="w")
            qn.place(x=70, y=140)
            return qn

        def radiobtns(self): #button pilihan
            val = 0
            b = []
            yp = 180
            while val < 4:
                btn = Radiobutton(root, text=" ", variable=self.opt_selected, value=val + 1, bg="#33576B", fg="#F1DDDB", activebackground="#33576B", activeforeground="#F1DDDB", selectcolor="#33576B", font=("berlin sans fb", 14))
                b.append(btn)
                btn.place(x=100, y=yp)
                val += 1
                yp += 40
            return b

        def display_options(self, qn): #pilihan
            val = 0
            self.opt_selected.set(0)
            self.ques['text'] = q[qn]
            for op in options[qn]:
                self.opts[val]['text'] = op
                val += 1

        def buttons(self): #next quit button
            nbutton = Button(root, text="Next",command=self.nextbtn, width=10,bg="#1c911a",fg="white",font=("rockwell",14,"bold"))
            nbutton.place(x=500,y=400)
            quitbutton = Button(root, text="Quit", command=root.destroy,width=10,bg="#a80f0f",fg="white", font=("rockwell",14,"bold"))
            quitbutton.place(x=680,y=400)

        def checkans(self, qn):
            temp = self.opt_selected.get()
            if(temp != 0):
            #jawaban akan dimasukan kedalam suatu list bernama total_score
            #total_score memiliki 25 index berupa jawaban dari user
                total_score.append(temp)
                print(temp)
                if temp == a[qn]:
                    return True
            else:
                mb.showinfo("Warning", "Pilih Jawaban")
            
        def nextbtn(self):
            if self.checkans(self.qn):
                self.correct += a[self.qn]
            self.qn += 1
            self.qno += 1
            print(self.opt_selected.get())
            if self.qn == len(q):
                self.display_result()
            elif self.opt_selected.get() == 0:
                self.qn -=1
                self.qno -=1
            else:
                self.quest.set(str(self.qno)+". "+q[self.qn])
                self.display_options(self.qn)       

        def display_result(self):
            #bipolar, anxiety, depresi, stress, ocd
            for i in total_score:
                print(i)
            temp_score = 0
            count = 0
            for i in total_score:
                if(i==1):
                    temp_score += 0
                elif(i==2):
                    temp_score += 5
                elif(i==3):
                    temp_score += 10
                elif(i==4):
                    temp_score += 20
            # apabila user menekan radio button ke-0 (alias tidak menekan sama sekali, maka jangan pindah ke pertanyaan selanjutnya)
                count+=1

                if(count%5 == 0):
                    score.append(temp_score)
                    temp_score = 0
            mb.showinfo("Result", "Nama : "+ obj["account"][uname]["nama"] + "\tUsia : " + str(obj["account"][uname]["usia"]) + "\t\tGender : "+ obj["account"][uname]["gender"]+"\n\nGejala bipolar pada diri anda\t: " + str(score[0])+"%"+"\nGejala anxiety pada diri anda\t: " + str(score[1])+"%"+"\nGejala depresi pada diri anda\t: " + str(score[2]) + "%"+"\nGejala stress pada diri anda\t\t: " + str(score[3]) + "%"+"\nGejala OCD pada diri anda\t\t: " + str(score[4])+"%")
            root.mainloop
            reminder(score)
    quiz = Quiz()

def reminder(score):
    root.destroy()
    # ini digunakan untuk mencari skor tertinggi
    # score = [100, 50, 100, 20, 75]
    # goalsnya menampilkan dua reminder, yaitu bipolar dan depresi
    max_score = 0
    # for loops ini digunakan untuk mencari angka tertinggi
    for i in score:
        if i > max_score:
            max_score = i

    index = []
    # 0 - 4
    for i in range (len(score)):
        if score[i] == max_score:
            index.append(i)
    ycoor = 0
    #bipolar[0], anxiety[1], depresi[2], stress[3], ocd[4]

    def reminder_bipolar(ycoor, bool):
        root1 = Tk()
        root1.geometry("1280x800")
        root1.title("Tips")
        root1["bg"]="#33576B"
        pesan = pengertian['Bipolar']
        texts = rekomen['Bipolar']
        Label(root1, text = "Bipolar", width=150, bg="#33576B", fg="#F1DDDB", font=("berlin sans fb demi", 16), anchor="w").place(x=0, y=ycoor)
        ycoor += 40

        for x in pesan:
            Label(root1, text = x, width=150, bg="#33576B", fg="#F1DDDB", font=("berlin sans fb demi", 12), anchor="w").place(x=20, y=ycoor)
            ycoor += 20

        ycoor += 20
        Label(root1, text = "Tips", width=150, bg="#33576B", fg="#F1DDDB", font=("berlin sans fb demi", 14), anchor="w").place(x=0, y=ycoor)
        ycoor += 40
        for a in range(len(texts)):
            Label(root1, text = texts[a], width=150, bg="#33576B", fg="#F1DDDB", font=("berlin sans fb demi", 12), anchor="w").place(x=20, y=ycoor)
            ycoor += 20

        if(bool == False):
            nbutton = Button(root1, text="Next",command=root1.destroy, width=10,bg="#1c911a",fg="white",font=("rockwell",14,"bold"))
            nbutton.place(x=600,y=600)
        else:
            quitbutton = Button(root1, text="Quit", command=root1.destroy,width=10,bg="#a80f0f",fg="white", font=("rockwell",14,"bold"))
            quitbutton.place(x=600,y=600)

        root1.mainloop()

    def reminder_anxiety(ycoor,bool):
        root1 = Tk()
        root1.geometry("1280x800")
        root1.title("Tips")
        root1["bg"]="#33576B"
        pesan = pengertian['Anxiety']
        texts = rekomen['Anxiety']
        Label(root1, text = "Anxiety", width=150, bg="#33576B", fg="#F1DDDB", font=("berlin sans fb demi", 16), anchor="w").place(x=0, y=ycoor)
        ycoor += 40
    
        for x in pesan:
            print(x , "\n")
            Label(root1, text = x, width=150, bg="#33576B", fg="#F1DDDB", font=("berlin sans fb demi", 12), anchor="w").place(x=20, y=ycoor)
            ycoor +=20

        ycoor += 20
        Label(root1, text = "Tips", width=150, bg="#33576B", fg="#F1DDDB", font=("berlin sans fb demi", 14), anchor="w").place(x=0, y=ycoor)
        ycoor += 40
        for a in range(len(texts)):
            Label(root1, text = texts[a], width=150, bg="#33576B", fg="#F1DDDB", font=("berlin sans fb demi", 12), anchor="w").place(x=20, y=ycoor)
            ycoor += 20

        if(bool == False):
            nbutton = Button(root1, text="Next",command=root1.destroy, width=10,bg="#1c911a",fg="white",font=("rockwell",14,"bold"))
            nbutton.place(x=600,y=600)
        else:
            quitbutton = Button(root1, text="Quit", command=root1.destroy,width=10,bg="#a80f0f",fg="white", font=("rockwell",14,"bold"))
            quitbutton.place(x=600,y=600)

        root1.mainloop()

    def reminder_stress(ycoor,bool):
        root1 = Tk()
        root1.geometry("1280x800")
        root1.title("Tips")
        root1["bg"]="#33576B"
        pesan = pengertian['Stress']
        texts = rekomen['Stress']
        Label(root1, text = "Stress", width=150, bg="#33576B", fg="#F1DDDB", font=("berlin sans fb demi", 16), anchor="w").place(x=0, y=ycoor)
        ycoor += 40

        for x in pesan:
            Label(root1, text = x, width=150, bg="#33576B", fg="#F1DDDB", font=("berlin sans fb demi", 12), anchor="w").place(x=20, y=ycoor)
            ycoor += 20
        
        ycoor += 20
        Label(root1, text = "Tips", width=150, bg="#33576B", fg="#F1DDDB", font=("berlin sans fb demi", 14), anchor="w").place(x=0, y=ycoor)
        ycoor += 40
        for a in range(len(texts)):
            Label(root1, text = texts[a], width=150, bg="#33576B", fg="#F1DDDB", font=("berlin sans fb demi", 12), anchor="w").place(x=20, y=ycoor)
            ycoor += 20

        if(bool == False):
            nbutton = Button(root1, text="Next",command=root1.destroy, width=10,bg="#1c911a",fg="white",font=("rockwell",14,"bold"))
            nbutton.place(x=600,y=600)
        else:
            quitbutton = Button(root1, text="Quit", command=root1.destroy,width=10,bg="#a80f0f",fg="white", font=("rockwell",14,"bold"))
            quitbutton.place(x=600,y=600)

        root1.mainloop()

    def reminder_ocd(ycoor,bool):
        root1 = Tk()
        root1.geometry("1280x800")
        root1.title("Tips")
        root1["bg"]="#33576B"
        pesan = pengertian['Stress']
        texts = rekomen['Stress']
        Label(root1, text = "Stress", width=150, bg="#33576B", fg="#F1DDDB", font=("berlin sans fb demi", 16), anchor="w").place(x=0, y=ycoor)
        ycoor += 40
        for x in pesan:
            Label(root1, text = x, width=150, bg="#33576B", fg="#F1DDDB", font=("berlin sans fb demi", 12), anchor="w").place(x=20, y=ycoor)
            ycoor += 20
        
        ycoor += 20
        Label(root1, text = "Tips", width=150, bg="#33576B", fg="#F1DDDB", font=("berlin sans fb demi", 14), anchor="w").place(x=0, y=ycoor)
        ycoor += 40
        for a in range(len(texts)):
            Label(root1, text = texts[a], width=150, bg="#33576B", fg="#F1DDDB", font=("berlin sans fb demi", 12), anchor="w").place(x=20, y=ycoor)
            ycoor += 20

        if(bool == False):
            nbutton = Button(root1, text="Next",command=root1.destroy, width=10,bg="#1c911a",fg="white",font=("rockwell",14,"bold"))
            nbutton.place(x=600,y=600)
        else:
            quitbutton = Button(root1, text="Quit", command=root1.destroy,width=10,bg="#a80f0f",fg="white", font=("rockwell",14,"bold"))
            quitbutton.place(x=600,y=600)

        root1.mainloop()

    def reminder_depresi(ycoor,bool):
        root1 = Tk()
        root1.geometry("1280x800")
        root1.title("Tips")
        root1["bg"]="#33576B"
        pesan = pengertian['OCD']
        texts = rekomen['OCD']
        Label(root1, text = "OCD", width=150, bg="#33576B", fg="#F1DDDB", font=("berlin sans fb demi", 16), anchor="w").place(x=0, y=ycoor)
        ycoor += 40
        for x in pesan:
            Label(root1, text = x, width=150, bg="#33576B", fg="#F1DDDB", font=("berlin sans fb demi", 12), anchor="w").place(x=20, y=ycoor)
            ycoor += 20
        
        ycoor += 20
        Label(root1, text = "Tips", width=150, bg="#33576B", fg="#F1DDDB", font=("berlin sans fb demi", 14), anchor="w").place(x=0, y=ycoor)
        ycoor += 40
        for a in range(len(texts)):
            Label(root1, text = texts[a], width=150, bg="#33576B", fg="#F1DDDB", font=("berlin sans fb demi", 12), anchor="w").place(x=20, y=ycoor)
            ycoor += 20
        
        if(bool == False):
            nbutton = Button(root1, text="Next",command=root1.destroy, width=10,bg="#1c911a",fg="white",font=("rockwell",14,"bold"))
            nbutton.place(x=600,y=600)
        else:
            quitbutton = Button(root1, text="Quit", command=root1.destroy,width=10,bg="#a80f0f",fg="white", font=("rockwell",14,"bold"))
            quitbutton.place(x=600,y=600)

        root1.mainloop()

    last_element = index[-1]
    bool = False
    for i in index:
        if i == last_element:
            bool = True

        ycoor = 0
        if(i == 0):
            reminder_bipolar(ycoor,bool)

        elif i == 1:
            reminder_anxiety(ycoor,bool)
        elif i == 2:
            reminder_stress(ycoor,bool)

        elif i == 3:
            reminder_ocd(ycoor,bool)

        elif i == 4:
            reminder_depresi(ycoor,bool)

#login page
def login():
    screen.destroy()
    reg = Tk()
    reg.title("Login")
    reg.geometry("300x200")
    reg.configure(bg = "#f5f5f5")
    Label(reg, text="Silahkan Login!", width=29, bg="#b2a4d4", font = ("berlin sans fb demi", 14)).place(x=0, y=0)
    global e1
    global e2
    Label(reg, text="Login")
    Label(reg, text="Username").place(x=30, y=55)
    Label(reg, text="Password").place(x=30, y=85)
    e1 = Entry(reg)
    e1.place(x=160, y=55)
    e2 = Entry(reg)
    e2.place(x=160, y=85)
    e2.config(show="*")
    account = (obj['account'])

    def back_screen():
        reg.destroy()
        main_screen()
    
    def destroy_reg():
        reg.destroy()

    def Ok():
        global uname
        uname = e1.get()
        password = e2.get()
        if(uname == "" and password == "") :
            mb.showinfo("", "Username dan password harus diisi")
        elif(uname in account.keys() and account[uname]["password"] == password):
            mb.showinfo("","Login Success")
            destroy_reg()
            quiz_dimulai()
        else :
            mb.showinfo("","Username dan password yang anda masukkan salah")
        
    Button(reg, text="Login", command=Ok ,height = 1, width = 10).place(x=160, y=120)
    Button(reg, text="Back", command=back_screen ,height = 1, width = 10).place(x=50, y=120)
    reg.mainloop()

#regis
def register():
    global screen1
    screen1=Toplevel(screen)
    screen1.title("Register")
    screen1.geometry("400x350")
    # screen1.configure(bg = "#b2a4d4")
    global id, pw, nama, usia, gender
    global id_entry, pw_entry, nama_entry, usia_entry, gender_entry
    id=StringVar()
    pw=StringVar()
    nama=StringVar()
    usia=StringVar()
    gender=StringVar()
    Label(screen1,text="Silahkan Masukkan Data Diri Anda" ,font = ("berlin sans fb demi", 14), bg = "#b2a4d4").pack()
    Label(screen1,text="").pack()
    Label(screen1,text="Username*").pack()
    id_entry=Entry(screen1,textvariable=id)
    id_entry.pack()
    Label(screen1,text="Password*").pack()
    pw_entry=Entry(screen1,textvariable=pw)
    pw_entry.pack()
    Label(screen1,text="Nama*").pack()
    nama_entry=Entry(screen1,textvariable=nama)
    nama_entry.pack()
    Label(screen1,text="Usia (e.g: 18)*").pack()
    usia_entry=Entry(screen1,textvariable=usia)
    usia_entry.pack()
    Label(screen1,text="Gender (L/P)*").pack()
    gender_entry=Entry(screen1,textvariable=gender)
    gender_entry.pack()
    Label(screen1,text="").pack()
    Button(screen1,text="Register",width=10,height=1,command=register_user).pack()

def register_user():
    print("Working")
    id_info=id.get()
    pw_info=pw.get()
    nama_info=nama.get()
    usia_info=usia.get()
    gender_info=gender.get()
    if id_info == ""\
        or pw_info == ""\
        or nama_info == ""\
        or usia_info == ""\
        or gender_info == "":
        mb.showinfo('Registrasi', "Data diri tidak boleh kosong")
        return 
    
    elif id_info in obj['account'].keys():
        mb.showinfo('Registrasi', "Registrasi gagal")
        id_entry.delete(0,END)
        pw_entry.delete(0,END)
    else :
        with open('ini.json', 'w') as r:    #agar data regis masuk ke ini.json yang ada di file Mental Health Quiz
            temp_account = {}               #copy path pada file Mental Health Quiz kemudian paste di terminal, baru jalankan program
            temp_account["password"] = pw_info
            temp_account["nama"] = nama_info
            temp_account["usia"] = usia_info
            temp_account["gender"] = gender_info
            obj["account"][id_info] = temp_account
            file = json.dumps(obj, indent=2)
            r.write(file)
            mb.showinfo('Registrasi', "Registrasi berhasil")
            screen1.destroy()

def info():
    mb.showinfo('Info', 
    "Program ini dibuat untuk memenuhi tugas mata kuliah Algortma Pemrograman II\n\n2110511050\tEsterlita Nugraheni Praharningtyas\n2110511078\tMuhammad Ilham Ramadhan\n2110511080\tIrmaya Salsabila\n\nReference\nhttps://www.clinical-partners.co.uk/online-tests")

def main_screen():
    global screen
    screen=Tk()
    screen.geometry("400x350")
    screen.title("Quiz")
    screen.configure(bg = "#b2a4d4")
    Label(text="", bg="#b2a4d4").pack() 
    Label(text="Mental Health Quiz",bg="#b2a4d4",width="300",height = "2",font = ("berlin sans fb demi", 20, "bold")).pack()
    Label(text="", bg="#b2a4d4").pack() 
    Button(text="Login",height="2",width="30",command=login).pack()
    Label(text="", bg="#b2a4d4").pack()
    Button(text="Register",height="2",width="30",command=register).pack()
    Label(text="", bg="#b2a4d4").pack()
    Button(text="Info",height="2",width="30",command=info).pack()
    Label(text="", bg="#b2a4d4").pack()
    screen.mainloop()

main_screen()