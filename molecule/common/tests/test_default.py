import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')

def test_installed_cavif_and_davif(host):
    assert host.package("cavif").is_installed
    assert host.package("davif").is_installed

def test_run_help_cavif_and_davif(host):
    assert host.run("cavif --help").succeeded
    assert host.run("davif --help").succeeded
