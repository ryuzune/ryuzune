from guizero import App, Text, PushButton, Box, TextBox, warn
from gpiozero import LED, Buzzer

ledRFid = LED(19)

# Function untuk membersihkan Display GUI
def clearDisplay():
    print("Clear Display")
    rfidStatus.value = "-"    # Status dari RFid
    rfidText.value = ""
    ledRFid.off()
    rfidStatus.repeat(1000, checkRFid)    # Setelah display clear, program akan menjalankan function checkRFid()

# Function untuk mendeteksi tag melalui RFid reader
def checkRFid():
    idTag = rfidText.value    # Deklarasi value dari rfidText
    if idTag != "":    # Jika tag RFid terbaca, akan ditampilkan di idTag dan tidak kosong lagi
        print(idTag)    # Menampilkan hasil output dari tag yang terbaca
        rfidStatus.value = "Tag Terbaca"
        rfidStatus.after(3000, clearDisplay)    # Setelah 3 detik, program akan dibersihkan
        rfidStatus.cancel(checkRFid)    # Setelah program dibersihkan, return ke fungsi checkRFid()
        
# Buat program GUI
app = App(title="Reading RFid", layout="auto")

instruksi = Text(app, text="Klik textbox di bawah, lalu tempelkan RFid tag ke RFid Reader.")
rfidText = TextBox(app)    # Menampilkan output di TextBoxt yang diambil dari variabel rfidText
rfidStatus = Text(app, "-")
rfidStatus.repeat(1000, checkRFid)

app.display()   #Menampilkan GUI