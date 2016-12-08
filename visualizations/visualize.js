google.charts.load('current', {'packages':['corechart']});
google.charts.setOnLoadCallback(init);

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
    width: 1000,
    height: 1000,
    hAxis: {title: 'Review Length'},
    vAxis: {title: 'Average Dish Price'},
    bubble: {textStyle: {fontSize: 8}}
    };

    var chart = new google.visualization.BubbleChart(document.getElementById(
    'series_chart_div'));
    chart.draw(data, options);
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

    details = obj.Bar_price(file_data);

    var data = google.visualization.arrayToDataTable(details);
    var options = {
        title: "Comparison Between Restaurants",
        width: 1000,
        height: 1000,
        hAxis: {title: 'Average Value'},
        bar: {groupWidth: "95%"},
        legend: { position: "none" },
      };
      var chart = new google.visualization.BarChart(document.getElementById(
        'series_chart_div'));
      chart.draw(data, options);
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
      vAxis: {title: 'Average Review Length'},
      legend: 'none'
    };

    var chart = new google.visualization.ScatterChart(document.getElementById(
      'series_chart_div'));
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
    //this.Openfile('restaurant_avg.json',this.Bubble);
  }
}