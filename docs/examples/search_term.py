# Stub that search for a specific term in the DeadDrops database

from deaddrops.database import DatabaseHelper

helper = DatabaseHelper()

# Search in all the database content for the value "Toronto"
# The parameter 'case_sensitive' can be set to True to make a case sensitive search
search_result = helper.searchTerm("Toronto")

for drop_id, drop_infos in search_result.items():
    print(f"Drop ID {drop_id} ({drop_infos.get('permalink')}) ")
    print(f"  Name : {drop_infos.get('name')}")
    print(f"  Date : {drop_infos.get('date')}")
    print(
        f"  Location : {drop_infos['location'].get('city')}, {drop_infos['location'].get('country')}"
    )
    print(f"  Size : {drop_infos.get('size')}")
    print(f"  Status : {drop_infos.get('status')}\n")
