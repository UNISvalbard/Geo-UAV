# Data acquisition
The initial phase of UAV-based photogrammetry is data acquisition, which involves capturing aerial photographs with a specific objective and subject. To gather high-quality data, it is crucial to adhere to best practices when taking photos for photogrammetry.

When acquiring data in the field, it's crucial to consider the requirements for acquisition. Like any project, there's a connection between time, quality, and costs. Time refers to the available period for data collection, cost represents the necessary resources, and quality represents the resolution and fit-to-purpose that we want for our DEM or 3D model.

Let's exemplify it. If you want a very high-resolution model of an outcrop, you will have to spend significant time acquiring good-quality data, and you will need many resources such as a high-quality camera and UAV, batteries for your UAV and controller, images in your memory card, etc. Suppose you have very little time to properly acquire data. In that case, the quality of the model will be very poor unless you use extremely expensive resources such as multiple multirotors flying simultaneously or predefined flights with a vertical take-off and landing (VTOL) UAV containing a very high-resolution camera. If you are limited by the resources, let's say, by only having one battery for your UAV, the time you will be able to spend acquiring data will be low, and you will either not cover the entire area that you want or collect general images ending up having a low-resolution model.

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
Most of the pieces of information in this section have been published by {cite:t}`howell2021acquisition`.
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

## Choice of outcrop
To be a valuable resource for studying, an ideal outcrop should be geologically interesting.Virtual outcrops can be quite vast and include overhangs and narrow canyons. When flying a UAV in these environments, it is essential to be extremely careful not to crash your UAV against the cliffs. Larger outcrops are typically flown in segments and pieced together, either when the models are built or can be collected as separate models and combined later.

For those who are new to acquisition campaigns, it is recommended to start with a small and compact outcrop for the first flights and gradually work up to more challenging locations. A reasonable size to begin with is around 200-300 meters long and up to 30 meters high. This way, you can always fly within line of sight and never exceed 120 meters in height.

```{admonition} Safety first!
:class: warning
Safety is crucial when using a UAV, so it is essential to ensure that the outcrop can be flown safely.
```

## Survey design
When planning to collect a virtual outcrop, it is important to ensure that it is legally and safely feasible (see [SESSION 1 - UAV flight regulations](https://unisvalbard.github.io/Geo-UAV/content/lessons/regulations/regulations.html) and [SESSION 2  - UAV pre-flight check list](https://unisvalbard.github.io/Geo-UAV/content/lessons/check_list/preflight_checklist.html)).
The next step is to design the survey, which can be done either in the field or in the lab. The purpose of the data being collected will determine the size of the area covered and the expected resolution of the virtual outcrop. 

#### Digital outcrop resolution
The resolution of the virtual outcrop is dependent on the camera's sensor resolution and the proximity of the photographs to the cliff. 

For instance, DJI Mavic Series or DJI Phantom Series cameras have a 94 degree lens equivalent to 20mm on a standard SLR. Therefore, the height of the image in landscape format is roughly equal to the distance of the camera from the cliffs. 

This means that as a rule of thumb, if you want to obtain a resolution of less than 1 cm per pixel, photographs should be taken at a distance of approximately 30 meters from the outcrop.

```{admonition} GSD Calculator
:class: tip
To estimate outcrop resolution, you can use the online app [GSD Calculator](https://www.propelleraero.com/gsd-calculator/). However, this estimate is only a guide since the surface may not be completely flat, making it difficult to maintain a consistent distance and causing the GSD to vary based on the terrain complexity.
```

#### Light and shadows
When planning your UAV acquisition survey, it is crucial to consider outcrop orientation and lighting. Bad light on your pictures will require strong post-processing and likely result in a bad model.

Smooth outcrops in direct sunlight will produce excellent results, but rough outcrops and harsh lighting can create shadows in the model. 

To get the best surveying results, it's recommended to do so on a bright, overcast day with even lighting. This helps to minimize shadows and provide ample light for your outcrop. Contrary to popular belief, a sunny day with clear blue skies is not ideal for surveying. The strong sunlight can create excessive shadows, which may cause issues with camera exposure and focus. This can lead to issues like flare and details being obscured by shadow, especially when the sun is directly behind or above the cliffs.

Although it may be necessary to collect data in these conditions, it is crucial to avoid them whenever possible by planning ahead. If time and weather permit, it would be beneficial to collect data at different times of day to optimize lighting.


## Flight pattern




```{figure} assets/howelletal1.png
:name: howelletal1

Figure published by {cite:t}`howell2021acquisition`. Fly three transects to ensure complete coverage of the cliff section.
```



## Literature

Pargiela et al., 2023. Optimising UAV Data Acquisition and Processing for Photogrammetry: A Review. https://doi.org/10.7494/geom.2023.17.3.29







