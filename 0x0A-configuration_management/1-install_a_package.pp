# install flask -v 2.1.0 from pip3

package { 'python3-pip':
  ensure => 'installed',
}

exec { 'install_flask':
  command => '/usr/bin/pip3 install flask==2.1.0 werkzeug==2.0.2',
  path    => '/usr/local/bin',
  require => Package['python3-pip'],
}
