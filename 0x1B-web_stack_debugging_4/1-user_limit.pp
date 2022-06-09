# Make it possible to login with the holberton user and open a file without any error message.
exec {"sed -i '/holberton/d' /etc/security/limits.conf":
  path    =>  ['/bin']
}