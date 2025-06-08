#  MAC Winbox Brute Force Tool
Tools brute force password MikroTik menggunakan protokol Winbox via MAC Address dalam jaringan lokal. 
Tools ini dirancang untuk melakukan brute force password Winbox MikroTik melalui protokol layer 2 (Ethernet) berdasarkan MAC Address , bukan IP address. Ini berguna ketika perangkat MikroTik tidak diketahui IP-nya atau hanya dapat diakses via mode Neighbor Discovery. Tools ini bekerja dengan memanfaatkan protokol biner Winbox (ethertype 0x8942) dan mendukung scanning otomatis perangkat MikroTik di jaringan lokal sebelum melakukan serangan.

# Fitur Utama
- Scan jaringan cari perangkat MikroTik (ARP scan)
- Brute force password Winbox langsung via MAC Address
- Tidak memerlukan IP address target
- Mendukung custom wordlist
- Kompatibel dengan sistem operasi Linux (karena akses raw socket diperlukan)

# Teknologi yang Digunakan
Python Library:
- scapy
- socket
- struct



# Cara Instalasi

Clone repository:
1. `git clone https://github.com/username/mac-winbox-bruteforce.git` 
2. `cd mac-winbox-bruteforce`

Instal dependensi:

3. `pip install scapy`
Jalankan script sebagai root:
4. `sudo python3 mac_winbox_bruteforce.py`


# Penggunaan

- Masukkan interface jaringan (contoh: eth0, enp0s3)
- Masukkan path ke file wordlist (contoh: wordlists/rockyou.txt)
- Jika tidak ada IP target, tools akan otomatis mencari perangkat MikroTik di jaringan
- Tools akan mulai mencoba password satu per satu


# Contoh output:

`[+] Scanning network on eth0...
 [+] MikroTik ditemukan: 00:0c:42:xx:xx:xx`

Masukkan path ke wordlist: wordlists/rockyou.txt

`[+] Mulai brute force pada 00:0c:42:xx:xx:xx`

`[~] Mencoba: admin`

`[~] Mencoba: password`

`[!] BERHASIL! Password ditemukan: mypassword123`


# Catatan Penting
TOOLS INI HANYA UNTUK TUJUAN EDUKASI DAN PENGETESAN KEAMANAN INTERNAL
JANGAN GUNAKAN DI JARINGAN ATAU PERANGKAT YANG BUKAN MILIKMU
Tools ini tidak menyalahgunakan kerentanan tertentu, hanya melakukan brute force password biasa melalui protokol Winbox.
Pastikan kamu memiliki izin resmi sebelum menggunakannya.

#Struktur Proyek

mac-winbox-bruteforce/

├── mac_winbox_bruteforce.py   # Script utama

├── wordlists/

│   └── rockyou.txt            # Wordlist contoh

└── README.md                  # Dokumentasi ini
