import pylever
import requests

TEST_SITE = 'coursera'


def test_can_create_lever_object():
    lever_object = pylever.Lever(TEST_SITE)
    assert type(lever_object) == pylever.Lever


def test_can_create_session():
    lever_object = pylever.Lever(TEST_SITE)
    assert type(lever_object.session) == requests.Session


def test_create_endpoint():
    lever_object = pylever.Lever(TEST_SITE)
    assert lever_object._endpoint('/test?endpoint') == 'https://api.lever.co/test?endpoint'


def test_list_postings():
    lever_object = pylever.Lever(TEST_SITE)
    assert len(lever_object.list_postings())
