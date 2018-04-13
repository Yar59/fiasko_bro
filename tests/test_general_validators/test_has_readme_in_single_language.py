from fiasko_bro import defaults
from fiasko_bro import validators


def test_has_readme_in_single_language_succeeds(test_repo):
    readme_filename = 'readme_in_single_language.md'
    min_percent = defaults.VALIDATION_PARAMETERS[
        'min_percent_of_another_language'
    ]
    output = validators.has_readme_in_single_language(
        project_folder=test_repo,
        readme_filename=readme_filename,
        min_percent_of_another_language=min_percent,
    )
    assert output is None


def test_has_readme_in_single_language_fails(test_repo):
    readme_filename = 'bilingual_readme.md'
    expected_output = 'bilingual_readme', ''
    min_percent = defaults.VALIDATION_PARAMETERS[
        'min_percent_of_another_language'
    ]
    output = validators.has_readme_in_single_language(
        project_folder=test_repo,
        readme_filename=readme_filename,
        min_percent_of_another_language=min_percent,
    )
    assert output == expected_output
