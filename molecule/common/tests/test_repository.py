import os
import subprocess
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')

def test_added_repository_pkg_link_u_co_jp(host):
    ## GPG キーのインストールテスト
    assert not host.ansible(
        "apt_key",
        "id=4DE76DC836A27DBAE17FAC4B09C9B9C18F429AAE" \
        "url=https://pkg.link-u.co.jp/key.asc" \
        "state=present")["changed"]

    ## link-u apt リポジトリのインストールテスト
    proc = subprocess.run(
        ["lsb_release", "-cs"],
        stdout = subprocess.PIPE,
        stderr = subprocess.PIPE)
    distro_name = proc.stdout.decode("utf8")[:-1]
    assert not host.ansible(
        "apt_repository",
        "repo=\"deb https://pkg.link-u.co.jp/" + \
        distro_name + " ./\" " \
        "state=present")["changed"]
