"""
AUTO LAYOUT FOR C++ DEVELOPMENT
Version 2.0 - Complete with Auto Refresh
Author: Sublime Text C++ Setup
"""

import sublime
import sublime_plugin
import os
import subprocess
import threading
import time


# ==============================================
# 1. AUTO LAYOUT SYSTEM
# ==============================================

class AutoCppLayoutCommand(sublime_plugin.TextCommand):
    """Tự động tạo layout 3 panel cho C++ development"""

    def run(self, edit):
        window = self.view.window()
        current_file = self.view.file_name()

        if not current_file:
            sublime.message_dialog("Please save the file first!")
            return

        # Chỉ áp dụng cho file .cpp
        if not current_file.endswith('.cpp'):
            sublime.message_dialog("This command only works with .cpp files!")
            return

        base_name = current_file[:-4]  # Bỏ .cpp
        in_file = base_name + '.in'
        out_file = base_name + '.out'

        # 1. Tạo layout 3 panel
        window.run_command("set_layout", {
            "cols": [0.0, 0.7, 1.0],  # Code 70%, Input/Output 30%
            "rows": [0.0, 0.5, 1.0],  # Input/Output chia đôi chiều dọc
            "cells": [
                [0, 0, 1, 2],  # Panel 0: Code (trái, full height)
                [1, 0, 2, 1],  # Panel 1: Input (phải trên)
                [1, 1, 2, 2]  # Panel 2: Output (phải dưới)
            ]
        })

        # 2. Mở file .in ở panel 1 (phải trên)
        if os.path.exists(in_file):
            input_view = window.open_file(in_file)
            window.set_view_index(input_view, 1, 0)
        else:
            # Tạo file .in mới nếu chưa có
            input_view = window.new_file()
            input_view.set_name(os.path.basename(in_file))
            input_view.retarget(in_file)
            input_view.set_syntax_file("Packages/Text/Plain text.tmLanguage")
            window.set_view_index(input_view, 1, 0)

        # 3. Mở file .out ở panel 2 (phải dưới)
        if os.path.exists(out_file):
            output_view = window.open_file(out_file)
            window.set_view_index(output_view, 2, 0)
        else:
            # Tạo file .out mới
            output_view = window.new_file()
            output_view.set_name(os.path.basename(out_file))
            output_view.retarget(out_file)
            output_view.set_syntax_file("Packages/Text/Plain text.tmLanguage")
            output_view.set_read_only(True)  # Chỉ đọc
            window.set_view_index(output_view, 2, 0)

        # 4. Di chuyển focus về code editor
        window.focus_view(self.view)

        # 5. Hiển thị thông báo
        sublime.status_message("✅ Auto layout created! Code(left) | Input(top-right) | Output(bottom-right)")


# ==============================================
# 2. AUTO LAYOUT ON LOAD
# ==============================================

class AutoLayoutOnLoad(sublime_plugin.EventListener):
    """Tự động tạo layout khi mở file .cpp"""

    def on_load(self, view):
        # Chỉ tự động với file .cpp
        if view.file_name() and view.file_name().endswith('.cpp'):
            # Kiểm tra setting có bật auto layout không
            settings = sublime.load_settings("Preferences.sublime-settings")
            if settings.get("cpp_auto_layout", True):
                # Chờ 100ms để file load xong
                sublime.set_timeout(lambda: view.run_command("auto_cpp_layout"), 100)


# ==============================================
# 3. QUICK INPUT/OUTPUT CREATION
# ==============================================

class QuickInputOutputCommand(sublime_plugin.TextCommand):
    """Nhanh chóng tạo file .in/.out và mở layout"""

    def run(self, edit):
        window = self.view.window()
        current_file = self.view.file_name()

        if not current_file or not current_file.endswith('.cpp'):
            return

        base_name = current_file[:-4]
        in_file = base_name + '.in'
        out_file = base_name + '.out'

        # Tạo file .in nếu chưa có
        if not os.path.exists(in_file):
            with open(in_file, 'w', encoding='utf-8') as f:
                f.write("// Input data for " + os.path.basename(current_file) + "\n")
                f.write("// Add your test cases here\n\n")
                f.write("Sample input:\n")
                f.write("10 20\n")
                f.write("Hello World\n")

        # Tạo file .out nếu chưa có
        if not os.path.exists(out_file):
            with open(out_file, 'w', encoding='utf-8') as f:
                f.write("// Output will appear here after running\n")
                f.write("// Last run: " + time.strftime("%Y-%m-%d %H:%M:%S") + "\n\n")

        # Tạo layout
        self.view.run_command("auto_cpp_layout")

        sublime.status_message("✅ Created .in/.out files and layout!")


