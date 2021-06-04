#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import sys
import numpy as np
import matplotlib.pyplot as plt
from math import sin
from numpy import float32, single, double, array, zeros, diag, diagflat, dot
from IPython import get_ipython
from pprint import pprint
from scipy.linalg import solve

print("-------------------------------------------------------\n",
      "TUGAS AKHIR PRAKTIKUM METODE NUMERIK 2021 \n",
      "KELOMPOK 5 \n",
      "OSEANOGRAFI 2019 \n",
      "------------------------------------------------------\n")

def modul2():  
  def setengahinterval (X1, X2):
    X1 = X1
    X2 = X2
    error = 1
    iterasi = 0
    while(error > 0.0001):
        iterasi +=1
        FXi = (float(-0.0058*(X1**3)))+(float(0.1044*(X1**2)))+(-0.3479*X1)+(-0.7929)
        FXii = (float(-0.0058*(X2**3)))+(float(0.1044*(X2**2)))+(-0.3479*X2)+(-0.7929)
        Xt = (X1 + X2)/2
        FXt = (float(-0.0058*(Xt**3)))+(float(0.1044*(Xt**2)))+(-0.3479*Xt)+(-0.7929)
        if FXi * FXt > 0:
            X1 = Xt
        elif FXi * FXt < 0:
            X2 = Xt
        else:
            print("Akar Penyelesaian: ", Xt) 
        if FXt < 0:
            error = FXt * (-1)
        else:
            error = FXt
        if iterasi > 100:
            print("Angka tak hingga")
            break
        print(iterasi, "|", FXi, "|", FXii, "|", Xt, "|", FXt, "|", error)
    print("Jumlah Iterasi: ", iterasi)
    print("Akar persamaan adalah: ", Xt)
    print("Toleransi Error: ", error)
  def interpolasilinier (X1):
    X1 = X1
    X2 = X1 + 1
    error = 1
    iterasi = 0
    while(error > 0.0001):
        iterasi +=1
        FX1 = (float(-0.0058*(X1**3)))+(float(0.1044*(X1**2)))+(-0.3479*X1)+(-0.7929)
        FX2 =  (float(-0.0058*(X2**3)))+(float(0.1044*(X2**2)))+(-0.3479*X2)+(-0.7929)
        Xt = X2 - ((FX2/(FX2-FX1)))*(X2-X1)
        FXt = (float(-0.0058*(Xt**3)))+(float(0.1044*(Xt**2)))+(-0.3479*Xt)+(-0.7929)
        if FXt*FX1 > 0:
            X2 = Xt
            FX2 = FXt
        else:
            X1 = Xt
            FX1 = FXt 
        if FXt < 0:
            error = FXt * (-1)
        else:
            error = FXt
        if iterasi > 500:
            print("Angka tak hingga")
        break
        print(iterasi, "|", FX1, "|", FX2, "|", Xt, "|", FXt, "|", error)
    print("Jumlah Iterasi: ", iterasi)
    print("Akar persamaan adalah: ", Xt)
    print("Toleransi Error: ", error)
  def newtonrhapson (X1):
    X1 = X1
    iterasi = 0
    akar = 1
    while (akar > 0.0001):
        iterasi += 1
        Fxn = 0.0533*(X1**3)-5.5006*(X1**2)+140.4*(X1)-1020.1
        Fxxn = ((3*0.0533)*(X1**2))-((2*5.5006)*X1)+140.4
        xnp1 = X1 - (Fxn/Fxxn)
        fxnp1 = (xnp1**3)+(xnp1**2)-(3*xnp1)-3
        Ea = ((xnp1-X1)/xnp1)*100
        if Ea < 0.0001:
            X1 = xnp1
            akar = Ea*(-1)
        else:
            akar = xnp1
            print("Nilai akar adalah: ", akar)
            print("Nilai error adalah: ", Ea)
        if iterasi > 100:
            break
        print(iterasi, "|", X1, "|", xnp1, "|", akar, "|", Ea)
    print("Jumlah Iterasi: ", iterasi)
    print("Akar persamaan adalah: ", xnp1)
    print("Toleransi Error: ", akar)
  def iterasi(X1):
    X1 = X1
    error = 1
    iterasi = 0
    while (error > 0.0001):
        iterasi +=1
        Fxn = (float(X1)**3)+(float(X1)**2)-(3*X1)-3
        X2 = ((X1**2)+(3*X1)+3)**(0.333334)
        Ea = (((X2-X1)/(X2))*100)
        if Ea < error:
            X1 = X2
            if Ea > 0:
                error = Ea
            else:
                error = Ea*(-1)
        else:
            error = Ea
        if iterasi > 100:
            print("Angka tak hingga")
            break
        print(iterasi, "|", X1, "|", X2, "|", Ea, "|", error)
    print("Jumlah Iterasi = ", iterasi)
    print("Akar Persamaan = ", X2)
    print("Toleransi Error = ", error)
  def secant(X1):
    X1 = X1
    X2 = X1 - 1
    error = 1
    iterasi = 0
    while(error > 0.0001):
      iterasi +=1
      FX1 = -0.0371*(X1**3)+(1.5072*(X1**2))-9.9433*(X1)-14.997
      FXmin = -0.0371*(X2**3)+(1.5072*(X2**2))-9.9433*(X2)-14.997
      X3 = X1 - ((FX1)*(X1-(X2)))/((FX1)-(FXmin))
      FXplus = -0.0371*(X3**3)+(1.5072*(X3**2))-9.9433*(X3)-14.997
      if FXplus < 0:
        error = FXplus * (-1)
      else:
        error = FXplus
      if error > 0.0001:
        X2 = X1
        X1 = X3
      else:
        print("Selesai")
      if iterasi > 100:
        print("Angka tak hingga")
        break
      print(iterasi, "|", FX1, "|", FXmin, "|", X3, "|", FXplus, "|", error)
    print("Jumlah Iterasi: ", iterasi)
    print("Akar persamaan adalah: ", X3)
    print("Toleransi Error: ", error)

  print("Kode penggunaan akar-akar persamaan: \n",
            "1. Metode Setengah Interval \n",
            "2. Metode Interpolasi Linier \n",
            "3. Metode Newton-Rhapson \n",
            "4. Metode Iterasi \n"
            "5. Metode Secant \n")

  setting = int(input("Masukkan Kode Penggunaan akar-akar persamaan: "))
  if (setting == 1):
    X1 = float(input("Masukkan Nilai Pertama: "))
    X2 = float(input("Masukkan Nilai Kedua: "))
    X = setengahinterval(X1,X2)
    print(X1)
  elif(setting == 2):
    X1 = float(input("Masukkan Nilai Pertama : "))
    X = interpolasilinier(X1)
    print(X)
  elif(setting == 3):
    X1 = float(input("Masukkan Nilai Pertama : "))
    X = newtonrhapson(X1)
    print(X)
  elif(setting == 4):
    X1 = float(input("Masukkan Nilai Pertama : "))
    X = iterasi(X1)
    print(X)
  else:
    X1 = float(input("Masukkan Nilai Pertama : "))
    X = secant(X1)
    print(X)

