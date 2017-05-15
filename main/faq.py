import flask
import flask_wtf
import wtforms

import auth
import model
import util

from main import app

class FaqUpdateForm(flask_wtf.FlaskForm):
  question = wtforms.TextAreaField('Question', [wtforms.validators.required()])
  answer = wtforms.TextAreaField('Answer', [wtforms.validators.required()])
  category = wtforms.SelectField('Category', [wtforms.validators.required()], choices=[('About/History','About/History'),('Financials','Financials'),('The Physical Space','The Physical Space'),('Other Hackerspaces','Other Hackerspaces'),('Paperwork and Logistics','Paperwork and Logistics'),('Miscellaneous','Miscellaneous')])

@app.route('/faqs/create/', methods=['GET', 'POST'])
@auth.login_required
def faq_create():
	form = FaqUpdateForm()
	if form.validate_on_submit():
		faq_db = model.Faq(
			user_key=auth.current_user_key(),
			question=form.question.data,
			answer=form.answer.data,
			category=form.category.data,
		)
		faq_db.put()
		return flask.redirect(flask.url_for('welcome'))
	return flask.render_template(
		'faq_create.html',
		html_class='faq-create',
		title='Create FAQ',
		form=form,
	)

@app.route('/faqs/')
# @auth.login_required
def faqs_list():
  faq_dbs, faq_cursor = model.Faq.get_dbs(
      user_key=auth.current_user_key(),
    )

  return flask.render_template(
      'faqs_list.html',
      html_class='faqs-list',
      title='Frequently Asked Questions',
      faq_dbs=faq_dbs,
      next_url=util.generate_next_url(faq_cursor),
    )

@app.route('/faqs/<int:faq_id>/update/', methods=['GET', 'POST'])
@auth.login_required
def faq_update(faq_id):
  faq_db = model.Faq.get_by_id(faq_id)
  if not faq_db or faq_db.user_key != auth.current_user_key():
    flask.abort(404)
  form = FaqUpdateForm(obj=faq_db)
  if form.validate_on_submit():
    form.populate_obj(faq_db)
    faq_db.put()
    return flask.redirect(flask.url_for('faqs_list', order='-modified'))
  return flask.render_template(
      'faq_update.html',
      html_class='faq-update',
      title=faq_db.name,
      form=form,
      faq_db=faq_db,
    )