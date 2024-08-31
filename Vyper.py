import os, sys, platform
bit = platform.architecture()[0]
if bit == '64bit':
    os.system(f"mv no.cpython-311.so {sys.path[2]}/no.cpython-311.so")
    import test
else:
    sys.exit(" [/] Your Device Not Work..!")
