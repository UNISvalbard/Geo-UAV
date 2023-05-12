# Data acquisition
The initial phase of UAV-based photogrammetry is data acquisition, which involves capturing aerial photographs with a specific objective and subject. To gather high-quality data, it is crucial to adhere to best practices when taking photos for photogrammetry.

When acquiring data in the field, it's crucial to consider the requirements for acquisition. Like any project, there's a connection between time, quality, and costs. Time refers to the available period for data collection, cost represents the necessary resources, and quality represents the resolution and fit-to-purpose that we want for our DEM or 3D model.

Let's exemplify it. If you want a very high-resolution model, you will have to spend significant time acquiring good-quality data, and you will need many resources such as a high-quality camera and UAV, batteries for your UAV and controller, images in your memory card, etc. Suppose you have very little time to properly acquire data. In that case, the quality of the model will be very poor unless you use extremely expensive resources such as multiple multirotors flying simultaneously or predefined flights with a vertical take-off and landing (VTOL) UAV containing a very high-resolution camera. If you are limited by the resources, let's say, by only having one battery for your UAV, the time you will be able to spend acquiring data will be low, and you will either not cover the entire area that you want or collect general images ending up having a low-resolution model.

Therefore, when collecting data in the field, it's vital to assess the resolution you need, the resources you have, and the time you can invest in flying to achieve the best possible data.

```{figure} assets/triangle.png
:name: triangle

The principle of the triangle suggests that of the three points, you can only have two at a time, not three.
```

The data acquisition stage also contains processes during which we collect additional data, for example, [Ground Control Points (GCPs)](https://unisvalbard.github.io/Geo-SfM/content/lessons/l2/gcps.html).

## Types of UAV

```{admonition} Data source
:class: tip
Most of the pieces of information in this section have been published by Howell et al., 2021.
```

There is a wide range of UAVs available on the market, with a spectrum of features and pricings covering hobbyists through to professional and scientific niches. Whilst high end UAVs which can carry full-frame single lens reflex (SLR) cameras may be necessary in certain cases, most people starting out in virtual outcrop modelling will probably do so with multirotors in the spectum of the DJI Mavic series or DJI Phantom series (Howell et al., 2021).

Fixed wing drones have also been used to good effect in some cases with horizontal outcrops and they have the advantage of covering large areas rapidly. However, they are limited by having only a nadir (down-facing) camera, are commonly expensive and require mission planning and execution which is not always ideal for fieldwork (Howell et al., 2021). 

```{admonition} DJI Mavic Series
:class: note
This module focusses on DJI Mavic Series. However, it is applicable to other brands and multirotor UAVs with small technical differences.
```

The basic requirements for a UAV for photogrammetric modelling of geological outcrops are:
1. The UAV can be piloted manually with a live camera feed.
2. The UAV should be stable in the wind and have satellite (e.g. Global Positioning System; GPS) assisted positioning -some much cheaper units are mainly suitable for flying indoors and lack this.
3. The UAV should have a range of at least 500 m. The max distance for line of sight flying in most countries is 500 m, but the unit should be able to achieve this comfortably. 
4. The camera should be of good quality with a range of controls (speed, aperture, etc). The DJI Phantom 4 Pro and Mavic Pro 2 havea 20mb 1-inch sensor that produces excellent results. Good results can also be obtained from the slightly smaller, 12mb sensor on the smaller Mavics and older Phantoms. 
5. The camera needs a timelapse function (intervalometer) which allows you to take photos at preset intervals (normally 3 to 5 seconds). 
6. The camera needs to be linked to the navigation system, such that the position of the UAV is recorded when each photo is taken.

### Limitations of UAV systems

## Types of Cameras

### Shutter used

### Camera calibration

## Flight pattern




```{figure} assets/howelletal1.png
:name: howelletal1

Figure published by Howell et al., 2021. Fly three transects to ensure complete coverage of the cliff section.
```



## Literature
Howell et al., 2021. Acquisition of Data for Building Photogrammetric Virtual Outcrop Modelsfor the Geosciences using Remotely Piloted Vehicles (UAVs). https://doi.org/10.31223/X54914

Pargiela et al., 2023. Optimising UAV Data Acquisition and Processing for Photogrammetry: A Review. https://doi.org/10.7494/geom.2023.17.3.29







