<head>
<title>reminder List</title>
<meta charset="utf-8"> 
<meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Reminders</title>
  <link rel="stylesheet" href="//code.jquery.com/ui/1.12.1/themes/base/jquery-ui.css">
  <link rel="stylesheet" href="/resources/demos/style.css">
  <script src="https://code.jquery.com/jquery-1.12.4.js"></script>
  <script src="https://code.jquery.com/ui/1.12.1/jquery-ui.js"></script>
  <script>
  $( function() {
    $( "#datepicker" ).datepicker();
  } );
  </script>
</head>

<link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
<body>
<div class="w3-margin">
  <table>
    <tr>
      <th>
        <a href="/">
        <div width=400 class="w3-card-4 w3-padding" style="min-width: 400px">reminder List</div>
        </a>
      </th>
      <form action="/search-results" method="post">
      <th>
        <div class="w3-card-4 w3-padding">
          <input autofocus type="text" name="key" placeholder="Search" style="min-width: 400px">
        </div>
      </th>
      <th>
        <div class="w3-padding w3-center">
          <input type="image" src="/static/save-task.png"/>
        </div>
      </th>
    </form>

    </tr>
      <form action="/new-reminder" method="post">
    <tr>
      <td>
        <div class="w3-card-4 w3-padding">
          <input autofocus type="text" name="event" placeholder="New event..." style="min-width: 400px">
        </div>
      </td>
      <td>
        <div class="w3-card-4 w3-padding">
          <input autofocus type="text" name="date" placeholder="New date..." id="datepicker" style="min-width: 400px">
        </div>
      </td>
      <td>
        <div class="w3-padding w3-center">
          <input type="image" src="/static/save-task.png"/>
        </div>
      </td>
      </tr>
    %for reminder in reminders:
      <tr>
        <td>
          <div class="w3-card-4 w3-padding">{{reminder['event']}}</div>
        </td>
        <td>
          <div class="w3-card-4 w3-padding">{{reminder['date']}}</div>
        </td>
        <td>
          <div class="w3-padding w3-center">
            <a href="/discard-reminder/{{reminder['_id']}}">
              <img src="/static/discard-task.png">
            </a>
          </div>
        </td>
        <td>
          <div class="w3-padding w3-center">
            <a href="/edit-reminder/{{reminder['_id']}}">
              <img src="/static/pencil-2x.png"">
            </a>
          </div>
        </td>
      </tr>
    %end
    </form>
  </table>
</body>