# kills a process named killmenow
exec {'kill-process':
command  => "ps -ef | grep killmenow | grep -v pts/1 | /bin/awk '{print \$2}' | xargs kill -9",
path     => ['/usr/bin', '/sbin', '/bin', '/usr/sbin'],
provider => 'shell',
}
