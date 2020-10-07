# pykeychain
A KeyChain Manager developed in Python 3. Currently with command line and ncurses interfaces.

If you are using openssl 1.1.0+ and you encrypted an archive with a previous version of openssl add the option
```-md md5```
to the unarchive command (account.py open_decrypt()). This enables the older passkey management with MD5 in place of the newer management using SHA256 and adopted by default by openssl 1.1.0+.

To open archive:
```sh
openssl enc -d -aes-256-cbc -md sha256 -in  archive.protected
```

In case an archive was saved with wrong encoding (e.g. on Windows):
```sh
iconv -f ISO885916 -t UTF-8 <input file> > <output file>
```