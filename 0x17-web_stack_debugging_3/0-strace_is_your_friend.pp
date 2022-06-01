# this manifest replace the mistake in php file
exec {'sed -i "s/class-wp-locale.phpp/class-wp-locale.php/g" /var/www/html/wp-settings.php':
  path    => ['/usr/bin'],
}
