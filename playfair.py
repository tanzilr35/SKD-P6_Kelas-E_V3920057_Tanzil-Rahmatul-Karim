# Buat variabel kunci, untuk menginput kunci
key = input("Masukkan kunci : ")
key = key.replace(" ", "")
key = key.upper() # Hanya menggunakan huruf kapital

# Membuat fungsi matrix
def matrix(x,y,initial):
  return [[initial for i in range(x)] for j in range(y)]
    
result = list()
for c in key: # Menyimpan kunci
  if c not in result:
    if c=='J':
      result.append('I') # Jika kunci mengandung huruf J, maka diubah jadi huruf I
    else:
      result.append(c)

flag = 0
for i in range(65,91): # Menyimpan karakter lain, jika plainteks memiliki jumlah huruf ganjil, maka akan ditambahkan suatu karakter (contoh: X) di huruf yang kosong
  if chr(i) not in result:
    if i==73 and chr(74) not in result:
      result.append("I")
      flag = 1
    elif flag==0 and i==73 or i==74:
      pass    
    else:
      result.append(chr(i))

k = 0
my_matrix = matrix(5,5,0) # Menginisialisasi matrix 5x5
for i in range(0,5): # Membuat matrix
  for j in range(0,5):
    my_matrix[i][j] = result[k]
    k+=1

# Membuat fungsi lokasi -> mendapatkan lokasi untuk setiap karakter
def locindex(c):
  loc = list()
  if c=='J':
    c = 'I' 
  for i,j in enumerate(my_matrix): # enumerate = untuk menambahkan penghitung ke setiap item dari objek yang dapat diubah dan dikembalikan objek enumerate
    for k,l in enumerate(j):
      if c==l:
        loc.append(i)
        loc.append(k)
        return loc

# Proses Enkripsi
def encrypt():
  msg = str(input("MASUKKAN PESAN : "))
  msg = msg.upper()
  msg = msg.replace(" ", "")

  # Buat perulangan untuk menghasilkan output enkripsi/cipher textnya  
  i = 0
  for s in range(0,len(msg)+1,2):
    if s<len(msg)-1:
      if msg[s]==msg[s+1]:
        msg = msg[:s+1]+'X'+msg[s+1:]
  if len(msg)%2!=0:
    msg = msg[:]+'X'
  print("CIPHER TEXT : ",end=' ')
  while i<len(msg):
    loc = list()
    loc = locindex(msg[i])
    loc1 = list()
    loc1 = locindex(msg[i+1])
    # Buat aturan enkripsi
    if loc[1]==loc1[1]:
      # Jika pasangan huruf (kedua huruf) berada pada satu kolom
      print("{}{}".format(my_matrix[(loc[0]+1)%5][loc[1]],my_matrix[(loc1[0]+1)%5][loc1[1]]),end=' ')
    elif loc[0]==loc1[0]:
      # Jika pasangan huruf (kedua huruf) berada pada satu baris
      print("{}{}".format(my_matrix[loc[0]][(loc[1]+1)%5],my_matrix[loc1[0]][(loc1[1]+1)%5]),end=' ')  
    else:
      # Jika pasangan huruf tidak berada pada baris atau kolom yang sama
      print("{}{}".format(my_matrix[loc[0]][loc1[1]],my_matrix[loc1[0]][loc[1]]),end=' ')    
    i = i+2        

# Proses Dekripsi  
def decrypt():
  msg = str(input("MASUKKAN CIPHER TEXT : "))
  msg = msg.upper()
  msg = msg.replace(" ", "")
  print("PLAIN TEXT : ",end=' ')

  # Buat perulangan untuk menghasilkan output dekripsi/plain textnya 
  i = 0
  while i < len(msg):
    loc = list()
    loc = locindex(msg[i])
    loc1 = list()
    loc1 = locindex(msg[i+1])
    # Buat aturan dekripsi
    if loc[1]==loc1[1]:
      # Jika pasangan huruf (kedua huruf) berada pada satu kolom
      print("{}{}".format(my_matrix[(loc[0]-1)%5][loc[1]],my_matrix[(loc1[0]-1)%5][loc1[1]]),end=' ')
    elif loc[0]==loc1[0]:
      # Jika pasangan huruf (kedua huruf) berada pada satu baris
      print("{}{}".format(my_matrix[loc[0]][(loc[1]-1)%5],my_matrix[loc1[0]][(loc1[1]-1)%5]),end=' ')  
    else:
      # Jika pasangan huruf tidak berada pada baris atau kolom yang sama
      print("{}{}".format(my_matrix[loc[0]][loc1[1]],my_matrix[loc1[0]][loc[1]]),end=' ')    
    i = i+2        

# Membuat pilihan cipher
while(1):
  choice=int(input("\n 1.Enkripsi \n 2.Dekripsi \n 3.EXIT"))
  if choice==1:
    encrypt()
  elif choice==2:
    decrypt()
  elif choice==3:
    exit()
  else:
    print("Choose correct choice")