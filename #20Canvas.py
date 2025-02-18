from tkinter import *
# *canvas = widget yang digunakan untuk menggambar grafik,plots,atau images dalam window

window = Tk()


canvas = Canvas(window,height=500,width=500)


# *membuat Garis
# canvas.create_line(0,           #posisi awal X
#                    0,           #posisi awal Y
#                    500,         #posisi akhir X
#                    500,         #posisi akhir Y
#                    fill="Blue", #mengubah warna garis
#                    width=5      #Ketebalan garis
#                    )
# canvas.create_line(0,500,500,0,fill="Red",width=5)

# *membuat segiempat
# canvas.create_rectangle(100,     #posisi awal X
#                         100,     #posisi awal Y
#                         400,     #posisi akhir X
#                         400,
#                         fill="Green",       #warna isi segi empat
#                         outline="White",    #warna garis luar segi empat
#                         width=5             #ketebalan garis luar
#                         )     #posisi akhir Y

# *membuat Polygon
# TODO | Polygon digunakan untuk menggambar poligon (bentuk dengan banyak sisi)
# TODO | di dalam widget Canvas. Poligon ini bisa berupa segitiga, segi empat, segi lima, 
# TODO | atau bentuk bebas dengan lebih banyak sisi. 

# points = [0,100,    #sisi satu dimulai dari x dan y
#           150,0,    #sisi dua dimulai dari x dan y
#           350,0,    #sisi tiga dimulai dari x dan y
#           500,100,  #sisi empat dimulai dari x dan y  
#           500,400,  #sisi lima dimulai dari x dan y
#           350,500,  #sisi enam dimulai dari x dan y
#           150,500,  #sisi tujuh dimulai dari x dan y
#           0,400     #sisi delapan dimulai dari x dan y
#           ]
# canvas.create_polygon(points,fill="purple",outline="Black")    

#*memuat bujur sangkar
# * | Di Tkinter, method "create_arc()" digunakan untuk menggambar busur (arc) pada widget Canvas. Busur ini bisa berupa sebagian lingkaran, setengah lingkaran, atau bahkan berbentuk seperti irisan kue (pie slice), tergantung pada argumen yang digunakan.
# canvas.create_arc(0,0,500,500,      #bbox [koordinat kotak tempat busur akan diletakkan didalamnya ]
#                 #   fill="Green",
#                 style=PIESLICE,     #ada beberapa style lain [ARC][CHORD]
#                 start=90,           #memutar bujur [int] derajat
#                 extent=270,         #Menentukan besar sudut busur dalam derajat yang akan digambar.
#                 )
#!membut pokemonball menggunakan canvas create_arc() dan create_oval()
canvas.create_arc(0,0,500,500,fill="Red",extent=180,width=10)
canvas.create_arc(0,0,500,500,fill="White",start=180,extent=180,width=10)
#*membuat oval
canvas.create_oval(190,190,310,310,fill="White",width=10)






canvas.pack(expand=True,fill='both',padx=10,pady=20)

window.mainloop()