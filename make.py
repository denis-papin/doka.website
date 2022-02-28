### Build the website, build the docker image, run the docker image

from subprocess import call
import os

SECRET_FOLDER = '../secrets'

def cp_dir(source, target):
    call(['cp', '-r', source, target]) # Linux

def build_website() :
    print ("Building the web site")
    cp_dir('./content', './docker/')


# Run commands to build the container
def build_docker_image() :

    print("Getting the certificates")

    if os.path.isdir(SECRET_FOLDER) and os.path.isfile(SECRET_FOLDER + '/certs/yukidb-website.crt') and  os.path.isfile(SECRET_FOLDER + '/certs/yukidb-website.key') :
        print("📃Found certificates in the secrets folder")
        call(['cp', SECRET_FOLDER + '/certs/yukidb-website.crt', './docker/config/yukidb-website.crt'])
        call(['cp', SECRET_FOLDER + '/certs/yukidb-website.key', './docker/config/yukidb-website.key'])
    else :
        print("⚠️ No secret folder found or yukidb-website CRT and KEY were not provided, we use the self signed certificate instead.")
        call(['cp', './docker/default-cert/self-signed.crt', './docker/config/yukidb-website.crt'])
        call(['cp', './docker/default-cert/self-signed.key', './docker/config/yukidb-website.key'])

    print("Building docker image...")
    call(['docker', 'build', './docker', '-t', 'yukidb-website'])

# Run commands to run the container
def run_docker_image() :
    print("Running docker image...")
    call(['docker', 'container', 'stop', 'yukidb-website'])
    call(['docker', 'container', 'rm', 'yukidb-website'])
    call(['docker', 'run', '-it', '-d', '-p', '80:80', '-p', '443:443', '--name', 'yukidb-website', 'yukidb-website' ])
    # docker run -it -d -p 80:80 -p 443:443 --name yukidb-website  yukidb-website

build_website()

build_docker_image()

run_docker_image()
