
```markdown
# 🐧 Hướng Dẫn Cài Đặt Trên Kubuntu Linux (KDE Plasma)

Tài liệu này hướng dẫn chi tiết cách thiết lập môi trường lập trình C++ tối ưu trên Linux, đặc biệt là môi trường KDE Plasma (Kubuntu).

## 📋 Mục Lục
1. [Yêu Cầu Hệ Thống](#️-yêu-cầu-hệ-thống)
2. [Phương Pháp Cài Đặt](#-phương-pháp-cài-đặt)
3. [Cấu Hình Compiler](#-cấu-hình-compiler)
4. [Sử Dụng Lần Đầu & Sửa Phím Tắt](#-sử-dụng-lần-đầu--sửa-phím-tắt)
5. [Troubleshooting](#-troubleshooting)
6. [Gỡ Cài Đặt](#-gỡ-cài-đặt)

---

## 🖥️ Yêu Cầu Hệ Thống

### Phần Mềm Bắt Buộc
*   **Hệ điều hành:** Kubuntu 20.04 LTS trở lên (hoặc các bản Linux khác dùng KDE/Gnome).
*   **Sublime Text 4:** Khuyến nghị cài bản mới nhất.
*   **Git:** Để đồng bộ cấu hình từ GitHub.
*   **build-essential:** Bộ công cụ biên dịch (g++, gcc, make).

---

## 🚀 Phương Pháp Cài Đặt

### 🔸 Phương Pháp 1: Cài đặt tự động (Khuyến Nghị)

Đây là cách nhanh nhất. Script sẽ tự động cài trình biên dịch, backup cấu hình cũ và tải cấu hình mới.

**Chạy lệnh duy nhất sau trong Terminal (Konsole):**
```bash
bash -c "$(curl -fsSL https://raw.githubusercontent.com/philimot/sublime-cpp-setup/main/install_linux.sh)"
```

---

### 🔸 Phương Pháp 2: Cài Đặt Thủ Công

**Bước 1: Cài đặt các công cụ cần thiết**
```bash
sudo apt update
sudo apt install -y git g++ build-essential gdb make
```

**Bước 2: Clone Repository**
```bash
# Di chuyển vào thư mục Packages của Sublime Text
cd ~/.config/sublime-text/Packages

# Backup cấu hình cũ nếu có
if [ -d "User" ]; then
    mv User User.backup.$(date +%Y%m%d)
fi

# Tải cấu hình từ GitHub
git clone https://github.com/philimot/sublime-cpp-setup.git User
```

---

## ⚙️ Cấu Hình Compiler

Đảm bảo máy bạn đã có `g++`. Kiểm tra bằng lệnh:
```bash
g++ --version
```
Nếu chưa có, hãy chạy:
```bash
sudo apt install g++
```

---

## 🎮 Sử Dụng Lần Đầu & Sửa Phím Tắt

### ⚠️ Quan trọng: Sửa xung đột phím tắt KDE
Mặc định, KDE Plasma sử dụng `Ctrl + Alt + L` để **Khóa màn hình**. Bạn phải tắt nó để phím tắt tạo Layout trong Sublime Text hoạt động.

**Cách 1: Chạy lệnh Terminal (Nhanh nhất)**
```bash
# Tắt phím tắt khóa màn hình
kwriteconfig5 --file kglobalshortcutsrc --group "ksmserver" --key "Lock Session" "none"

# Áp dụng thay đổi ngay lập tức
kquitapp5 kglobalaccel && sleep 2 && kglobalaccel5
```

**Cách 2: Chỉnh qua giao diện (GUI)**
1. Mở **System Settings** -> **Shortcuts**.
2. Tìm từ khóa **"Lock Session"**.
3. Chọn nó và đặt thành **None** hoặc đổi sang phím khác.

### 🧪 Test Tính Năng
1. Mở Sublime Text bằng lệnh `subl` hoặc menu ứng dụng.
2. Mở một file `.cpp`.
3. Nhấn **Ctrl + Alt + L** → Layout 3 màn hình sẽ xuất hiện.
4. Nhấn **F5** → Code sẽ được biên dịch và chạy tự động.

---

## 🛠️ Cấu Hình Nâng Cao Cho KDE

### Dolphin Integration (Menu chuột phải)
Để mở nhanh file C++ từ trình quản lý file Dolphin:
```bash
mkdir -p ~/.local/share/kservices5/ServiceMenus/

cat > ~/.local/share/kservices5/ServiceMenus/sublimecpp.desktop << EOF
[Desktop Entry]
Type=Service
ServiceTypes=KonqPopupMenu/Plugin
MimeType=text/x-c++src;
Actions=OpenWithSublimeCPP;
X-KDE-Priority=TopLevel

[Desktop Action OpenWithSublimeCPP]
Name=Open with Sublime C++ Setup
Icon=sublime-text
Exec=subl %f
EOF
```

---

## 🐛 Troubleshooting

| Lỗi | Cách Khắc Phục |
| :--- | :--- |
| **Không tìm thấy đường dẫn cấu hình** | Nếu bạn cài Sublime qua **Snap**, đường dẫn sẽ là `~/snap/sublime-text/current/.config/sublime-text`. Hãy di chuyển file vào đó. |
| **g++ not found** | Chạy `sudo apt install build-essential`. |
| **Lỗi Permission denied** | Chạy `sudo chown -R $USER:$USER ~/.config/sublime-text/`. |

---

## 🎉 Danh Sách Phím Tắt
| Phím tắt | Chức năng |
| :--- | :--- |
| **Ctrl + Alt + L** | Tự động chia 3 màn hình (Layout) |
| **F5** | Biên dịch và Chạy (Compile & Run) |
| **Ctrl + 1/2/3** | Di chuyển giữa Code / Input / Output |
| **Ctrl + Shift + L** | Tạo nhanh file .in và .out |

---
*Tài liệu được cập nhật bởi philimot - 2024*
```

---

### 🚀 Các bước cuối cùng để đưa lên GitHub:

1.  Mở **Git Bash** trên Windows (hoặc Terminal trên Linux).
2.  Chạy các lệnh sau:

```bash
cd "/c/Users/TDG/AppData/Roaming/Sublime Text/Packages/User"

# Thêm file đã sửa
git add LINUX_KDE_INSTALL.md

# Tạo commit
git commit -m "Docs: Complete and optimize Linux KDE guide"

# Đẩy lên GitHub
git push origin main
```
