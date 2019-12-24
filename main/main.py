import sys
import os
import subprocess
sys.path.append("/Users/harsh/Documents/Documents/DevelopmentEnvironnment/Projects/Secured-PnP-IoT/helperLibraries/")
from configParser import configParser

class IOT:

    def __init__(self,path):
        print("hello")
        self.path = path
        self.configObject = configParser(self.path)

    def getConfig(self):
        config = self.configObject.configReader()
        return config
    
    def extractConfig(self):
        config = self.getConfig()
        localNetworkCommunicationInterface = config["localNetworkConfig"]["localNetworkCommunicationInterface"]
        localNetworkCommunicationProtocol = config["localNetworkConfig"]["localNetworkCommunicationProtocol"]
        localNetworkEncryptionAlgorithm = config["localNetworkConfig"]["localNetworkEncryptionAlgorithm"]
        localNetworkEncryptionBit = config["localNetworkConfig"]["localNetworkEncryptionBit"]
        localNetworkEndpoint = config["localNetworkConfig"]["localNetworkEndpoint"]
        localNetworkConnectionPort = config["localNetworkConfig"]["localNetworkConnectionPort"]
        hardware = config["platformDetails"]["hardwarePlatform"]
        architecture = config["platformDetails"]["architecture"]
        os = config["platformDetails"]["os"]
        return [architecture,hardware,os,localNetworkCommunicationInterface,localNetworkCommunicationProtocol,localNetworkConnectionPort]

    def setup(self):
        filteredConfig = self.extractConfig()
        architecture = filteredConfig[0]
        hardware = filteredConfig[1]
        os = filteredConfig[2]
        localNetworkCommunicationProtocol = filteredConfig[4]
        argumentList= ["./installer.sh",architecture,hardware,os,localNetworkCommunicationProtocol]
        subprocess.call(argumentList)



if __name__=="__main__":
    obj=IOT("/Users/harsh/Documents/Documents/DevelopmentEnvironnment/Projects/Secured-PnP-IoT/configuration/config.json")
    #obj.extractConfig()
    obj.setup()



