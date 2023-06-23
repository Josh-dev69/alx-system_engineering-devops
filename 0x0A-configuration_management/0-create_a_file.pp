# Create a file using Puppet

file { '/tmp/school':
  ensure  => 'present',
  content => 'I love Puppet',
  mode    => '0744',
  owner   => 'www-data',
  group   => 'www-data'
}
