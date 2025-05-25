import allure


@allure.step('test_success')
def test_success():
    assert 1 == 1


@allure.step('test_failure')
def test_failure():
    assert 1 == 2
