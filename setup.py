from cx_Freeze import setup,Executable
base=None
exe = Executable(
        script = "gui.py",
        icon = "book.ico",
        targetName = "ORG.exe",
        base = base
        )
includefiles = ["book.ico"]
setup(name="organizador",version= '0.1', description =" organize files ",
      executables=[exe])
