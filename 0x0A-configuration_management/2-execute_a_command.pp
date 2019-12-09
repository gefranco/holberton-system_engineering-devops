# kills a process named killmenow
exec {'kill-process':
command  => 'pgrep -f killmenow | xargs kill',
path     => ['/usr/bin', '/sbin', '/bin', '/usr/sbin'],
provider => 'shell',
}
