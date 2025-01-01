# sg_postal_code_constituencies

## Objective
To either:
1) create a script that takes a provided postal code and returns a constituiency, or
2) create a lookup table of postal codes mapped to constituiencies.

The end goal is to allow website visitors to find their constituiency by postal code.

Possible approaches:
* 302 redirect, probably based on an uploaded lookup table (PAP does this)
* Simple lookup table and javascript based redirect
* Calculate and map the postal code on each search

## Resources
* [Turf](https://github.com/turfjs/turf): A modular geospatial engine written in JavaScript and TypeScript
* [OneMap API](https://www.onemap.gov.sg/apidocs/): Can return lat-long from postal code
    * [Search API](https://www.onemap.gov.sg/apidocs/search)
* [ELD Election Boundary 2020 dataset](https://data.gov.sg/datasets/d_6077aa5ab73d447b32f451ea224221b6/view)

## Potentially useful
* [StackOverflow: Check if geo-point is inside or outside of polygon](https://stackoverflow.com/questions/43892459/check-if-geo-point-is-inside-or-outside-of-polygon)
* [StackOverflow: Check if Point Is Inside A Polygon](https://stackoverflow.com/questions/22521982/check-if-point-is-inside-a-polygon)
* [Tutorial: JavaScript lookup table](https://www.basedash.com/blog/tutorial-javascript-lookup-table)
