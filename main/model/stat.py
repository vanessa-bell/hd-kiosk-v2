from google.appengine.ext import ndb
import model

class Stat(model.Base):
  faq_key = ndb.KeyProperty(kind=model.Faq, required=True)
  timestamp = ndb.DateTimeProperty(required=True, auto_now_add=True)