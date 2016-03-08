This script can:

Find lfi vulnerability in each parameter automatically<br>
Find the root of the file system automatically <br>
Find default files inside the server in linux and windows<br>
Find passwords in config files<br>
Support basic authentication<br>
Send null bytes to bypass some controls<br>
Write a report of the scan<br>
Support proxy<br>
Detect  OS and send only test according the OS detected <br>
Hexaencode support<br>
Output in html format<br>

Examples:<br>
Without proxy:<br>
$ python lfimap.py -t "<a href='http://localhost/lfi.php?page=home.txt&module=home'>http://localhost/lfi.php?page=home.txt&amp;module=home</a>" -o report.html<br>

With proxy:<br>
$ python lfimap.py -t "<a href='http://localhost/lfi.php?page=home.txt&module=home'>http://localhost/lfi.php?page=home.txt&amp;module=home</a>" -w <a href='http://proxy:80'>http://proxy:80</a> -o report.html<br>

Encoding in hexa:<br>
$ python lfimap.py -t "<a href='http://localhost/lfi.php?page=home.txt&module=home'>http://localhost/lfi.php?page=home.txt&amp;module=home</a>" -x <br>

Sending null byte: <br>
$ python lfimap.py -t "<a href='http://localhost/lfi.php?page=home.txt&module=home'>http://localhost/lfi.php?page=home.txt&amp;module=home</a>" -n <br>

In this site exist a good article about this tool.<br>
<a href='http://www.aldeid.com/index.php/Lfimap'>http://www.aldeid.com/index.php/Lfimap</a> <br>

Mailme to aepereyra (at) gmail dot com<br>
