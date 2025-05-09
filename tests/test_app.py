import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import sort


def test_standard_package():
    assert sort(10, 52, 3, 3.8) == "STANDARD"

def test_bulky_only():
    assert sort(160, 100, 100, 10) == "SPECIAL"

def test_heavy_only():
    assert sort(8, 96, 55, 25) == "SPECIAL"

def test_rejected_package():
    assert sort(160, 100, 100, 25) == "REJECTED"

def test_edge_case_volume_exactly_1_million():
    assert sort(100, 100, 100, 10) == "SPECIAL"

def test_edge_case_dimension_exactly_150():
    assert sort(150, 100, 100, 10) == "SPECIAL"

def test_edge_case_mass_exactly_20():
    assert sort(88, 10, 56, 20) == "SPECIAL"

def test_edge_case_both_limits():
    assert sort(150, 100, 100, 20) == "REJECTED"
