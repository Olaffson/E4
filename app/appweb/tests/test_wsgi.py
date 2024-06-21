def test_wsgi_application():
    from appweb.wsgi import application
    assert application is not None
