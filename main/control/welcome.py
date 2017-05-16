# coding: utf-8

import flask

import config

from main import app


###############################################################################
# Welcome
###############################################################################
@app.route('/')
def welcome():
  return flask.redirect('/faqs/')

@app.route('/building_map/')
def building_map():
	return flask.render_template(
		'building-map.html',
		html_class='building-map',
		title='Building Map',
	)

@app.route('/about_us/')
def about_us():
	return flask.render_template(
		'about-us.html',
		html_class='about-us',
		title='About Us',
	)

@app.route('/membership/')
def membership():
	return flask.render_template(
		'membership.html',
		html_class='membership',
		title='Membership',
	)



###############################################################################
# Sitemap stuff
###############################################################################
@app.route('/sitemap.xml')
def sitemap():
  response = flask.make_response(flask.render_template(
    'sitemap.xml',
    lastmod=config.CURRENT_VERSION_DATE.strftime('%Y-%m-%d'),
  ))
  response.headers['Content-Type'] = 'application/xml'
  return response


###############################################################################
# Warmup request
###############################################################################
@app.route('/_ah/warmup')
def warmup():
  # TODO: put your warmup code here
  return 'success'
