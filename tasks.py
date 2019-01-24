from pathlib import Path
import shutil

from docutils.core import publish_cmdline
from invoke import task
from rellu.tasks import clean


assert Path.cwd() == Path(__file__).parent

@task
def project_docs(ctx):
    """Generate project documentation.

    These docs are visible at http://robotframework.org/WebDemo/.
    """
    args = ['--stylesheet=style.css,extra.css',
            '--link-stylesheet',
            'README.rst',
            'docs/index.html']
    publish_cmdline(writer_name='html5', argv=args)
    print(Path(args[-1]).absolute())

@task
def move_docs(ctx):
    """Move report.html and log.html to docs

    These docs are visible http://robotframework.org/WebDemo/.
    """
    log = Path('./log.html')
    report = Path('./report.html')
    dest = Path('.') / 'docs'
    print(log.absolute())
    shutil.copy(log.absolute(), str(dest))
    print(report.absolute())
    shutil.copy(report.absolute(), str(dest))
