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
  scatter_rating : function(file_data)
  {
    if(file_data)
    {
      //arraydata is a list of lists
      var arraydata = new Array();
      arraydata.push(['Price','Rating']);
      for(i in file_data)
      {
        arraydata.push([i,file_data[i]]);
      }
      //console.log(arraydata);
      var data = google.visualization.arrayToDataTable(arraydata);
      var options = {
        title: 'Price vs. Rating',
        width: 900,
      	height: 670,
        hAxis: {title: 'Price'},
        vAxis: {title: 'Rating'},
        legend: 'none'
      };
      var chart = new google.visualization.ScatterChart(document.getElementById('scatter2'));
      chart.draw(data, options);
    }
  },
  scatter_popl : function(file_data)
  {
    if(file_data)
    {
      //arraydata is a list of lists
      var arraydata = new Array();
      arraydata.push(['Price','Popularity']);
      for(i in file_data)
      {
        arraydata.push([i,file_data[i]]);
      }
      //console.log(arraydata);
      var data = google.visualization.arrayToDataTable(arraydata);
      var options = {
        title: 'Price vs. Popularity',
        width: 900,
      	height: 670,
        hAxis: {title: 'Price'},
        vAxis: {title: 'Popularity'},
        legend: 'none'
      };
      var chart = new google.visualization.ScatterChart(document.getElementById('scatter3'));
      chart.draw(data, options);
    }
  },
  donut: function(file_data)
  {
    if(file_data)
    {
      var arraydata = new Array();
      arraydata.push(['Rating','Number of Reviews']);
      for(i in file_data)
      {
        //console.log(i);
        arraydata.push([i,file_data[i]]);
      }
      var data = google.visualization.arrayToDataTable(arraydata);
      var options = {
          title: 'Rating vs Number of Reviews',
          width: 900,
          height: 670,
          pieHole: 0.4,
        };
      var chart = new google.visualization.PieChart(document.getElementById('donut'));
      chart.draw(data, options);
    }
  },
  bar_avgrating : function(file_data)
  {
    //rating vs avg review length
    if(file_data)
    {
      var arraydata = new Array();
      arraydata.push(['Rating', 'Average Length']);
      var sorted = [];
      for(var key in file_data) {
          sorted[sorted.length] = key;
      }
      sorted.sort();
      //console.log(sorted);
      for(var i=0; i<sorted.length; i++)
      {
          var key = sorted[i];
          //console.log(typeof(parseInt(sorted[i],10)));
          arraydata.push([key,file_data[key]]);
      }
      var data = google.visualization.arrayToDataTable(arraydata);
      var options = {
        title: "Rating vs Average Length of corresponding Review",
        hAxis: {title: 'Average Review Length'},
        yAxis: {title: 'Rating'},
        width: 900,
        height: 670,
        bar: {groupWidth: "95%"},
        legend: { position: "none" },
      };
      var chart = new google.visualization.BarChart(document.getElementById('bar4'));
      chart.draw(data, options);
    }
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
    this.Openfile('../data/visualizations/restaurant_avg.json',this.Bubble);
    this.Openfile('../data/visualizations/price_vs_rating.json',this.scatter_rating);
    this.Openfile('../data/visualizations/price_vs_popl.json',this.scatter_popl);
    this.Openfile('../data/visualizations/rating_vs_numrev.json',this.donut);
    this.Openfile('../data/visualizations/rating_vs_avgrevlen.json', this.bar_avgrating);
  }
}
