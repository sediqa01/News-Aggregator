function displayDate() {

    let today = new Date();
    // return number
    let dayName = today.getDay(),
      dayNum = today.getDate(),
      month = today.getMonth(),
      year = today.getFullYear();

const months = [
      "January",
      "February",
      "March",
      "April",
      "May",
      "June",
      "July",
      "August",
      "September",
      "October",
      "November",
      "December",
    ];
    const Weeksday = [
      "Sunday",
      "Monday",
      "Tuesday",
      "Wednesday",
      "Thursday",
      "Friday",
      "Saturday",
    ];
    // the html element
    const id = ["day", "daynum", "month", "year"];

    // return value array with number as a index
    const val = [Weeksday[dayName], dayNum, months[month], year];
    for (let i = 0; i < id.length; i++) {
      document.getElementById(id[i]).firstChild.nodeValue = val[i];
    }
  }

  displayDate();
  
  
  