Here's the deal. I love motorcycles, I want to buy a motorcycle, maybe a few. But everyone tells me they are dangerous and they have more accidents than regular vehicles.

I can't think of a better way to find out the truth than to analyse the collision data provided by Seattle's Department Of Transportation (SDOT).

You can read more about the two files I'll be working in links below :
1. [Collisions Vehicles] (https://data-seattlecitygis.opendata.arcgis.com/datasets/SeattleCityGIS::sdot-collisions-vehicles/about)
2. [Collisions All year](https://data-seattlecitygis.opendata.arcgis.com/datasets/SeattleCityGIS::sdot-collisions-all-years-2/about)
***

Database tables

Collision | type |
--- | --- |
source | `string` |
type | `string` |
severity | `string` |
vehicle count | `int` |
pedestrian count | `int` |
injuries | `int` |
pedestrian cycle count | `string` |


Vehicle | type |
--- | --- |
type | `string` |
vehicle condition | `string` |
action | `string` |


Location | type |
--- | --- |
type | `string` |
latitude | `int` |
longitude | `int` |
address | `string` |
road surface | `string` |
traffic control | `string` |
posted speed | `string` |


Date | type |
--- | --- |
incident date | `string` |
modified date | `string` |