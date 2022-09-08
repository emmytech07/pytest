"""
Fixture scopes
Fixtures are created when first requested by a test, and are destroyed based on their scope:
• function: the default scope, the fixture is destroyed at the end of the test.
• class: the fixture is destroyed during teardown of the last test in the class.
• module: the fixture is destroyed during teardown of the last test in the module.
• package: the fixture is destroyed during teardown of the last test in the package.
• session: the fixture is destroyed at the end of the test session
"""
import pytest
def determine_scope(fixture_name, config):
    if config.getoption("--keep-containers", None):
        return "sesssion"
    return "function"

@pytest.fixture(scope=determine_scope)
def docker_container():
    yield spawn_container()