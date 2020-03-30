import pytest


@pytest.fixture()
def function_fixture(request):
    print({request.scope})

    def fin():
        print(f"\n Finalize from {request.scope} fixture!")

    request.addfinalizer(fin)


@pytest.fixture(scope="class")
def class_fixture(request):
    print({request.scope})

    def fin():
        print(f"\n Finalize from {request.scope} fixture!")

    request.addfinalizer(fin)


@pytest.fixture(scope="module")
def module_fixture(request):
    print({request.scope})

    def fin():
        print(f"\n Finalize from {request.scope} fixture!")

    request.addfinalizer(fin)


@pytest.fixture(scope="session")
def session_fixture(request):
    print({request.scope})

    def fin():
        print(f"\n Finalize from {request.scope} fixture!")

    request.addfinalizer(fin)



