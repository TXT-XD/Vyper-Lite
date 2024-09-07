import os, sys, platform
bit = platform.architecture()[0]
if bit == '64bit':
    os.system(f"mv no.cpython-311.so {sys.path[2]}/no.cpython-311.so")
    os.system("chmod +x test")
    import test
else:
    #os.system(f"mv no32.cpython-311.so {sys.path[2]}/no32.cpython-311.so")
    #import test33
    sys.exit("32 bit not work 🙂")
