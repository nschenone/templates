from pathlib import Path

Path('default.env').rename('.env')

REMOVE_PATHS = [
    '{% if not cookiecutter.pyservice %}src{% endif %}',
    '{% if not cookiecutter.pyservice %}.env{% endif %}',
    '{% if not cookiecutter.pyservice %}Dockerfile{% endif %}',
    '{% if not cookiecutter.pyservice %}pyproject.toml{% endif %}',
    '{% if not cookiecutter.pyservice %}requirements.txt{% endif %}',
]

# Loop through paths and remove them if they exist
for path_str in REMOVE_PATHS:
    path = Path(path_str)
    if path.exists():
        if path.is_file():
            path.unlink()  # Remove file
        elif path.is_dir():
            path.rmdir()  # Remove directory