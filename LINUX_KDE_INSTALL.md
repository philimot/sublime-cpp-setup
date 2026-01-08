# 🐧 Hướng Dẫn Cài Đặt Trên Kubuntu Linux (KDE Plasma)
... [# 🐧 Hướng Dẫn Cài Đặt Trên Kubuntu Linux (KDE Plasma)

## 📋 Mục Lục
1. [Yêu Cầu Hệ Thống](#️-yêu-cầu-hệ-thống)
2. [Phương Pháp Cài Đặt](#-phương-pháp-cài-đặt)
3. [Cấu Hình Compiler](#-cấu-hình-compiler)
4. [Sử Dụng Lần Đầu](#-sử-dụng-lần-đầu)
5. [Troubleshooting](#-troubleshooting)
6. [Gỡ Cài Đặt](#-gỡ-cài-đặt)

---

## 🖥️ Yêu Cầu Hệ Thống

### Phần Mềm Bắt Buộc
*   **Kubuntu 20.04 LTS** trở lên (hoặc distro dựa trên Ubuntu với KDE Plasma).
*   **Sublime Text 4** (khuyến nghị) hoặc Sublime Text 3.
*   **Git** - Hệ thống quản lý phiên bản.
*   **g++ compiler** - Trình biên dịch C++.

### Kiểm Tra Hệ Thống
```bash
# Kiểm tra phiên bản hệ điều hành
lsb_release -a

# Kiểm tra KDE Plasma
plasmashell --version

# Kiểm tra dung lượng trống
df -h ~/
```

---

## 🚀 Phương Pháp Cài Đặt

### 🔸 Phương Pháp 1: Auto-Installer Script (Khuyến Nghị)

**Bước 1: Tải Installer Script**
```bash
# Mở Konsole (Terminal)
# Tải installer từ GitHub
curl -L -o ~/Downloads/install_cpp_sublime.sh \
https://raw.githubusercontent.com/philimot/sublime-cpp-setup/main/install_linux.sh

# Nếu không có sẵn, tạo script thủ công
cat > ~/Downloads/install_cpp_sublime.sh << 'EOF'
#!/bin/bash
echo "========================================="
echo "   Sublime Text C++ Setup for Linux KDE"
echo "========================================="
echo ""

# Check Sublime Text
echo "[1/6] Checking Sublime Text..."
if ! command -v subl &> /dev/null; then
    echo "❌ Sublime Text not installed!"
    echo "Installing Sublime Text 4..."
    sudo snap install sublime-text --classic
    if [ $? -ne 0 ]; then
        echo "⚠ Snap not available, installing via apt..."
        wget -qO - https://download.sublimetext.com/sublimehq-pub.gpg | sudo apt-key add -
        sudo apt-add-repository "deb https://download.sublimetext.com/ apt/stable/"
        sudo apt update
        sudo apt install sublime-text
    fi
fi
echo "✅ Sublime Text installed"

# Install dependencies
echo "[2/6] Installing dependencies..."
sudo apt update
sudo apt install -y git g++ build-essential gdb make

# Configure Sublime path
echo "[3/6] Configuring Sublime Text..."
ST_PATH="$HOME/.config/sublime-text"
mkdir -p "$ST_PATH/Packages"

# Backup existing
echo "[4/6] Backing up existing config..."
if [ -d "$ST_PATH/Packages/User" ]; then
    BACKUP="$ST_PATH/Packages/User.backup.$(date +%Y%m%d_%H%M%S)"
    cp -r "$ST_PATH/Packages/User" "$BACKUP"
    echo "✅ Backup: $(basename $BACKUP)"
fi

# Clone repository
echo "[5/6] Downloading C++ setup..."
cd "$ST_PATH/Packages"
rm -rf User 2>/dev/null
git clone https://github.com/philimot/sublime-cpp-setup.git User

# Create test files
echo "[6/6] Creating test files..."
cat > "$HOME/Desktop/test.cpp" << 'TEST'
#include <iostream>
using namespace std;

int main() {
    cout << "=== C++ Setup Test ===" << endl;
    cout << "✅ Linux KDE Installation Successful!" << endl;
    int a, b;
    cin >> a >> b;
    cout << "Sum: " << a + b << endl;
    cout << "Product: " << a * b << endl;
    return 0;
}
TEST

echo "15 25" > "$HOME/Desktop/test.in"

echo ""
echo "========================================="
echo "         🎉 INSTALLATION COMPLETE!"
echo "========================================="
echo ""
echo "Quick Test:"
echo "1. subl ~/Desktop/test.cpp"
echo "2. Press Ctrl+Alt+L"
echo "3. Press F5"
echo ""
EOF
```

**Bước 2: Chạy Installer**
```bash
# Cấp quyền thực thi
chmod +x ~/Downloads/install_cpp_sublime.sh

# Chạy với quyền user (KHÔNG dùng sudo)
bash ~/Downloads/install_cpp_sublime.sh
```

**Bước 3: Kiểm Tra Cài Đặt**
```bash
# Kiểm tra file đã được cài
ls -la ~/.config/sublime-text/Packages/User/

# Kiểm tra test files
ls ~/Desktop/*.cpp ~/Desktop/*.in
```

---

### 🔸 Phương Pháp 2: Cài Đặt Thủ Công

**Bước 1: Cài Đặt Dependencies**
```bash
# Cập nhật package list
sudo apt update
sudo apt upgrade -y

# Cài Sublime Text (nếu chưa có)
sudo snap install sublime-text --classic

# Cài compiler và tools
sudo apt install -y \
    git \
    g++ \
    build-essential \
    gdb \
    make \
    cmake \
    pkg-config
```

**Bước 2: Clone Repository**
```bash
# Tạo thư mục Packages nếu chưa có
mkdir -p ~/.config/sublime-text/Packages
cd ~/.config/sublime-text/Packages

# Backup configuration cũ
if [ -d "User" ]; then
    timestamp=$(date +%Y%m%d_%H%M%S)
    mv User "User.backup.$timestamp"
    echo "✅ Đã backup cấu hình cũ: User.backup.$timestamp"
fi

# Clone từ GitHub
git clone https://github.com/philimot/sublime-cpp-setup.git User
```

---

## ⚙️ Cấu Hình Compiler

### Kiểm Tra Compiler
```bash
# Kiểm tra g++ đã cài chưa
g++ --version

# Nếu chưa có, cài đặt bản mới nhất (g++-12)
sudo apt install g++-12 gcc-12

# Chọn phiên bản mặc định
sudo update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-12 100
sudo update-alternatives --install /usr/bin/g++ g++ /usr/bin/g++-12 100
```

### Test Compiler
```bash
# Tạo file test đơn giản
cat > /tmp/test_compiler.cpp << 'EOF'
#include <iostream>
int main() {
    std::cout << "Compiler works!" << std::endl;
    return 0;
}
EOF

# Biên dịch và chạy
g++ /tmp/test_compiler.cpp -o /tmp/test_compiler
/tmp/test_compiler
```

---

## 🎮 Sử Dụng Lần Đầu

### Bước 1: Mở Sublime Text
```bash
# Từ terminal
subl ~/Desktop/test.cpp
```

### Bước 2: Cấu Hình KDE Shortcuts (Quan Trọng)
KDE Plasma thường sử dụng `Ctrl+Alt+L` để khóa màn hình. Bạn cần thay đổi shortcut này để dùng cho Sublime:

1.  Mở **System Settings**.
2.  Chọn **Shortcuts** -> **Global Shortcuts**.
3.  Tìm **Session Management** hoặc **Screen Locking**.
4.  Đổi phím tắt **Lock Session** sang phím khác hoặc Disable nó.

Hoặc dùng lệnh terminal:
```bash
kwriteconfig5 --file kglobalshortcutsrc --group "ksmserver" --key "Lock Session" "none"
```

### Bước 3: Test Tính Năng
1.  Mở `test.cpp` trong Sublime.
2.  Nhấn **Ctrl+Alt+L** → Chia 3 màn hình (Layout).
3.  Nhập dữ liệu vào `test.in`.
4.  Nhấn **F5** → Biên dịch và chạy.
5.  Xem kết quả tại `test.out`.

---

## 🐛 Troubleshooting

| Lỗi | Cách Khắc Phục |
| :--- | :--- |
| **g++ not found** | Chạy `sudo apt install build-essential` |
| **Shortcut không chạy** | Kiểm tra xung đột phím tắt trong KDE System Settings |
| **Permission Denied** | Chạy `sudo chown -R $USER:$USER ~/.config/sublime-text/` |
| **Git Clone Failed** | Kiểm tra kết nối internet hoặc dùng phương pháp tải ZIP |

---

## 🛠️ Cấu Hình Nâng Cao Cho KDE

### Dolphin Integration (Menu chuột phải)
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
Name=Open with Sublime C++
Icon=sublime-text
Exec=subl %f
EOF
```

---

## 🗑️ Gỡ Cài Đặt
```bash
# Xóa cấu hình C++ setup
rm -rf ~/.config/sublime-text/Packages/User

# Khôi phục backup nếu có
latest_backup=$(ls -td ~/.config/sublime-text/Packages/User.backup.* 2>/dev/null | head -1)
if [ -n "$latest_backup" ]; then
    mv "$latest_backup" ~/.config/sublime-text/Packages/User
fi

# Xóa test files
rm -f ~/Desktop/test.cpp ~/Desktop/test.in ~/Desktop/test.out
```

---

## 🎉 Bắt Đầu Code!
```text
┌─────────────────────────────────────┐
│         ESSENTIAL SHORTCUTS         │
├─────────────────────────────────────┤
│ Ctrl + Alt + L  → 3-panel layout    │
│ F5              → Compile & Run     │
│ Ctrl + 1        → Focus code panel  │
│ Ctrl + 2        → Focus input panel │
│ Ctrl + 3        → Focus output panel│
└─────────────────────────────────────┘] ...
└─────────────────────────────────────┘
