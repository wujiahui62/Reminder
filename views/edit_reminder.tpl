<head>
<title>Story List</title>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Reminders-edit</title>
  <link rel="stylesheet" href="//code.jquery.com/ui/1.12.1/themes/base/jquery-ui.css">
  <link rel="stylesheet" href="/resources/demos/style.css">
  <script src="https://code.jquery.com/jquery-1.12.4.js"></script>
  <script src="https://code.jquery.com/ui/1.12.1/jquery-ui.js"></script>
  <script>
  $( function() {
    $( "#datepicker" ).datepicker({
      onSelect: function() {
        return $(this).datepicker('getDate');
      }
    });
  } );
  </script>

</head>
<link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
<body>
<div class="w3-margin">
  <table id="mytable">
  <tbody>
    <tr>
      <form action="/edit-reminder/{{reminder['_id']}}" method="post">
      <td>
        <div class="w3-card-4 w3-padding">
          Event: <input type="text" name="event" placeholder="{{reminder['event']}}" style="min-width: 400px">
        </div>
      </td>
      <td>
      <div class="w3-card-4 w3-padding">Date: <input type="text" id="datepicker" name="date"></div>
      </td>
      <td>
        <div class="w3-padding w3-center">
          <input type="image" src="/static/save-task.png"/>
        </div>
      </td>
      </form>
    </tr>
  </tbody>
  </table>
</body>
