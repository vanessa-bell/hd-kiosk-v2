from google.appengine.ext import ndb
import model

class Faq(model.Base):
  user_key = ndb.KeyProperty(kind=model.User, required=True)
  question = ndb.StringProperty(required=True)
  answer = ndb.StringProperty(required=True)
  count = ndb.IntegerProperty(default=0)
  category = ndb.StringProperty(required=True)