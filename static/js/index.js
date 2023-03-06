function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== "") {
      var cookies = document.cookie.split(";");
      for (var i = 0; i < cookies.length; i++) {
        var cookie = cookies[i].trim();
        if (cookie.substring(0, name.length + 1) === name + "=") {
          cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
          break;
        }
      }
    }
    return cookieValue;
  }
  
  function deleteAnswer(id) {
    let csrftoken = getCookie("csrftoken");
  
    fetch("/question_ans/deleteanswer/", {
      method: "post",
      body: JSON.stringify({
        id: id,
      }),
      headers: {
        Accept: "application/json, text/plain, */*",
        "Content-Type": "application/json",
        "X-CSRFToken": csrftoken,
      },
    })
      .then((res) => {
        return res.json();
      })
      .then((i) => {
        document.getElementById(id).remove();
      });
  }
  