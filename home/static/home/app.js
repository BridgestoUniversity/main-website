$(document).ready(function () {
  // console.log("hello!!");
  //   alert("hello!");

  // var navButton = $("bars-container");
  $(".bars-container").click(toggleNav);

  $(".hero").click(closeNav);
  $(".recent-events").click(closeNav);
  $(".footer-container").click(closeNav);
});

function toggleNav() {
  console.log("navButton clicked");

  var navButton = $(".bars-container");
  navButton.toggleClass("nav-open");

  var navList = $(".nav-items-collapse");
  navList.toggleClass("nav-open");
}

function closeNav() {
  var navButton = $(".bars-container");
  navButton.removeClass("nav-open");

  var navList = $(".nav-items-collapse");
  navList.removeClass("nav-open");
}
