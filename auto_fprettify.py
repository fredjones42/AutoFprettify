import os.path
import shutil
import subprocess

import sublime
import sublime_plugin

FORTRAN_EXTENSIONS = [".f", ".for", ".ftn", ".f90", ".f95", ".f03", ".fpp"]
FORTRAN_EXTENSIONS += [ext.upper() for ext in FORTRAN_EXTENSIONS]


class AutoFprettifyCommand(sublime_plugin.TextCommand):
    def is_enabled(self):
        file_name = self.view.file_name()
        file_ext = os.path.splitext(file_name)[1] if file_name else None
        if (
            (file_ext is not None and file_ext in FORTRAN_EXTENSIONS)
            or (self.view.match_selector(0, "source.modern-fortran"))
            or (self.view.match_selector(0, "source.fixedform-fortran"))
            or (self.view.match_selector(0, "source.fortran"))
        ):
            return True
        return False

    def run(self, edit):
        if shutil.which("fprettify") is None:
            sublime.status_message("'fprettify' command not found!")
            return

        file_name = self.view.file_name()

        if file_name is None:
            sublime.status_message("plugin only supports on-disk files")
            return

        settings = sublime.load_settings("AutoFprettify.sublime-settings")

        args = []
        args.append("fprettify")
        for option in settings.get("options", []):
            args.append(option)
        args.append(file_name)

        returncode = subprocess.call(args, shell=True)

        if returncode != 0:
            sublime.status_message("fprettify: error (return code = %d)" % returncode)


class AutoFprettifyListener(sublime_plugin.EventListener):
    def on_post_save(self, view):
        settings = sublime.load_settings("AutoFprettify.sublime-settings")
        if settings.get("format_on_save"):
            view.run_command("auto_fprettify")
