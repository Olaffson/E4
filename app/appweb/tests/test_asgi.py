def test_asgi_application():
    from appweb.asgi import application
    assert application is not None
