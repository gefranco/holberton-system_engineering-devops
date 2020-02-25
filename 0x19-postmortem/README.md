ISSUE SUMARY
On Tuesday 12 March 2019, the service experienced a service disruption for a duration of 4 hours and 10 minutes. 

DETAILED DESCRIPTION OF IMPACT


On Tuesday 12 March 2019 from 18:40 to 22:50 PDT, storage service experienced elevated error rates, averaging 20% error rates with a short peak of 31% errors during the incident.

The services that experienced the most significant customer impact were the following:

DBStorage experienced elevated long tail latency and an average error rate of 4.8%. All bucket locations and storage classes were impacted.


The service API experienced elevated latency and an error rate that peaked at 21% for fetching data.

ROOT CAUSE

On Monday 11 March 2019, we were alerted to a significant increase in storage resources for data used by the internal DataBase service. On Tuesday 12 March, to reduce resource usage, we made a configuration change which had a side effect of overloading a key part of the system for looking up the location of data. The increased load eventually lead to a cascading failure.

REMEDIATION AND PREVENTION

We were alerted to the service disruption at 18:56 PDT and immediately stopped the job that was making configuration changes. In order to recover from the failure, we manually reduced traffic levels to allow tasks to start up without crashing due to high load.

In order to prevent service disruptions of this type, we will be improving our ability to more quickly provision resources in order to recover from a cascading failure triggered by high load.
