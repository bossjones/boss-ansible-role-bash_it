import os
import pytest
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')

@pytest.mark.parametrize('bash_it_files',
                         ['/home/vagrant/.bash_it/',
                          '/home/vagrant/.bash_it/completion/available/git.completion.bash',
                          '/home/vagrant/.bash_it/aliases/available/general.aliases.bash',
                          '/home/vagrant/.bash_it/plugins/available/base.plugin.bash',
                          '/home/vagrant/.bash_it/plugins/available/history.plugin.bash'])
def test_bash_it_folders(host, bash_it_files):
    f = host.file(bash_it_files)

    assert f.exists
    assert f.user == 'vagrant'
    assert f.group == 'vagrant'
