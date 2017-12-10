<html>
    <head>
        <title>Russians Flask Home</title>
        <meta charset="utf-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/css/bootstrap.min.css" integrity="sha512-dTfge/zgoMYpP7QbHy4gWMEGsbsdZeCXz7irItjcC3sPUFtf0kuFbDz/ixG7ArTxmDjLXDmezHubeNikyKGVyQ==" crossorigin="anonymous">
    </head>

    <body>

        <nav class="navbar navbar-inverse">
          <div class="container">
            <div class="navbar-header">
              <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#navbar" aria-expanded="false" aria-controls="navbar">
                <span class="sr-only">Toggle navigation</span>
                <span class="icon-bar"></span>
                <span class="icon-bar"></span>
                <span class="icon-bar"></span>
              </button>
              <a class="navbar-brand" href="#">Oceans Scratchpad</a>
            </div>
            <ul class="nav navbar-nav navbar-right">
                {% if current_user.is_authenticated %}
                    <li><a href="{{ url_for('logout') }}">Log out</a></li>
                {% else %}
                    <li><a href="{{ url_for('login') }}">Log in</a></li>
                {% endif %}
            </ul>
          </div>
        </nav>

        <br><br><br>
        <div class="container">
            <div class="row">
                <div class="col-md-12">
                    Add your comments below.
                </div>

                <div class="col-md-12">
                    This is the the second dummy comment.
                </div>

                <div class="col-md-12">
                    Your posted comments:
                </div>
            </div>
        </div>

        <br><br>

       <div class="container">
            {% for comment in comments %}
                <div class="row">
                    {{ comment.content }}
                </div>
                <div>
                    <small>
                        Posted
                        {% if comment.posted %}
                            {{ comment.posted.strftime("%A, %d %B %Y at %H:%M") }}
                        {% else %}
                            at an unknown time
                        {% endif %}
                        {% if comment.commenter %}
                            {{ comment.commenter.username }}
                        {% else %}
                            anonymous
                        {% endif %}
                    </small>
                </div>
            {% endfor %}
            <br><br>
            {% if current_user.is_authenticated %}
            <div class="row">
                <form action="." method="POST">
                    <textarea class="form-control" name="contents" placeholder="Enter a comment"></textarea>
                    <br><br>
                    <input type="submit" class="btn btn-primary" value="Post comment">
                </form>
            </div>
            {% endif %}
        </div>

    </body>
</html>