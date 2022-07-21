from . import mysqlc
from datetime import datetime
from urllib.parse import urlparse
from urllib.parse import parse_qs


class ezapi:
    def __init__(self, logging=False) -> None:
        self.methods = []
        self.parameters = {}
        self.dbconnection = False
        self.mapfunctions = {}
        self.querys = {}
        self.methodlist = ['POST', 'GET', 'PUT', 'PATCH', 'DELETE']
        self.logging = logging

    def RegisterDB(self, host: str, port: int, password: str, login: str, dbname: str) -> None:
        """Register database login information (mysql)

        Args:
            host (str): db host
            port (int): db port
            password (str): db password
            login (str): db user
        """
        self.dbconnection = mysqlc.CheckConnection(
            host=host, port=port, password=password, login=login, db=dbname)

    def AddMethod(self, method: str, params: list, query=False, map=None) -> None:
        """Add a new method to the endpoint

        Args:
            method (str): method in ['POST', 'GET', 'PUT', 'PATCH', 'DELETE']
            params (array): parameters
            query (array): SQL query, can be false if we just want to handle data
            map (function): map function for GET
        """
        if method in self.methodlist:
            self.methods.append(method)
            self.parameters[method] = params
            self.mapfunctions[method] = map
            self.querys[method] = query

    def Mapdefault(self, _):
        return _

    def log(self, type: str, msg: str) -> str:
        """Formate log

        Args:
            type (str): log type
            msg (str): log message

        Returns:
            str: The log message formatted
        """
        dt_string = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        return f"[API-{type}] - [{dt_string}] - {msg}"

    def CheckParam(self, method, params):
        for p in self.parameters[method]:
            if p not in params:
                if self.logging:
                    print(
                        self.log("ERROR", f"Parameter {p} is missing"))
                self.dbconnection.close()
                raise parameterError(p)

    def GetParams(self, request):
        if request.method in ["GET", "DELETE"]:
            params = request.args
            if type(request.form) is not dict:
                params = params.to_dict(flat=False)
            params = dict(map(lambda k: (k[0], k[1][0]), params.items()))
            return params
        elif request.method in ['POST', 'PUT', 'PATCH']:
            # data could be in a form or raw data
            if len(request.form) > 0:
                if type(request.form) is not dict:
                    params = request.form.to_dict(flat=False)
                else:
                    params = request.form
            else:
                parsed_data = urlparse("?"+request.data.decode('utf-8'))
                params = parse_qs(parsed_data.query)
            params = dict(
                map(lambda k: (k[0], k[1][0]), params.items()))
            return params

    def Handler(self, request, defp=False):
        if request.method not in self.methods:
            if self.logging:
                print(self.log("ERROR", "Method not supported"))
            raise methodError(request.method)
        else:
            if request.method in ["GET", "DELETE"]:
                # args in url

                # Formatting ImmutableDict
                if defp:
                    params = defp
                else:
                    params = self.GetParams(request)

                self.CheckParam(request.method, params)
                if self.querys[request.method] and self.dbconnection:
                    queryparams = tuple([params[i]
                                        for i in self.parameters[request.method]])
                    try:
                        r = mysqlc.ReadDB(
                            self.querys[request.method], self.dbconnection, queryparams)
                        self.dbconnection.close()
                        return True, {
                            "params": params,
                            "fetch": r
                        }
                    except Exception:
                        self.dbconnection.close()
                        return False, e

            elif request.method in ['POST', 'PUT', 'PATCH']:
                # args in body
                if defp:
                    params = defp
                else:
                    params = self.GetParams(request)
                # check if evry single parameter is in the request
                self.CheckParam(request.method, params)
                if self.querys[request.method] and self.dbconnection:
                    queryparams = tuple([params[i]
                                        for i in self.parameters[request.method]])
                    # Try to write in database
                    try:
                        mysqlc.WriteDB(
                            self.querys[request.method], self.dbconnection, queryparams)
                        self.dbconnection.close()
                        return True, {
                            "params": params
                        }
                    except Exception as e:
                        self.dbconnection.close()
                        return False, e


class parameterError(Exception):
    def __init__(self, param):
        self.message = f"parameterError missing parameter : {param}"

        super().__init__(self.message)

    def __str__(self):
        return self.message


class methodError(Exception):
    def __init__(self, methode):
        self.message = f"methodError bad method : {methode}"

        super().__init__(self.message)

    def __str__(self):
        return self.message
