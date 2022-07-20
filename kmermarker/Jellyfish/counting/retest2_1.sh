#!/bin/bash
for ((num=0;num<=19;num++))
do
	echo $num
	echo `jellyfish count -m 24 -o reoutput$num.jf -s 100M -t 16 -C output$num.fa`
	sleep 2
	echo `jellyfish count -m 24 -o rereoutput$num.jf -s 100M -t 16 -C output$num.fa`
	sleep 2
done

for ((i=0;i<=19;i++))
do
	echo $num
	echo `jellyfish merge reoutput$i.jf rereoutput$i.jf -o outputx2_$i.jf`
	sleep 3;
done

