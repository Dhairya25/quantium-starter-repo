import app
import pytest
from dash import html


@pytest.fixture
def app_instance():
    return app.app


# Test the header presence
def test_header_present(dash_duo, app_instance):
    dash_duo.start_server(app_instance)
    assert dash_duo.find_element('h1').text == 'Sales Data Visualizer'
    dash_duo.stop_server()


# Test the visualization presence
def test_visualization_present(dash_duo, app_instance):
    dash_duo.start_server(app_instance)
    assert dash_duo.find_element('#sales-chart').is_displayed()
    dash_duo.stop_server()


# Test the region picker presence
def test_region_picker_present(dash_duo, app_instance):
    dash_duo.start_server(app_instance)
    assert dash_duo.find_element('#region-selector').is_displayed()
    dash_duo.stop_server()
