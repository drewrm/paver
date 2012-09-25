from unittest2 import TestCase
from os import chdir, getcwd, pardir, environ
from os.path import join, dirname, exists
from shutil import rmtree, copyfile
from subprocess import check_call
import sys
from tempfile import mkdtemp

class TestHgIntegrationSpecification(TestCase):

    def setUp(self):
        super(TestHgIntegrationSpecification, self).setUp()
        self.basedir = mkdtemp(prefix="test_paver_env")
        self.working_dir = mkdtemp(prefix="test_paver_hg")
        self.oldcwd = getcwd()

    def tearDown(self):
        chdir(self.oldcwd)
        rmtree(self.basedir)
        rmtree(self.working_dir)
        super(TestHgIntegrationSpecification, self).tearDown()

    def test_hg(self):
        pavement_py = """
from paver import hg, easy

WORKING_DIR = '%(working_dir)s'
REPO_URL = 'https://bitbucket.org/drewrm/jira-issue-assignee-history'

hg.clone(REPO_URL, WORKING_DIR)

branches = hg.branches(WORKING_DIR)
print branches
""" % dict(working_dir=self.working_dir)

        try:
            pavement_file = join(self.basedir, "pavement.py")
            f = open(pavement_file, "w")
            f.write(pavement_py)
            f.close
            check_call(["paver", "-f", pavement_file])
        finally:
            pass
