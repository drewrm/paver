""" Convenience functions for working with mercurial. 

Requires the hg binary on the path"""

from paver.easy import sh

def clone(url, dest):
    """ Clones a mercurial repository """
    sh("hg clone %(url)s %(dest)s" % dict(url=url, dest=dest))

def pull(dest):
    """ Performs a hg pull on the specified repository """
    sh("cd %(dest)s; hg pull" % dict(dest=dest))

def update(dest, rev="tip"):
    sh("cd %(dest)s; hg update -r %(rev)s" % dict(dest=dest,rev=rev))

def branch(dest):
    output = sh("cd %(dest)s; hg branch" % dict(dest=dest))

    if output == None:
        current_branch = "default"
    else:
        current_branch = output.strip().split()[0]

    return current_branch

def branches(dest, include_closed=False, __override__=None):
    """ Get a list of branches as well as the current branch """
    closed_flag = ""
    if include_closed == True:
        closed_flag = " -c"

    if __override__ == None:
        output = sh("cd %(dest)s; hg branches %(closed_flag)s" % dict(dest=dest, closed_flag=closed_flag))
    else:
        output = __override__

    if output == None:
        return None, []

    branches = []
    for line in output.split("\n"):
        branches.append(line.strip().split()[0])

    return branch(dest), branches
