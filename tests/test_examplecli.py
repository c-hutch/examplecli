from examplecli.examplecli import MyClass


def test_constructor():
    cli = MyClass()
    assert isinstance(cli, MyClass)