# ==============================================
# 4. PANEL NAVIGATION
# ==============================================

class SwitchToCodePanelCommand(sublime_plugin.TextCommand):
    """Chuyển focus về panel code"""

    def run(self, edit):
        window = self.view.window()
        # Tìm view chứa file .cpp
        for view in window.views():
            if view.file_name() and view.file_name().endswith('.cpp'):
                window.focus_view(view)
                window.focus_group(0)  # Focus group 0 (code panel)
                break


class SwitchToInputPanelCommand(sublime_plugin.TextCommand):
    """Chuyển focus về panel input"""

    def run(self, edit):
        window = self.view.window()
        window.focus_group(1)  # Focus group 1 (input panel)


class SwitchToOutputPanelCommand(sublime_plugin.TextCommand):
    """Chuyển focus về panel output"""

    def run(self, edit):
        window = self.view.window()
        window.focus_group(2)  # Focus group 2 (output panel)


# ==============================================
# 5. FILE MANAGEMENT
# ==============================================

class ClearOutputCommand(sublime_plugin.TextCommand):
    """Xóa nội dung file .out"""

    def run(self, edit):
        current_file = self.view.file_name()
        if not current_file:
            return

        # Tìm file .out tương ứng
        if current_file.endswith('.cpp'):
            base_name = current_file[:-4]
            out_file = base_name + '.out'
        elif current_file.endswith('.in'):
            base_name = current_file[:-3]
            out_file = base_name + '.out'
        else:
            return

        # Xóa nội dung file .out
        if os.path.exists(out_file):
            with open(out_file, 'w', encoding='utf-8') as f:
                f.write("// Output cleared at " + time.strftime("%H:%M:%S") + "\n\n")

            # Refresh trong Sublime nếu đang mở
            window = self.view.window()
            for view in window.views():
                if view.file_name() == out_file:
                    view.run_command("revert")

            sublime.status_message("🧹 Cleared output file")


class CreateTestFilesCommand(sublime_plugin.TextCommand):
    """Tạo bộ test files đầy đủ"""

    def run(self, edit):
        current_file = self.view.file_name()
        if not current_file or not current_file.endswith('.cpp'):
            return

        base_name = current_file[:-4]
        files_to_create = {
            '.in': 'Input test cases',
            '.out': 'Program output',
            '.ans': 'Expected answer',
            '.txt': 'Additional notes'
        }

        created = []
        for ext, description in files_to_create.items():
            file_path = base_name + ext
            if not os.path.exists(file_path):
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(f"// {description} for {os.path.basename(current_file)}\n")
                    f.write(f"// Created: {time.strftime('%Y-%m-%d %H:%M:%S')}\n\n")
                created.append(ext)

        if created:
            sublime.message_dialog(f"✅ Created files: {', '.join(created)}")
            self.view.run_command("auto_cpp_layout")
        else:
            sublime.message_dialog("All test files already exist!")


# ==============================================
# 6. AUTO REFRESH OUTPUT SYSTEM
# ==============================================