def modul3():
  def GaussSeidel (A, b, x, n):
      L = np.tril(A)
      U = A -L
      for i in range(n):
          x=np.dot(np.linalg.inv(L), b - np.dot(U,x))
          print (f'Iterasi Ke-{str(i+1).zfill(3)}'),
          print (x)
      return x
  def GaussJordan(a,n):
      #Step1 ===> Looping untuk pengolahan metode Gauss Jordan
      print('==============Mulai Iterasi===============')
      for i in range(n):
          if a[i][i]==0:
              sys.exit('Dibagi dengan angka nol (proses tidak dapat dilanjutkan)')
          for j in range(n):
              if i !=j:
                  ratio=a[j][i]/a[i][i]
                  #print('posisi nol di:[',j,i,']', 'nilai rasio:',ratio)
                  for k in range(n+1):
                      a[j,k]=a[j][k]-ratio*a[i][k]
                  print(a)
                  print(f'============================================')
      # Step 2 ====> Membuat semua variabel(x,y,z,...)==1
      ax=np.zeros((n,n+1))
      for i in range(n):
          for j in range(n+1):
              ax[i,j]=a[i][j]/a[i][i]
      print('===================Akhir Iterasi===================')
      return ax
  def Gauss(A, f):
      A = np.array((A), dtype=float)
      f = np.array((f), dtype=float)
      n = len(f)
      for i in range(0, n - 1):  # Looping untuk kolom matriks
          if np.abs(A[i, i]) == 0:
              for k in range(i + 1, n):
                  if np.abs(A[k, i]) > np.abs(A[i, i]):
                      A[[i, k]] = A[[k, i]]  # Tukar antara baris i dan k
                      f[[i, k]] = f[[k, i]]
                      break
          for j in range(i + 1, n):  # Ulangi baris yang ada di bawah diagonal untuk setiap kolom
              m = A[j, i] / A[i, i]
              A[j, :] = A[j, :] - m * A[i, :]
              f[j] = f[j] - m * f[i]
      return A, f
  def jacobi(A,b,x,n):
      D = np.diag(A)
      R = A-np.diagflat(D)
      for i in range(n):
        x = (b-np.dot(R,x))/D
        print (f'Iterasi Ke-{str(i+1).zfill(3)}'),
        print (x)
      return x
      
  print("Kode penggunaan akar-akar persamaan: \n",
      "1. Metode Gauss-Siedel \n",
      "2. Metode Gauss-Jordan \n",
      "3. Metode Gauss \n",
      "4. Metode Jacobi \n")

  setting = int(input("Masukkan kode penggunaan akar-akar persamaan: "))
  if (setting == 1):
      A = np.array(eval(input('Masukkan matriks augmented dari SPL yang akan diselesaikan : ')))
      b = np.array(eval(input("Masukkan nilai hasil dari SPL yang akan diselesaikan : ")))
      x = np.zeros_like(b)
      n = int(input("Masukkan berapa banyak iterasi yang mau dilakukan : "))
      GS = GaussSeidel(A, b, x, n)
      print(f'Hasil pengerjaan menggunakan Gauss Seidel didapatkan nilai tiap variabel {GS}')
  elif (setting == 2):
      m = np.array(eval(input('Masukkan matriks augmented dari SPL yang akan diselesaikan : ')))
      n = int(input("Masukkan nilai : "))
      print('Matriks Persamaan')
      print(m)
      m = GaussJordan(m,n)
      print(f"""Hasil Pengolahan menggunakan metode Gauss Jordan didapatkan hasil sebagai berikut: {m} \n""")
  elif (setting == 3):
      A = np.array(eval(input('Masukkan matriks augmented dari SPL yang akan diselesaikan : ')))
      f = np.array(eval(input("Masukkan nilai hasil dari SPL yang akan diselesaikan : ")))
      print('A = \n%s and f = %s \n' % (A, f))
      Cel = Gauss(A, f)
      x = np.linalg.solve(A, f)
      print('Hasil perhitungan dengan metode Gauss adalah x = \n %s \n' % x)
  else:
      A = np.array(eval(input('Masukkan matriks augmented dari SPL yang akan diselesaikan : ')))
      b = np.array(eval(input("Masukkan nilai hasil dari SPL yang akan diselesaikan : ")))
      x = np.array(eval(input("Masukkan nilai x : ")))
      n = int(input("Masukkan berapa banyak iterasi yang mau dilakukan : "))
      J = jacobi(A,b,x,n)
      print(f'Hasil pengerjaan menggunakan Jacobi didapatkan nilai tiap variabel {J}')

