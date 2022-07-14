import blocksmith
from lxml import html
import requests
import os
import time
import base58
import binascii
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich import box, live
import random

console = Console()


def getbal(addr0: object) -> object:
    urlblock = "https://ethereum.atomicwallet.io/address/" + addr0
    respone_block = requests.get(urlblock)
    byte_string = respone_block.content
    source_code = html.fromstring(byte_string)
    xpatch_txid = '/html/body/main/div/div[2]/div[1]/table/tbody/tr[1]/td[2]'
    treetxid = source_code.xpath(xpatch_txid)
    xVol = str(treetxid[0].text_content())
    return xVol


def privx0():
    paddress_1aphrase = blocksmith.KeyGenerator()
    paddress_1aphrase.seed_input('qwertyuiopasdfghjklzxcvbnm1234567890')
    priv0 = paddress_1aphrase.generate_key()
    addr0 = blocksmith.EthereumWallet.generate_address(priv0)
    return priv0, addr0


def privx1():
    paddress_1aphrase = blocksmith.KeyGenerator()
    paddress_1aphrase.seed_input('qwertyuiopasdfghjklzxcvbnm1234567890')
    priv1 = paddress_1aphrase.generate_key()
    addr1 = blocksmith.EthereumWallet.generate_address(priv1)
    return priv1, addr1


def privx2():
    paddress_1aphrase = blocksmith.KeyGenerator()
    paddress_1aphrase.seed_input('qwertyuiopasdfghjklzxcvbnm1234567890')
    priv2 = paddress_1aphrase.generate_key()
    addr2 = blocksmith.EthereumWallet.generate_address(priv2)
    return priv2, addr2


def privx3():
    paddress_1aphrase = blocksmith.KeyGenerator()
    paddress_1aphrase.seed_input('qwertyuiopasdfghjklzxcvbnm1234567890')
    priv3 = paddress_1aphrase.generate_key()
    addr3 = blocksmith.EthereumWallet.generate_address(priv3)
    return priv3, addr3


def privx4():
    paddress_1aphrase = blocksmith.KeyGenerator()
    paddress_1aphrase.seed_input('qwertyuiopasdfghjklzxcvbnm1234567890')
    priv4 = paddress_1aphrase.generate_key()
    addr4 = blocksmith.EthereumWallet.generate_address(priv4)
    return priv4, addr4


def privx5():
    paddress_1aphrase = blocksmith.KeyGenerator()
    paddress_1aphrase.seed_input('qwertyuiopasdfghjklzxcvbnm1234567890')
    priv5 = paddress_1aphrase.generate_key()
    addr5 = blocksmith.EthereumWallet.generate_address(priv5)
    return priv5, addr5


def privx6():
    paddress_1aphrase = blocksmith.KeyGenerator()
    paddress_1aphrase.seed_input('qwertyuiopasdfghjklzxcvbnm1234567890')
    priv6 = paddress_1aphrase.generate_key()
    addr6 = blocksmith.EthereumWallet.generate_address(priv6)
    return priv6, addr6


def privx7():
    paddress_1aphrase = blocksmith.KeyGenerator()
    paddress_1aphrase.seed_input('qwertyuiopasdfghjklzxcvbnm1234567890')
    priv7 = paddress_1aphrase.generate_key()
    addr7 = blocksmith.EthereumWallet.generate_address(priv7)
    return priv7, addr7


def privx8():
    paddress_1aphrase = blocksmith.KeyGenerator()
    paddress_1aphrase.seed_input('qwertyuiopasdfghjklzxcvbnm1234567890')
    priv8 = paddress_1aphrase.generate_key()
    addr8 = blocksmith.EthereumWallet.generate_address(priv8)
    return priv8, addr8


def privx9():
    paddress_1aphrase = blocksmith.KeyGenerator()
    paddress_1aphrase.seed_input('qwertyuiopasdfghjklzxcvbnm1234567890')
    priv9 = paddress_1aphrase.generate_key()
    addr9 = blocksmith.EthereumWallet.generate_address(priv9)
    return priv9, addr9


