import pytest

def test_index(client):
  response = client.get("/")
  assert b"Hello Flask App!" in response.data