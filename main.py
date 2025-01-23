import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget, QFileDialog, QMessageBox, QComboBox, QProgressBar
from PySide6.QtGui import QFont
from yt_dlp import YoutubeDL

class YouTubeDownloaderApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("تحميل من اليوتيوب")
        self.setGeometry(100, 100, 500, 350)

        # Apply CSS styles to make friendly GUI
        self.setStyleSheet("""
            QMainWindow {
                background-color: #2E3440;
            }
            QLabel {
                color: #D8DEE9;
                font-size: 16px;
                font-weight: bold;
            }
            QLineEdit {
                background-color: #4C566A;
                color: #ECEFF4;
                border: 2px solid #81A1C1;
                border-radius: 5px;
                padding: 5px;
                font-size: 14px;
            }
            QPushButton {
                background-color: #81A1C1;
                color: #2E3440;
                border: 2px solid #81A1C1;
                border-radius: 5px;
                padding: 10px;
                font-size: 14px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #5E81AC;
                border: 2px solid #5E81AC;
            }
            QPushButton:pressed {
                background-color: #4C566A;
                border: 2px solid #4C566A;
            }
            QComboBox {
                background-color: #4C566A;
                color: #ECEFF4;
                border: 2px solid #81A1C1;
                border-radius: 5px;
                padding: 5px;
                font-size: 14px;
            }
            QComboBox QAbstractItemView {
                background-color: #4C566A;
                color: #ECEFF4;
                selection-background-color: #81A1C1;
            }
            QProgressBar {
                background-color: #4C566A;
                color: #ECEFF4;
                border: 2px solid #81A1C1;
                border-radius: 5px;
                text-align: center;
            }
            QProgressBar::chunk {
                background-color: #81A1C1;
                border-radius: 5px;
            }
        """)

        # Create interface elements
        self.url_label = QLabel("رابط الفيديو أو قائمة التشغيل:")
        self.url_entry = QLineEdit()
        self.path_label = QLabel("مجلد الحفظ:")
        self.path_entry = QLineEdit()
        self.browse_button = QPushButton("اختر مجلد")
        self.format_label = QLabel("اختر الصيغة:")
        self.format_combo = QComboBox()
        self.format_combo.addItems(["MP4 (فيديو)", "MP3 (صوت فقط)"])
        self.download_button = QPushButton("تحميل")
        self.progress_bar = QProgressBar()
        self.progress_bar.setValue(0)
        self.status_label = QLabel("عدد الفيديوهات التي تم تحميلها: 0 / 0")

        # Customize fonts
        font = QFont()
        font.setPointSize(12)
        self.url_label.setFont(font)
        self.path_label.setFont(font)
        self.format_label.setFont(font)
        self.browse_button.setFont(font)
        self.download_button.setFont(font)
        self.status_label.setFont(font)

        # Organizing elements in a layout
        layout = QVBoxLayout()
        layout.addWidget(self.url_label)
        layout.addWidget(self.url_entry)
        layout.addWidget(self.path_label)
        layout.addWidget(self.path_entry)
        layout.addWidget(self.browse_button)
        layout.addWidget(self.format_label)
        layout.addWidget(self.format_combo)
        layout.addWidget(self.download_button)
        layout.addWidget(self.progress_bar)
        layout.addWidget(self.status_label)

        #  Create main interface
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        # Bind buttons to functions
        self.browse_button.clicked.connect(self.select_directory)
        self.download_button.clicked.connect(self.download_media)

        # Variables to track progress
        self.total_videos = 0
        self.downloaded_videos = 0

    # Function to select save folder
    def select_directory(self):
        directory = QFileDialog.getExistingDirectory(self, "اختر مجلد الحفظ")
        if directory:
            self.path_entry.setText(directory)

    # Function to download video or playlist
    def download_media(self):
        url = self.url_entry.text()
        output_path = self.path_entry.text()
        format_choice = self.format_combo.currentText()

        if not url or not output_path:
            QMessageBox.critical(self, "خطأ", "يرجى إدخال رابط ومجلد الحفظ")
            return

        try:
            if format_choice == "MP4 (فيديو)":
                ydl_opts = {
                    'outtmpl': f'{output_path}/%(title)s.%(ext)s',
                    'format': 'bestvideo+bestaudio/best',
                    'progress_hooks': [self.update_progress],
                }
            else:  # MP3 (صوت فقط)
                ydl_opts = {
                    'outtmpl': f'{output_path}/%(title)s.%(ext)s',
                    'format': 'bestaudio/best',
                    'postprocessors': [{
                        'key': 'FFmpegExtractAudio',
                        'preferredcodec': 'mp3',
                    }],
                    'progress_hooks': [self.update_progress],
                }

            with YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(url, download=False)
                if 'entries' in info:  # For playlist
                    self.total_videos = len(info['entries'])
                else:  # For one vedio
                    self.total_videos = 1
                self.downloaded_videos = 0
                self.progress_bar.setValue(0)
                self.status_label.setText(f"عدد الفيديوهات التي تم تحميلها: 0 / {self.total_videos}")
                ydl.download([url])

            QMessageBox.information(self, "نجاح", "تم التحميل بنجاح!")
        except Exception as e:
            QMessageBox.critical(self, "خطأ", f"حدث خطأ أثناء التحميل: {e}")

    # Function to update download progress
    def update_progress(self, d):
        if d['status'] == 'finished':
            self.downloaded_videos += 1
            progress = int((self.downloaded_videos / self.total_videos) * 100)
            self.progress_bar.setValue(progress)
            self.status_label.setText(f"عدد الفيديوهات التي تم تحميلها: {self.downloaded_videos} / {self.total_videos}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = YouTubeDownloaderApp()
    window.show()
    sys.exit(app.exec())