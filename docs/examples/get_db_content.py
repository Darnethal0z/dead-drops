from deaddrops.database import DatabaseHelper

helper = DatabaseHelper()

# Get the 20 first entries of the database
db_content = helper.getDatabaseContent(amount=20)

for drop_id, drop_infos in db_content["results"].items():
	print(f"Drop ID {drop_id} ({drop_infos.get('permalink')}) ")
	print(f"  Name : {drop_infos.get('name')}")
	print(f"  Date : {drop_infos.get('date')}")
	print(f"  Location : {drop_infos['location'].get('city')}, {drop_infos['location'].get('country')}")
	print(f"  Size : {drop_infos.get('size')}")
	print(f"  Status : {drop_infos.get('status')}\n")
