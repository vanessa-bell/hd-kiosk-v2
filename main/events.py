import flask

import model
import util

from main import app

@app.route('/events/')

def events():

  return flask.render_template(
      'events.html',
      html_class='events',
      title='Upcoming Events',
    )