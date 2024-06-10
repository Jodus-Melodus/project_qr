from cx_Freeze import Executable, setup

exe = Executable(
    script="oneQR.py"
)

setup(
    name='oneQR',
    executables=[exe]
)