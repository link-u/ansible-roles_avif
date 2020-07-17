import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')

def test_installed_package(host):
    assert host.package("cavif").is_installed
    assert host.package("davif").is_installed

def test_run_help_command(host):
    assert host.run("cavif --help").succeeded
    assert host.run("davif --help").succeeded
