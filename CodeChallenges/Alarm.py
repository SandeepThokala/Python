from playsound import playsound
from time import sleep, time, ctime


s1 = r"C:\Users\sande\Desktop\Deepu\CodeChallenges\mixkit-street-public-alarm-997.wav"
def alarm(timed, audio, message):
	while 1:
		sleep(1)
		if ctime(time()) == timed:
			playsound(audio)
			print(message)
			break

alarm('Sat Feb 27 14:55:00 2021', s1, 'Check upstox..!')

#not my solution

'''import sched, winsound as ws

def set_alarm(alarm_time, wav_file, message):
	s = sched.scheduler(time, sleep)
	s.enterabs(alarm_time, 1, print, argument = (message,))
	s.enterabs(alarm_time, 1, ws.PlaySound, argument = (wav_file, ws.SND_FILENAME))
	print('Alarm set for', time.asctime(time.localtime(alarm_time)))
	s.run'''