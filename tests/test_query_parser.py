from app.services.query_parser import JobQueryParser


def test_query_parser():

    parser = JobQueryParser()

    query = """
    Find senior Python backend jobs in Bengaluru and Noida,
    posted in the last 24 hours, requiring 4 to 7 years of experience.
    """

    result = parser.parse(query)

    print(result.model_dump(mode="json"))

    assert "Bengaluru" in result.locations
    assert "Noida" in result.locations
    assert result.post_time.value == "24h"
    assert result.experience_min == 4
    assert result.experience_max == 7