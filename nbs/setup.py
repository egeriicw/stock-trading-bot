import os
import sys
import pathlib

THIS_FILE_PATH = pathlib.Path(__file__).resolve()
NBS_DIR = THIS_FILE_PATH.parent
REPO_DIR = NBS_DIR.parent
DJANGO_BASE_DIR = REPO_DIR / "src" 



def init_django(project_name='cfehome'):
    os.chdir(DJANGO_BASE_DIR)
    sys.path.insert(0, str(DJANGO_BASE_DIR))
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', f"{project_name}.settings")
    os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"
    import django
    django.setup()

if __name__ == '__main__':
    init_django()
