import json
class configParser:

    def __init__(self,path):
        self.path = path

    def configReader(self):
        with open(self.path) as json_file:
            data = json.load(json_file)
            return data


#if __name__=="__main__":
 #   a = configParser("/Users/harsh/Documents/Documents/DevelopmentEnvironnment/Projects/Secured-PnP-IoT/configuration/config.json")
 #   a.configReader()