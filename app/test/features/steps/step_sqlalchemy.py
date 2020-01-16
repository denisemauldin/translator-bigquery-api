import sys
sys.path.append('../../')

from behave import *

import sqlalchemy
from sqlalchemy import orm
from app.database.factories import *
from app.main import app, db
from app.database.models import Study, Substudy, SubstudyTissue

@given('a configured sqlalchemy engine')
def step_configure_sqlalchemy(context):
    engine = sqlalchemy.create_engine('sqlite://')
    # It's a scoped_session, and now is the time to configure it.
    Session = orm.scoped_session(orm.sessionmaker())
    Session.configure(bind=engine)
    context.sqlalchemy_configured = True
    context.Session = Session
    context.session = Session()
    with app.app_context():
      # TODO: FIX why this isn't creating the tables in the database
      db.create_all()
      print("TABLENAMES:", engine.table_names())

@given('a Study Factory')
def setp_study_factory(context):
  context.study = StudyFactory(context.session).create()

@given('a Substudy Factory')
def step_substudy_factory(context):
  context.substudy = SubstudyFactory(context.session).create()

@given('a SubstudyTissue Factory')
def step_substudytissue_factory(context):
  context.stubstudytissue = SubstudyTissueFactory(context.session).create()

@then('reset sqlalchemy database')
def reset_sqlalchemy(context):
  session = context.session
  session.rollback()
  Session = context.Session
  Session.remove()