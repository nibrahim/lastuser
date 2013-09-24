from fabric.api import run, cd, env, settings, sudo, local, shell_env


env.hosts = ['ubuntu@ec2-54-251-215-76.ap-southeast-1.compute.amazonaws.com']
env.key_filename = ['/home/noufal/.ssh/id_rsa_pratham']


app_repository = "https://github.com/nibrahim/lastuser"

app_base = "/opt/lastuser"
deployments_dir = "{0}/deployments".format(app_base)
currently_deployed_dir = "{0}/deployed".format(app_base)

virtualenv_home = "/opt/frp/environments"
app_virtualenv = "lastuser"

#Remote commands
def obtain_code(tag):
    with cd(deployments_dir):
        run("rm -Rf {0}".format(tag))
        run("git clone -q {0} {1}".format(app_repository, tag))
        run("cd {0}/{1} && git checkout {1}".format(deployments_dir, tag))
        
def set_deployed_version(tag):
    with cd(app_base):
        run("rm -f {0}".format(currently_deployed_dir))
        run("ln -s {0}/{1} {2}".format(deployments_dir, tag, currently_deployed_dir))
    
def update_virtualenv(tag):
    with cd(app_base):
        run(". {0}/{1}/bin/activate && pip install -M -r {2}/requirements.txt".format(virtualenv_home, app_virtualenv, currently_deployed_dir))

def monit_restart():
    sudo("sudo monit restart lastuser")

def reset_database():
    with cd(currently_deployed_dir):
        # run(". {0}/{1}/bin/activate && python manage.py db drop -e production".format(virtualenv_home, app_virtualenv))
        run(". {0}/{1}/bin/activate && python manage.py db create -e production".format(virtualenv_home, app_virtualenv))


# Local commands
def push_code():
    local("git push")

# Public commands
def deploy(tag, venv = False, resetdb = False):
    "Deploy the application tagged by :tag:"
    push_code()
    obtain_code(tag)
    set_deployed_version(tag)
    if venv:
        update_virtualenv(tag)
    if resetdb:
        reset_database()
    monit_restart()

def rollback(tag):
    "Roll back to given tag"
    set_deployed_version(tag)
    update_monit_config()
    monit_restart()
