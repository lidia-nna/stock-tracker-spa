from api import create_app 
from api.config import TestConfig
from api.models import Tickers
from api.today.logic import Summary
from api.db import db 
from api.mail import mail
import json
import pytest

import os



@pytest.fixture()
def app():
    _app = create_app(cfg=TestConfig)
    _app.testing = True
    db.init_app(_app)
    mail.init_app(_app)
    yield _app

@pytest.fixture()
def client(app):
    client = app.test_client()
    ctx = app.app_context()
    ctx.push()
    yield client
    ctx.pop()

@pytest.fixture()
def init_databse(client):
    db.create_all()
    yield db
    db.drop_all()


@pytest.fixture()
def summary(client, init_databse):
    return Summary()

# @pytest.fixture(scope = "session")
# def candle_chart(init_databse):
#     return CandleChart()