def modul4():
  def trapesium1pias():
    x = np.linspace(-10, 10, 100)
    y = eval(input('Masukkan Persamaan untuk Trapesium 1 pias : ')) # 3 * (x**3) + 3 * (x**2) sebagai contoh
    plt.plot(x, y)
    x1 = 0
    x2 = 1
    fx1 = eval(input('Batas atas (X1) : ')) # 3 * x1**3
    fx2 = eval(input('Batas bawah (X2) : ')) # 3 * x2**2
    plt.fill_between([x1, x2], [fx1, fx2])
    plt.xlim([-1.5, 1.5]);
    plt.ylim([0, 4]);
    plt.title('Trapesium 1 pias')
    plt.savefig('C:/Users/TRITON 300/OneDrive/Documents/TA Metnum Kelompok 5/image/Trapesium 1 Pias.png')
    L = 0.5*(fx2 + fx1)*(x2 - x1)
    print("Luas dengan metode trapesium 1 pias:", L)
    print(L)
  def trapesiumbanyakpias(f,a,b,N):
    x = np.linspace(a,b,N+1)
    y = f(x)
    y_kanan = y[1:]
    y_kiri = y[:-1]
    dx = (b - a)/N
    T = (dx/2) * np.sum(y_kanan + y_kiri)
    return T
  def simpson13(x0,xn,n):
      h = (xn - x0) / n
      integral = f(x0) + f(xn)
      for i in range(1,n):
          k = x0 + i*h
          if i%2 == 0:
              integral = integral + 2 * f(k)
          else:
              integral = integral + 4 * f(k)
      integral = integral * h/3
      return integral
  def simpson38(x0,xn,n):
      h = (xn - x0) / n
      integral = f(x0) + f(xn)
      for i in range(1,n):
          k = x0 + i*h
          if i%2 == 0:
              integral = integral + 3 * f(k)
          else:
              integral = integral + 3 * f(k)
      integral = integral * 3 * h / 8
      return integral

  print("Kode untuk penyelesaian integrasi numerik: \n",
          "1. Metode Trapesium 1 Pias \n",
          "2. Metode Trapesium Banyak Pias \n",
          "3. Metode Simpson 1/3 \n",
          "4. Metode Simpson 3/8 \n")

  setting = int(input("Masukkan kode penyelesaian integrasi numerik: "))
  if (setting == 1):
    cel = trapesium1pias()
  elif (setting == 2):
    f = eval(input('Masukkan Persamaan untuk Trapesium banyak pias (harus menggunakan lamda) : ')) # lambda x : 3*(x**3) + 3*(x**2) harus menggunakan lambda agar menjadi sebuah fungsi
    a = 0
    b = 10
    N = int(input('Masukkan jumlah pias : '))
    x = np.linspace(a,b,N+1)
    y = f(x)
    X = np.linspace(a,b+1,N)
    Y = f(X)
    plt.plot(X,Y)
    for i in range(N):
      xs = [x[i],x[i],x[i+1],x[i+1]]
      ys = [0,f(x[i]),f(x[i+1]),0]
      plt.fill(xs,ys, 'b', edgecolor='b',alpha=0.2)
    plt.title('Trapesium banyak pias, N = {}'.format(N))
    plt.savefig('C:/Users/TRITON 300/OneDrive/Documents/TA Metnum Kelompok 5/image/Trapesium Banyak Pias.png')
    L = trapesiumbanyakpias(f,a,b,N)
    print(L)
  elif (setting == 3):
    f = eval(input('Masukkan Persamaan untuk Simpson 1/3 (harus menggunakan lamda) : '))
    x1 = float(input("batas bawah (x1): "))
    x2 = float(input("batas atas (x2) : "))
    hasil = simpson13(x1,x2,2)
    print("nilai integral metode Simpson 1/3:",hasil )
  else:
    f = eval(input('Masukkan Persamaan untuk Simpson 3/8 (harus menggunakan lamda) : '))
    x1 = float(input("Batas bawah (x1): "))
    x2 = float(input("Batas atas (x2): "))
    hasil = simpson38(x1, x2, 3)
    print("Nilai integral metode Simpson 3/8:", hasil)

