# kill_process.pp

exec { 'kill process':
  command  => 'pkill killmenow',
  path     => '/usr/bin',
  provider => shell
}
