function myFunction() {
  var x = document.getElementById("MyNav");
  if (x.className === "nav-masthead") {
    x.className += " responsive";
  } else {
    x.className = "nav-masthead";
  }
}