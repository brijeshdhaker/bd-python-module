import os
from typing import Iterator

# This is only needed for windows
def setEnv():
    # Replace with your Spark dir in windows
    os.environ['PYTHONUNBUFFERED'] = "1"
    os.environ['PYTHONPATH'] = "/home/brijeshdhaker/IdeaProjects/bd-notebooks-module/src/main/py"

def printEnv():
    print(f"PYTHONUNBUFFERED : {os.environ['PYTHONUNBUFFERED']}")
    print(f"PYTHONPATH :  {os.environ['PYTHONPATH']}")

def main(spark):
    print(" I am inside main .. ")



if __name__ == "__main__":

    # If running on windows , set env variables , for Linux skip
    if os.name == 'nt':
        print("Windows OS , printing env variable set") 
        setEnv()
    else:
        print("Linux OS , printing env variable set") 
        printEnv()
