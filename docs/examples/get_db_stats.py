# Fetch actual DeadDrops database statistics and print them

from deaddrops.database import DatabaseHelper

helper = DatabaseHelper()
db_stats_dict = helper.getDatabaseStatistics()

print("Actual database statistics : ")
print(f"  Total USB drops : {db_stats_dict.get('total_usb_drops')}")
print(f"  Total USB storage : {db_stats_dict.get('total_usb_storage')}\n")
