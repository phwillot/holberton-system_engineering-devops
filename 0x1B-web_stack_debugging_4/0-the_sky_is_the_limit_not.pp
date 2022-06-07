# this manifest will fix the requests on the nginx server
exec {'sed -i '$d' /etc/default/nginx && echo ULIMIT=\"-n 4096\" >> /etc/default/nginx && sudo service nginx restart':
  path    =>  ['/bin']
}
