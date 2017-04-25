def clickUrl():  #按「確定」鈕後處理函式
    global listvideo, listradio
    labelMsg.config(text="")  #清除提示訊息
    if(url.get()==""):  #若未輸入網址就顯示提示訊息
        labelMsg.config(text="網址欄位必須輸入！")
    else:
        try:  #捕捉影片不存在的錯誤
            yt.url = url.get()  #取得輸入網址
            rbvalue = 1  #設定選項按鈕的值
            filename.set(yt.filename)  #取得影片名稱
            for v1 in yt.get_videos():  #建立影片格式串列
                listvideo.append(v1)
            for v2 in listvideo:  #建立影片格式選項按鈕
                rbtem = tk.Radiobutton(frame3, text=v2, variable=video, value=rbvalue, command=rbVideo)
                if(rbvalue==1):  #選取第1個選項按鈕       
                    rbtem.select()
                listradio.append(rbtem)  #建立選項按鈕串列        
                rbtem.grid(row=rbvalue-1, column=0, sticky="w")
                rbvalue += 1
            btnDown.config(state="normal")  #設定「下載影片」按鈕有效
        except:  #顯示影片不存在訊息
            labelMsg.config(text="找不到此 Youtube 影片！")
        
def rbVideo():  #點選選項按鈕後處理函式
    global getvideo, strftype
    labelMsg.config(text="")
    strvideo = str(listvideo[video.get()-1])  #取得點選項目
    #取得影片型態
    start1 = strvideo.find("(.")
    end1 = strvideo.find(")")
    strftype = strvideo[start1+2 : end1]
    #取得影片解析度
    end2 = strvideo.rfind(" - ")
    strresolution = strvideo[end1+4 : end2]
    getvideo = yt.get(strftype, strresolution)  #取得影片格式
        
def clickDown():  #按「下載影片」鈕後處理函式
    global getvideo, strftype, listradio
    labelMsg.config(text="")
    fpath = path.get()  #取得輸入存檔資料夾
    fpath = fpath.replace("\\", "\\\\")  #將「\」轉換為「\\」
    vpath = "" + fpath + filename.get() + "." + strftype  #存檔路徑
    getvideo.download(vpath)  #下載影片
    for r in listradio:  #移除選項按鈕
        r.destroy()
    listradio.clear()  #清除串列
    listvideo.clear()
    url.set("")  #清除輸入框
    filename.set("")
    btnDown.config(state="disabled")  #設定「下載影片」按鈕無效
        
import tkinter as tk
from pytube import YouTube

win=tk.Tk()
win.geometry("450x320")  #設定主視窗解析度
win.title("下載Youtube影片")
getvideo = ""  #影片格式
strftype = ""  #影片型態
listvideo = []  #影片格式串列
listradio = []  #選項按鈕串列
video = tk.IntVar()  #選項按鈕值
url = tk.StringVar()  #影片網址
path = tk.StringVar()  #存檔資料夾
filename = tk.StringVar()  #存檔名稱
yt = YouTube()

frame1 = tk.Frame(win, width=450)
frame1.pack()
label1=tk.Label(frame1, text="Youtube網址：")
entryUrl = tk.Entry(frame1, textvariable=url)
entryUrl.config(width=40)
btnUrl = tk.Button(frame1, text="確定", command=clickUrl)
label1.grid(row=0, column=0, sticky="e")
entryUrl.grid(row=0, column=1)
btnUrl.grid(row=0, column=2)

label2=tk.Label(frame1, text="存檔路徑：")
entryPath = tk.Entry(frame1, textvariable=path)
entryPath.config(width=40)
label2.grid(row=1, column=0, pady=6, sticky="e")
entryPath.grid(row=1, column=1)

label3=tk.Label(frame1, text="檔案名稱：")
entryFile = tk.Entry(frame1, textvariable=filename)
entryFile.config(width=40)
label3.grid(row=2, column=0, pady=3, sticky="e")
entryFile.grid(row=2, column=1)

frame2 = tk.Frame(win)
frame2.pack()
btnDown = tk.Button(frame2, text="下載影片", command=clickDown)
btnDown.pack(pady=6)
btnDown.config(state="disabled")  #開始時設定「下載影片」按鈕無效

labelMsg = tk.Label(win, text="", fg="red")  #訊息標籤
labelMsg.pack()

frame3 = tk.Frame(win)  #選項按鈕區塊
frame3.pack()
    
win.mainloop()