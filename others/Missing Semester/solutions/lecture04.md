# Solution for Lecture 04

1. Take this [short interactive regex tutorial](https://regexone.com/).

2. Find the number of words (in `/usr/share/dict/words`) that contain at least three `a`s and don’t have a `'s` ending. What are the three most common last two letters of those words? `sed`’s `y` command, or the `tr` program, may help you with case insensitivity. How many of those two-letter combinations are there? And for a challenge: which combinations do not occur?

	
	Find the number of words that contain at least three `a`s and don't have a `'s` ending:
	
	```shell
	cat /usr/share/dict/words | grep -E '^(.*a){3}.*$' | grep -v ".*'s" | wc -l
	```
	
	The three most comon last two letters of those words:
	
	```shell
	cat /usr/share/dict/words | grep -E '^(.*a){3}.*$' | grep -v ".*'s" | sed -E 's/^.*(..)$/\1/' | tr [:upper:] [:lower:] | sort | uniq -c | sort -rnk1.1 | head -n3 | awk '{print $2}'
	```
	
	How many of those two-letter cobinations are there:
	
	```shell
	cat /usr/share/dict/words | grep -E '^(.*a){3}.*$' | grep -v ".*'s" | sed -E 's/^.*(..)$/\1/' | tr [:upper:] [:lower:] | uniq | wc -l
	```
	
	No available solution for the challenge.
	
3. To do in-place substitution it is quite tempting to do something like `sed s/REGEX/SUBSTITUTION/ input.txt > input.txt`. However this is a bad idea, why? Is this particular to `sed`? Use` man sed` to find out how to accomplish this.

	Bash processes the redirects `>` first, so by the time the `sed` command is executed, the file is already empty. Append `>>` also won't work and the `sed` command will try to read the file it is appending to. It will never reach EOF and eat CPU resources (Ref: [Why does redirecting sed output to same input file make my machine unresponsive?](https://askubuntu.com/questions/795713/why-does-redirecting-sed-output-to-same-input-file-make-my-machine-unresponsive))
	
	Use `-i` to operate inplace replacement: `sed -i s/REGEX/SUBSTITUTION/ input.txt > input.txt`
	
4. Find your average, median, and max system boot time over the last ten boots. Use `journalctl` on Linux and `log show` on macOS, and look for log timestamps near the beginning and end of each boot.

	Omitted
	
5. Look for boot messages that are not shared between your past three reboots (see `journalctl`’s `-b` flag). Break this task down into multiple steps. First, find a way to get just the logs from the past three boots. There may be an applicable flag on the tool you use to extract the boot logs, or you can use sed `'0,/STRING/d'` to remove all lines previous to one that matches `STRING`. Next, remove any parts of the line that always varies (like the timestamp). Then, de-duplicate the input lines and keep a count of each one (`uniq` is your friend). And finally, eliminate any line whose count is 3 (since it was shared among all the boots).

	Omited
	
6. Find an online data set like [this one](https://stats.wikimedia.org/EN/TablesWikipediaZZ.htm), [this one](https://ucr.fbi.gov/crime-in-the-u.s/2016/crime-in-the-u.s.-2016/topic-pages/tables/table-1). or maybe one [from here](https://www.springboard.com/blog/free-public-data-sets-data-science-project/). Fetch it using `curl` and extract out just two columns of numerical data. If you’re fetching HTML data, `pup` might be helpful. For JSON data, try `jq`. Find the min and max of one column in a single command, and the sum of the difference between the two columns in another.
