class Api {
  constructor(url) {
    this.url = url;
  }

  Respjson(obj) {
    return obj.json();
  }

  Fetch({
    endpoint,
    method = "GET",
    funct,
    typef,
    headers = {},
    args = {},
    funcerror = false,
  }) {
    var Fheaders = new Headers(headers);
    args.headers = {
      "Access-Control-Allow-Origin": "*",
      Accept: "application/json",
    };
    // args.headers = Fheaders;
    args.method = method;
    args.mode = "cors";
    fetch(this.url + endpoint, args)
      .then((resp) => {
        if (!resp.ok) {
          throw new Error("response code " + resp.status);
        } else {
          return resp;
        }
      })
      .then((resp) => typef(resp))
      .then((resp) => funct(resp))
      .catch(function (error) {
        if (funcerror) {
          funcerror(error);
        } else {
          console.log({
            fetch: endpoint,
            type: "failure",
            message: "A problem occurred during the request : " + error,
          });
        }
      });
  }
}
