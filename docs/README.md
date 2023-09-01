# `deaddrops` documentation
---

See the `examples` folder to get some ready-to-run examples stubs.

## Interact with the dead drops database

### Declaration

```
class DatabaseHelper()
```

*Package* : `deaddrops.database`

*Parameters*: 

- None

### Methods

```
getDatabaseStatistics() -> dict
```

> Get the actual database statistics

*Parameters*: 

- None

*Return value*:

- A dictionary representing the actual database statistics : 

```
{
	"total_usb_drops": TOTAL_USB_DROPS,
	"total_usb_storage": TOTAL_USB_STORAGE
}
```

- `TOTAL_USB_DROPS` : The total amount of dead drops recorded
- `TOTAL_USB_STORAGE` : The total storage amount provided by dead drops recorded

---

```
getDatabaseContent(location: str = "", max_distance: int = 5000, amount: int = 99999)
```

> Get the actual database content

*Parameters* : 

- `location` : Specific coordinates to search around. Can be tuned with the `max_distance` parameter
- `max_distance` : The maximum distance to search around, in meters
- `amount` : The amount of entries to retrieve

*Return value*:

- A dictionary representing the search result : 

```
{
	"results": {
		DROP_ID: {
			"date": DATE,
			"name": NAME,
			"permalink": PERMALINK,
			"location": {
				"street": STREET,
				"city": CITY,
				"state": STATE,
				"country": COUNTRY
			}
			"size": SIZE,
			"status": STATUS
		}
		...
	}
}
```

- `DROP_ID` : The dead drop entry ID
- `DATE` : The dead drop creation date
- `NAME` : The dead drop name
- `PERMALINK` : The dead drop permalink
- `STREET` : The indicated street
- `CITY` : The indicated city
- `STATE` : The indicated state
- `COUNTRY` : The indicated country
- `SIZE` : The dead drop size, in Gb
- `STATUS` : The actual dead drop status

*Additional note* : The parameter `location` will be geocoded into coordinates on the deaddrops.com server side. It is a search by city and country.

---

```
searchTerm(term: str, case_sensitive: bool = False)
```

> Search for a specific term in the dead drop database content

*Parameters*:

- `term` : The term to search
- `case_sensitive` : Indicate a case sensitive search or not

*Return value*: 

- The corresponding entries as a dictionary : 

```
{
	DROP_ID: {
		"date": DATE,
		"name": NAME,
		"permalink": PERMALINK,
		"location": {
			"street": STREET,
			"city": CITY,
			"state": STATE,
			"country": COUNTRY
		}
		"size": SIZE,
		"status": STATUS
	}
	...
}
```

- `DROP_ID` : The dead drop entry ID
- `DATE` : The dead drop creation date
- `NAME` : The dead drop name
- `PERMALINK` : The dead drop permalink
- `STREET` : The indicated street
- `CITY` : The indicated city
- `STATE` : The indicated state
- `COUNTRY` : The indicated country
- `SIZE` : The dead drop size, in Gb
- `STATUS` : The actual dead drop status

## Submit a dead drop

### Constants

| Constant           | Value | Description                                         |
| ------------------ | ----- | --------------------------------------------------- |
| TYPE_USB           | 1     | Specify an USB dead drop                            |
| TYPE_WIRELESS      | 2     | Specify a wireless drop                             |
| TYPE_LIVE          | 3     | Specify a live dea drop                             |
| TYPE_OTHER         | 9     | Specify an another kind of dead drop                |
| STATUS_BDSG        | 0     | Set the dead drop status as broken/dead/stolen/gone |
| STATUS_UNCONFIRMED | 1     | Set the dead drop status as unconfirmed             |
| STATUS_WORKING     | 2     | Set the dead drop status as working                 |

### Declaration

```
class SubmitHelper()
```

*Package* : `deaddrops.submit`

*Parameters*: 

- None

### Methods

```
setGeneralInformations(self, name: str, size: int, d_type: int) -> None
```

> Set the general dead drop informations

*Parameters*:

- `name` : The name of the dead drop
- `size` : The storage size of the dead drop
- `d_type`  : The dead drop type. Can be :
	- `TYPE_USB` : The dead drop is a USB
	- `TYPE_WIRELESS` : The dead drop is a wireless drop
	- `TYPE_LIVE` : The dead drop is a live drop
	- `TYPE_OTHER` : The dead drop is something unspecified

*Return value*: 

- None

---

```
setLocationInformations(
    alpha2_country: str,
    state: str = "",
    city: str = "",
    zipcode: str = "",
    address: str = "",
    latitude: str = "",
    longitude: str = ""
) -> None
```

> Set the location dead drop informations

*Parameters*:

- `alpha2_country` : The dead drop location country, in alpha2 format : https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2
- `state` : The dead drop location state
- `city` : The dead drop location city
- `zipcode` : The dead drop location zipcode
- `address` : The dead drop location address
- `latitude` : The dead drop location coordinates latitude
- `longitude` : The dead drop location coordinates longitude

*Return value*: 

- None

**NOTE** : The `latitude` and `longitude` format must be normalized coordinates format

---

```
setDescriptionInformations(
    overview_img_file_path: str = None,
    medium_img_file_path: str = None,
    closeup_img_file_path: str = None,
    about: str = "",
) -> None
```

> Set the description dead drop informations

*Parameters*:

- `overview_img_file_path` : The dead drop overview photo file path.
- `medium_img_file_path` : The dead drop medium view photo file path.
- `closeup_img_file_path` : The dead drop closeup view photo file path.
- `about` : The dead drop description


**NOTE** : Photo images must be less than 1 Mb and smaller than 300x300px

---

```
submitDeadDrop(status: int = STATUS_WORKING) -> int | None
```

> Submit a dead drop on the official website

*Parameters*:

- `status` : The status to set on the dead drop permalink page. Can be :
	- `STATUS_BDSG`: Specify the dead drop as broken/dead/stolen/gone
	- `STATUS_UNCONFIRMED`: Specify the dead drop as unconfirmed
	- `STATUS_WORKING`: Specify the dead drop as working

*Return value*: 

- The created dead drop permalink page ID if exists, `None` otherwise