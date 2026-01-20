```markdown
# 📥 Hướng dẫn cài đặt chi tiết (Detailed Installation)

Tài liệu này hướng dẫn cách thiết lập môi trường lập trình C++ trên Sublime Text cho cả Windows và Linux.

---

## 📌 1. Yêu cầu về Trình biên dịch (Prerequisites)

Để code chạy được, bạn cần cài đặt trình biên dịch (compiler) phù hợp với hệ điều hành đang dùng:

### 🪟 Trên Windows (Khuyến nghị MSYS2)
1. Tải và cài đặt [MSYS2](https://www.msys2.org/).
2. Mở **MSYS2 UCRT64** và chạy lệnh: 
   `pacman -S --needed base-devel mingw-w64-ucrt-x86_64-toolchain`
3. Thêm đường dẫn sau vào **Environment Variables (PATH)** của Windows:
   `C:\msys64\ucrt64\bin`

### 🐧 Trên Linux (Ubuntu/Kubuntu/Debian)
1. Mở Terminal (Konsole) và cài đặt bộ công cụ build:
   ```bash
   sudo apt update && sudo apt install build-essential gdb -y
   ```

---

## 🚀 2. Cài đặt tự động (Automated Install)

Đây là cách nhanh nhất để cài đặt toàn bộ cấu hình (Plugin, Build System, Shortcuts).

### 🔹 Cách làm trên Windows
Tải file [install.bat](install.bat), chuột phải và chọn **Run as Administrator**.

### 🔹 Cách làm trên Linux
Mở Terminal và chạy lệnh:
```bash
bash -c "$(curl -fsSL https://raw.githubusercontent.com/philimot/sublime-cpp-setup/main/install_linux.sh)"
```

---

## 📂 3. Cài đặt thủ công (Manual Install)

Nếu bạn không muốn dùng script, hãy làm theo các bước sau:

1. Truy cập thư mục cấu hình của Sublime Text:
   - **Windows:** `%APPDATA%\Sublime Text\Packages\`
   - **Linux:** `~/.config/sublime-text/Packages/`
2. Clone repository này vào thư mục `User`:
   ```bash
   git clone https://github.com/philimot/sublime-cpp-setup.git User
   ```
3. Khởi động lại Sublime Text.

---

## ⚠️ 4. Lưu ý quan trọng về Phím tắt (Shortcuts)

Hệ thống sử dụng phím tắt mặc định là `Ctrl + Alt + L` để chia layout.

*   **Trên Windows:** Hoạt động ngay lập tức.
*   **Trên Linux (KDE Plasma):** Phím này thường bị trùng với lệnh **Lock Screen (Khóa màn hình)**.
    *   *Cách sửa:* Vào **System Settings** -> **Shortcuts** -> Tìm **Lock Session** và đổi sang phím khác hoặc Disable nó.

---

## 🎮 5. Kiểm tra sau khi cài đặt

1. Mở Sublime Text, tạo một file `test.cpp`.
2. Nhấn `Ctrl + Alt + L` để chia 3 màn hình.
3. Nhấn `F5` để biên dịch và chạy.
4. Nếu hiện thông báo `✅ COMPILE SUCCESS`, chúc mừng bạn đã thành công!

---

## 📖 Tài liệu bổ sung
- [Hướng dẫn riêng cho Linux KDE](LINUX_KDE_INSTALL.md)
- [Quay lại Trang chủ README](README.md)
```

---