{{{
  "title": "Creating a Scheduled Task",
  "date": "7-28-2014",
  "author": "Richard Seroter",
  "attachments": [],
  "contentIsHTML": true
}}}

<p><strong>Description:</strong>
</p>
<p>Scheduled Tasks are used to set automated activities against cloud servers. This empowers users to do things like coordinate maintenance activities, turn off developer machines over the weekend, or automatically archive servers at the end of a project.
  Scheduled Tasks can be run against individual servers, or an entire Group of servers.</p>
<div><strong>1. Locate the Scheduled Tasks configuration page.</strong>
</div>
<ul>
  <li>For either Group or server details, find the navigation tab called <strong>Scheduled Tasks</strong>.
    <br />
    <br /><img src="https://t3n.zendesk.com/attachments/token/vHkSgU6iuSOQgJDX876WJvyKL/?name=schedule-task-tab.png" alt="schedule-task-tab.png" />
  </li>
</ul>
<div><strong>2. Create a Scheduled Task</strong>
</div>
<ul>
  <li>Click the button <strong>Schedule Task</strong>&nbsp;to start creating a scheduled task.
    <br />
    <br /><img src="https://t3n.zendesk.com/attachments/token/YIuGFw0XogW9NA6ZcPROsKjoW/?name=schedule-task-create.png" alt="schedule-task-create.png" />
  </li>
  <li>Set the status of the task to "On" (active) or "Off" (inactive).</li>
  <li>Select the type of task. Options include: <strong>Archive</strong> (stop and move to low-cost storage), <strong>Delete</strong>, <strong>Pause</strong>, <strong>Power On</strong>, <strong>Reboot</strong>, <strong>Shutdown</strong>,<strong>&nbsp;Create Snapshot</strong>,
    and<strong>&nbsp;Delete Snapshot</strong>.</li>
  <li>Set the starting scheduled for the task. If the task is repeating, this is the first occurrence of the series. If this is a one-time task, then this is the date of the single execution.</li>
  <li>Choose the repeat settings. Options are: <strong>Never</strong> (only occur once), <strong>Daily</strong>, <strong>Weekly</strong>, <strong>Monthly</strong>, and <strong>Weekly Custom</strong>.&nbsp;If&nbsp;<strong>Weekly Custom&nbsp;</strong>recurrence
    is chosen, then the user can select&nbsp;the day(s) of the week to run the task on.
    <br />
    <br /><img src="https://t3n.zendesk.com/attachments/token/PxHg3pcYML7TNGMbSmApJLeqW/?name=schedule-task-repeat.png" alt="schedule-task-repeat.png" />
  </li>
  <li>Set the task expiration. Options include: <strong>Never</strong> (run forever), <strong>After Count</strong>, <strong>After Date</strong>. If the user chooses "After Count", then they are asked for the number of occurrences to run. If the users chooses
    "After Date", then they are asked for the date to stop the task.</li>
  <li>Click <strong>Create</strong>&nbsp;button to save the Scheduled Task. The task can be changed by selecting the task and altering any of the properties. Tasks can also be deleted by selecting the task and clicking the <strong>Delete</strong>&nbsp;button.</li>
</ul>
