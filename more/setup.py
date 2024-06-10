from cx_Freeze import Executable, setup

exe = Executable(
    script="moreQR.py"
)

setup(
    name='moreQR',
    executables=[exe]
)