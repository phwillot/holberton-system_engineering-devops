# this manifest replace the mistake in php file
exec {'sed -i "s/phpp/php/g /var/www/html/wp-settings.php':
  path    => ['/usr/bin'],
}
