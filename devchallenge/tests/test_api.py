from devchallenge.api import Prescription


def test_get_prescription_doc():
    resource = Prescription()
    doc = resource.get(1)

    assert doc is not None
