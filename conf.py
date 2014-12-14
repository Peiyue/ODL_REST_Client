from requests.auth import HTTPBasicAuth
def conf():
    
    #change the following settings if necessary      
    controllerIp='http://192.168.80.136:8080'
    ODL_user='admin'
    ODL_password='admin'

    auth = HTTPBasicAuth(ODL_user,ODL_password)
    setting={'controllerIp':controllerIp,'auth':auth}
    return setting
