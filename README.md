# Brute-Force

Tools ini dirancang untuk melakukan brute force password Winbox MikroTik melalui protokol layer 2 (Ethernet) berdasarkan MAC Address , bukan IP address. Ini berguna ketika perangkat MikroTik tidak diketahui IP-nya atau hanya dapat diakses via mode Neighbor Discovery.

Tools ini bekerja dengan memanfaatkan protokol biner Winbox (ethertype 0x8942) dan mendukung scanning otomatis perangkat MikroTik di jaringan lokal sebelum melakukan serangan.

🔍 Fitur Utama
✅ Scan jaringan cari perangkat MikroTik (ARP scan)
✅ Brute force password Winbox langsung via MAC Address
✅ Tidak memerlukan IP address target
✅ Mendukung custom wordlist
✅ Kompatibel dengan sistem operasi Linux (karena akses raw socket diperlukan)
🧰 Teknologi yang Digunakan
Python 3.x
Library:
scapy
socket
struct
📦 Persyaratan Sistem
OS: Linux (karena protokol Winbox menggunakan raw socket Ethernet)
Hak akses root / administrator
Python 3.x
Akses ke jaringan lokal yang sama dengan perangkat MikroTik
🚀 Cara Instalasi
Clone repository:
bash


1
2
git clone https://github.com/username/mac-winbox-bruteforce.git 
cd mac-winbox-bruteforce
Instal dependensi:
bash


1
pip install scapy
Jalankan script sebagai root:
bash


1
sudo python3 mac_winbox_bruteforce.py
🧪 Penggunaan
Masukkan interface jaringan (contoh: eth0, enp0s3)
Masukkan path ke file wordlist (contoh: wordlists/rockyou.txt)
Jika tidak ada IP target, tools akan otomatis mencari perangkat MikroTik di jaringan
Tools akan mulai mencoba password satu per satu
Contoh output:

bash


1
2
3
4
5
6
7
[+] Scanning network on eth0...
[+] MikroTik ditemukan: 00:0c:42:xx:xx:xx
Masukkan path ke wordlist: wordlists/rockyou.txt
[+] Mulai brute force pada 00:0c:42:xx:xx:xx
[~] Mencoba: admin
[~] Mencoba: password
[!] BERHASIL! Password ditemukan: mypassword123
⚠️ Catatan Penting
TOOLS INI HANYA UNTUK TUJUAN EDUKASI DAN PENGETESAN KEAMANAN INTERNAL
JANGAN GUNAKAN DI JARINGAN ATAU PERANGKAT YANG BUKAN MILIKMU
Tools ini tidak menyalahgunakan kerentanan tertentu, hanya melakukan brute force password biasa melalui protokol Winbox.
Pastikan kamu memiliki izin resmi sebelum menggunakannya.
📁 Struktur Proyek


1
2
3
4
5
mac-winbox-bruteforce/
├── mac_winbox_bruteforce.py   # Script utama
├── wordlists/
│   └── rockyou.txt            # Wordlist contoh
└── README.md                  # Dokumentasi ini
