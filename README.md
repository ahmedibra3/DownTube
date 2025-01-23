# DownTube - YouTube Video Downloader with Modern GUI

![Python](https://img.shields.io/badge/Python-3.x-blue)
![PySide6](https://img.shields.io/badge/PySide6-GUI-orange)
![yt-dlp](https://img.shields.io/badge/yt--dlp-YouTube%20Downloader-red)
![FFmpeg](https://img.shields.io/badge/FFmpeg-Audio%20Conversion-green)

**DownTube** is a Python-based application with a modern graphical user interface (GUI) for downloading YouTube videos or playlists in **MP4** (video) or **MP3** (audio-only) formats. Built using **PySide6** for the GUI and **yt-dlp** for downloading videos, DownTube provides a seamless and user-friendly experience.

---

## Features

- **User-Friendly Interface**: A clean and modern GUI designed with **CSS** for a seamless user experience.
- **Multiple Download Options**: Choose between downloading videos as **MP4** or **MP3**.
- **Playlist Support**: Download entire playlists with a single click.
- **Progress Tracking**: Real-time progress bar and video count (downloaded/remaining).
- **Customizable Output Path**: Users can select the directory where downloaded files will be saved.

---

## Technologies Used

- **Python**: The core programming language.
- **PySide6**: For building the graphical user interface.
- **yt-dlp**: A powerful library for downloading YouTube videos.
- **FFmpeg**: For converting videos to **MP3** format.

---

## How It Works

1. **Enter the URL**: Paste the YouTube video or playlist URL into the input field.
2. **Choose the Format**: Select either **MP4** (video) or **MP3** (audio-only).
3. **Select the Output Directory**: Choose where the downloaded files will be saved.
4. **Start Downloading**: Click the "Download" button to begin. The progress bar and video count will update in real-time.

---

## Installation

### Prerequisites

- **Python 3.x**: Make sure Python is installed on your system.
- **FFmpeg**: Required for audio conversion. Download it from [here](https://ffmpeg.org/download.html) and add it to your system's PATH.

### Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/ahmedibra3/DownTube.git
   cd DownTube
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
3. Run the application:
   ```bash
   python main.py