class RefreshOutputCommand(sublime_plugin.TextCommand):
    """Tự động refresh file .out sau khi build xong"""

    def run(self, edit):
        window = self.view.window()
        current_file = self.view.file_name()

        if not current_file:
            return

        # Tìm file .out tương ứng
        if current_file.endswith('.cpp'):
            base_name = current_file[:-4]
            out_file = base_name + '.out'
        elif current_file.endswith('.in'):
            base_name = current_file[:-3]
            out_file = base_name + '.out'
        else:
            return  # Không phải file .cpp hay .in

        # Kiểm tra file .out tồn tại
        if not os.path.exists(out_file):
            return

        # Refresh tất cả views đang mở file .out
        refreshed = False
        for view in window.views():
            if view.file_name() == out_file:
                # Lưu vị trí scroll hiện tại
                viewport_position = view.viewport_position()

                # Reload file từ disk
                view.run_command("revert")

                # Khôi phục vị trí scroll
                sublime.set_timeout(lambda v=view, pos=viewport_position:
                                    v.set_viewport_position(pos, False), 10)

                # Di chuyển cursor đến cuối file
                view.show(view.size())

                # Đánh dấu đã refresh
                refreshed = True

        if refreshed:
            sublime.status_message("🔄 Output refreshed from disk")
        else:
            # Nếu file .out chưa mở, mở nó
            if window.num_groups() > 2:
                out_view = window.open_file(out_file)
                window.set_view_index(out_view, 2, 0)  # Group 2 (bottom-right)


class AutoRefreshOutput(sublime_plugin.EventListener):
    """Tự động refresh output khi file .out thay đổi"""

    def on_post_save(self, view):
        """Khi file được save"""
        if view.file_name() and view.file_name().endswith('.out'):
            # Chờ 100ms rồi refresh
            sublime.set_timeout(lambda: self.refresh_output_view(view), 100)

    def on_activated(self, view):
        """Khi chuyển sang tab/file mới"""
        if view.file_name() and view.file_name().endswith('.out'):
            # Tự động refresh khi active file .out
            sublime.set_timeout(lambda: view.run_command("revert"), 50)

    def refresh_output_view(self, view):
        """Refresh output view"""
        if view.window():
            # Tìm file .cpp tương ứng
            for v in view.window().views():
                if v.file_name() and v.file_name().endswith('.cpp'):
                    v.run_command("refresh_output")
                    break


class WatchOutputChanges(sublime_plugin.EventListener):
    """Theo dõi thay đổi file .out từ bên ngoài"""

    def on_activated_async(self, view):
        """Kiểm tra khi active view"""
        self.check_and_refresh(view)

    def check_and_refresh(self, view):
        """Kiểm tra file .out có thay đổi không"""
        if not view.file_name() or not view.file_name().endswith('.out'):
            return

        # Kiểm tra nếu file bị modified từ bên ngoài
        if view.is_dirty():
            return

        # So sánh thời gian modified
        try:
            current_mtime = os.path.getmtime(view.file_name())
        except:
            return

        # Lưu thời gian modified lần cuối
        if not hasattr(view, 'last_mtime'):
            view.last_mtime = current_mtime
            return

        if current_mtime > view.last_mtime + 0.5:  # Thay đổi ít nhất 0.5s
            view.last_mtime = current_mtime
            sublime.set_timeout(lambda: view.run_command("revert"), 100)


# ==============================================
# 7. BUILD SYSTEM INTEGRATION
# ==============================================

class PostBuildRefresh(sublime_plugin.EventListener):
    """Tự động refresh sau khi build xong"""

    def on_post_save(self, view):
        """Khi save file .cpp, tự động compile nếu enabled"""
        if not view.file_name() or not view.file_name().endswith('.cpp'):
            return

        # Kiểm tra setting auto-compile
        settings = sublime.load_settings("Preferences.sublime-settings")
        if settings.get("cpp_auto_compile", False):
            sublime.set_timeout(lambda: view.window().run_command("build"), 500)

    def on_post_build(self, v):
        """Sau khi build xong, refresh output"""
        window = v.window()
        if not window:
            return

        # Tìm view .cpp đang active
        for view in window.views():
            if view.file_name() and view.file_name().endswith('.cpp'):
                sublime.set_timeout(lambda: view.run_command("refresh_output"), 300)
                break


# ==============================================
# 8. OUTPUT PANEL MANAGEMENT
# ==============================================

