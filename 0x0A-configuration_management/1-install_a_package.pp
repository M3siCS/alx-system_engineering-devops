# 1-install_a_package.pp

package { 'Flask':
  ensure   => '2.1.0',
  provider => 'pip',
}

package { 'Werkzeug':
  ensure   => '2.1.1',
  provider => 'pip',
  require  => Package['Flask'],
}

