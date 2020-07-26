#!/bin/bash

mysql -u root -pwelcome1 -e 'SHOW SLAVE STATUS\G' | while IFS= read -r loop
do
	if [ "$loop" == "             Slave_IO_Running: Yes" ]; then
		echo "0:0:OK"
	elif [ "$loop" == "             Slave_IO_Running: No" ];then
		echo "4:4:Slave_IO_Running Down"
	fi
done

