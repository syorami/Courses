# Solution for Lecture 09

## Entropy

1. Suppose a password is chosen as a concatenation of five lower-case dictionary words, where each word is selected uniformly at random from a dictionary of size 100,000. An example of such a password is `correcthorsebatterystaple`. How many bits of entropy does this have?

	Compute entropy as `log_2(100000^5) = 83.048`.
	
2. Consider an alternative scheme where a password is chosen as a sequence of 8 random alphanumeric characters (including both lower-case and upper-case letters). An example is `rg8Ql34g`. How many bits of entropy does this have?

	The total possibility for a single character is `26 + 26 + 10 = 62`. So the entropy is computed as `log_2(62 ** 8) = 47.634`.
	
3. Which is the stronger password?
	
	The first one.
	
4. Suppose an attacker can try guessing 10,000 passwords per second. On average, how long will it take to break each of the passwords?

	The attacker will take `10^21` seconds to break the first password type and `2.2^10` seoncds to break the second password type.
	
## Cryptographic hash functions

1. Download a Debian image from a [mirror](https://www.debian.org/CD/http-ftp/) (e.g. [from this Argentinean mirror](http://debian.xfree.com.ar/debian-cd/current/amd64/iso-cd/). Cross-check the hash (e.g. using the `sha256sum` command) with the hash retrieved from the official Debian site (e.g. [this file](https://cdimage.debian.org/debian-cd/current/amd64/iso-cd/SHA256SUMS) hosted at `debian.org`, if you've downloaded the linked file from the Argentinean mirror).

	Download `debian-mac-10.4.0-amd64-netinst.iso` and use `shasum` command to compute the hash results of the file as below:
	
	```shell
	shasum -a 256 debian-mac-10.4.0-amd64-netinst.iso 
	```

	The output `d0971275adf607ad5527c3c1404f642d788431942767a6943477c1d0ebbe2bd2` is the same as [original checksum](https://cdimage.debian.org/debian-cd/current/amd64/iso-cd/SHA256SUMS).


## Symmetric cryptography

1. Encrypt a file with AES encryption, using [OpenSSL](https://www.openssl.org/): `openssl aes-256-cbc -salt -in {input filename} -out {output filename}`. Look at the contents using `cat` or `hexdump`. Decrypt it with `openssl aes-256-cbc -d -in {input filename} -out {output filename}` and confirm that the contents match the original using `cmp`.

	Succeeded.

## Asymmetric cryptography

1. Set up [SSH keys](https://www.digitalocean.com/community/tutorials/how-to-set-up-ssh-keys--2) on a computer you have access to (not Athena, because Kerberos interacts weirdly with SSH keys). Rather than using RSA keys as in the linked tutorial, use more secure [ED25519 keys](https://wiki.archlinux.org/index.php/SSH_keys#Ed25519). Make sure your private key is encrypted with a passphrase, so it is protected at rest.

2. [Set up GPG](https://www.digitalocean.com/community/tutorials/how-to-use-gpg-to-encrypt-and-sign-messages)

3. Sign a Git commit with `git commit -S` or create a signed Git tag with `git tag -s`. Verify the signature on the commit with `git show --show-signature` or on the tag with `git tag -v`.