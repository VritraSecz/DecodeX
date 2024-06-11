#!/bin/python3
# tool by VritraSecz
# https://github.com/VritraSecz

import hashlib
import os
import time
from time import sleep

rest = """\033[0m\033[38;5;40m ______                       _     \033[1;37m  _     _ \033[38;5;40m
(______)                     | |    \033[1;37m (_)   (_) \033[38;5;40m
 _     _ _____  ____ ___   __| |_____   ___
| |   | | ___ |/ ___) _ \ / _  | ___ | |   |
| |__/ /| ____( (__| |_| ( (_| | ____|/ / \ \\
|_____/ |_____)\____)___/ \____|_____)_|   |_|
        ..:: \033[1;37mTool By - VritraSecz \033[38;5;40m::..

\033[1;37m[░░] \033[38;5;40mSelect Hash To Crack:

\033[1;37m[01]\033[38;5;40m MD5
\033[1;37m[02]\033[38;5;40m SHA1
\033[1;37m[03]\033[38;5;40m SHA224
\033[1;37m[04]\033[38;5;40m SHA256
\033[1;37m[05]\033[38;5;40m SHA384
\033[1;37m[06]\033[38;5;40m SHA512
\033[1;37m[07]\033[38;5;40m SHA3-224
\033[1;37m[08]\033[38;5;40m SHA3-256
\033[1;37m[09]\033[38;5;40m SHA3-384
\033[1;37m[10]\033[38;5;40m SHA3-512
\033[1;37m[99]\033[38;5;40m Exit
╔═══╗
╚═══[\033[1;37mdecodex\033[0m\033[38;5;40m]>\033[1;37m """


def main():
    print()
    while True:
        target_hash = input("\033[1;37m[~]\033[38;5;40m Enter target Hash: \033[1;37m")
        if target_hash == '':
            pass
        else:
            break

    while True:
        wordlist_path = input("\033[1;37m[~]\033[38;5;40m Want to use your own word list to crack hash [\033[1;37my/N\033[38;5;40m]: \033[1;37m")
        if wordlist_path == 'n' or wordlist_path == 'N' or wordlist_path == '':
            wordlist_path = 'core/default_list.txt'
            print("\033[1;37m[+] \033[38;5;40mDefault Wordlist selected")
            break
        elif wordlist_path == 'y' or wordlist_path == 'Y':
            while True:
                lsd = input("\033[1;37m[~]\033[38;5;40m Enter your wordlist path: \033[1;37m")
                if lsd == '':
                    pass
                else:
                    wordlist_path = lsd
                    break
            break
        else:
            pass
    
    print()
    total_words = sum(1 for line in open(wordlist_path, 'r', encoding='latin-1'))
    with open(wordlist_path, 'r', encoding='latin-1') as wordlist_file:
        tried = 0
        start_time = time.time()  
        for line in wordlist_file:
            word_hash = getattr(hashlib, hash_type)(line.strip().encode()).hexdigest()

            tried += 1
            print(f"\r\033[1;37m[~]\033[38;5;40m Trying:\033[1;37m {tried}/{total_words}", end='')

            if word_hash == target_hash:
                end_time = time.time() 
                elapsed_time = end_time - start_time  
                attack_speed = tried / elapsed_time 

                print("\n")
                print("\033[38;5;40m="*20 + " \033[1;37mSummery " + "\033[38;5;40m="*20)
                print(f"\n\033[1;37m[+] \033[38;5;40mCracked Hash:\033[1;37m {line.strip()}")
                print(f"\033[1;37m[+] \033[38;5;40mTarget Hash:\033[1;37m {target_hash}")
                print(f"\033[1;37m[+] \033[38;5;40mHash Type:\033[1;37m {hash_type}")
                print(f"\033[1;37m[+] \033[38;5;40mWordlist Used:\033[1;37m {wordlist_path}")
                print(f"\033[1;37m[+] \033[38;5;40mCracking Status:\033[1;37m Success")
                print(f"\033[1;37m[+] \033[38;5;40mTime Taken:\033[1;37m {elapsed_time:.2f} Seconds")
                print(f"\033[1;37m[+] \033[38;5;40mHighest Attacking Speed:\033[1;37m {attack_speed:.2f} Words/Second")
                print(f"\033[1;37m[+] \033[38;5;40mWordlist Total Words:\033[1;37m {total_words}")
                print(f"\033[1;37m[+] \033[38;5;40mUsed Total Words:\033[1;37m {tried}")
                print()
                break

        else:
            end_time = time.time() 
            elapsed_time = end_time - start_time
            attack_speed = tried / elapsed_time  

            print("\n")
            print("\033[38;5;40m="*20 + " \033[1;37mSummery " + "\033[38;5;40m="*20)
            print(f"\n\033[1;37m[+] \033[38;5;40mCracked Hash:\033[1;31m Not found")
            print(f"\033[1;37m[+] \033[38;5;40mTarget Hash:\033[1;37m {target_hash}")
            print(f"\033[1;37m[+] \033[38;5;40mHash Type:\033[1;37m {hash_type}")
            print(f"\033[1;37m[+] \033[38;5;40mWordlist Used:\033[1;37m {wordlist_path}")
            print(f"\033[1;37m[+] \033[38;5;40mCracking Status:\033[1;31m Failed")
            print(f"\033[1;37m[+] \033[38;5;40mTime Taken:\033[1;37m {elapsed_time:.2f} Seconds")
            print(f"\033[1;37m[+] \033[38;5;40mHighest Attacking Speed:\033[1;37m {attack_speed:.2f} Words/Second")
            print(f"\033[1;37m[+] \033[38;5;40mWordlist Total Words:\033[1;37m {total_words}")
            print(f"\033[1;37m[+] \033[38;5;40mUsed Total Words:\033[1;37m {tried}")
            print()


# Open my youtube channel

os.system('xdg-open https://youtube.com/@Technolex')
print()
sleep(2)

while True:
    os.system('clear')
    asr = input(rest)
    if asr == '':
        pass
    elif asr == '1' or asr == '01':
        hash_type = 'md5'
        main()
        input("\n\033[1;34mPress ENTER To Continue")
    elif asr == '2' or asr == '02':
        hash_type = 'sha1'
        main()
        input("\n\033[1;34mPress ENTER To Continue")
    elif asr == '3' or asr == '03':
        hash_type = 'sha224'
        main()
        input("\n\033[1;34mPress ENTER To Continue")
    elif asr == '4' or asr == '04':
        hash_type = 'sha256'
        main()
        input("\n\033[1;34mPress ENTER To Continue")
    elif asr == '5' or asr == '05':
        hash_type = 'sha384'
        main()
        input("\n\033[1;34mPress ENTER To Continue")
    elif asr == '6' or asr == '06':
        hash_type = 'sha512'
        main()
        input("\n\033[1;34mPress ENTER To Continue")
    elif asr == '7' or asr == '07':
        hash_type = 'sha3_224'
        main()
        input("\n\033[1;34mPress ENTER To Continue")
    elif asr == '8' or asr == '08':
        hash_type = 'sha3_256'
        main()
        input("\n\033[1;34mPress ENTER To Continue")
    elif asr == '9' or asr == '09':
        hash_type = 'sha3_384'
        main()
        input("\n\033[1;34mPress ENTER To Continue")
    elif asr == '10':
        hash_type = 'sha3_512'
        main()
        input("\n\033[1;34mPress ENTER To Continue")
    elif asr == '99':
        print("\n\033[1;37m[+] \033[38;5;40mThank you for using DecodeX! If you ever need to crack hashes again, feel free to come back. And have a great day!\n")
        exit()
    else:
        pass
