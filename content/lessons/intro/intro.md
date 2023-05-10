# Introduction to Geo-MOD

The Geo-MOD Course is a module that teaches students how to collect and process AUV-based field data for geoscientific use using advanced techniques. The course is designed to be interactive and openly accessible to everyone.

Throughout the course, students will learn how to plan, execute, and process AUV-based acquisition campaigns using structure-from-motion techniques to create 3D and DEM models. The course is divided into six sessions that include a variety of engaging components, such as videos, animations, and in-person training. 

Upon completing the course, students will receive a certificate affirming their ability to independently acquire, process, and disseminate data in a scientific manner.

````{margin}
```{admonition} Data source
:class: note

This course contains bits and pieces from all over the internet, supplemented by in-house knowledge by Peter Betlem and Nil Rodes.
```
````


```{admonition} Certification
:class: tip
The certificate will only be available for the students taking the course in person at The University Centre in Svalbard.
```


## Some useful definitions

Before starting with the technical parts, let's discuss some popular (and not that popular) terms such as "drone", "AUV", "UAS" or "RPA". Which one should we use?
For starters, every UAV is a drone, but not every drone is a UAV. Here's a description of the different phrases you've likely heard to help you understand what each one means and what the difference (if any) there is between them:

**Drone**
While "Drones" make most people think of "an unmanned aircraft that can fly autonomously-that is, without a human in control." It can actually be used to describe a wide variety of vehicles. For example, there are seafaring or land based autonomously vehicles that also count under the given definition of drone.

Of course, the most common usage of the term refers to an aircraft that can be remotely or autonomously guided. Unfortunately, the only thing most experts can agree on with this term is that a drone doesn't have a pilot inside.

**UAV**
A UAV is an Unmanned Aerial Vehicle. They are able to fly remotely such as with a controller or tablet or autonomously. So, is UAV a drone? Basically, it is. The two terms are often used interchangeably. 

However, many professionals in the industry believe UAVs need to have autonomous flight capabilities, whereas drones do not. Therefore, all UAVs are drones but not vice versa. But for now, go ahead and use the phrase you're most comfortable with! 

**UAS**
A UAS or Unmanned Aircraft Systems includes not only the UAV or Drone but also the person on the ground controlling the flight and the system in place that connects both of them. Basically, the UAV is a component of the UAS, since it refers to only the vehicle itself. 

**RPA**
Many pilots prefer the term "Remotely Piloted Aircraft." This is because flying certain types of UAVs require a lot more skill than anything you could buy in a store. Taking control of an RPA requires more than simple handheld controls.




## Creation of a ArcGIS Pro project

````{margin}
```{note}
An excellent albeit bit long guide for QGIS exists on the interwebz.
Those who would like an open and free experience, may try QGIS and follow the tutorial here:
[https://www.qgistutorials.com/en/](https://www.qgistutorials.com/en/)
```
````

To create a new project in ArcGIS Pro, follow these steps:

New, Blank Templates, Map. Define the Name of the new project.
```{admonition} Tip
:class: tip
Ideally the name of the project won't conatin any spaces, dots, or commas.
```
In Location, define the folder path where you want to save the project.
This last step is important to have a good data structure because everything related to your project will be saved there.
Also, select the tick that says *Create a new folder for this project*.

```{figure} assets/1_create_project.gif
:name: 1_create_project


```

### Specify a coordinate system for your project

```{note}
A coordinate (or Spatial) reference systems (CRS) define specific map projections and the transformations that are needed between different systems. A CRS is always composed of a coordinate system and datum component. A coordinate system is a set of mathematical rules that specify how coordinates are to be assigned to points. A datum is a set of parameters that define the position of the origin, the scale, and the orientation of a coordinate system.
Luckily, these are pre-defined by the European Petroleum Survey Group (EPSG) for the most common CRSs in use.
```

In ArcGIS Pro, we can define a vertical coordinate system for a map or scene.
In the Table of Contents right click on the layer or map you want to modify > Properties > Coordinate system.

