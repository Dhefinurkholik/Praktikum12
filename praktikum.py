# rubah string
txt = 'Hello World'
print("\njumlah karakter pada kata \33[32m{}\33[37m adalah :\33[31m".format(txt), len(txt))
print("'\33[37mKarakter terakhir pada kata \33[32m{}\33[37m adalah : \33[31m".format(txt),txt[10])
print("'\33[37mKarakter ke 2 s/d 4 pada \33[32m{}\33[37m adalah : \33[31m".format(txt), txt[2:5])
print("'\33[37mKarakter spasi pada \33[32m{}\33[37m di hilangkan menjadi :\33[31m".format(txt), txt.replace(txt[5], ""))
print("'\33[37mKarakter pada \33[32m{}\33[37m di ubah menjadi huruf besar :\33[31m".format(txt), txt.upper())
print("'\33[37mKarakter pada \33[32m{}\33[37m di ubah menjadi huruf kecil :\33[31m".format(txt), txt.lower())
print("'\33[37mKarakter H pada kata \33[32m{}\33[37m di rubah menggunakan karakter J menjadi :\33[31m".format(txt), txt.replace(txt[:1], "J"))

# lengkapi code
nama = 'Dhefi Nurkholik'
umur = 19
text = '\33[37m\tHello, Nama saya \33[32m{}\33[37m, dan umur saya \33[32m{}\33[37m tahun\n'
print("\n")
print(text.format(nama, umur))