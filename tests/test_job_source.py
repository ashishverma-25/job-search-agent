from app.sources.mock_linkedin import MockLinkedInSource


def test_mock_linkedin_source():

    source = MockLinkedInSource()

    jobs = source.search(
        "https://www.linkedin.com/jobs/search/?keywords=Python"
    )

    assert len(jobs) == 2

    assert jobs[0].title == "Senior Python Backend Developer"
    assert jobs[0].company == "ABC Technologies"
    assert jobs[0].source == "linkedin"

    assert jobs[1].location == "Noida"

    print(jobs)