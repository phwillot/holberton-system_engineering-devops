# Make change to ssh configuration file to connect to our web server

exec {'sudo sed -i "s/^.*PasswordAuthentication.*$/    PasswordAuthentication no/g" /etc/ssh/ssh_config':
  path => ['/usr/bin']
}

exec {'sudo sed -i "s/^.*id_rsa.*$/    IdentityFile ~\/.ssh\/school/g" /etc/ssh/ssh_config':
  path => ['/usr/bin']
}
