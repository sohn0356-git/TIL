# HTML



## 3일차



### AJAX

* 새로운 언어가 아닌 JavaScript에 추가된 통신 방식
* 화면 전체를 재로드하지 않고도 서버에서 특정 데이터를 송수신 할 수 있다.

　

#### JavaScript를 이용한 AJAX

1. XMLHttpRequest 객체 생성

```javascript
var xmlhttp;
if (window.XMLHttpRequest) {
 xmlhttp=new XMLHttpRequest(); // IE7+, Firefox, Chrome, Opera, Safari
}else{
 xmlhttp=new ActiveXObject("Microsoft.XMLHTTP"); // IE6, IE5
}
```

　

2. 서버에서 결과를 받을 준비

```javascript
xmlhttp.onreadystatechange=function(){
 if (xmlhttp.readyState==4 && xmlhttp.status==200){
 document.getElementById("myDiv").innerHTML=xmlhttp.responseText;
 }
}
```

　

3. 서버에 요청

```javascript
xmlhttp.open("GET",“serverApp.jsp",true);
xmlhttp.send();

xmlhttp.open("POST"," serverApp.jsp",true);
xmlhttp.setRequestHeader("Content-type","application/x-www-formurlencoded");
xmlhttp.send("fname=Henry&lname=Ford");
```


　

* 기타 example

```html
{% extends 'base.html' %}

{% block header %}
<script src="https://code.highcharts.com/highcharts.js"></script>
<script src="https://code.highcharts.com/modules/series-label.js"></script>
<script src="https://code.highcharts.com/modules/exporting.js"></script>
<script src="https://code.highcharts.com/modules/export-data.js"></script>
<script src="https://code.highcharts.com/modules/accessibility.js"></script>
<style>
    div{
        widows: 300px;
        border:2px solid red;
    }
    #container{
        width: 500px;
        height: 400px;
        border:1px solid darkcyan;
    }
</style>
<script>
    function graph(data){
        Highcharts.chart('container', {
        title: {
            text: 'Solar Employment Growth by Sector, 2010-2016'
        },

        subtitle: {
            text: 'Source: thesolarfoundation.com'
        },

        yAxis: {
            title: {
                text: 'Number of Employees'
            }
        },

        xAxis: {
            accessibility: {
                rangeDescription: 'Range: 2010 to 2017'
            }
        },

        legend: {
            layout: 'vertical',
            align: 'right',
            verticalAlign: 'middle'
        },

        plotOptions: {
            series: {
                label: {
                    connectorAllowed: false
                },
                pointStart: 2010
            }
        },

        series: data,

        responsive: {
            rules: [{
                condition: {
                    maxWidth: 500
                },
                chartOptions: {
                    legend: {
                        layout: 'horizontal',
                        align: 'center',
                        verticalAlign: 'bottom'
                    }
                }
            }]
        }

        });
    };
    function getData(pk){
 
        $.ajax({
            url:'{% url "blog:graph" %}',
            data:{'pk':pk},
            success:function(data){
                console.log(data);
                graph(data.datas);
            }
        })
       
    };
    
    $(document).ready(function(){
        $('input[name="id"]').keyup(function(){
            id = $(this).val();
            console.log(id);
            $.ajax({
                url:"{% url 'blog:getid' %}",
                data:{'id':id},
                type:'GET',
                success:function(data){
                    if(data.trim() == '1'){
                        $('span').html('<h2 style="color:green;">ok</h2>');
                    }else{
                        $('span').html('<h2 style="color:red;">no</h2>');
                    }
                }
            });
        });
        $('button[name="b1"]').click(function(){
            getData(1);
        });
        $('button[name="b2"]').click(function(){
            getData(2);
        });
    });
</script>
{% endblock %}

{% block content %}
<form>
    ID<input type="text" name="id"><span></span><br/><br/>
    PWD<input type="text" name="pwd"><br/>
    
    
</form>
<button name="b1">Graph1</button>
<button name="b2">Graph2</button>
<div id="container">

</div>
{% endblock %}
```

