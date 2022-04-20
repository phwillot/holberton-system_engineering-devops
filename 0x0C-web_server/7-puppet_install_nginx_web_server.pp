# Install and configures nginx server
exec {'apt update -y && apt upgrade -y':
  path    => ['/usr/bin'],
}

exec {'apt install nginx -y':
  path    => ['/usr/bin'],
}

exec {'echo "Hellow World" > /var/www/html/index.nginx-debian.html':
  path    => ['/usr/bin'],
}

exec {"sed -i '/listen \[::\]:80 default_server;/a\\trewrite ^\/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent' /etc/nginx/sites-available/default":
  path    => ['/usr/bin'],
}
