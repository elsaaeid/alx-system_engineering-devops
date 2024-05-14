#!/usr/bin/env puppet
# Puppet script to change OS configuration for the holberton user

# Increase hard file limit for the holberton user
file { '/etc/security/limits.conf':
  ensure  => file,
  content => "holberton hard nofile 50000\n",
  mode    => '0644',
}

# Increase soft file limit for the holberton user
file { '/etc/security/limits.conf':
  ensure  => file,
  content => "holberton soft nofile 50000\n",
  mode    => '0644',
}

# Apply changes to the PAM configuration file
file { '/etc/pam.d/common-session':
  ensure  => file,
  content => "session required pam_limits.so\n",
  mode    => '0644',
}

# Restart the system to apply the changes
reboot { 'apply-os-configuration-changes':
  apply    => finished,
  subscribe => [File['/etc/security/limits.conf'], File['/etc/pam.d/common-session']],
}
