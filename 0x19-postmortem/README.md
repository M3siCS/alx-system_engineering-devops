# Postmortem: Nginx Outage on [Date]

## Issue Summary
- **Duration:** The outage lasted for 2 hours, from 14:00 to 16:00 UTC.
- **Impact:** The website was down, affecting 70% of users, who saw a "502 Bad Gateway" error.
- **Root Cause:** A misconfigured Nginx file caused the service to fail on restart.

## Timeline
- **14:00 - Detection:** Monitoring alert for website unresponsiveness.
- **14:05 - Initial Investigation:** Checked server load, assumed high traffic.
- **14:15 - Misleading Path:** Suspected a DDoS attack; traffic was normal.
- **14:30 - Escalation:** Issue escalated to the DevOps team.
- **14:45 - Root Cause Identification:** Found a syntax error in the Nginx configuration file.
- **15:00 - Resolution:** Corrected the configuration and restarted Nginx.
- **16:00 - Service Restoration:** Website was fully operational.

## Root Cause and Resolution
- **Root Cause:** A typo in the Nginx configuration file caused the service to fail on restart.
- **Resolution:** The typo was corrected, and Nginx was successfully restarted.

## Corrective and Preventative Measures
- **Improvements:**
  - Enhance testing procedures for configuration changes.
  - Validate configuration files before applying changes.
- **TODO List:**
  1. Patch Nginx server to include automated syntax checks.
  2. Add monitoring for service failures.
  3. Implement a rollback mechanism for configuration changes.


