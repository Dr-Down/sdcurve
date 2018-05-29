google.charts.load('current', {'packages':['corechart']});
google.charts.setOnLoadCallback(drawChart);

function convertToArray(string) {
  string = string.replace(/'/g, '"');
  var array = JSON.parse(string)

  // Insert new curve with null
  for(i=2; i<array.length; i++) {
    array[i][8] = null
  }

  populatePatientCurve(array)

  console.log(array)

  return array
}

function populatePatientCurve(array) {
  array[10][8] = 67.10
  array[11][8] = 70.00
  array[12][8] = 73.69
  array[13][8] = 74.77
  array[14][8] = 79.00
  array[17][8] = 80.23
  array[18][8] = 83.22
  array[19][8] = 85.60
  array[20][8] = 85.62
  array[22][8] = 85.62
}

function defineOptions(title) {
  return {
    title: title,
    hAxis: {
      title: 'Age',
      titleTextStyle: {color: '#333'},
      minValue: 25
    },
    vAxis: {
      title: 'Height',
      titleTextStyle: {color: '#333'},
      minValue: 0,
      format: 'decimal',
    },
    explorer: {
      actions: ['dragToZoom', 'rightClickToReset'],
      axis: 'horizontal',
      keepInBounds: true,
      maxZoomIn: 4.0
    },
    crosshair: { trigger: 'selection' },
    lineWidth: 2,
    series: {
      0: { color: '#e2431e' },
      1: { color: '#e7711b' },
      2: { color: '#f1ca3a' },
      3: { color: '#6f9654' },
      4: { color: '#1c91c0' },
      5: { color: '#e7711b' },
      6: { color: '#e2431e' },
    },
    is3D: true
  };
}

function drawChart() {
  var array = convertToArray(document.getElementById("graphic").innerText)
  var data = google.visualization.arrayToDataTable(array);
  var options = defineOptions(title='Height-based growth curve for males aged 0 to 36 months')
  var chart = new google.visualization.AreaChart(document.getElementById('chart_height_curve'));
  chart.draw(data, options);
}
