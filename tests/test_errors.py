import warnings

import pytest

from gotham import PalantirRPCException
from gotham._errors.utils import deserialize_error
from gotham.v1.gotham.errors import InvalidSidc
from gotham.v1.gotham.errors import InvalidTrackRid

ERRORS_MAP = {
    "InvalidSidc": InvalidSidc,
    "InvalidTrackRid": InvalidTrackRid,
}


def test_correctly_deserializes_error():
    error = deserialize_error(
        {
            "errorName": "InvalidTrackRid",
            "errorInstanceId": "123",
            "parameters": {"trackRid": "ri.a.b.c.d"},
        },
        ERRORS_MAP,
    )

    assert isinstance(error, PalantirRPCException)
    assert isinstance(error, InvalidTrackRid)
    assert error.name == "InvalidTrackRid"
    assert error.error_instance_id == "123"
    assert error.parameters == {"trackRid": "ri.a.b.c.d"}


def test_falls_back_to_standard_if_parsing_fails():
    with warnings.catch_warnings(record=True) as w:
        error = deserialize_error(
            {
                "errorName": "InvalidTrackRid",
                "errorInstanceId": "123",
                "parameters": {"trackRid": "ri.a.b.c.d"},
            },
            ERRORS_MAP,
        )

        assert len(w) == 1
        assert error is None
