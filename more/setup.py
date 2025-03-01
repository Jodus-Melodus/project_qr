from cx_Freeze import Executable, setup

exe = Executable(
    script="more_qr.py"
)

setup(
    name='more_qr',
    executables=[exe]
)