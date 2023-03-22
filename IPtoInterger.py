#! /usr/bin/env python3
# coding: utf-8
# author: Lilin32
# IP转换数字工具

import socket
import colorama


def ip_to_int(ip):
    # 检查输入的IP地址是否合法
    try:
        socket.inet_aton(ip)
    except socket.error:
        print(colorama.Fore.RED + "[!] 无效的IP地址!")
        return
    
    # 将IP地址转换为数字
    return int.from_bytes(socket.inet_aton(ip), byteorder='big')


def banner():
    banner = """
.________________________    .___        __
|   \______   \__    ___/___ |   | _____/  |_  ____   ____   ___________
|   ||     ___/ |    | /  _ \|   |/    \   __\/ __ \ / ___\_/ __ \_  __ \\
|   ||    |     |    |(  <_> )   |   |  \  | \  ___// /_/  >  ___/|  | \/
|___||____|     |____| \____/|___|___|  /__|  \___  >___  / \___  >__|
                                      \/          \/_____/      \/
    """
    print(colorama.Fore.GREEN + banner)
    print(colorama.Fore.GREEN + '-' * 90 + "\n")


def main():
    colorama.init(autoreset=True)
    banner()
    ip_address = input(colorama.Fore.GREEN + "[-] " + colorama.Fore.RESET + "请输入一个IP地址：")
    ip_int = ip_to_int(ip_address)
    if ip_int is not None:
        print(colorama.Fore.GREEN + "[-] " + colorama.Fore.RESET + "转换后的数字为：")
        print(colorama.Fore.GREEN + "[+] " + colorama.Fore.RESET + "16进制：", hex(ip_int))
        print(colorama.Fore.GREEN + "[+] " + colorama.Fore.RESET + "10进制：", ip_int)
        print(colorama.Fore.GREEN + "[+] " + colorama.Fore.RESET + " 8进制：", oct(ip_int))


if __name__ == '__main__':
    main()
