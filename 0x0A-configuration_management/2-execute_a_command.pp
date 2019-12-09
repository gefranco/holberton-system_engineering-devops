# kills a process named killmenow
exec {'kill-process':
command  => "pkill 'killmenow' | awk '{print \$2}'",
path     => ['/usr/bin', '/sbin', '/bin', '/usr/sbin'],
provider => 'shell',
}
