import timeit

import pytest


def test_import_v1_client_performance():
    import_time = timeit.timeit(
        stmt="import gotham.v1", setup="import sys; sys.modules.pop('gotham.v1', None);", number=1
    )

    assert import_time < 0.25


def test_client_v1_initialization_performance():
    init_time = timeit.timeit(
        stmt="gotham.v1.FoundryClient(gotham.UserTokenAuth(token='token'), hostname='localhost')",
        setup="import sys; sys.modules.pop('gotham.v1', None);import gotham; import gotham.v1",
        number=1,
    )

    assert init_time < 0.25


def test_federated_sources_v1_client_access_performance():
    init_and_access_time = timeit.timeit(
        stmt="gotham.v1.FoundryClient(gotham.UserTokenAuth(token='token'), hostname='localhost').federated_sources",
        setup="import sys; sys.modules.pop('gotham.v1', None);import gotham; import gotham.v1",
        number=1,
    )

    assert init_and_access_time < 0.5


def test_federated_sources_v1_models_import_performance():
    init_and_access_time = timeit.timeit(
        stmt="import gotham.v1.federated_sources.models",
        setup="import sys; sys.modules.pop('gotham.v1.federated_sources.models', None)",
        number=1,
    )

    assert init_and_access_time < 0.5


def test_gaia_v1_client_access_performance():
    init_and_access_time = timeit.timeit(
        stmt="gotham.v1.FoundryClient(gotham.UserTokenAuth(token='token'), hostname='localhost').gaia",
        setup="import sys; sys.modules.pop('gotham.v1', None);import gotham; import gotham.v1",
        number=1,
    )

    assert init_and_access_time < 0.5


def test_gaia_v1_models_import_performance():
    init_and_access_time = timeit.timeit(
        stmt="import gotham.v1.gaia.models",
        setup="import sys; sys.modules.pop('gotham.v1.gaia.models', None)",
        number=1,
    )

    assert init_and_access_time < 0.5


def test_geotime_v1_client_access_performance():
    init_and_access_time = timeit.timeit(
        stmt="gotham.v1.FoundryClient(gotham.UserTokenAuth(token='token'), hostname='localhost').geotime",
        setup="import sys; sys.modules.pop('gotham.v1', None);import gotham; import gotham.v1",
        number=1,
    )

    assert init_and_access_time < 0.5


def test_geotime_v1_models_import_performance():
    init_and_access_time = timeit.timeit(
        stmt="import gotham.v1.geotime.models",
        setup="import sys; sys.modules.pop('gotham.v1.geotime.models', None)",
        number=1,
    )

    assert init_and_access_time < 0.5


def test_inbox_v1_client_access_performance():
    init_and_access_time = timeit.timeit(
        stmt="gotham.v1.FoundryClient(gotham.UserTokenAuth(token='token'), hostname='localhost').inbox",
        setup="import sys; sys.modules.pop('gotham.v1', None);import gotham; import gotham.v1",
        number=1,
    )

    assert init_and_access_time < 0.5


def test_inbox_v1_models_import_performance():
    init_and_access_time = timeit.timeit(
        stmt="import gotham.v1.inbox.models",
        setup="import sys; sys.modules.pop('gotham.v1.inbox.models', None)",
        number=1,
    )

    assert init_and_access_time < 0.5


def test_map_rendering_v1_client_access_performance():
    init_and_access_time = timeit.timeit(
        stmt="gotham.v1.FoundryClient(gotham.UserTokenAuth(token='token'), hostname='localhost').map_rendering",
        setup="import sys; sys.modules.pop('gotham.v1', None);import gotham; import gotham.v1",
        number=1,
    )

    assert init_and_access_time < 0.5


def test_map_rendering_v1_models_import_performance():
    init_and_access_time = timeit.timeit(
        stmt="import gotham.v1.map_rendering.models",
        setup="import sys; sys.modules.pop('gotham.v1.map_rendering.models', None)",
        number=1,
    )

    assert init_and_access_time < 0.5


def test_media_v1_client_access_performance():
    init_and_access_time = timeit.timeit(
        stmt="gotham.v1.FoundryClient(gotham.UserTokenAuth(token='token'), hostname='localhost').media",
        setup="import sys; sys.modules.pop('gotham.v1', None);import gotham; import gotham.v1",
        number=1,
    )

    assert init_and_access_time < 0.5


def test_media_v1_models_import_performance():
    init_and_access_time = timeit.timeit(
        stmt="import gotham.v1.media.models",
        setup="import sys; sys.modules.pop('gotham.v1.media.models', None)",
        number=1,
    )

    assert init_and_access_time < 0.5


def test_target_workbench_v1_client_access_performance():
    init_and_access_time = timeit.timeit(
        stmt="gotham.v1.FoundryClient(gotham.UserTokenAuth(token='token'), hostname='localhost').target_workbench",
        setup="import sys; sys.modules.pop('gotham.v1', None);import gotham; import gotham.v1",
        number=1,
    )

    assert init_and_access_time < 0.5


def test_target_workbench_v1_models_import_performance():
    init_and_access_time = timeit.timeit(
        stmt="import gotham.v1.target_workbench.models",
        setup="import sys; sys.modules.pop('gotham.v1.target_workbench.models', None)",
        number=1,
    )

    assert init_and_access_time < 0.5
