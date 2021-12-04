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
### HTML
```sh
 <!doctype html>
    <head>
    </head>
    <body>
        <table border = "1" cellpadding = "5" cellspacing = "5">
             <tr>
                <th>Name and surname</th>
                <th>Profession</th>
                <th>Salary</th>
             </tr>
             <tr>
                <td>Mobolaji Abdsalam</td>
                <td>Elect Technician</td>
                <td>55,000</td>
             </tr>
             <tr>
                <td>Ibraheem Abdsalam</td>
                <td>Software Engineer</td>
                <td>700,000</td>
             </tr>
             <tr>
                <td>IBM Abdsalam</td>
                <td>Elect Engineer</td>
                <td>500, 000</td>
             </tr>
             <tr>
                <td>Mobolaji Abdsalam</td>
                <td>Elect. Technician</td>
                <td>55, 000</td>
             </tr>
             <tr>
                <td>Ibraheem Abdsalam</td>
                <td>Software Engineer</td>
                <td>700, 000</td>
             </tr>
             <tr>
                <td>IBM Abdsalam</td>
                <td>Elect Engineer</td>
                <td>500, 000</td>
             </tr>
        </table>
    </body>
</html>
```
### HTML file
```sh
import pyT.Table as table
json = table.HTML('./tab.html', n=0)# n specifies which table to be parsed and rendered.
n = 0 => First table on the page.
n = 1 => Second table on the page.
html_table = Table(*json)
html_table.draw()
```
### Output
```sh
+------------------+------------------+------------------+
| Name and surname |    Profession    |      Salary      |
+------------------+------------------+------------------+
|Mobolaji Abdsalam | Elect Technician |      55,000      |
+------------------+------------------+------------------+
|Ibraheem Abdsalam |Software Engineer |     700,000      |
+------------------+------------------+------------------+
|   IBM Abdsalam   |  Elect Engineer  |     500, 000     |
+------------------+------------------+------------------+
|Mobolaji Abdsalam |Elect. Technician |     55, 000      |
+------------------+------------------+------------------+
|Ibraheem Abdsalam |Software Engineer |     700, 000     |
+------------------+------------------+------------------+
|   IBM Abdsalam   |  Elect Engineer  |     500, 000     |
+------------------+------------------+------------------+
```
