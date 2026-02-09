import os
import sys

if sys.platform == "win32":
    scada_bin = os.path.join(
        os.environ.get("ProgramFiles(x86)", r"C:\Program Files (x86)"),
        "Telecontrol SCADA",
        "bin",
    )
    if os.path.isdir(scada_bin):
        os.add_dll_directory(scada_bin)