The coordinate System for Svalbard is: **WGS1984 UTM Zone 33N**.
You can do a quick search by looking for the **EPSG:32633**.

```{figure} assets/2_coordinate_system.gif
:name: 2_coordinate_system


```


#### Change Projected Coordinate System in a layer

We differentiate two common cases for why you would like to change the projection of your layer:

```{admonition} Layer with a wrong projection
:class: tip
Create a new Feature Class > Geoprocessing > Create Feature Class > Only fill “Feature Class Name” > Run >> Geoprocessing > Define Projection Tool > Input Dataset of Feature Class: select the layer with the wrong projection system and Coordinate System: select the layer that has an unknown coordinate system > Run. The layer will match the coordinate characteristics of the project.
```

```{admonition} Layer with an Unknown Projection
:class: tip
Geoprocessing > Define Projection Tool > Input Dataset of Feature Class: Select the layer you want to change the projection system and
Coordinate System: Select a layer that has already the projection you want > Run.
```


### Adding data

#### Importing data

Map > Add data > Go to the folder where you saved the data you want to import.
Once you add it, it will appear as a new layer in the Table of Contents.

```{figure} assets/3_add_data.gif
:name: 3_add_data

```

```{admonition} Added the data but don’t know where it is? Here is some magic...
:class: tip
1. Click on View and “Catalog pane”.
2. The ArcGIS servers you have added are now visible on the catalog pane.
3. You can drag the data layers to your map.

```

#### Importing GPX tracks

ArcGIS Pro uses a Georeferencing tool to import GPX tracks.
Click on the Tools icon in the Analysis tab to open up the Geoprocessing panel.
Then search for *GPX to Features*.

```{figure} assets/4_import_gpx.gif
:name: 4_import_gpx

Select the GPX file as *Input to GPX File*, give the *Output Feature class* a distinguishable name, and click RUN to add the GPS track to the map.
```


#### Importing a digital terrain model

Go to Map and click on the Add Data icon, selecting Data.
Then browse to the folder where you have your DTM and select it.
Once again, go to the Tools option in Analysis to open up the Geoprocessing toolbox.
Set the imported DEM layer as the *Input Raster*, fill out targeted output and the measurements, and then click on *Run* to generate a slope.

````{margin}
```{admonition} Zenodo
:class: tip

Zenodo is a general-purpose open-access repository. It allows researchers to deposit research papers, data sets, research software...
All the DTM in svalbox.no are uploaded there to assure free access to the data.
```
````

