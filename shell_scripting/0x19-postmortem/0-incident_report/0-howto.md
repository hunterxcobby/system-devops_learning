Issue Summary

short summary (5 sentences)
list the duration along with start and end times (include timezone)
state the impact (most user requests resulted in 500 errors, at peak 100%)
close with root cause
Timeline

list the timezone
covers the outage duration
when outage began
when staff was notified
actions, events, …
when service was restored
Root Cause

give a detailed explanation of event
do not sugarcoat
Resolution and recovery

give detailed explanation of actions taken (includes times)
Corrective and Preventative Measures

itemized list of ways to prevent it from happening again
what can we do better next time?
This Incident Report also points to the fact that Google has lots of internal systems and procedural machinery happening behind the scenes. I think of these as best practices for any company. For example, they have automated service monitoring and alerting capabilities, we know this because they listed when the outage began, and when the team was alerted via pager. They also have change management, in that they were able to see who did what when, and ultimately try and roll back the changes. In my mind this is key, if you do not have this visibility into changes, then it will take time to figure out what triggered the issue in the first place, never mind trying to roll it back. They also did not sugarcoat the fact that the configuration push was not the safest and skipped testing.

So, if you ever find yourself in a situation where you have to write an Incident Report, I highly suggest checking out Google’s Incident Report listed in the episode notes below. I would also recommend thinking about how their internal systems and procedural machinery can be replicated in your environment.

url : https://sysadmincasts.com/episodes/20-how-to-write-an-incident-report-postmortem