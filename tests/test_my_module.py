from app.my_module import MyWork


def test_constructor():
    cli = MyWork()
    assert isinstance(cli, MyWork)
