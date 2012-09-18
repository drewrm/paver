from paver import hg, easy
from paver.tests.mock import Mock, patch

import os

@patch(hg, "sh")
def test_clone(sh):
    hg.clone("https://foo", "bar")
    assert sh.called
    assert sh.call_args[0][0] == "hg clone https://foo bar"

@patch(hg, "sh")
def test_pull(sh):
    hg.pull("bar")
    assert sh.called
    assert sh.call_args[0][0] == "cd bar; hg pull"

@patch(hg, "sh")
def test_simple_update(sh):
    hg.update("bar")
    assert sh.called
    assert sh.call_args[0][0] == "cd bar; hg update -r tip"

@patch(hg, "sh")
def test_update_with_revision(sh):
    hg.update("bar", "120")
    assert sh.called
    assert sh.call_args[0][0] == "cd bar; hg update -r 120"

@patch(hg, "sh")
def test_branch(sh):
    assert hg.branch("bar") == "default"

@patch(hg, "sh")
def test_branches(sh):
    branches = hg.branches("bar",
            include_closed=False,
            __override__="""default 7:bb638753724c
        branch1 3:abb43356434c""")
    assert branches == ("default", ["default", "branch1"])

@patch(hg, "sh")
def test_branches_with_closed(sh):
    branches = hg.branches("bar",
            include_closed=True,
            __override__="""default 7:bb638753724c
        branch1 3:abb43356434c
        branch2 6:cbb63234214e (closed)""")
    assert branches == ("default", ["default", "branch1", "branch2"])
