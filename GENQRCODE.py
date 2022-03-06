#Code by Kanento
import qrcode

enter = input("Enter the link for the QRcode : ")

if enter == str(enter):
  img = qrcode.make(str(enter))
  img.save("qrcode.png")
  print("Qrcode as been create.")
else:
  print("ERROR.")
#Code By Kanento