#@author: kalari499
import os, sys

def execute(command):
    print("Running: {}".format(command))
    os.system(command)

def welcome(): print("Run [h / help] or to see all commands or [q / quit] to quit.")

def print_help():
    print("""
    Disclaimer: This script is meant for the hackathon to install/interact with gaia, it is not meant for production.\n
    Usage:
    - compile_stuff
    - install everything        Install multi-node network. (Normally just run this once if this is the first time)
    - testnet start/init        Start testnet from the beginning (height = 1)
    """)

def compile_stuff():
    execute("make tools install")

def install_everything():
    print("* Step 1: Install gaiad and gaiacli")
    execute("make tools install")

    print("\n* Step 2: Install docker and docker-compose")
    print("""Sorry you have to install this manually, I'm too lazy to automate this:
    - https://docs.docker.com/install/linux/docker-ce/ubuntu/
    - https://docs.docker.com/compose/install/""")

    print("\n* Step 3: Build Multi-node, local testnet")
    execute("make build-linux")
    execute("make build-docker-gaiadnode")

    print("\n\nInstallation finished (Assume no errors). Run 'testnet start' to start.")

def testnet_start():
    execute("[ -d build/gentxs ] && sudo rm -rf build/")
    execute("make build-linux localnet-start")

def main():
    os.chdir(os.path.abspath(os.path.join(os.path.realpath(__file__), "../..")))
    welcome()
    while True:
        print("1337-h4x0r.club > ", end="")
        line = input().strip()
        if line in ["h", "help"]:
            print_help()
        elif line in ["q", "quit", "exit", "bye"]:
            print("Bye!")
            break
        elif line == "compile":
            compile_stuff()
        elif line == "install everything":
            install_everything()
        elif line in ["testnet start", "testnet init"]:
            testnet_start()
        elif line == "clean":
            execute("rm -f $HOME/.gaiad/config/addrbook.json $HOME/.gaiad/config/genesis.json")
            execute("gaiad unsafe-reset-all")
        else:
            print("Invalid command")

if __name__ == "__main__":
    main()
