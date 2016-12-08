google.charts.load('current', {'packages':['corechart']});
//google.charts.setOnLoadCallback(obj.Draw);



obj =
{
  data : new Object(),
  options : new Object(),
  chart : new Object(),

  Bubble : function(file_data)
  {

    var details = new Array();
    titles = ['ID','Customer Rating','Avg Dish Price','Restaurant','Review Length'];
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
          details[i] = [name,arr[0],arr[1],name,arr[2]];
          console.log(details[i])
          ++i;
        }
      }
    }

    /*
    this.data = google.visualization.arrayToDataTable(details);

    this.options = {
    title: 'Correlation between Average Price, Rating & Review length',
    hAxis: {title: 'Avg Dish Price'},
    vAxis: {title: 'Customer Rating'},
    bubble: {textStyle: {fontSize: 8}}
    };

    this.chart = new google.visualization.BubbleChart(document.getElementById(
                                                        'series_chart_div'));*/
  },

  Bar_rating : function()
  {

  },

  Bar_price : function()
  {

  },

  Bar_revlength : function()
  {

  },

  Line : function()
  {

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
    //this.chart.draw(this.data, this.options);
  }
}