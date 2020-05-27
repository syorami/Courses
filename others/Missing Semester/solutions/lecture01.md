# Solution for Lecture 01

1. Create a new directory called `missing` under `/tmp`.

	`mkdir /tmp/missing`

2. Look up the `touch` program. The `man` program is your friend.

	Use `man touch` to find out the usage of `touch` programs. The `touch` command is a standard command used in UNIX/Linux operating system which is used to create, change and modify timestamps of a file
	
3. Use `touch` to create a new file called `semester` in `missing`.

	`touch /tmp/missing/semester`
	
4. Write the following into that file, one line at a time:

	```shell
	#!/bin/sh
	curl --head --silent https://missing.csail.mit.edu
	```
	
	Use `echo` to write online into the file at a time:
	
	```shell
	echo '#!/bin/sh' > /tmp/missing/semester 
	echo 'curl --head --silent https://missing.csail.mit.edu' >> /tmp/missing/semester
	```

5. Try to execute the file, i.e. type the path to the script (`./semester`) into your shell and press enter. Understand why it doesn’t work by consulting the output of `ls` (hint: look at the permission bits of the file).

	The permission for this file is `-rw-r--r--` so it is not allowed to execute the script.
	
6. Run the command by explicitly starting the `sh` interpreter, and giving it the file `semester` as the first argument, i.e. `sh semester`. Why does this work, while `./semester` didn’t?

	Executing a file as a program requires execute permission. When you use `sh semester`, it's not being executed as a program, it's just an input file to the `sh` program, and that program just needs to be able to read it (just like `cat semester` only needs to be able to **read** it).
	
7. Look up the `chmod` program (e.g. use `man chmod`).

8. Use `chmod` to make it possible to run the command `./semester` rather than having to type `sh` semester. How does your shell know that the file is supposed to be interpreted using `sh`?

	Use `chmod 744 /tmp/missing/semester` to give execute permission for the create user but only read permission for group and other users.
	
	The shell knows the interpreter of the file through the **shebang** line of the file - `#!/bin/sh`
	
9. Use `|` and `>` to write the “last modified” date output by `semester` into a file called `last-modified.txt` in your home directory.

	`ls -l semester | cut -c 32-44 > ~/last-modified.txt`
	
10. Write a command that reads out your laptop battery’s power level or your desktop machine’s CPU temperature from `/sys`. Note: if you’re a macOS user, your OS doesn’t have sysfs, so you can skip this exercise.

	macOS user just skips this one :)
