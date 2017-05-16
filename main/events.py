import flask

from datetime import date, datetime, timedelta

import requests
import ssl
import config

import requests_toolbelt

if config.DEVELOPMENT:
  requests_toolbelt.adapters.__path__.append('./lib/requests_toolbelt/adapters')
else:
  requests_toolbelt.adapters.__path__.append('lib.zip/requests_toolbelt/adapters')

from requests_toolbelt.adapters import appengine

import json

from main import app

# Use the App Engine Requests adapter. This makes sure that Requests uses
# URLFetch.
appengine.monkeypatch()

@app.route('/events/')


def events():
	url = 'https://events.hackerdojo.com/events.json'
	response = requests.get(url=url)
	data = response.json()
	
	yesterday = datetime.strftime(date.today() - timedelta(1), "%A, %B %d, %Y")
	today = datetime.strftime(date.today(), "%A, %B %d, %Y")

	for event in data:
		event['start_time'] = datetime.strptime(event['start_time'], '%Y-%m-%dT%H:%M:%S')
		event['end_time'] = datetime.strptime(event['end_time'], '%Y-%m-%dT%H:%M:%S')
		event['day_raw'] = event['start_time'].strftime("%j")
		event['day'] = event['start_time'].strftime("%A, %B %d, %Y")
		event['start'] = event['start_time'].strftime("%I:%M %p")
		event['end'] = event['end_time'].strftime("%I:%M %p")

	return flask.render_template(
		'events.html',
		html_class='events',
		title='Upcoming Events',
		data=data,
		today=today,
		yesterday=yesterday,
	)