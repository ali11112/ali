from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtPrintSupport import *

import os, sys

class mainWindow(QMainWindow):
    def __init__(self):
        super(). __init__()

        self.editor = QPlainTextEdit()
        self.setCentralWidget(self.editor)
        font = QFontDatabase.systemFont(QFontDatabase.FixedFont)
        font.setPointSize(12)
        self.editor.setFont(font)

        self.path = None

        toolbar = QToolBar()
        toolbar.setIconSize(QSize(14,14))
        self.addToolBar(toolbar)

        menu_bar = QMenuBar()
        menu_bar = self.menuBar()

        dosya_menu = menu_bar.addMenu("File")
        ekle_menu = menu_bar.addMenu("Edit")
        dosya_ac = QAction(QIcon(os.path.join("dosya_ac.png")), "Open", self)
        dosya_ac.setShortcut("Ctrl+O")
        toolbar.addAction(dosya_ac)
        dosya_menu.addAction(dosya_ac)

        kaydet = QAction(QIcon(os.path.join("kaydet.png")), "Edit", self)
        kaydet.setShortcut("Ctrl+S")
        toolbar.addAction(kaydet)
        dosya_menu.addAction(kaydet)


        farkli_kaydet = QAction(QIcon(os.path.join("farkli_kaydet.png")), "Save As", self)
        toolbar.addAction(farkli_kaydet)
        dosya_menu.addAction(farkli_kaydet)

        yazdir = QAction(QIcon(os.path.join("yazdir.png")), "Print", self)
        yazdir.setShortcut("Ctrl+P")
        toolbar.addAction(yazdir)
        dosya_menu.addAction(yazdir)

        geri_al = QAction(QIcon(os.path.join("geri_al.png")), "Undo Typing", self)
        geri_al.setShortcut("Ctrl+Z")
        toolbar.addAction(geri_al)
        ekle_menu.addAction(geri_al)

        ileri_al = QAction(QIcon(os.path.join("ileri_al.png")), "Redo", self)
        ileri_al.setShortcut("Ctrl+Y")
        toolbar.addAction(ileri_al)
        ekle_menu.addAction(ileri_al)

        kes = QAction(QIcon(os.path.join("kes.png")), "Cut", self)
        kes.setShortcut("Ctrl+X")
        toolbar.addAction(kes)
        ekle_menu.addAction(kes)

        kopyala = QAction(QIcon(os.path.join("kopyala.png")), "Copy", self)
        kopyala.setShortcut("Ctrl+C")
        toolbar.addAction(kopyala)
        ekle_menu.addAction(kopyala)

        yapistir = QAction(QIcon(os.path.join("yapistir.png")), "Paste", self)
        yapistir.setShortcut("Ctrl+V")
        toolbar.addAction(yapistir)
        ekle_menu.addAction(yapistir)

        hepsini_sec = QAction(QIcon(os.path.join("hepsini_sec.png")), "Select All", self)
        hepsini_sec.setShortcut("Ctrl+A")
        toolbar.addAction(hepsini_sec)
        ekle_menu.addAction(hepsini_sec)

        dosya_ac.triggered.connect(self.dosya_ac_def)
        kaydet.triggered.connect(self.kaydet_def)
        farkli_kaydet.triggered.connect(self.farkli_kaydet_def)
        yazdir.triggered.connect(self.yazdir_def)

        geri_al.triggered.connect(self.editor.undo)
        ileri_al.triggered.connect(self.editor.redo)
        kes.triggered.connect(self.editor.cut)
        kopyala.triggered.connect(self.editor.copy)
        yapistir.triggered.connect(self.editor.paste)
        hepsini_sec.triggered.connect(self.editor.selectAll)

        self.basligi_guncelle()
        self.setGeometry(100,100,500,500)
        self.show()
    def basligi_guncelle(self):
        self.setWindowTitle("{} - NotePad".format(os.path.basename(self.path)
        if self.path else "Untitled"))
    def dosya_ac_def(self):
        path, _ =QFileDialog.getOpenFileName(self, "Open File", "", "Text Dosyaları (*.txt)")
        if path:
            try:
                with open(path, "r") as file:
                    text = file.read()
            except Exception as e:
                print(e)
            else:
                self.editor.setPlainText(text)
                self.path = path
                self.basligi_guncelle()
    def kaydet_def(self):
        if self.path == None:
            return self.farkli_kaydet_def()
        text = self.editor.toPlainText()
        try:
            with open(self.path, "w") as file:
                file.write(text)
        except Exception as e:
            print(e)

    def farkli_kaydet_def(self):
        path, _ = QFileDialog.getSaveFileName(self, "Save As", "", "Text Files (*.txt)")
        if not path:
            return
        text = self.editor.toPlainText()

        try:
            with open(path, "w") as file:
                file.write(text)
        except Exception as e:
            print(e)
        else:
            self.path = path
            self.basligi_guncelle()
    def yazdir_def(self):
        mesaj = QPrintDialog()
        if mesaj.exec_():
            self.editor.print_(mesaj.printer())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setApplicationName("NotePad")

    window = mainWindow()

    app.exec_()