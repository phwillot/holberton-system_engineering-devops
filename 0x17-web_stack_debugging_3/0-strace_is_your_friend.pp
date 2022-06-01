# this manifest replace the mistake in php file
exec {'sed -i "s/class-wp-locale.phpp/class-wp-locale.php/" /var/www/html/wp-settings.php':
  path    =>  ['/bin', '/usr/bin']
}