def privx10():
    paddress_1aphrase = blocksmith.KeyGenerator()
    paddress_1aphrase.seed_input('qwertyuiopasdfghjklzxcvbnm1234567890')
    priv10 = paddress_1aphrase.generate_key()
    addr10 = blocksmith.EthereumWallet.generate_address(priv10)
    return priv10, addr10


def privx11():
    paddress_1aphrase = blocksmith.KeyGenerator()
    paddress_1aphrase.seed_input('qwertyuiopasdfghjklzxcvbnm1234567890')
    priv11 = paddress_1aphrase.generate_key()
    addr11 = blocksmith.EthereumWallet.generate_address(priv11)
    return priv11, addr11


def privx12():
    paddress_1aphrase = blocksmith.KeyGenerator()
    paddress_1aphrase.seed_input('qwertyuiopasdfghjklzxcvbnm1234567890')
    priv12 = paddress_1aphrase.generate_key()
    addr12 = blocksmith.EthereumWallet.generate_address(priv12)
    return priv12, addr12


def privx13():
    paddress_1aphrase = blocksmith.KeyGenerator()
    paddress_1aphrase.seed_input('qwertyuiopasdfghjklzxcvbnm1234567890')
    priv13 = paddress_1aphrase.generate_key()
    addr13 = blocksmith.EthereumWallet.generate_address(priv13)
    return priv13, addr13


def privx14():
    paddress_1aphrase = blocksmith.KeyGenerator()
    paddress_1aphrase.seed_input('qwertyuiopasdfghjklzxcvbnm1234567890')
    priv14 = paddress_1aphrase.generate_key()
    addr14 = blocksmith.EthereumWallet.generate_address(priv14)
    return priv14, addr14


def privx15():
    paddress_1aphrase = blocksmith.KeyGenerator()
    paddress_1aphrase.seed_input('qwertyuiopasdfghjklzxcvbnm1234567890')
    priv15 = paddress_1aphrase.generate_key()
    addr15 = blocksmith.EthereumWallet.generate_address(priv15)
    return priv15, addr15


def privx16():
    paddress_1aphrase = blocksmith.KeyGenerator()
    paddress_1aphrase.seed_input('qwertyuiopasdfghjklzxcvbnm1234567890')
    priv16 = paddress_1aphrase.generate_key()
    addr16 = blocksmith.EthereumWallet.generate_address(priv16)
    return priv16, addr16


def privx17():
    paddress_1aphrase = blocksmith.KeyGenerator()
    paddress_1aphrase.seed_input('qwertyuiopasdfghjklzxcvbnm1234567890')
    priv17 = paddress_1aphrase.generate_key()
    addr17 = blocksmith.EthereumWallet.generate_address(priv17)
    return priv17, addr17


def privx18():
    paddress_1aphrase = blocksmith.KeyGenerator()
    paddress_1aphrase.seed_input('qwertyuiopasdfghjklzxcvbnm1234567890')
    priv18 = paddress_1aphrase.generate_key()
    addr18 = blocksmith.EthereumWallet.generate_address(priv18)
    return priv18, addr18


def privx19():
    paddress_1aphrase = blocksmith.KeyGenerator()
    paddress_1aphrase.seed_input('qwertyuiopasdfghjklzxcvbnm1234567890')
    priv19 = paddress_1aphrase.generate_key()
    addr19 = blocksmith.EthereumWallet.generate_address(priv19)
    return priv19, addr19


def privx20():
    paddress_1aphrase = blocksmith.KeyGenerator()
    paddress_1aphrase.seed_input('qwertyuiopasdfghjklzxcvbnm1234567890')
    priv20 = paddress_1aphrase.generate_key()
    addr20 = blocksmith.EthereumWallet.generate_address(priv20)
    return priv20, addr20


def privx21():
    paddress_1aphrase = blocksmith.KeyGenerator()
    paddress_1aphrase.seed_input('qwertyuiopasdfghjklzxcvbnm1234567890')
    priv21 = paddress_1aphrase.generate_key()
    addr21 = blocksmith.EthereumWallet.generate_address(priv21)
    return priv21, addr21


def privx22():
    paddress_1aphrase = blocksmith.KeyGenerator()
    paddress_1aphrase.seed_input('qwertyuiopasdfghjklzxcvbnm1234567890')
    priv22 = paddress_1aphrase.generate_key()
    addr22 = blocksmith.EthereumWallet.generate_address(priv22)
    return priv22, addr22


