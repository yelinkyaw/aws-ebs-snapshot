AWS Volume Snapshot
===================
Simple python script to create aws volume snapshot.
It can be executed from crontab for automated snapshot.

Requirements
===================
1. Python 2.7 and later
2. Boto 2.9 and later

Configurations
===================
1. Update aws_access_key and aws_secret_key
2. Update aws_region
3. Update aws_volume_id for taking snapshot
3 Update max_snapshot for number of lates snapshot to keep