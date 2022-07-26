const host = "flaskezs.com:5000";
const api = new Api(window.location.protocol + "//api." + host + "/v1/");

function TestApp(resp) {
  let Title = document.getElementById("Title");
  let Message = document.getElementById("Msg");
  Title.textContent = resp.slug;
  Message.textContent = resp.msg;
}

function TestAppError(error) {
  let Title = document.getElementById("Title");
  let Message = document.getElementById("Msg");
  Title.textContent = "Oups...";
  Message.textContent = `Something went wrong (${error})`;
}

document.addEventListener("DOMContentLoaded", function () {
  if (window.fetch) {
    api.Fetch({
      endpoint: "test",
      method: "GET",
      funct: TestApp,
      typef: api.Respjson,
      funcerror: TestAppError,
    });
  }
});
