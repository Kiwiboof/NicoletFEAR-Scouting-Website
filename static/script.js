var mins = 2;
var seconds = 30;
var auto_pickup = 0;
var auto_high = 0;
var auto_low = 0;
var auto_miss = 0;
var teleop_high = 0;
var teleop_low = 0;
var teleop_miss = 0;
var climb = 0;

$('#cargo-pickup').click(function() {
  auto_pickup++;
  $('#auto-pickup').html(auto_pickup);
});

$('#auto-high-goal').click(function() {
  auto_high++;
  $('#auto-high').html(auto_high);
});

$('#auto-low-goal').click(function() {
  auto_low++;
  $('#auto-low-shots').html(auto_low);
});

$('#auto-missed-goal').click(function() {
  auto_miss++;
  $('#auto-miss').html(auto_miss);
});

$('#high-goal').click(function() {
  teleop_high++;
  $('#teleop-high-shots').html(teleop_high);
});

$('#low-goal').click(function() {
  teleop_low++;
  $('#teleop-low-shots').html(teleop_low);
});

$('#start').click(function() {
  startTimer();
});

$('#stop').click(function() {
  clearTimeout(timex);
});

$('#reset').click(function() {
  mins = 2;
  seconds = 30;
  $('#mins').html('2:');
  $('#seconds').html('30');
});

function startTimer() {
  timex = setTimeout(function() {
    seconds--;
    if (seconds < 0) {
      seconds = 59;
      mins--;
      $("#mins").text(mins + ':');
    }
    $("#seconds").text(seconds);

    if (seconds > 0 || mins > 0) {
      startTimer();
    }
  }, 1000);
}
