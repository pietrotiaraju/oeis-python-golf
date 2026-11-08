"""Audit hook that tools/verify.py installs around each program it runs.

verify.py copies this file as sitecustomize.py into an empty temporary folder,
next to the program, and starts `python -u py3.py` there with PYTHONPATH pointing
at that folder and an otherwise empty environment. Python imports it before the
program starts, so the program runs exactly as written, but cannot:

  - open files outside the Python installation and that folder, or open any file
    for writing (so the b-files in the repository are out of reach);
  - list other folders, change folder, or touch the file system;
  - start processes, use the network, ctypes or the garbage collector's object lists.

Audit hooks are not a sandbox against a determined attacker, but they close the
easy ways to look up answers, and any attempt to get around them would stand out
in a program of a few hundred bytes.
"""
import sys


def _install():
    import os

    def norm(p):
        return os.path.normcase(os.path.abspath(os.fsdecode(p)))

    here = os.path.dirname(os.path.abspath(__file__))
    roots = tuple({norm(p) + os.sep for p in (sys.prefix, sys.base_prefix, sys.exec_prefix,
                                              sys.base_exec_prefix, here)})
    write = os.O_WRONLY | os.O_RDWR | os.O_CREAT | os.O_APPEND | os.O_TRUNC
    denied = ("os.", "subprocess.", "_posixsubprocess.", "_winapi.", "socket.", "ctypes.",
              "shutil.", "winreg.", "msvcrt.", "urllib.", "http.", "ftplib.", "smtplib.",
              "imaplib.", "poplib.", "nntplib.", "telnetlib.", "webbrowser.", "mmap.", "fcntl.",
              "pty.", "resource.", "syslog.", "sqlite3.", "glob.", "pathlib.", "tempfile.",
              "gc.get_", "builtins.input", "sys._current_frames")
    harmless = frozenset({"os.putenv", "os.unsetenv"})

    def inside(path):
        if path is None:
            path = "."
        if isinstance(path, int):
            return False
        try:
            return (norm(path) + os.sep).startswith(roots)
        except (TypeError, ValueError):
            return False

    def hook(event, args):
        if event == "open":
            path, mode, flags = (*args, None, None, None)[:3]
            if isinstance(path, int) and path in (0, 1, 2):
                return
            if not any(c in (mode or "") for c in "wax+") and not (flags or 0) & write and inside(path):
                return
            raise PermissionError(f"verify.py sandbox: cannot open {path!r}")
        if event.startswith(denied) and event not in harmless:
            if event in ("os.listdir", "os.scandir") and inside((*args, None)[0]):
                return
            raise PermissionError(f"verify.py sandbox: {event} is not allowed")

    sys.addaudithook(hook)


_install()
del _install
