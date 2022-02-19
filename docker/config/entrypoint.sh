# Main shell script that is run at the time that the Docker image is run
# Go to default.conf directory
cd /etc/nginx;

# ENV VARS

# A list of environment variables that are passed to the container and their defaults
# CRT - double check that the file exists
export CRT="${CRT:=yukidb-website.crt}";
if [ -f "/etc/ssl/certs/$CRT" ]
then
    # set crt file in the default.conf file
    sed -i "/ssl_certificate \//c\\\tssl_certificate \/etc\/ssl\/certs\/$CRT;" nginx.conf;
fi

# KEY - double check that the file exists
export KEY="${KEY:=yukidb-website.key}";
if [ -f "/etc/ssl/private/$KEY" ]
then
    # set key file in the default.conf file
    sed -i "/ssl_certificate_key \//c\\\tssl_certificate_key \/etc\/ssl\/private\/$KEY;" nginx.conf;
fi

# Needed to make sure nginx is running after the commands are run
nginx -g 'daemon off;'; nginx -s reload;
