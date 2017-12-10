<html>
    <head>
        <meta charset="utf-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1">

        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/css/bootstrap.min.css" integrity="sha512-dTfge/zgoMYpP7QbHy4gWMEGsbsdZeCXz7irItjcC3sPUFtf0kuFbDz/ixG7ArTxmDjLXDmezHubeNikyKGVyQ==" crossorigin="anonymous">

        <title>Russians Flask: log in</title>
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
                    <a class="navbar-brand" href="/">Russians Flask: back to home page</a>
                </div>
            </div>
        </nav>

        <div class="container">
            <div class="row">
                <div class="col-md-12">
                    {% if error %}
                        <div class="alert alert-danger" role="alert">
                            Incorrect username or password
                        </div>
                    {% endif %}
                </div>
            </div>
        </div>

        <div class="container">
            <div class="row">
                <div class="col-md-8">
                   <div class="container">
                       <div class="row">
                           <div class="col-sm-3">
                            <img src="../static/images/FLASK4741.jpg" height="500" width="500">
                           </div>

                           <div class="col-sm-3">

                           </div>

                           <div class="col-sm-3">

                           </div>
                       </div>
                   </div>
                </div>

                <div class="col-md-4">
                     <form action="." method="POST">
                      <div class="form-group">
                        <label for="username">Username:</label>
                        <input class="form-control" id="username" name="username" placeholder="Enter your username">
                      </div>
                      <div class="form-group">
                        <label for="password">Password:</label>
                        <input type="password" class="form-control" id="password" name="password" placeholder="Enter your password">
                      </div>
                      <button type="submit" class="btn btn-success">Log in</button>
                    </form>
                </div>
            </div>
        </div>

    </body>
</html>