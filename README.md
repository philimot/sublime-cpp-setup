### 1. Cập nhật `README.md` (Trang chủ Repository)
Bạn nên thêm các "Badges" và phần hướng dẫn nhanh cho cả 2 hệ điều hành.

```markdown
# 🚀 Sublime Text C++ Development Setup

![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey)
![Language](https://img.shields.io/badge/language-C%2B%2B17%2F20-blue)

Bộ công cụ tối ưu để lập trình C++ trên Sublime Text, hỗ trợ đa nền tảng với layout 3 màn hình tự động.

## ✨ Tính năng mới (Multi-platform)
- **Hỗ trợ đa nền tảng:** Cùng một cấu hình chạy hoàn hảo trên Windows 11 và Linux (KDE/Gnome).
- **Build System thông minh:** Tự động nhận diện OS để dùng tập lệnh biên dịch phù hợp (`.exe` trên Win, binary trên Linux).
- **Installer 1-click:** Có sẵn script cài đặt tự động cho cả Windows (`.bat`) và Linux (`.sh`).

## ⚡ Cài đặt nhanh

### 🪟 Windows
Mở CMD (Admin) và chạy:
```bash
powershell -Command "Invoke-WebRequest -Uri 'https://raw.githubusercontent.com/philimot/sublime-cpp-setup/main/install.bat' -OutFile 'install.bat'"; .\install.bat
```

### 🐧 Linux (Kubuntu/Ubuntu/Other)
Mở Terminal và chạy:
```bash
bash -c "$(curl -fsSL https://raw.githubusercontent.com/philimot/sublime-cpp-setup/main/install_linux.sh)"
```

## 🎮 Phím tắt chính
- `Ctrl + Alt + L`: Tạo layout 3 panel (Code | Input | Output).
- `F5`: Biên dịch và Chạy (tự động nhận diện file `.in`).
- `Ctrl + 1/2/3`: Di chuyển nhanh giữa các panel.
```

---

### 2. Cập nhật `INSTALL.md` (Hướng dẫn chi tiết)
Phần này cần làm rõ sự khác biệt về đường dẫn và trình biên dịch giữa 2 máy.

```markdown
## 🛠 Yêu cầu trình biên dịch

### Trên Windows
- Cài đặt **MSYS2 (UCRT64)**.
- Thêm `C:\msys64\ucrt64\bin` vào **PATH**.

### Trên Linux (Kubuntu)
- Cài đặt gói `build-essential`:
```bash
sudo apt update && sudo apt install build-essential gdb -y
```

## ⚠️ Lưu ý quan trọng cho người dùng KDE (Kubuntu)
Mặc định KDE sử dụng phím `Ctrl + Alt + L` để **Khóa màn hình**. Để sử dụng tính năng tạo Layout trong Sublime Text:
1. Vào **System Settings** -> **Shortcuts**.
2. Tìm **Session Management** hoặc **Lock Screen**.
3. Đổi phím tắt Khóa màn hình sang phím khác hoặc tắt nó đi.
```

---

### 3. Cập nhật Build System (Nếu bạn chưa thêm flags)
Đảm bảo file `C++ Auto Layout.sublime-build` của bạn có đầy đủ logic cho cả 2 bên (như chúng ta đã làm ở bước trước) để tránh lỗi `if exist` trên Linux.

---

### 4. Các bước thực hiện cập nhật lên GitHub
Bây giờ bạn dùng Git Bash (hoặc terminal trên Linux) để đẩy các thay đổi này lên:

```bash
cd "/c/Users/TDG/AppData/Roaming/Sublime Text/Packages/User"

# Thêm các thay đổi vào hướng dẫn
git add README.md INSTALL.md LINUX_KDE_INSTALL.md

# Commit với message đầy đủ
git commit -m "Docs: Update documentation for multi-platform support

- Added quick install commands for Windows and Linux
- Added KDE shortcut conflict warning
- Updated feature list to reflect cross-platform compatibility"

# Push lên GitHub
git push origin main
```

### 💡 Một mẹo nhỏ:
Bây giờ bạn đã có file `install_linux.sh` trên GitHub, mỗi khi bạn sang một máy Linux mới (như Kubuntu), bạn chỉ cần mở Konsole và gõ đúng 1 dòng này là xong cả bộ code:

```bash
curl -fsSL https://raw.githubusercontent.com/philimot/sublime-cpp-setup/main/install_linux.sh | bash
```
