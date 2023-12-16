Here's the deal. I love motorcycles, I want to buy a motorcycle, maybe a few. But everyone tells me they are dangerous and they have more accidents than regular vehicles.

Since I want one, I will get to the bottom of this. I can't think of a better way to find out the truth than to analyze the collision data provided by the Seattle Department Of Transportation (SDOT).

You can read more about the two files I'll be working in links below :
1. [Collisions Vehicles](https://data-seattlecitygis.opendata.arcgis.com/datasets/SeattleCityGIS::sdot-collisions-vehicles/about)
2. [Collisions All year](https://data-seattlecitygis.opendata.arcgis.com/datasets/SeattleCityGIS::sdot-collisions-all-years-2/about)
***


And then load the data into the following tables
**Collision** table will store all the details about the collision.

dtype | Collision |
--- | --- |
`string` |report number `PK` |
`string` |source |
`string` |collision type |
`string` |severity |
`int` |vehicle count |
`int` |pedestrian count |
`int` |fatalities |
`int` |serious injuries |
`int` |injuries |
`int` |pedestrian cycle count |

The **Vehicle** table will store all details available about the vehicle in question.

dtype | Vehicle |
--- | --- |
`string` |type |
`string` |vehicle condition |
`string` |vehicle action |
`string` |report number `FK` |


The **Location** table will store all details about that location.

dtype | Location |
--- | --- |
`string` |type |
`float` |latitude |
`float` |longitude |
`string` |address |
`string` |road surface |
`string` |traffic control |
`string` |posted speed |
`string` |report number `FK` |


And finally the **Date** table store all the dates related to the event.

dtype | Date |
--- | --- |
`string` |incident date |
`string` |modified date |
`string` |report number `FK` |