def privx23():
    paddress_1aphrase = blocksmith.KeyGenerator()
    paddress_1aphrase.seed_input('qwertyuiopasdfghjklzxcvbnm1234567890')
    priv23 = paddress_1aphrase.generate_key()
    addr23 = blocksmith.EthereumWallet.generate_address(priv23)
    return priv23, addr23


def privx24():
    paddress_1aphrase = blocksmith.KeyGenerator()
    paddress_1aphrase.seed_input('qwertyuiopasdfghjklzxcvbnm1234567890')
    priv24 = paddress_1aphrase.generate_key()
    addr24 = blocksmith.EthereumWallet.generate_address(priv24)
    return priv24, addr24


def privx25():
    paddress_1aphrase = blocksmith.KeyGenerator()
    paddress_1aphrase.seed_input('qwertyuiopasdfghjklzxcvbnm1234567890')
    priv25 = paddress_1aphrase.generate_key()
    addr25 = blocksmith.EthereumWallet.generate_address(priv25)
    return priv25, addr25


def privx26():
    paddress_1aphrase = blocksmith.KeyGenerator()
    paddress_1aphrase.seed_input('qwertyuiopasdfghjklzxcvbnm1234567890')
    priv26 = paddress_1aphrase.generate_key()
    addr26 = blocksmith.EthereumWallet.generate_address(priv26)
    return priv26, addr26


def privx27():
    paddress_1aphrase = blocksmith.KeyGenerator()
    paddress_1aphrase.seed_input('qwertyuiopasdfghjklzxcvbnm1234567890')
    priv27 = paddress_1aphrase.generate_key()
    addr27 = blocksmith.EthereumWallet.generate_address(priv27)
    return priv27, addr27


