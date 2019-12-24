import requests
class Http:
    """
    An http interface used for making http request.
    
    Attributes:
        host (string): Host you want to send requests to
        port (number): Default none
    """

    def __init__(self, host, port=None):
        """
        The contructor to initizalise host and port to which communication is to be done
        
        Parameters:
            host (string)
            port (string)
        """
        self.host = host
        if port and port != None:
            self.host = self.host+':'+str(port)
        
    def get(self, path, queryParams=None, headers = None):
        """
        For doing get requests to the server, will return a dictonary 
        
        Parameters:
            path (string)
            queryParams (dict)
            headers (dict)

        Returns:
            dict of data or empty dict if data sent is empty
        
        """
        try:
            address = self.host+path
            response = requests.get(address,params = queryParams, headers=None)
            if response.status_code >= 200 and response.status_code < 300:
                if len(response.text) == 0:
                    return {}
                return response.json()
            else:
                response.raise_for_status()
        except requests.exceptions.InvalidURL as error:
            print("Invalid URL")
            print(error)
        except requests.exceptions.HTTPError as error:
            print("Request failed with status "+ str(response.status_code))
            print(error)
        except requests.exceptions.ConnectTimeout:
            print("Connection timeout")
        except ValueError as error:
            print(str(error))
        except Exception as err:
            print(str(err))
    def post(self, path, params, headers = None):
        """
        For doing post requests to the server, will return a dictonary 
        
        Parameters:
            path (string)
            params (dict)
            headers (dict)

        Returns:
            dict of data or empty dict if data sent is empty
        
        """
        address = self.host+path
        try:
            response = requests.post(address,data = params, headers= headers)
            if response.status_code >= 200 and response.status_code < 300:
                if len(response.text) == 0:
                        return {}
                return response.json()
            else:
                response.raise_for_status()
        except requests.exceptions.HTTPError as error:
            print("Request failed with status "+ str(response.status_code))
            print(error)
        except requests.exceptions.InvalidURL:
            print("Invalid URL")
        except requests.exceptions.ConnectTimeout:
            print("Connection timeout")
        except Exception as err:
            print(str(err))
    def put(self, path, params=None, headers = None):
        """
        For doing put requests to the server, will return a dictonary 
        
        Parameters:
            path (string)
            params (dict)
            headers (dict)

        Returns:
            dict of data or empty dict if data sent is empty
        
        """
        address = self.host+path
        try:
            response = requests.put(address,data = params,headers= headers)
            if response.status_code >= 200 and response.status_code < 300:
                if len(response.text) == 0:
                        return {}
                return response.json()
            else:
                response.raise_for_status()
        except requests.exceptions.HTTPError as error:
            print("Request failed with status "+ str(response.status_code))
            print(error)
        except requests.exceptions.InvalidURL:
            print("Invalid URL")
        except requests.exceptions.ConnectTimeout:
            print("Connection timeout")
        except Exception as err:
            print(str(err))