class ShowOutputInPanelCommand(sublime_plugin.TextCommand):
    """Hiển thị output trong panel thay vì file"""

    def run(self, edit):
        current_file = self.view.file_name()
        if not current_file or not current_file.endswith('.cpp'):
            return

        base_name = current_file[:-4]
        out_file = base_name + '.out'

        if not os.path.exists(out_file):
            sublime.error_message("Output file not found!")
            return

        # Đọc nội dung output
        with open(out_file, 'r', encoding='utf-8') as f:
            content = f.read()

        # Tạo output panel
        window = self.view.window()
        panel = window.create_output_panel("cpp_output")
        panel.set_read_only(False)
        panel.run_command("append", {"characters": "=== PROGRAM OUTPUT ===\n\n" + content + "\n\n=== END ==="})
        panel.set_read_only(True)
        window.run_command("show_panel", {"panel": "output.cpp_output"})


class ToggleOutputModeCommand(sublime_plugin.TextCommand):
    """Chuyển đổi giữa file output và panel output"""

    def run(self, edit):
        window = self.view.window()

        # Kiểm tra mode hiện tại
        if window.active_panel() == "output.cpp_output":
            # Đang ở panel mode, chuyển sang file mode
            window.run_command("hide_panel", {"panel": "output.cpp_output"})
            self.view.run_command("refresh_output")
            sublime.status_message("Output mode: File")
        else:
            # Đang ở file mode, chuyển sang panel mode
            self.view.run_command("show_output_in_panel")
            sublime.status_message("Output mode: Panel")


# ==============================================
# 9. COMPILE AND RUN SYSTEM
# ==============================================

class RunCppWithInputCommand(sublime_plugin.TextCommand):
    """Biên dịch và chạy C++ với input từ file"""

    def run(self, edit):
        current_file = self.view.file_name()
        if not current_file or not current_file.endswith('.cpp'):
            sublime.message_dialog("Please open a .cpp file first!")
            return

        base_name = current_file[:-4]
        exe_file = base_name + '.exe'
        in_file = base_name + '.in'
        out_file = base_name + '.out'

        # Hiển thị progress
        sublime.status_message("🔨 Compiling...")

        # Chạy trong thread riêng
        thread = threading.Thread(target=self.compile_and_run,
                                  args=(current_file, exe_file, in_file, out_file))
        thread.start()

    def compile_and_run(self, cpp_file, exe_file, in_file, out_file):
        """Biên dịch và chạy chương trình"""
        # Biên dịch
        compile_cmd = ["g++", "-std=c++17", "-O2", "-Wall", "-Wextra", cpp_file, "-o", exe_file]

        try:
            result = subprocess.run(compile_cmd, capture_output=True, text=True, shell=True)

            if result.returncode != 0:
                sublime.set_timeout(lambda: self.show_compile_error(result.stderr), 0)
                return

            # Chạy chương trình
            if os.path.exists(in_file):
                with open(in_file, 'r') as f_in, open(out_file, 'w') as f_out:
                    run_result = subprocess.run([exe_file], stdin=f_in, stdout=f_out,
                                                stderr=subprocess.PIPE, text=True, shell=True)

                if run_result.stderr:
                    sublime.set_timeout(lambda: self.show_runtime_error(run_result.stderr), 0)

                sublime.set_timeout(lambda: self.show_success_message(out_file), 0)
            else:
                # Chạy interactive
                sublime.set_timeout(lambda: self.run_interactive(exe_file), 0)

        except Exception as e:
            sublime.set_timeout(lambda: sublime.error_message(f"Error: {str(e)}"), 0)

    def show_compile_error(self, error_msg):
        """Hiển thị lỗi biên dịch"""
        window = sublime.active_window()
        panel = window.create_output_panel("compile_error")
        panel.set_read_only(False)
        panel.run_command("append", {"characters": "=== COMPILE ERROR ===\n\n" + error_msg})
        panel.set_read_only(True)
        window.run_command("show_panel", {"panel": "output.compile_error"})

    def show_runtime_error(self, error_msg):
        """Hiển thị lỗi runtime"""
        window = sublime.active_window()
        panel = window.create_output_panel("runtime_error")
        panel.set_read_only(False)
        panel.run_command("append", {"characters": "=== RUNTIME ERROR ===\n\n" + error_msg})
        panel.set_read_only(True)
        window.run_command("show_panel", {"panel": "output.runtime_error"})

    def show_success_message(self, out_file):
        """Hiển thị thông báo thành công"""
        sublime.status_message("✅ Program executed successfully!")

        # Tự động refresh output
        window = sublime.active_window()
        for view in window.views():
            if view.file_name() and view.file_name().endswith('.cpp'):
                sublime.set_timeout(lambda: view.run_command("refresh_output"), 100)
                break

    def run_interactive(self, exe_file):
        """Chạy interactive mode"""
        window = sublime.active_window()
        panel = window.create_output_panel("interactive")
        panel.set_read_only(False)
        panel.run_command("append", {"characters": "=== INTERACTIVE MODE ===\n\n"})
        panel.set_read_only(True)
        window.run_command("show_panel", {"panel": "output.interactive"})

        # TODO: Implement interactive input
        sublime.status_message("Interactive mode - not fully implemented")


