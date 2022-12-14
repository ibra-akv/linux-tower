from helpers.programs import Apache
import pytest


def test_is_installed():
    """
    GIVEN a 'Apache' class that groups together methods relevant to the Apache systemd service
    WHEN 'is_installed' method is called
    THEN check that the returned value is true
    """

    is_installed = Apache.is_installed()
    assert is_installed is True


def test_status():
    """
    GIVEN a 'Apache' class that groups together methods relevant to the Apache systemd service
    WHEN 'status' method is called
    THEN check that the returned value contains text saying apache2 is running
    """

    status = Apache.status()
    assert type(status) is str
    assert 'active (running) since' in status


def test_service_show():
    """
    GIVEN a 'Apache' class that groups together methods relevant to the Apache systemd service
    WHEN 'service_show' method is called
    THEN check that the returned value is dict and contains relevant information
    """

    service_data = Apache.service_show()
    assert type(service_data) is dict
    assert 'SubState' in service_data
    assert service_data['SubState'] == 'running'


def test_state_details():
    """
    GIVEN a 'Apache' class that groups together methods relevant to the Apache systemd service
    WHEN 'state_details' method is called
    THEN check that the returned value is dict and contains formatted data
    """

    state_details = Apache.state_details()
    assert type(state_details) is dict
    assert 'id' in state_details
    assert 'description' in state_details
    assert state_details['state'] == 'running'
    assert 'started_at' in state_details


def test_metrics_expect_exception():
    """
    GIVEN a 'Apache' class that groups together methods relevant to the Apache systemd service
    WHEN 'metrics' method is called
    THEN expect exception
    """

    with pytest.raises(Exception) as e:
        Apache.metrics()
