from cx_Freeze import Executable, setup

exe = Executable(
    script="one_qr.py"
)

setup(
    name='one_qr',
    executables=[exe]
)