import re
import os
from logmodule import logger

class PhoneInfo(object):
    UNKNOWN = "Unknown"
    PHONE_MODEL = "ro.product.model"
    SERIAL_NUM = "ro.serialno"
    INSTALL_MODEL = "pm.dexopt.install"
    ANDROID_VERSION = "ro.build.version.release"

    def __init__(self):
        propList = self.getPropertyList()
        self.productModel = self.getPropertyByName(propList, self.PHONE_MODEL)
        self.serialNum = self.getPropertyByName(propList, self.SERIAL_NUM)
        self.installMode = self.getPropertyByName(propList, self.INSTALL_MODEL)
        self.androidVersion = self.getPropertyByName(propList, self.ANDROID_VERSION)
        self.checkPropValue()

    def getPropertyList(self):
        cmd = "adb shell getprop"
        return os.popen(cmd).read().split('\n')
    
    def getPropertyByName(self, propList, property_name):
        property_name = "[" + property_name + "]"
        for prop in propList:
            if prop.find(property_name) != -1:
                return self.findValue(prop)
    
    def findValue(self, rawdata):
        data = re.findall(r'\[(.*?)\]', rawdata)
        if len(data) == 2:
            return data[1]
        else:
            return self.UNKNOWN
    
    def checkPropValue(self):
        logger.info(self.productModel)
        logger.info(self.serialNum)
        logger.info(self.installMode)
        logger.info(self.androidVersion)


def main():
    abc = PhoneInfo()

if __name__ == "__main__":
    main()