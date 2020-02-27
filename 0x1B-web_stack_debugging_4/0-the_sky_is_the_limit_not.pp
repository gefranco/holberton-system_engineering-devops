# fix nginx by augmented the limit of open files
exec { 'fix wp':
  command => '/bin/sed -i "s/15/1500/g" /etc/default/nginx',
}
