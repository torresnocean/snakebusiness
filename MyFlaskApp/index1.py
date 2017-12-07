{% extends 'layout.html' %}

{% block body %}

    <div class="jumbotron text-center">
        <h1><u>Welcome to Umber's FlaskApp</u></h1><br /><br />

        <div class="container text-left">
        {% for comment in comments %}
                <div class="row">
                    {{ comment.content }}
                </div>
            {% endfor %}

<!--The comment input field form-->
        {% if current_user.is_authenticated %}
            <div class="row">
                <form action="." method="POST">
                    <textarea class="form-control" name="contents" placeholder="Enter a comment"></textarea>
                    <input type="submit" class="btn btn-success" value="Post comment">
                </form>
            </div>
        {% endif %}
<!--The comment input field form-->

        </div>
    </div>

{% endblock %}

<!--End of file-->

<!--<p class="lead">My application is built on the Python Flask framework, Enjoy!..</p>-->
<!--<p>Don't be rude, be polite, and have fun.</p><br/><br/>-->