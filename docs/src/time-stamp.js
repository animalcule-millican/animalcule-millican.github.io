// Get the current point in time 
const timestamp = new Date();

// advance by 24 hours, to get to tomorrow
timestamp.setTime(timestamp.getTime() + (24 * 60 * 60 * 1000));

// format and output the result
const locale = undefined; // use the user's current locale (language/region)
document.getElementById("spanDate").innerHTML = timestamp.toLocaleString(locale, {
  timeZone: 'America/Chicago', // use the US Central Time Zone
  year: 'numeric', // include the year as a number
  month: 'long',   // include the month as the long name
  day: 'numeric'   // include the day as a number
});