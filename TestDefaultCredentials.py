#!/usr/local/bin/python3
import paramiko
import telnetlib


def SSHLogin(host, port, username, password):
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_kay_policy(paramiko.AutoAddPolicy())
        ssh.connect(host, port=port, username=username, password=password)
        ssh_session = ssh.get_transport().open_session()
        if ssh_session.active:
            print("SSH login sucessful on %s:%s with username %s and password %s" % (
                host, port, username, password))
    except Exception as e:
        return
    ssh.close()


def TelnetLogin(host, port, username, password):

    user = bytes(username + "\n", "utf-8")
    passwd = bytes(password + "\n", "utf-8")

    tn = telnetlib.Telnet(host, port)
    tn.read_until(bytes("login: ", "utf-8"))
    tn.write(user)
    tn.read_until(bytes("Password: ", "utf-8"))
    tn.write(passwd)
    try:
        result = tn.expect([bytes("Last login", "utf-8")], timeout=2)
        if (result[0] >= 0):
            print("Telent login sucessful on %s:%s with username %s and password %s" % (
                host, port, username, password))
    except EOFError:
        print("login failed %s %s" % (username,password))
    tn.close()
              
def main():              
    host = "192.168.0.1"
    with open("default.txt","r") as f:
        for line in f:
            vals = line.split()
            username = vals[0].strip()
            password = vals[1].strip()
            SSHLogin(host,22,username,password)
            TelnetLogin(host, 53, username, password)


if __name__ == "__main__":
    main()