w = 0
z = 0
while True:
    z += 1
    priv0, addr0 = privx0()
    priv1, addr1 = privx1()
    priv2, addr2 = privx2()
    priv3, addr3 = privx3()
    priv4, addr4 = privx4()
    priv5, addr5 = privx5()
    priv6, addr6 = privx6()
    priv7, addr7 = privx7()
    priv8, addr8 = privx8()
    priv9, addr9 = privx9()
    priv10, addr10 = privx10()
    priv11, addr11 = privx11()
    priv12, addr12 = privx12()
    priv13, addr13 = privx13()
    priv14, addr14 = privx14()
    priv15, addr15 = privx15()
    priv16, addr16 = privx16()
    priv17, addr17 = privx17()
    priv18, addr18 = privx18()
    priv19, addr19 = privx19()
    priv20, addr20 = privx20()
    priv21, addr21 = privx21()
    priv22, addr22 = privx22()
    priv23, addr23 = privx23()
    priv24, addr24 = privx24()
    priv25, addr25 = privx25()
    priv26, addr26 = privx26()
    priv27, addr27 = privx27()

    bal0 = getbal(addr0)
    bal1 = getbal(addr1)
    bal2 = getbal(addr2)
    bal3 = getbal(addr3)
    bal4 = getbal(addr4)
    bal5 = getbal(addr5)
    bal6 = getbal(addr6)
    bal7 = getbal(addr7)
    bal8 = getbal(addr8)
    bal9 = getbal(addr9)
    bal10 = getbal(addr10)
    bal11 = getbal(addr11)
    bal12 = getbal(addr12)
    bal13 = getbal(addr13)
    bal14 = getbal(addr14)
    bal15 = getbal(addr15)
    bal16 = getbal(addr16)
    bal17 = getbal(addr17)
    bal18 = getbal(addr18)
    bal19 = getbal(addr19)
    bal20 = getbal(addr20)
    bal21 = getbal(addr21)
    bal22 = getbal(addr22)
    bal23 = getbal(addr23)
    bal24 = getbal(addr24)
    bal25 = getbal(addr25)
    bal26 = getbal(addr26)
    bal27 = getbal(addr27)
    ifer: str = '0 ETH'
    table = Table(title="Ethereum Private Key Clear\n[PROGRAMMER [b red]Mmdrza.COM[/]]", style="green", border_style="gold1", box=box.ROUNDED, header_style="gold1 on grey7")
    table.add_column("No.", justify="center", style="grey78")
    table.add_column("[i]ADDRESS[/]", justify="center", style="green on grey7", no_wrap=False)
    table.add_column("PrivateKey", justify="center", style="gold1", no_wrap=False)
    table.add_column("Balance", justify="center", style="i white on grey7")

    if str(bal0) != str(ifer) or str(bal1) != str(ifer) or str(bal2) != str(ifer) or str(bal3) != str(ifer) or str(bal4) != str(ifer) or str(bal5) != str(ifer) or str(bal6) != str(ifer) or str(bal7) != str(ifer) or str(bal8) != str(ifer) or str(bal9) != str(ifer) or str(bal10) != str(ifer) or str(bal11) != str(ifer) or str(bal12) != str(
            ifer) or str(bal13) != str(ifer) or str(bal14) != str(ifer) or str(bal15) != str(ifer) or str(bal16) != str(ifer) or str(bal17) != str(ifer) or str(bal18) != str(ifer) or str(bal19) != str(ifer) or str(bal20) != str(ifer) or str(bal21) != str(ifer) or str(bal22) != str(ifer) or str(bal23) != str(ifer) or str(bal24) != str(
        ifer) or str(bal25) != str(ifer) or str(bal26) != str(ifer) or str(bal27) != str(ifer):
        w += 1
        os.system("cls")
        os.system(f"title Checked:{z} Total:{z + 28} Win: {w}")
        with open("Found.txt", "a") as xf:
            xf.write('\nADDR: ' + str(addr0) + '   BAL:' + str(bal0) + '\nPrivateKey: ' + str(priv0))
            xf.write('\nADDR: ' + str(addr1) + '   BAL:' + str(bal1) + '\nPrivateKey: ' + str(priv1))
            xf.write('\nADDR: ' + str(addr2) + '   BAL:' + str(bal2) + '\nPrivateKey: ' + str(priv2))
            xf.write('\nADDR: ' + str(addr3) + '   BAL:' + str(bal3) + '\nPrivateKey: ' + str(priv3))
            xf.write('\nADDR: ' + str(addr4) + '   BAL:' + str(bal4) + '\nPrivateKey: ' + str(priv4))
            xf.write('\nADDR: ' + str(addr5) + '   BAL:' + str(bal5) + '\nPrivateKey: ' + str(priv5))
            xf.write('\nADDR: ' + str(addr6) + '   BAL:' + str(bal6) + '\nPrivateKey: ' + str(priv6))
            xf.write('\nADDR: ' + str(addr7) + '   BAL:' + str(bal7) + '\nPrivateKey: ' + str(priv7))
            xf.write('\nADDR: ' + str(addr8) + '   BAL:' + str(bal8) + '\nPrivateKey: ' + str(priv8))
            xf.write('\nADDR: ' + str(addr9) + '   BAL:' + str(bal9) + '\nPrivateKey: ' + str(priv9))
            xf.write('\nADDR: ' + str(addr10) + '   BAL:' + str(bal10) + '\nPrivateKey: ' + str(priv10))
            xf.write('\nADDR: ' + str(addr11) + '   BAL:' + str(bal11) + '\nPrivateKey: ' + str(priv11))
            xf.write('\nADDR: ' + str(addr12) + '   BAL:' + str(bal12) + '\nPrivateKey: ' + str(priv12))
            xf.write('\nADDR: ' + str(addr13) + '   BAL:' + str(bal13) + '\nPrivateKey: ' + str(priv13))
            xf.write('\nADDR: ' + str(addr14) + '   BAL:' + str(bal14) + '\nPrivateKey: ' + str(priv14))
            xf.write('\nADDR: ' + str(addr15) + '   BAL:' + str(bal15) + '\nPrivateKey: ' + str(priv15))
            xf.write('\nADDR: ' + str(addr16) + '   BAL:' + str(bal16) + '\nPrivateKey: ' + str(priv16))
            xf.write('\nADDR: ' + str(addr17) + '   BAL:' + str(bal17) + '\nPrivateKey: ' + str(priv17))
            xf.write('\nADDR: ' + str(addr18) + '   BAL:' + str(bal18) + '\nPrivateKey: ' + str(priv18))
            xf.write('\nADDR: ' + str(addr19) + '   BAL:' + str(bal19) + '\nPrivateKey: ' + str(priv19))
            xf.write('\nADDR: ' + str(addr20) + '   BAL:' + str(bal20) + '\nPrivateKey: ' + str(priv20))
            xf.write('\nADDR: ' + str(addr21) + '   BAL:' + str(bal21) + '\nPrivateKey: ' + str(priv21))
            xf.write('\nADDR: ' + str(addr22) + '   BAL:' + str(bal22) + '\nPrivateKey: ' + str(priv22))
            xf.write('\nADDR: ' + str(addr23) + '   BAL:' + str(bal23) + '\nPrivateKey: ' + str(priv23))
            xf.write('\nADDR: ' + str(addr24) + '   BAL:' + str(bal24) + '\nPrivateKey: ' + str(priv24))
            xf.write('\nADDR: ' + str(addr25) + '   BAL:' + str(bal25) + '\nPrivateKey: ' + str(priv25))
            xf.write('\nADDR: ' + str(addr26) + '   BAL:' + str(bal26) + '\nPrivateKey: ' + str(priv26))
            xf.write('\nADDR: ' + str(addr27) + '   BAL:' + str(bal27) + '\nPrivateKey: ' + str(priv27))
            xf.close()
    else:
        console.clear()
        table.add_row(str(z), str(addr0), str(priv0), str(bal0))
        z += 1
        table.add_row(str(z), str(addr1), str(priv1), str(bal1))
        z += 1
        table.add_row(str(z), str(addr2), str(priv2), str(bal2))
        z += 1

        table.add_row(str(z), str(addr3), str(priv3), str(bal3))
        z += 1

        table.add_row(str(z), str(addr4), str(priv4), str(bal4))
        z += 1

        table.add_row(str(z), str(addr5), str(priv5), str(bal5))
        z += 1
        table.add_row(str(z), str(addr6), str(priv6), str(bal6))
        z += 1
        table.add_row(str(z), str(addr7), str(priv7), str(bal7))
        z += 1
        table.add_row(str(z), str(addr8), str(priv8), str(bal8))
        z += 1
        table.add_row(str(z), str(addr9), str(priv9), str(bal9))
        z += 1
        table.add_row(str(z), str(addr10), str(priv10), str(bal10))
        z += 1
        table.add_row(str(z), str(addr11), str(priv11), str(bal11))
        z += 1
        table.add_row(str(z), str(addr12), str(priv12), str(bal12))
        z += 1
        table.add_row(str(z), str(addr13), str(priv13), str(bal13))
        z += 1
        table.add_row(str(z), str(addr14), str(priv14), str(bal14))
        z += 1
        table.add_row(str(z), str(addr15), str(priv15), str(bal15))
        z += 1
        table.add_row(str(z), str(addr16), str(priv16), str(bal16))
        z += 1
        table.add_row(str(z), str(addr17), str(priv17), str(bal17))
        z += 1
        table.add_row(str(z), str(addr18), str(priv18), str(bal18))
        z += 1
        table.add_row(str(z), str(addr19), str(priv19), str(bal19))
        z += 1
        table.add_row(str(z), str(addr20), str(priv20), str(bal20))
        z += 1
        table.add_row(str(z), str(addr21), str(priv21), str(bal21))
        z += 1
        table.add_row(str(z), str(addr22), str(priv22), str(bal22))
        z += 1
        table.add_row(str(z), str(addr23), str(priv23), str(bal23))
        z += 1
        table.add_row(str(z), str(addr24), str(priv24), str(bal24))
        z += 1
        table.add_row(str(z), str(addr25), str(priv25), str(bal25))
        z += 1
        table.add_row(str(z), str(addr26), str(priv26), str(bal26))
        z += 1
        table.add_row(str(z), str(addr27), str(priv27), str(bal27))
        z += 1
        console.print(table)
        console.print(f'[b white on dark_blue] [ Check:{z} ]   [/][b red on white] [ Total:{z * 28} ] [/][i white on blue] Found: {w} [/] [b gold1] [ TRIAL VERSION ] [MMDRZA.COM]')
