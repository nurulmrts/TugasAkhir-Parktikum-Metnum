import os
os.system('color a')
setting = int(input("Apakah library Numpy, IPython, Matplotlib, Sys, scipy.linalg, matplotlib.pyplot, Math sudah anda install? 1: Ya, 2:Tidak>>"))
if setting == 1:
 os.system('pip install numpy')
 os.system('pip install matplotlib')
 os.system('pip install ipython')
 os.system('pip install sys')
 os.system('pip install scipy.linalg')
 os.system('pip install matplotlib.pyplot')
 os.system('pip install math')
else:
 print("Baik kita lanjutkan!")
os.system('python code/CodeMetnum5.py')
k=input("Tekan ENTER untuk exit")