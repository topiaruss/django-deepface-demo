"""
Test suite that runs django_deepface's own test suite
"""
import pytest
from django_deepface.tests.test_views import *  # noqa

# This file imports all tests from django_deepface's test suite
# The tests will run with our project's settings and configuration 