# ==============================================
# 10. SIDEBAR INTEGRATION
# ==============================================

class SidebarCreateInOutCommand(sublime_plugin.WindowCommand):
    """Tạo file .in/.out từ sidebar"""

    def run(self):
        # Lấy file đang selected trong sidebar
        files = self.window.extract_variables().get('file')
        if not files:
            return

        file_path = files[0] if isinstance(files, list) else files
        if not file_path.endswith('.cpp'):
            sublime.message_dialog("Select a .cpp file first!")
            return

        base_name = file_path[:-4]
        in_file = base_name + '.in'
        out_file = base_name + '.out'

        # Tạo files
        if not os.path.exists(in_file):
            with open(in_file, 'w') as f:
                f.write("// Input for " + os.path.basename(file_path))

        if not os.path.exists(out_file):
            with open(out_file, 'w') as f:
                f.write("// Output for " + os.path.basename(file_path))

        # Refresh sidebar
        self.window.run_command("refresh_folder_list")
        sublime.status_message("✅ Created .in/.out files for " + os.path.basename(file_path))


class OpenWithLayoutCommand(sublime_plugin.WindowCommand):
    """Mở file .cpp với layout từ sidebar"""

    def run(self, files):
        if files and files[0].endswith('.cpp'):
            # Mở file .cpp
            view = self.window.open_file(files[0])

            # Chờ file load xong rồi tạo layout
            sublime.set_timeout(lambda: view.run_command("auto_cpp_layout"), 300)


# ==============================================
# 11. SETTINGS MANAGEMENT
# ==============================================

class OpenCppSettingsCommand(sublime_plugin.TextCommand):
    """Mở settings cho C++ setup"""

    def run(self, edit):
        window = self.view.window()

        # Tạo settings panel
        settings_content = """// C++ Development Settings
// Save this to Packages/User/Preferences.sublime-settings

{
    // Auto Layout Settings
    "cpp_auto_layout": true,
    "cpp_auto_compile": false,
    "cpp_auto_refresh": true,

    // Build Settings
    "cpp_compiler": "g++",
    "cpp_std_version": "c++17",
    "cpp_flags": "-O2 -Wall -Wextra",

    // Layout Settings
    "cpp_layout_code_width": 0.7,
    "cpp_layout_split_ratio": 0.5,

    // File Settings
    "save_on_focus_lost": true,
    "refresh_output_delay": 300,

    // UI Settings
    "highlight_line": true,
    "show_definitions": true,
    "word_wrap": false
}
"""

        # Tạo buffer cho settings
        settings_view = window.new_file()
        settings_view.set_name("C++ Settings.json")
        settings_view.set_syntax_file("Packages/JavaScript/JSON.sublime-syntax")
        settings_view.run_command("append", {"characters": settings_content})

        sublime.status_message("Edit settings and save to Preferences.sublime-settings")


# ==============================================
# 12. UTILITY FUNCTIONS
# ==============================================

def plugin_loaded():
    """Khi plugin được load"""
    print("=" * 60)
    print("C++ Auto Layout Plugin v2.0 loaded successfully!")
    print("Commands available:")
    print("  - Ctrl+Alt+L: Auto layout")
    print("  - F5: Compile & Run")
    print("  - Ctrl+F5: Refresh output")
    print("  - Ctrl+Shift+L: Quick create .in/.out")
    print("=" * 60)


def plugin_unloaded():
    """Khi plugin bị unload"""
    print("C++ Auto Layout Plugin unloaded")

# ==============================================
# END OF FILE
# ==============================================