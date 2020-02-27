# fix nginx by augmented the limit of open files
exec { 'fix nginx':
  command => '/bin/sed -i "s/15/1500/g" /etc/default/nginx; sudo service nginx restart'
}
