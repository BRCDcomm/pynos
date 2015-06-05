#pyNOS
pyNOS is a python library for working with Brocade devices running NOS.

##Usage
The following is an example usage of pyNOS. Full documentation can be found on
the wiki.
```
from pynos.netconf import Device

NOS_DEVICE = Device(('10.10.10.1', '22'), ('admin', 'pass'))

NOS_DEVICE.interface.set_ip('tengigabitethernet',
                            '1/0/1',
                            '10.1.1.1/24')
```

##Testing
Tests are inteded to be run using nose
```
$nosetests
```

##License
pyNOS is released under the APACHE 2.0 license. See ./LICENSE for more
information.