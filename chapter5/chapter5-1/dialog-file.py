#ダイアログを表示するために必要なモジュール
import tkinter.filedialog as fd

#ファイル洗濯ダイアログを表示する
path = fd.askopenfilename(
    title = "処理対象のファイルを指定してください",
    filetypes=[('HTML', '.html')]
)
print(path)
