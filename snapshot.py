#!/usr/bin/env python
import boto.ec2
import collections

# Constants
aws_access_key = 'AWS Access Key'
aws_secret_key = 'AWS Secret Key'
#AWS Regions
# us-east-1 (N. Virginai)
# us-west-1 (Oregon)
# us-west-2 (N. California)
# eu-west-1 (Ireland)
# ap-southeast-1 (Singapore)
# ap-northeast-1 (Tokyo)
# ap-southeast-2 (Sydney)
# se-east-1 (Sao Paulo)
aws_region = 'ASW Region' 
aws_volume_id = 'vol-volumeid'
max_snapshot = 5

# Connect to AWS
con = boto.ec2.connect_to_region(aws_region, aws_access_key_id=aws_access_key, aws_secret_access_key=aws_secret_key)

# Create Snapshot
print datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), 'Creating snapshot of volume:', aws_volume_id
new_snapshot = con.create_snapshot(aws_volume_id, 'Automated Snapshot')
print datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), 'Started creating snapshot:', new_snapshot.id

# Get snapshot list
snapshot_raw = con.get_all_snapshots(filters={'volume-id': aws_volume_id})

# Un-ordered List
snapshot_list = {}
for snapshot in snapshot_raw:
	snapshot_list[snapshot.start_time]=snapshot.id

# Sort by Date
snapshots = collections.OrderedDict(sorted(snapshot_list.items()))

# Delete the oldest snapshot
if len(snapshots.keys())>max_snapshot:
	oldest_snapshot_id = snapshots[snapshots.keys()[0]]
	print datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), 'Deleting snapshot:', oldest_snapshot_id
	con.delete_snapshot(oldest_snapshot_id)
	print datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), 'Finish deleting snapshot'
