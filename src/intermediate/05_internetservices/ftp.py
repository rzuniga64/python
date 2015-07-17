import ftplib
import sys


def getdir():
    connect = ftplib.FTP("www.ualr.edu")
    connect.login("facstaff\mmmcmillan", "meredith26")
    data = list()
    connect.dir(data.append)
    connect.quit()
    for line in data:
        print(line)


def getfile():
    filename = sys.argv[1]
    connect = ftplib.FTP("www.ualr.edu")
    connect.login("facstaff\mmmcmillan", "meredith26")
    connect.retrlines("RETR " + filename)
    connect.quit()


def main():
    getdir()
    
main()