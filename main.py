import os
import tkinter as tk
from tkinter import filedialog
from pytube import YouTube

def downloadfomatto():
    dougaurl = urlentori.get()
    daunrodoforuda = forudapasu.get()
    serekutofomatto = formatvar.get()

    try:
        yt = YouTube(dougaurl)

        if serekutofomatto == "MP4":
            stream = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
            download_path = os.path.join(daunrodoforuda, yt.title + ".mp4")
            stream.download(output_path=download_path)
            sutetasuraberu.config(text="MP4ダウンロードが完了しました")
        elif serekutofomatto == "MP3":
            stream = yt.streams.filter(only_audio=True).first()
            download_path = os.path.join(daunrodoforuda, yt.title + ".mp3")
            stream.download(output_path=daunrodoforuda, filename=yt.title + ".mp3")
            sutetasuraberu.config(text="MP3ダウンロードが完了しました")

    except Exception as e:
        sutetasuraberu.config(text=f"エラー: {str(e)}")

def sanshouforuda():
    sentakusitaforuda = filedialog.askdirectory()
    forudapasu.set(sentakusitaforuda)

window = tk.Tk()
window.title("YouTube動画/MP3ダウンローダー")

urlraberu = tk.Label(window, text="YouTubeの動画URL:")
urlraberu.pack()
urlentori = tk.Entry(window, width=40)
urlentori.pack()

forudaraberu = tk.Label(window, text="ダウンロード先フォルダ:")
forudaraberu.pack()
forudapasu = tk.StringVar()
folder_entry = tk.Entry(window, textvariable=forudapasu, width=40)
folder_entry.pack()
botansanshousita = tk.Button(window, text="フォルダを選択", command=sanshouforuda)
botansanshousita.pack()

fomattokeisiki = tk.Label(window, text="ダウンロード形式:")
fomattokeisiki.pack()
formatvar = tk.StringVar()
formatvar.set("MP4") 
fomattomenu = tk.OptionMenu(window, formatvar, "MP4", "MP3")
fomattomenu.pack()

daunrodobotan = tk.Button(window, text="ダウンロード", command=downloadfomatto)
daunrodobotan.pack()

sutetasuraberu = tk.Label(window, text="")
sutetasuraberu.pack()

window.mainloop()