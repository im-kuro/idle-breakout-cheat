import base64, argparse
from colorama import Fore, Back, Style

argsToParse = argparse.ArgumentParser(description="Coolmath Games 'Idle Breakout' Tool -- OpSec WH")


argsToParse.add_argument("--setlevel", "-sl", help="Enable storing passwords to a local disk.", default=10000)
argsToParse.add_argument("--setmoney", "-sm", help="", default=999999999)
argsToParse.add_argument("--setgold", "-sg", help="", default=99999999)
argsToParse.add_argument("--setunclaimedgold", "-suc", help="", default=999999)

argsToParse.add_argument("--numberpowerup", "-np", help="", default=100) 

argsToParse.add_argument("--basicballdamage", "-bbd", help="", default=5)# balls Damage level 
argsToParse.add_argument("--plasmaballdamage", "-pbd", help="", default=5)
argsToParse.add_argument("--sniperballdamage", "-sbd", help="", default=5)
argsToParse.add_argument("--scatterballdamage", "-scbd", help="", default=5)
argsToParse.add_argument("--cannonballdamage", "-cbd", help="", default=5)
argsToParse.add_argument("--poisonballdamage", "-pobd", help="", default=5)

argsToParse.add_argument("--basicballspeed", "-bbs", help="", default=5) # balls Speed level
argsToParse.add_argument("--plasmaballspeed", "-pbs", help="", default=5)
argsToParse.add_argument("--sniperballspeed", "-sbs", help="", default=5)
argsToParse.add_argument("--scatterballspeed", "-scbs", help="", default=5)
argsToParse.add_argument("--cannonballspeed", "-cbs", help="", default=5)
argsToParse.add_argument("--poisonballspeed", "-pobs", help="", default=5)




argsToParse.add_argument("--bossbricks", "-bb", help="", default=20000)
argsToParse.add_argument("--skillpoints", "-sp", help="", default=500)

argParsedObj = argsToParse.parse_args()

def printError(ErrorID, ErrorInfo): print(f"[ ERROR ] - {ErrorID} - {ErrorInfo}")
def printInfo(Info): print(f"[ INFO ] - {Info}")


JSONAccCodes =  """

"BreakoutCodes": {
    "GodMode": "MTEwLDI0MjUwODQyLjEyLDI4ODM5MzQ3NSw2LDEsMTA1MDMsMTA3MDgsMTE5LDUsMjQsMTUsMSwxLDAsNDQ4NzAuMDgsNTgsMCwwLDk1MjYyLDk1MjYyLDExMTgyMywxMTE4MjMsMzkyMzQxLDM5MjM0MSw1MCw1MCw1MCw1MCw1MCw1MCw1MCw1MCw1MCw1MCw1MCw1MCw1MCw1MCw1MCw1MCw1MCw1MCw1MCw1MCw1MCw1MCw1MCw1MCw1MCw1MCw1MCw1MCw1MCw1MCw1MCw1MCw1MCw1MCw1MCw1MCw1MCw1MCw1MCw1MCw1MCw1MCw1MCw1MCw1MCw1MCw1MCw1MCw1MCw1MCw1MCw1MCw1MCw1MCw1MCw1MCw1MCw1MCw1MCw1MCw1MCw1MCw1MCw1MCw1MCw1MCw1MCw1MCw1MCw1MCw1MCw1MCw1MCw1MCw1MCw1MCw1MCw1MCw1MCw1MCw1MCw1MCw1MCw1MCwxLDEwMCw1MCw1MCw1MCw="
    "EasyStart": "MTAwLDk5OTk5OTksMTAwLDEwMCwwLDEsMSwwLDAsMSwwLDEsMSwwLDQ0ODcwLjU1LDk5OTk5OSwwLDAsMCwwLDAsMCwwLDAsMCwwLDAsMCwwLDAsMCwwLDAsMCwwLDAsMCwwLDAsMCwwLDAsMCwwLDAsMCwwLDAsMCwwLDAsMCwwLDAsMCwwLDAsMCwwLDAsMCwwLDAsMCwwLDAsMCwwLDAsMCwwLDAsMCwwLDAsMCwwLDAsMCwwLDAsMCwwLDAsMSwwLDAsMCwwLDAsMCwwLDAsMCwwLDAsMCwwLDAsMCwwLDAsMCwwLDAsMCwwLDAsMSwwLDEsMCwwLA=="
}

"""
def __init__():
    main.BuildCode()


class main:

    def BuildCode():

        BaseCodeNum = f"{argParsedObj.setlevel},{argParsedObj.setmoney},{argParsedObj.setgold},{argParsedObj.setgold},0,19,19,0,0,19,0,1,1,0,44869.98,999999,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,"
        EncodedCode = base64.b64encode(BaseCodeNum.encode())
        
        
        printInfo(f"Base64 Encoded Code ==> {EncodedCode}")
      
      
      
__init__()