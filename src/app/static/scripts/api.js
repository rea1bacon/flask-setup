class Api {
  constructor(endpoint) {
    this.endpoint = endpoint;
  }

  Respjson(obj) {
    return obj.json();
  }

  Fetch({
    target,
    method = "GET",
    funct,
    typef,
    headers = {},
    args = {},
    funcerror = false,
  }) {
    var Fheaders = new Headers(headers);
    args.headers = Fheaders;
    args.method = method;
    fetch(this.endpoint + target, args)
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
            fetch: target,
            type: "failure",
            message: "A problem occurred during the request : " + error,
          });
        }
      });
  }
}
