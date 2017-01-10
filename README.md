liveboot
---

Liveboot is intended to make building live usbs for booting OS distributions fast, and friendly. 

## Installation
```
$ pip install git+https://github.com/tcoyze/liveboot.git
```

## Usage
```
$ liveboot URL FILE
$ liveboot --chunk [NUMBER OF BYTES] URL FILE
$ liveboot --help
$ liveboot 'http://releases.ubuntu.com/16.04/ubuntu-16.04.1-server-amd64.iso' /dev/disk3
```

