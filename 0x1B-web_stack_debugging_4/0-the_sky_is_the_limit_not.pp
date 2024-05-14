#!/usr/bin/env puppet
# To solve the issue of a high number of failed requests

# Increase the ULIMIT of the default file
file { '/etc/default/nginx':
  ensure  => file,
  content => "ULIMIT='-n 4096'\n",
}

# Restart Nginx
service { 'nginx':
  ensure  => running,
  enable  => true,
  require => File['/etc/default/nginx'],
}
