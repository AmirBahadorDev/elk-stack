from src.elk import check_elastic_connection
import pytest

@pytest.mark.parametrize("elatic_host, ecpected_output",
                         [
                             ("junk_url", False)
                         ]
                         )
def test_check_elastic_connection_with_offline_elasicsearch(elatic_host, ecpected_output):
    assert check_elastic_connection(elatic_host) == ecpected_output