def modul5():
    # Metode Euler
    def euler():
        Nama = (input("Masukkan Nama: "))
        Nim = (input("Masukkan NIM: "))
        Kelas = (input("Masukkan Kelas: "))
        plt.style.use('seaborn-poster')
        ipy = get_ipython()
        if ipy is not None:
            ipy.run_line_magic('matplotlib', 'inline')
        h = float(input("Masukkan nilai h: ")) #Banyak langkah yang akan digunakan (Ose B = 0.05)
        x0 = float(input("Masukkan nilai x awal: ")) #Masukkan kondisi awal 0
        xn = float(input("Masukkan nilai x akhir: ")) #Untuk x akhir ketentuan 2 nim akhir dibalik (nilainya 3,0)
        x = np.arange(x0, xn + h, h) #Grid
        y0 = float(input("Masukkan nilai y awal: ")) #Masukkan kondisi awal 0
        G = 2*(x**3) + 9*(x**2) + 3*(x) + 3 #Fungsi
        f = lambda x, y: 2*(x**3) + 9*(x**2) + 3*(x) + 3 #Persamaan Diferensial Biasa
        y = np.zeros(len(x))
        y[0] = y0
        for i in range(0, len(x) - 1):
            y[i + 1] = y[i] + h*f(x[i], y[i])
        print(y)
        error = G-y
        print(error)
        judul = ("\n Grafik Pendekatan Persamaan Differensial Biasa Dengan Metode Euler \n\n %s_%s_%s \n" % (Nama,Nim,Kelas))
        plt.figure(figsize = (12, 10))
        plt.plot(x, y, 'b--', color='r', label='Hasil Pendekatan')
        plt.plot(x, G, '-g', color='y', label='Hasil Analitik')
        plt.title(judul) #Judul Plot
        plt.xlabel('x') #Label u/ sumbu x
        plt.ylabel('F(x)') #Label u/ sumbu y
        plt.grid() #u/ menampilkan grid
        plt.legend(loc='lower right')
        plt.savefig('C:/Users/TRITON 300/OneDrive/Documents/TA Metnum Kelompok 5/image/Euler.png')
    # Metode Heun
    def heun():
        Nama = (input("Masukkan Nama: "))
        Nim = (input("Masukkan NIM: "))
        Kelas = (input("Masukkan Kelas: "))
        plt.style.use('seaborn-poster')
        ipy = get_ipython()
        if ipy is not None:
            ipy.run_line_magic('matplotlib', 'inline')
        h = float(input("Masukkan nilai h: ")) #Banyak langkah yang akan digunakan (Ose B = 0.05)
        x0 = float(input("Masukkan nilai x awal: ")) #Masukkan kondisi awal 0
        xn = float(input("Masukkan nilai x akhir: ")) #Untuk x akhir ketentuan 2 nim akhir dibalik (nilainya 3,0)
        x = np.arange(x0, xn + h, h) #Grid
        y0 = float(input("Masukkan nilai y awal: ")) #Masukkan kondisi awal 0
        G = 2*(x**3) + 9*(x**2) + 3*(x) + 3 #Fungsi
        f = lambda x, y: 2*(x**3) + 9*(x**2) + 3*(x) + 3 #Persamaan Diferensial Biasa
        y = np.zeros(len(x))
        y[0] = y0
        for i in range(0, len(x) - 1):
            k1 = f(x[i], y[i])
            k2 = f((x[i] + h), (y[i] + (h*k1)))
            y[i+1] = y[i] + (0.5 * h * (k1 + k2))
        print(y)
        error = G-y
        print(error)
        judul = ("\n Grafik Pendekatan Persamaan Differensial Biasa Dengan Metode Heun \n\n %s_%s_%s \n" % (Nama,Nim,Kelas))
        plt.figure(figsize = (12, 10))
        plt.plot(x, y, 'b--', color='r', label='Hasil Pendekatan')
        plt.plot(x, G, '-g', color='y', label='Hasil Analitik')
        plt.title(judul) #Judul Plot
        plt.xlabel('x') #Label u/ sumbu x
        plt.ylabel('F(x)') #Label u/ sumbu y
        plt.grid() #u/ menampilkan grid
        plt.legend(loc='lower right')
        plt.savefig('C:/Users/TRITON 300/OneDrive/Documents/TA Metnum Kelompok 5/image/Heun.png')
    print("Kode untuk penyelesaian persamaan differensial biasa: \n",
         "1. Metode Euler \n",
         "2. Metode Heun \n")
    setting = int(input("Masukkan kode penyelesaian persamaan differensial biasa: "))
    if (setting == 1):
        Cel = euler()
    elif (setting == 2):
        Cel = heun()
    else:
        print("Kode yang dimasukkan salah!")

print("Kode untuk penggunaan modul: \n",
      "1. Modul 2 Akar-akar Persamaan \n",
      "2. Modul 3 Sistem Persamaan Linier dan Matriks \n",
      "3. Modul 4 Integrasi Numerik \n",
      "4. Modul 5 Persamaan Persamaan Differensial Biasa \n")
setting = int(input("Masukkan kode modul yang ingin digunakan: "))
if (setting == 1):
    Cel = modul2()
elif (setting == 2):
    Cel = modul3()
elif (setting == 3):
    Cel = modul4()
elif (setting == 4):
    Cel = modul5()
else:
    print("Kode yang dimasukkan salah!")


# In[ ]:




