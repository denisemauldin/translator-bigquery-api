import sys
sys.path.append('../../')

from behave import given, when, then
from mock import patch

from app.api.bigquery.business_interactions import run_bglite_gt2g_query
from app.main import app


@when('a bglite run_bglite_gt2g_query with invalid request')
def invalid_run_bglite_gt2g_query(context):
  """
  The invalid request still needs to have valid structure because the
  endpoint validation prevents bad structure
  """
  invalid_request = {'ids': '5532'}
  with app.app_context():
    json_response = run_bglite_gt2g_query(invalid_request)
    context.json_response = json_response

@when('I run a valid run_bglite_gt2g_query')
def valid_run_bglite_gt2g_query(context):
  valid_request = {
    "tissue": "urinary_bladder",
    "limit": 100,
    "ids": "5111"
  }
  googleinterface = context.googleinterface
  print(googleinterface.query.return_value)
  with patch('app.api.bigquery.bigclam_interactions.GoogleInterface') as mock_googleinterface:
    mock_googleinterface().query.return_value = googleinterface.query.return_value
    with app.app_context():
      json_response = run_bglite_gt2g_query(valid_request)
      print("json_response in valid_run_bglite_gt2g_query", json_response)
      context.json_response = json_response

