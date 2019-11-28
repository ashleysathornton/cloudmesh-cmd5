###############################################################
# pip install .; pytest -v --capture=no -v --nocapture tests/test_cmd5.py:Test_cmd5.test_001
# pytest -v --capture=no tests/test_cmd5.py
# pytest -v  tests/test_cmd5.py
###############################################################
from __future__ import print_function

from cloudmesh.common.Shell import Shell
from cloudmesh.common.util import HEADING

from cloudmesh.common.variables import Variables
import pytest
from cloudmesh.common.run.subprocess import run


def run(command):
    print(command)
    parameter = command.split(" ")
    shell_command = parameter[0]
    args = parameter[1:]
    result = Shell.execute(shell_command, args)
    print(result)
    return result


@pytest.mark.incremental
class Test_cmd5(object):

    def test_variables_assign(self):
        HEADING("assign key=value")
        v = Variables()
        n = len(v)
        v["gregor"] = "gregor"
        assert (len(v) == n + 1)
        assert "gregor" in v
        v.close()

    def test_variables_delete(self):
        HEADING("delete")
        v = Variables()
        del v["gregor"]
        assert "gregor" not in v
        v.close()

    def test_variables_add(self):
        HEADING("directory add ")
        d = {"a": "1", "b": "2"}
        v = Variables()
        v + d
        print(v)
        assert "a" in v and "b" in v
        del v["a"]
        del v["b"]

        v + d
        assert "a" in v and "b" in v
        v - d
        assert "a" not in v and "b" not in v

        print(v)
        v.close()

    def test_test_variable_remove(self):
        HEADING("directory and key subtract ")
        d = {"a": "1", "b": "2"}
        v = Variables()
        v + d
        print(v)
        assert "a" in v and "b" in v
        v - d.keys()
        assert "a" not in v and "b" not in v

        print(v)
        v.close()

    def test_cli_set(self):
        r = run("cms var deleteme=abc")
        v = Variables()
        print(r)
        assert v['deleteme'] == 'abc'

    def test_cli_get(self):
        r = run("cms var deleteme")
        v = Variables()
        print(r)
        assert v['deleteme'] == 'abc'

    def test_cli_list(self):
        r = run("cms var list")
        v = Variables()
        print(r)
        assert v['deleteme'] == 'abc'
        assert "deleteme='abc'" in r

    def test_cli_delete(self):
        r = run("cms var delete deleteme")
        v = Variables()
        print("Result:", r)
        print("Variable:", v)

        assert v['deleteme'] != 'abc'

    def test_cli_delete(self):
        r = run("cms var delete deleteme")
        v = Variables()
        print("Result:", r)
        print("Variable:", v)

        assert v['deleteme'] != 'abc'
