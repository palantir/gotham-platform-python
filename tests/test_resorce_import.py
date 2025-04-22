def test_federated_sources_v1_federated_source_import():
    from gotham.v1.federated_sources.federated_source import FederatedSourceClient

    assert FederatedSourceClient is not None


def test_gaia_v1_map_import():
    from gotham.v1.gaia.map import MapClient

    assert MapClient is not None


def test_geotime_v1_geotime_import():
    from gotham.v1.geotime.geotime import GeotimeClient

    assert GeotimeClient is not None


def test_inbox_v1_messages_import():
    from gotham.v1.inbox.messages import MessagesClient

    assert MessagesClient is not None


def test_map_rendering_v1_map_rendering_import():
    from gotham.v1.map_rendering.map_rendering import MapRenderingClient

    assert MapRenderingClient is not None


def test_media_v1_media_import():
    from gotham.v1.media.media import MediaClient

    assert MediaClient is not None


def test_target_workbench_v1_high_priority_target_lists_import():
    from gotham.v1.target_workbench.high_priority_target_lists import (
        HighPriorityTargetListsClient,
    )  # NOQA

    assert HighPriorityTargetListsClient is not None


def test_target_workbench_v1_target_boards_import():
    from gotham.v1.target_workbench.target_boards import TargetBoardsClient

    assert TargetBoardsClient is not None


def test_target_workbench_v1_targets_import():
    from gotham.v1.target_workbench.targets import TargetsClient

    assert TargetsClient is not None
