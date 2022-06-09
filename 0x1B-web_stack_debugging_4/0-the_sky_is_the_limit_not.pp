# this manifest will fix the requests on the nginx server
exec {"sed -i 's/n 15/n 4096/' /etc/default/nginx && sudo service nginx restart":
  path    =>  ['/bin', '/usr/bin']
}