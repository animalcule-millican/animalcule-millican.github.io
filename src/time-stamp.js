var timestamp = new Date();
var spanDate = document.getElementById("spanDate").innerHTML = timestamp.toLocaleString({
  timeZone: 'America/Chicago', // use the US Central Time Zone
  year: 'numeric', // include the year as a number
  month: 'long',   // include the month as the long name
  day: 'numeric'   // include the day as a number
});
spanDate.innerHTML = currentDate.toLocaleString();