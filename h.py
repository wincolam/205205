from flask import Flask

app = Flask (__name__)

@app.route("/")
def hello_world():
	return 'Hello 205CDE!'

if __name__ == '__main__':
	app.debug = True
	app.run(host="0.0.0.0", port=8000)



{% extends "bootstrap/base.html" %}
{% import "bootstrap/wtf.html" as wtf %}


{% block title %}
Log in
{% endblock %}


{% block styles %}
{{super()}}
<link rel="stylesheet" href="{{url_for('.static', fliename='login.css')}}">
{% endblock %}


{% block contect %}

     <div class="container">
     	
       <form class="form-signin" method="POST" action="/login" >
         <h2 class="form-sgnin-heading">Please sign in</h2>
         {{ form.hidden_tag() }}
         {{ wtf.form_field(form.username) }}
         {{ wtf.form_field(form.password) }}
         {{ wtf.form_field(form.remember) }}
         <button class="btn btn-lg btn-primary btn-block" type="submit">Sign in</button>
          
       </form>

     </div>

{% endblock %}
             
        	   
          



