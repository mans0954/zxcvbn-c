#
# Regular cron jobs for the zxcvbn-c package
#
0 4	* * *	root	[ -x /usr/bin/zxcvbn-c_maintenance ] && /usr/bin/zxcvbn-c_maintenance
