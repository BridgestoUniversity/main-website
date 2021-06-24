$(document).ready(function () {
  // console.log("hello!!");
  //   alert("hello!");

  // var navButton = $("bars-container");
  $(".bars-container").click(toggleNav);

  $(".hero").click(closeNav);
  $(".recent-events").click(closeNav);
  $(".footer-container").click(closeNav);

  $(".mentee-option").click(toggleMenteeOffers);
  $(".mentor-option").click(toggleMentorOffers);
  $(".editorial-option").click(toggleEditorialOffers);
  $(".dev-option").click(toggleDevOffers);
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

function toggleMenteeOffers() {
  $(".mentee-option").toggleClass("active");
}

function toggleMentorOffers() {
  $(".mentor-option").toggleClass("active");
}

function toggleEditorialOffers() {
  $(".editorial-option").toggleClass("active");
}

function toggleDevOffers() {
  $(".dev-option").toggleClass("active");
}
