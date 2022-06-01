# this manifest replace the mistake in php file
exec {'sed -i "s/phpp/php/" /var/www/html/wp-settings.php':
  path    =>  ['/bin']
}
