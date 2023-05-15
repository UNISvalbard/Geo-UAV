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

```{admonition} Learn how to fly
:class: warning
In order to collect virtual outcrop data, it's important to have expertise in operating a UAV, or in other words, that you know how to fly. Don't rely on the availability of automated mapping software to do this for you.
```

## Types of UAV

```{admonition} Data source
:class: tip
Most of the pieces of information in this section have been published by Howell et al., 2021.
```

The market offers a wide selection of UAVs, each with different features and price ranges suitable for hobbyists, professionals, and scientific purposes. When it comes to virtual outcrop modelling, multirotors like the DJI Mavic series or DJI Phantom series are ideal for beginners. While fixed wing drones are useful for horizontal outcrops and can cover large areas quickly, they come with a few limitations such as having only a downward-facing camera, being expensive, and requiring mission planning that may not always be suitable for fieldwork.

```{admonition} DJI Mavic Series
:class: note
This module focusses on DJI Mavic Series. However, it is applicable to other brands and multirotor UAVs with small technical differences.
```

To effectively use a UAV for photogrammetric modelling of geological outcrops, there are certain requirements that need to be met. These include:

1. The UAV should have the ability to be piloted manually while providing a live camera feed.
2. The UAV should be stable in windy conditions and have satellite-assisted positioning. Cheaper units that lack these features are only suitable for indoor flying.
3. The UAV should have a range of at least 500 meters, which is the maximum distance for line of sight flying in most countries. The unit should be capable of achieving this comfortably.
4. The camera should be of good quality and have various controls like speed, aperture, etc. The DJI Phantom 4 Pro and Mavic Pro 2 have a 20-megapixel 1-inch sensor that produces excellent results. Good results can also be achieved with slightly smaller sensors like the 12-megapixel sensor on smaller Mavics and older Phantoms.
5. The camera must have a timelapse function (intervalometer) that allows for taking photos at preset intervals (normally 3 to 5 seconds).
6. The camera should be linked to the navigation system so that the UAV's position is recorded when each photo is taken.

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







