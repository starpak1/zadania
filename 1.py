#!/usr/bin/env  python3
import subprocess,os,sys,argparse,re,signal
from subprocess import Popen, PIPE

parser = argparse.ArgumentParser(description = 'Simply program to killing process on selected ports')
parser.add_argument('-p', help='port number for process', type=str)

args = parser.parse_args()

if args.p:
    print('port number= ' + args.p)
    output = Popen(["lsof", "-i", ":{0}".format(args.p)], stdout=PIPE, stderr=PIPE)
    stdout, stderr = output.communicate()
    print(stdout.decode())
    for output in str(stdout.decode("utf-8")).split("\n")[1:]:
        #data = [x for x in output.split(" ") if x != '']
        data = []
        for x in output.split(" "):
            if x !='':
                data.append(x)

        if (len(data) != 0):
             print(data[1])
             os.kill(int(data[1]), signal.SIGKILL)
             print('Process working on port: ' +args.p + ' was killed')
else:
    print('nie podales argumentow, wpisz ponownie')



