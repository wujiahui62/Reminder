<head>
    <title>reminder-dashboard</title>
    <meta charset="utf-8"> 
    <link rel="stylesheet" href="./static/Monthly/css/monthly.css">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
    <script type="text/javascript" src="./static/Monthly/js/jquery.js"></script>
    <script type="text/javascript" src="./static/Monthly/js/monthly.js"></script>
    <script type="text/javascript">
    $(window).load( function() {
        $('#mycalendar').monthly({
            mode: 'event',
            dataType: 'json',
            jsonUrl: '/events'
        });
    });
    </script>   
</head>
<body>
<div class="monthly" id="mycalendar"></div>
</body>
