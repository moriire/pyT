# pyT
PyT is a a  command line tool and as well a library for visualising various data formats like:
- JSON
- HTML Table
- CSV
- XML, etc.
## Pros
- Print table of any size without distortions.
- Support multiple file formats.
- Better presentation of various data structures, types. 

## Usage
### JSON data
```sh

{
  "squadName": "Super hero squad",
  "homeTown": "Metro City",
  "formed": 2016,
  "secretBase": "Super tower",
  "active": true,
  "members": [
    {
      "name": "Molecule Man",
      "age": 29,
      "secretIdentity": "Dan Jukes",
      "powers": "Turning tiny"
    },
    {
      "name": "Madame Uppercut",
      "age": 39,
      "secretIdentity": "Jane Wilson",
      "powers": "Million punch"
    },
    {
      "name": "Eternal Flame",
      "age": 1000000,
      "secretIdentity": "Unknown",
      "powers": "Immortality"
    }
  ]
}
```
```sh
import pyT.Table as table
table = Table(*item["members"])
json_table.draw()
```
### JSON file
```sh
import pyT.Table as table
json = table.JSON('./tab.json', "members")
json_table = Table(*json)
json_table.draw()
```
### Output
```sh
+----------------+----------------+----------------+----------------+
|      name      |      age       | secretIdentity |     powers     |
+----------------+----------------+----------------+----------------+
|  Molecule Man  |       29       |   Dan Jukes    |  Turning tiny  |
+----------------+----------------+----------------+----------------+
|Madame Uppercut |       39       |  Jane Wilson   | Million punch  |
+----------------+----------------+----------------+----------------+
| Eternal Flame  |    1000000     |    Unknown     |  Immortality   |
+----------------+----------------+----------------+----------------+
```
