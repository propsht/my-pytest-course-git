import pytest

from fibonacci.dynamic import fibonacci_dynamic_v2
from fibonacci.conftest import track_performance


@pytest.mark.performance
@track_performance
def test_performance():
    # sleep(3)
    fibonacci_dynamic_v2(100)
