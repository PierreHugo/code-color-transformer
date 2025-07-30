# 🎨 CodeColorTransformer

A simple desktop application that automatically transforms color values in **SwiftUI code**.  
Currently, only **SwiftUI** is supported, but future updates will add support for additional languages.

![Preview](https://dummyimage.com/800x400/1e1e1e/ffffff&text=CodeColorTransformer+UI)

## 🚀 Features
- Minimal interface with two side-by-side code editors (input/output)
- Automatically replaces SwiftUI `Color.xxx` values with predefined colors
- "Transform" button and `Ctrl+Enter` (or `Cmd+Enter` on macOS) shortcut

## 🛠 Installation

### Clone the repository
```
git clone https://github.com/PierreHugo/CodeColorTransformer.git
cd CodeColorTransformer
```

### Run directly with Python
Make sure you have **Python 3.8+** installed:
```
python main.py
```

### (Optional) Build a standalone executable
If you want to create a `.exe` (Windows) :
```
pip install pyinstaller
pyinstaller --noconsole --onefile --windowed --name CodeColor main.py
```
or `.app` (macOS) :
```
python3 -m pip install pyinstaller
python3 -m PyInstaller --noconsole --onefile --windowed --name CodeColor main.py
```

Your executable will be located in the `dist/` folder.

## 📦 Direct Download (Recommended)
If you don't want to install Python, go to the [Releases](../../releases) page and download the latest version:
- **Windows:** `CodeColor.exe`
- **macOS:** `CodeColor.app`

## 🖼 Example

### Input:
```
.foregroundStyle(Color.Background.primary)
.background(Color.red)
.overlay(Color.secondary.opacity(0.5))
```

### Output:
```
.foregroundStyle(Color.red)
.background(Color.blue)
.overlay(Color.green.opacity(0.5))
```

## 👨‍💻 Author
Created by **[@PierreHugo](https://github.com/PierreHugo)** ❤️  

## 📜 License
MIT License - feel free to use, modify, and contribute!