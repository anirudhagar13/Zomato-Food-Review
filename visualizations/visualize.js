google.charts.load('current', {'packages':['corechart']});
google.charts.setOnLoadCallback(init);

//******For Carousel*******
var slideIndex = 1;

function plusDivs(n) {
  showDivs(slideIndex += n);
}

function showDivs(n) {
  var i;
  var x = document.getElementsByClassName("mySlides");
  if (n > x.length) {slideIndex = 1}
  if (n < 1) {slideIndex = x.length}
  for (i = 0; i < x.length; i++) {
     x[i].style.display = "none";
  }
  x[slideIndex-1].style.display = "block";
}
//*************************

function init()
{
  obj.Draw();
}

obj =
{
  Bubble : function(file_data)
  {

    var details = new Array();
    titles = ['ID','Review Length','Avg Dish Price','Restaurant','Customer Rating'];
    details[0] = titles;

    //Filling data
    if(file_data)
    {
      for (i in file_data)
      {
        var i = 1;
        for(name in file_data)
        {
          var arr = file_data[name];
          details[i] = [name.split(" ")[0],arr[2],arr[1],name,parseInt(arr[0])];
          ++i;
        }
      }
    }

    var data = google.visualization.arrayToDataTable(details);

    var options = {
    title: 'Correlation between Average Price, Rating & Review length',
    width: 900,
    height: 670,
    hAxis: {title: 'Review Length'},
    vAxis: {title: 'Average Dish Price'},
    bubble: {textStyle: {fontSize: 8}}
    };

    var chart = new google.visualization.BubbleChart(document.getElementById(
    'bubble'));
    chart.draw(data, options);

    obj.Bar_Common(file_data);
  },

  Getrandomcolor : function()
  {
    var letters = '0123456789ABCDEF';
    var color = '#';
    for (var i = 0; i < 6; i++ ) {
        color += letters[Math.floor(Math.random() * 16)];
    }
    return color;
  },

  Bar_rating : function(file_data)
  {
    var details = new Array();
    titles = ["Restaurant", "Value", { role: 'style' }];
    details[0] = titles;

    for (i in file_data)
    {
      var i = 1;
      for(name in file_data)
      {
        var arr = file_data[name];
        details[i] = [name,parseInt(arr[0]),obj.Getrandomcolor()];
        ++i;
      }
    }
    return details;
  },

  Bar_price : function(file_data)
  {
    var details = new Array();
    titles = ["Restaurant", "Value", { role: 'style' }];
    details[0] = titles;

    for (i in file_data)
    {
      var i = 1;
      for(name in file_data)
      {
        var arr = file_data[name];
        details[i] = [name,parseInt(arr[1]),obj.Getrandomcolor()];
        ++i;
      }
    }
    return details;
  },

  Bar_revlength : function(file_data)
  {
    var details = new Array();
    titles = ["Restaurant", "Value", { role: 'style' }];
    details[0] = titles;

    for (i in file_data)
    {
      var i = 1;
      for(name in file_data)
      {
        var arr = file_data[name];
        details[i] = [name,parseInt(arr[2]),obj.Getrandomcolor()];
        ++i;
      }
    }
    return details;
  },

  Bar_Common : function(file_data)
  {

    details1 = obj.Bar_price(file_data);
    details2 = obj.Bar_revlength(file_data);
    details3 = obj.Bar_rating(file_data);

    var data1 = google.visualization.arrayToDataTable(details1);
    var data2 = google.visualization.arrayToDataTable(details2);
    var data3 = google.visualization.arrayToDataTable(details3);

    var options1 = {
        title: "Comparison Between Restaurants, Price Wise",
        width: 900,
        height: 670,
        hAxis: {title: 'Average Price'},
        bar: {groupWidth: "95%"},
        legend: { position: "none" },
      };

    var options2 = {
        title: "Comparison Between Restaurants, Review Length Wise",
        width: 900,
        height: 670,
        hAxis: {title: 'Average Review Length'},
        bar: {groupWidth: "95%"},
        legend: { position: "none" },
      };

    var options3 = {
        title: "Comparison Between Restaurants, Rating Wise",
        width: 900,
        height: 670,
        hAxis: {title: 'Average Rating'},
        bar: {groupWidth: "95%"},
        legend: { position: "none" },
      };

      var chart = new google.visualization.BarChart(document.getElementById(
        'bar1'));
      chart.draw(data1, options1);

      chart = new google.visualization.BarChart(document.getElementById(
        'bar2'));
      chart.draw(data2, options2);

      chart = new google.visualization.BarChart(document.getElementById(
        'bar3'));
      chart.draw(data3, options3);

    obj.Scatter(file_data);
  },

  Scatter : function(file_data)
  {
    var details = new Array();
    titles = ["Average Price", "Average Review Length"];
    details[0] = titles;

    for (i in file_data)
    {
      var i = 1;
      for(name in file_data)
      {
        var arr = file_data[name];
        details[i] = [arr[1],arr[2]];
        ++i;
      }
    }

    var data = google.visualization.arrayToDataTable(details);

    var options = {
      title: 'Price VS Review Length',
      hAxis: {title: 'Average Price'},
      width: 900,
      height: 670,
      vAxis: {title: 'Average Review Length'},
      legend: 'none'
    };

    var chart = new google.visualization.ScatterChart(document.getElementById(
      'scatter1'));
    chart.draw(data, options);

  },

  Openfile : function(name,callback)
  {
    //Open json file via Jquery, Asynchronous
    $.getJSON(name,function(json){
      callback(json);
    });
  },

  Draw : function()
  {
    //Opening and Updating data
    this.Openfile('restaurant_avg.json',this.Bubble);
  }
}