````{admonition} Note
:class: note
You can download all the information related to the Digital Terrain Models uploaded in [Svalbox](http://www.svalbox.no/outcrops/) from the [Zenodo](https://zenodo.org/) database.

The files needed to plot the models in ArcGIS Pro are in the *export.zip* folder.

```{figure} assets/download_zenodo.gif
:name: download_zenodo

Click on the DOI link of the model. A new tab will open linking to the [Zenodo](https://zenodo.org/) database, from where you can download all the data.
```
````

##### Creating slopes, hillshades and contours

- Hillshade: Imagery > Raster Functions > Surface > Hillshade > Choose the layer you want to do the hillshade from > Define the vertical exaggeration > Create New Layer.
- Contour: Imagery > Raster Functions > Surface > Contour > Choose the layer you want to do the contours from > Define the contour separation > Create New Layer.
- You can do this with lots of other tools: Aspect, Slope, Shaded relief, Curvature, etc.

(section:gis:new_features)=
#### Adding new features

**Option 1**
: Open Catalog > Right Click on the geodatabase file (.gdb) > New > Feature Class > Define a name and the type of feature you want to create.
Once it is created, drag the new .gdb to the Table of Contents.
Select the new layer > Edit > Create > Define the feature you want to work with.

```{figure} assets/5.1_new_features.gif
:name: 5.1_new_features


```

**Option 2**
: Geoprocessing Pane > Search for Create Feature Class.
Define all the parameters.
The Name cannot contain Spaces, points, or commas.
Make sure to select the Coordinate System of the Current Map.
Through this step, the New Feature layer will automatically appear in the table of contents.

```{figure} assets/5.2_new_features.gif
:name: 5.2_new_features
```

After adding the Feature Class, you may add additional fields to it, important to capture descriptions, dates and more all within the same point.
You can do so by right-clicking your newly created layer, and proceeding with the *Attribute Table*.
A newly created layer usually comes in empty, with just the *OBJECTID* and *Shape* columns created.
Before doing anything else, click the *Field: Add* button to open the column editor and add additional fields as is done in {numref}`fig:gis:add_new_fields`.

```{figure} assets/add_new_fields.gif
:name: fig:gis:add_new_fields


```

Once done, points can then be added and changed as shown in {numref}`fig:gis:edit_attributes`.
Here it is important to click both *Apply* in the *Attributes window* and click the *Save* button in the *Edit* panel after everything has been input.
Otherwise you may risk losing all your newly added data points! :(

```{figure} assets/edit_attributes.gif
:name: fig:gis:edit_attributes


```

### Georeference image/raster

Import an image you want to georeference in the map in JPG or PNG format.
Then go to Imagery > Georeference > Add control points.
Click an exact point on the image and then click this point in the map before saving the changes.

```{figure} assets/6_figure_georeference.gif
:name: 6_figure_georeference


```

### Connecting to ArcGIS Servers

Insert > Connections > Add ArcGIS Server

```{figure} assets/7_server_connection.gif
:name: 7_server_connection


```
#### NPI server

While Npolar provides a very useful service through [toposvalbard](https://toposvalbard.npolar.no/) and [svalbardkartet](https://geokart.npolar.no/Html5Viewer/index.html?viewer=Svalbardkartet), these have limited abilities for interacting with the data.
As such, it may be wise to import the toposvalbard data straight into ArcGIS by going to the Insert tab and click on the Connections icon.

Then select *New ArcGIS Server*, and fill out the Server URL as below:

```url
https://geodata.npolar.no/arcgis/rest/services/
```

Once connected, drag over the **NP_Basiskart_Svalbard_WMTS_32633** onto your map.

#### Svalbox server

Although you could probably manually check the [svalbox](www.svalbox.no/map) webpage and check which outcrops are closest, easier ways exist.
Let’s proceed by connecting directly to the Svalbox ArcGIS server. Go to the Connections icon. Then select New ArcGIS Server, and fill out the Server URL as below:

```url
http://svalbox.unis.no/arcgis/rest/services/
```

Then you should be able to find the Svalbox data in the Catalog panel, and you can drag and drop different data sets straight into your map.

```{figure} assets/server.png
:name: server


```

(section:gis:360image-to-frame)=
##### Harvesting metadata: the 360image to iframe example

Once the Svalbox ArcGIS server has been added to your project, drag and drop the images360 layer into your map.
The location of 360 images should now be visible on your map.
However, when clicking on them, you will not be shown the 360 image in the way it is served to you on [www.svalbox.no/map](www.svalbox.no/map).
Instead, a popup featuring all the image's metadata will show up.
Here, the most important is to copy the svalbox_i0wpurl link - this link can be pasted into the [Pannellum panorama url link box](https://pannellum.org/documentation/overview/tutorial/) to generate a 360 view of the image.  


### Edit layer characteristics

Depending on the layer characteristics that we want to modify we will go to:

- Appearance tab
- Symbology: Right click on the feature layer in the Control Pane > Symbology

### Exporting a map

Insert tab > New Layout > Generate the frame you want for your map.

Map > Activate Map Frame to move and edit the map. Add Legend, North Arrow and Scale bar.

- Export map: Share > Export Layout. Export Raster in -PNG and Vectors in -EPS. It is important to select *Clip to Graphics Extent*.

```{figure} assets/8_new_layout.gif
:name: 8_new_layout


```
