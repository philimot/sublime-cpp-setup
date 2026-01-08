#!/bin/bash
echo "========================================="
echo "   Sublime Text C++ Setup - Linux Installer"
echo "   Repository: github.com/philimot/sublime-cpp-setup"
echo "========================================="
echo ""

# Check if running as root
if [ "$EUID" -eq 0 ]; then 
    echo "⚠ Please do NOT run as root/sudo"
    echo "Run as normal user: ./install_linux.sh"
    exit 1
fi

# Color codes
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Check Sublime Text
echo "[1/6] 🔍 Checking Sublime Text..."
if ! command -v subl &> /dev/null; then
    echo -e "${YELLOW}⚠ Sublime Text not found!${NC}"
    echo "Installing Sublime Text 4..."
    
    # Detect distribution
    if command -v apt &> /dev/null; then
        # Debian/Ubuntu
        wget -qO - https://download.sublimetext.com/sublimehq-pub.gpg | sudo apt-key add -
        sudo apt-add-repository "deb https://download.sublimetext.com/ apt/stable/"
        sudo apt update
        sudo apt install sublime-text -y
    elif command -v dnf &> /dev/null; then
        # Fedora
        sudo rpm -v --import https://download.sublimetext.com/sublimehq-rpm-pub.gpg
        sudo dnf config-manager --add-repo https://download.sublimetext.com/rpm/stable/x86_64/sublime-text.repo
        sudo dnf install sublime-text -y
    elif command -v pacman &> /dev/null; then
        # Arch Linux
        sudo pacman -S sublime-text --noconfirm
    else
        echo -e "${RED}❌ Unsupported Linux distribution${NC}"
        echo "Please install Sublime Text manually from:"
        echo "https://www.sublimetext.com/download"
        exit 1
    fi
    echo -e "${GREEN}✅ Sublime Text installed${NC}"
else
    echo -e "${GREEN}✅ Sublime Text found${NC}"
fi

# Install dependencies
echo "[2/6] 📦 Installing dependencies..."
if command -v apt &> /dev/null; then
    sudo apt update
    sudo apt install -y git g++ build-essential gdb make
elif command -v dnf &> /dev/null; then
    sudo dnf install -y git gcc-c++ make gdb
elif command -v pacman &> /dev/null; then
    sudo pacman -S git gcc make gdb --noconfirm
fi
echo -e "${GREEN}✅ Dependencies installed${NC}"

# Configure Sublime path
echo "[3/6] ⚙️ Configuring Sublime Text..."
ST_PATH="$HOME/.config/sublime-text"
mkdir -p "$ST_PATH/Packages"

# Backup existing
echo "[4/6] 💾 Backing up existing config..."
if [ -d "$ST_PATH/Packages/User" ]; then
    BACKUP="$ST_PATH/Packages/User.backup.$(date +%Y%m%d_%H%M%S)"
    cp -r "$ST_PATH/Packages/User" "$BACKUP"
    echo -e "${GREEN}✅ Backup created: $(basename "$BACKUP")${NC}"
    echo "   To restore: mv '$BACKUP' '$ST_PATH/Packages/User'"
else
    echo "ℹ No existing User folder found"
fi

# Clone repository
echo "[5/6] ⬇ Downloading C++ setup..."
cd "$ST_PATH/Packages"
rm -rf "User" 2>/dev/null
git clone https://github.com/philimot/sublime-cpp-setup.git "User"

if [ $? -eq 0 ]; then
    echo -e "${GREEN}✅ Repository cloned successfully${NC}"
else
    echo -e "${RED}❌ Git clone failed${NC}"
    echo "Trying alternative method..."
    curl -L https://github.com/philimot/sublime-cpp-setup/archive/main.tar.gz | tar -xz
    mv sublime-cpp-setup-main User
    echo -e "${YELLOW}⚠ Downloaded via curl (git not available)${NC}"
fi

# Create test files
echo "[6/6] 🧪 Creating test files..."
cat > "$HOME/Desktop/test.cpp" << 'TEST_CPP'
#include <iostream>
using namespace std;

int main() {
    cout << "=== C++ Setup Test ===" << endl;
    cout << "✅ Linux Installation Successful!" << endl;
    cout << "   Distro: $(lsb_release -ds 2>/dev/null || uname -s)" << endl;
    cout << "   Compiler: $(g++ --version | head -1)" << endl;
    cout << endl;
    
    int a, b;
    cout << "Enter two numbers: ";
    cin >> a >> b;
    cout << "Sum: " << a + b << endl;
    cout << "Product: " << a * b << endl;
    cout << "=== TEST COMPLETE ===" << endl;
    return 0;
}
TEST_CPP

cat > "$HOME/Desktop/test.in" << 'TEST_IN'
15 25
TEST_IN

# Make test.cpp executable (for direct testing)
chmod +x "$HOME/Desktop/test.cpp" 2>/dev/null

echo ""
echo "========================================="
echo -e "         ${GREEN}🎉 INSTALLATION COMPLETE!${NC}"
echo "========================================="
echo ""
echo -e "${GREEN}✅ What was installed:${NC}"
echo "  ✓ C++ Auto Layout plugin"
echo "  ✓ Multi-platform build system"
echo "  ✓ Keyboard shortcuts (F5, Ctrl+Alt+L)"
echo "  ✓ Linux-specific configuration"
echo ""
echo -e "${YELLOW}🚀 Quick Start Guide:${NC}"
echo "  1. RESTART Sublime Text"
echo "  2. Open test.cpp from your Desktop:"
echo "     subl ~/Desktop/test.cpp"
echo "  3. Press Ctrl+Alt+L (3-panel layout)"
echo "  4. Press F5 to compile & run"
echo ""
echo -e "${YELLOW}🔧 Important for Linux:${NC}"
echo "  • If Ctrl+Alt+L doesn't work, check KDE/GNOME shortcuts"
echo "  • Default shortcut: KDE uses Ctrl+Alt+L for lock screen"
echo "  • Disable conflicting shortcuts in System Settings"
echo ""
echo -e "${YELLOW}📚 Documentation:${NC}"
echo "  • Full guide: ~/.config/sublime-text/Packages/User/LINUX_KDE_INSTALL.md"
echo "  • GitHub: https://github.com/philimot/sublime-cpp-setup"
echo ""
echo "To test immediately:"
echo "  cd ~/Desktop && g++ test.cpp -o test && ./test < test.in"
echo ""