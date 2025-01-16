import os

os.rename('default.env', '.env')

REMOVE_PATHS = [
    '{% if cookiecutter.pyservice %}src{% endif %}',
    '{% if cookiecutter.pyservice %}.env{% endif %}',
    '{% if cookiecutter.pyservice %}Dockerfile{% endif %}',
    '{% if cookiecutter.pyservice %}pyproject.toml{% endif %}',
    '{% if cookiecutter.pyservice %}requirements.txt{% endif %}',
]

for path in REMOVE_PATHS:
    path = path.strip()
    if path and os.path.exists(path):
        os.unlink(path) if os.path.isfile(path) else os.rmdir(path)