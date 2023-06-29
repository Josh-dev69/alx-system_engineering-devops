#!/usr/bin/env bash
# using puppet to make changes on our configuration file

file { 'etc/ssh/ssh_config';
	ensure => present;

content =>"

	# SSH Client Configuration
	host*
	IdentityFile ~/.ssh/school
	PasswordAuthentication no
}
