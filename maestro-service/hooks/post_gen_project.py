from pathlib import Path
import shutil

Path('default.env').rename('.env')

REMOVE_PATHS = [
    '{% if not cookiecutter.pyservice %}src{% endif %}',
    '{% if not cookiecutter.pyservice %}.env{% endif %}',
    '{% if not cookiecutter.pyservice %}Dockerfile{% endif %}',
    '{% if not cookiecutter.pyservice %}pyproject.toml{% endif %}',
    '{% if not cookiecutter.pyservice %}requirements.txt{% endif %}',
]

for path_str in REMOVE_PATHS:
    if path_str:
        path = Path(path_str.strip())
        if path.exists():
            if path.is_file():
                path.unlink()
            elif path.is_dir():
                shutil.rmtree(path)