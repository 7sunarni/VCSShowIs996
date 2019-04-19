import sys
import os
import re
import numpy as np
import matplotlib.pyplot as plt

def main():

	
	if len(sys.argv)<2:
		print("please input project path")
		return
	dir = sys.argv[1]
	if not os.path.exists(dir):
		print("path not exist")
		return
	if not os.path.exists(dir+"/.git"):
		print("path not git project")
		return

	
	os.chdir(dir)

	logFile = os.path.join(dir, "log.txt")

	os.system("git log > log.txt")

	times = []
	timeCount = [0] * 24
	weeks = []
	weeksCount = [0] * 7

	
	with open(logFile) as log: # 
		while True:
			
			line = log.readline()
			if line == "":
				break
			if line[0] == "D":
				rawTime = re.search(".*\\d{2}\\:\\d{2}:\\d{2}",line).group()
				week = rawTime[8:11]
				time = rawTime[-8:-1]
				times.append(time)
				weeks.append(week)

	
	os.remove(logFile)

	
	for i in range (0,len(times)):
			time = int(times[i][0:2])
			count = timeCount[time]
			timeCount[time] = count + 1

	for i in range(0,len(weeks)):
		week = weeks[i]
		if week == "Mon":
			weeksCount[0] = weeksCount[0] + 1
		elif week == "Tue":
			weeksCount[1] = weeksCount[1] + 1
		elif week == "Wed":
			weeksCount[2] = weeksCount[2] + 1
		elif week == "Thu":
			weeksCount[3] = weeksCount[3] + 1	
		elif week == "Fri":
			weeksCount[4] = weeksCount[4] + 1
		elif week == "Sat":
			weeksCount[5] = weeksCount[5] + 1
		elif week == "Sun":
			weeksCount[6] = weeksCount[6] + 1
		else:
			print("not found")


	plt.subplot(1,2,1)
	plt.bar(range(len(timeCount)),timeCount)
	plt.xlabel("commit time")
	plt.ylabel("commit count")
	plt.xticks(np.arange(0,24,1))

	plt.subplot(1,2,2)
	plt.bar(range(7), weeksCount)
	plt.xlabel("commit weekday")
	plt.ylabel("commit count")
	plt.xticks(range(7),["mon","tues","wed","thurs","fri","sat","sun"])
	plt.show()

if __name__ == '__main__':
	main()
