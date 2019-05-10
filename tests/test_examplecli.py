from examplecli.examplecli import ExampleCli


def test_constructor():
    cli = ExampleCli()
    assert isinstance(cli, ExampleCli)
