# kill_process.pp

exec { 'killmenow_process':
  command     => '/usr/bin/pkill killmenow',
  refreshonly => true,
}
