# 📦 Installation Guide

## 🚀 Quick Install (Windows)

### Method 1: One-click Installer (Recommended)
**Using our auto-installer is the easiest way:**

```bash
# Direct download and run
cd "%APPDATA%\Sublime Text\Packages"
powershell -Command "Invoke-WebRequest -Uri 'https://raw.githubusercontent.com/philimot/sublime-cpp-setup/main/install.bat' -OutFile 'install.bat'"
install.bat
```

**Or manually:**
1. **Download** [install.bat](install.bat)
2. **Right-click** → "Run as administrator"
3. **Follow** the on-screen instructions

### Method 2: Manual Git Clone
```bash
# Open Command Prompt as Administrator
cd "%APPDATA%\Sublime Text\Packages"

# Backup existing settings
if exist User ren User User.backup.%date:~10,4%%date:~4,2%%date:~7,2%

# Clone the repository
git clone https://github.com/philimot/sublime-cpp-setup.git User

# Restart Sublime Text
```

### Method 3: Download ZIP
1. **Download** [ZIP archive](https://github.com/philimot/sublime-cpp-setup/archive/refs/heads/main.zip)
2. **Extract** to: `%APPDATA%\Sublime Text\Packages\User`
3. **Restart** Sublime Text

## ⚙️ Requirements

### Required Software
- **Sublime Text 3 or 4** (Download: https://www.sublimetext.com/)
- **C++ Compiler**: MSYS2 UCRT64 (recommended) or MinGW-w64

### C++ Compiler Setup (MSYS2)
1. **Download** from: https://www.msys2.org/
2. **Install** to: `C:\msys64`
3. **Add to PATH**: `C:\msys64\ucrt64\bin`
4. **Restart** your computer

## 🎮 First Run Guide

### Step-by-Step Setup
1. **Open** any `.cpp` file in Sublime Text
2. **Press** `Ctrl+Alt+L` → Creates 3-panel layout
3. **Add input** to `.in` file (right-top panel)
4. **Press** `F5` → Compile & run
5. **View output** in `.out` file (right-bottom panel)

### Test Configuration
Run this quick test to verify everything works:
```bash
# Create test files
echo #include ^<iostream^> > test.cpp
echo using namespace std; >> test.cpp
echo int main^(^) { int a,b; cin^>^>a^>^>b; cout^<^<"Sum: "^<^<a+b^<^<endl; return 0; } >> test.cpp
echo 10 20 > test.in

# Open test.cpp in Sublime
# Press Ctrl+Alt+L then F5
```

## 🎯 Features Overview

### Layout & Navigation
- `Ctrl+Alt+L` - Auto 3-panel layout
- `Ctrl+1/2/3` - Switch between panels
- Auto-create `.in/.out` files

### Compile & Run
- `F5` - Compile & run with input
- `F6` - Compile only
- `F7` - Run only
- `Ctrl+F5` - Refresh output

### File Management
- `Ctrl+Shift+L` - Quick create .in/.out
- `Ctrl+Shift+C` - Clear output file
- `Ctrl+Shift+T` - Create test files

## 🔧 Troubleshooting

### Common Issues & Solutions

| Problem | Solution |
|---------|----------|
| **"g++ not found"** | Install MSYS2 and add `C:\msys64\ucrt64\bin` to PATH |
| **Shortcuts not working** | Restart Sublime Text after installation |
| **Layout not appearing** | Save the .cpp file first, then press `Ctrl+Alt+L` |
| **Build system not selected** | Go to `Tools` → `Build System` → Select `C++ Auto Layout` |
| **No output in panel** | Check if `.in` file exists in same directory |

### Debug Commands
```python
# Open Sublime Console (Ctrl+`)
import sublime
print("Plugin loaded:", sublime.active_window() != None)

# Check build system
print("Build system:", sublime.active_window().active_view().settings().get('build_system'))
```

## 📁 File Structure

```
User/
├── auto_layout.py              # Main plugin with layout system
├── C++ Auto Layout.sublime-build  # Build system configuration
├── Default.sublime-keymap      # Keyboard shortcuts (F5, Ctrl+Alt+L, etc.)
├── Preferences.sublime-settings # Editor preferences
├── Context.sublime-menu        # Right-click context menu
├── install.bat                 # Windows auto-installer
├── INSTALL.md                  # This file
└── README.md                   # Project overview
```

## 🔄 Updates & Maintenance

### Update to Latest Version
```bash
# Navigate to User folder
cd "%APPDATA%\Sublime Text\Packages\User"

# Pull latest changes
git pull origin main

# Restart Sublime Text
```

### Create Custom Modifications
1. Edit files in `Packages/User/`
2. Test your changes
3. Commit and push (if you have write access)
```bash
git add .
git commit -m "Your custom modifications"
git push origin main
```

## 🗑️ Uninstall

### Complete Removal
1. **Delete** the User folder:
   ```bash
   rmdir /s /q "%APPDATA%\Sublime Text\Packages\User"
   ```
2. **Restore backup** if needed:
   ```bash
   ren User.backup.* User
   ```
3. **Restart** Sublime Text

### Partial Removal
To remove only C++ setup but keep other settings:
1. Delete specific files:
   ```bash
   del "C++ Auto Layout.sublime-build"
   del auto_layout.py
   ```
2. Restart Sublime Text

## ❓ Need Help?

- **GitHub Issues**: https://github.com/philimot/sublime-cpp-setup/issues
- **Check README**: More details in [README.md](README.md)
- **Test First**: Always run the test procedure above

## 📄 License
This setup is distributed under the MIT License. Feel free to modify and distribute.
