# Solution for Lecture 02

1. Read `man ls` and write an `ls` command that lists files in the following manner

	* Includes all files, including hidden files
	* Sizes are listed in human readable format (e.g. 454M instead of 454279954)
	* Files are ordered by recency
	* Output is colorized
	
	`ls -a -l -h -t --color`
	
	`-a` shows hidden files; `-l` uses a long listing format; `-h` prints human readable sizes; `-t` sorts by modification time; `--color` colorizes the output.
	
2. Write bash functions `marco` and `polo` that do the following. Whenever you execute `marco` the current working directory should be saved in some manner, then when you execute `polo`, no matter what directory you are in, `polo` should `cd` you back to the directory where you executed `marco`. For ease of debugging you can write the code in a file `marco.sh` and (re)load the definitions to your shell by executing `source marco.sh`.

	```shell
	#!/bin/sh
	macro () {
	    pwd > /tmp/pwd.log
	}
	
	polo () {
	    cd $(cat /tmp/pwd.log)
	}
	```

3. Say you have a command that fails rarely. In order to debug it you need to capture its output but it can be time consuming to get a failure run. Write a bash script that runs the following script until it fails and captures its standard output and error streams to files and prints everything at the end. Bonus points if you can also report how many runs it took for the script to fail.

	```shell
	 #!/usr/bin/env bash
	
	 n=$(( RANDOM % 100 ))
	
	 if [[ n -eq 42 ]]; then
	    echo "Something went wrong"
	    >&2 echo "The error was using magic numbers"
	    exit 1
	 fi
	
	 echo "Everything went according to plan"
	```

	The implementation is as below:
	
	```shell
	#!/usr/bin/env bash
	
	stdout=/tmp/std.log
	error=/tmp/error.log
	
	> $stdout
	> $error
	
	count=0
	
	while [[ true ]]; do
		count=$((count+1))
		sh failure_script.sh >> $stdout 2>> $error ||break
	done
	
	cat $stdout
	cat $error
	
	echo "Take $count runs for the script to fail"
	```
	
4. Your task is to write a command that recursively finds all HTML files in the folder and makes a zip with them. Note that your command should work even if the files have spaces (hint: check `-d` flag for `xargs`)

	```shell
	find . -name '*.html' | xargs tar czf html.tar.gz
	```
	
5. (Advanced) Write a command or script to recursively find the most recently modified file in a directory. More generally, can you list all files by recency?

	Find the most recently modified file in a directory:
	
	```shell
	find . -type f -printf '%T+ %p\n' | sort -r | head -n 1 | awk '{print $2}'
	```

	List all files by recency:
	
	```shell
	find . -type f -printf '%T+ %p\n' | sort -r | awk '{print $2}'
	```