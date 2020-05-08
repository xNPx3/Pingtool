import socket
import time
import getopt
import sys
import mysql.connector
import signal
import os
from sys import argv
from prettytable import PrettyTable

from random import randint, choice
from string import hexdigits

ip = "localhost"
port = 80
timeout = 1
retry = 1
_range = 10
delay = 0
verbose = False
single_address = True
single_port = True
up = 0
down = 0
db = False
portscan = False

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root",
    database="ipscanner"
)
mycursor = mydb.cursor()

full_cmd_arguments = argv
argument_list = full_cmd_arguments[1:]
arguments = len(argv) - 1

short_options = "hp:vt:r:abi:ds"
long_options = ["help", "port=", "verbose",
                "timeout=", "range=", "r-address", "r-port", "ip-address=", "database", "portscan"]


def handler(signum, frame):
    print("\nKeyboardInterrupt")
    os._exit(0)

signal.signal(signal.SIGINT, handler)

def random_ip():
    octets = []
    for x in range(4):
        octets.append(str(randint(0, 255)))
    return '.'.join(octets)


def isOpen(ip, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(timeout)
    try:
        s.connect((ip, int(port)))
        s.shutdown(socket.SHUT_RDWR)
        return True
    except:
        return False
    finally:
        s.close()


def checkHost(ip, port):
    ipup = False
    for i in range(retry):
        if isOpen(ip, port):
            ipup = True
            break
        else:
            time.sleep(delay)
    return ipup


def main(ip, port):
    signal.signal(signal.SIGINT, handler)
    up = 0
    down = 0
    print("------------------------------")
    print("Starting...")
    print("------------------------------")
    if portscan:
        for i in range(65536):
            if(i == 100):
                raise KeyboardInterrupt('hello')
            if checkHost(ip, i):
                print(ip + ":" + str(i) + " is OPEN")
                up += 1
                if db:
                    InsertToDB(ip, i)
            else:
                if verbose:
                    print(ip + ":" + str(i) + " is CLOSED")
                down += 1
    else:
        if single_address:
            if single_port:
                if checkHost(ip, port):
                    print(ip + ":" + str(port) + " is UP")
                    if db:
                        InsertToDB(ip, port)
                else:
                    print(ip + ":" + str(port) + " is DOWN")
            else:
                for i in range(_range):
                    port = randint(0, 65535)
                    if checkHost(ip, port):
                        print(ip + ":" + str(port) + " is UP")
                        up += 1
                        if db:
                            InsertToDB(ip, port)
                    else:
                        if verbose:
                            print(ip + ":" + str(port) + " is DOWN")
                        down += 1

        else:
            if single_port:
                for i in range(_range):
                    ip = random_ip()
                    if checkHost(ip, port):
                        print(ip + ":" + str(port) + " is UP")
                        up += 1
                        if db:
                            InsertToDB(ip, port)
                    else:
                        if verbose:
                            print(ip + ":" + str(port) + " is DOWN")
                        down += 1
            else:
                for i in range(_range):
                    ip = random_ip()
                    port = randint(0, 65535)
                    if checkHost(ip, port):
                        print(ip + ":" + str(port) + " is UP")
                        up += 1
                        if db:
                            InsertToDB(ip, port)
                    else:
                        if verbose:
                            print(ip + ":" + str(port) + " is DOWN")
                        down += 1

    print("------------------------------")
    if portscan:
        print(f"{up} ports were OPEN")
        print(f"{down} ports were CLOSED")
    else:
        print(f"{up} IPs were UP")
        print(f"{down} IPs were DOWN")


def InsertToDB(_ip, _port):
    sql = "INSERT INTO results (IP, Port) VALUES (%s, %s)"
    val = (_ip, str(_port))
    mycursor.execute(sql, val)

    mydb.commit()


if __name__ == '__main__':
    address = "localhost"
    port = 80
    try:
        arguments, values = getopt.getopt(
            argument_list, short_options, long_options)
    except getopt.error as err:
        # Output error, and return with an error code
        print(str(err))
        sys.exit(2)
    for current_argument, current_value in arguments:
        if current_argument in ("-h", "--help"):
            print("Displaying help")

            x = PrettyTable()
            x.field_names = ["Argument", "Alternative",
                             "Parameter type", "Info", "Default"]
            x.add_row(["--help", "-h", "None", "Displays help", "None"])
            x.add_row(["--verbose", "-v", "None", "Enables verbose mode", "False"])
            x.add_row(["--port", "-p", "Integer", "Sets port to scan", "80"])
            x.add_row(["--timeout", "-t", "Float", "Sets scan timeout (seconds)", "1"])
            x.add_row(["--range", "-r", "Integer",
                       "Sets the amount of times to scan", "10"])
            x.add_row(["--r-address", "-a", "None",
                       "Enables random address mode", "False"])
            x.add_row(["--r-port", "-b", "None",
                       "Enables random port mode", "False"])
            x.add_row(["--ip-address", "-i", "Str",
                       "Sets IP address to scan", "localhost"])
            x.add_row(["--database", "-d", "None",
                       "Saves online addresses to a MySQL database", "None"])
            x.add_row(["--portscan", "-s", "None",
                       "Enables portscan mode", "False"])
            print(x)

            sys.exit()
        elif current_argument in ("-v", "--verbose"):
            print("Enabling verbose mode")
            verbose = True
        elif current_argument in ("-p", "--port"):
            print(("Port set as %s") % (current_value))
            port = int(current_value)
        elif current_argument in ("-t", "--timeout"):
            print(("Timeout set as %s") % (current_value))
            timeout = float(current_value)
        elif current_argument in ("-r", "--range"):
            print(("Range set as %s") % (current_value))
            _range = int(current_value)
        elif current_argument in ("-a", "--r-address"):
            print("Enabling random address mode")
            single_address = False
        elif current_argument in ("-b", "--r-port"):
            print("Enabling random port mode")
            single_port = False
        elif current_argument in ("-i", "--ip-address"):
            print(("IP address set as %s") % (current_value))
            address = current_value
        elif current_argument in ("-d", "--database"):
            print("Enabling database mode")
            db = True
        elif current_argument in ("-s", "--portscan"):
            print("Enabling portscan mode")
            portscan = True
    try:
        main(address, port)
    except:
        print(sys.exc_info())
        os._exit(0)
