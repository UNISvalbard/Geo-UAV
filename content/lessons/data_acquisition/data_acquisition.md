# Data acquisition
Data acquisition is the first stage of UAV-based photogrammetry. It consists in aerial photography with a specific purpose and subject. In order to collect good data, we must keep to best practices of capturing photos for photogrammetry.

When acquiring data in the field, it is very important to take into account the requirements of the acquisition. As in any project, there is a relationship between time, quality and costs. Time is the available time to acquire the data, cost represents the amount of resources needed and quality represents the resolution and fit-to-purpose that we want for our DEM or 3D model. Let's exemplify it. If you want a very high resolution model, you will have to spend a lot of time acquiring good-quality data and you will need many resources such as a high-quality camera and UAV, batteries for your UAV and controller, images in you memmory card, etc. If you have very little time to properly acquire data, the quality of the model will be very poor unless you use extremely expensive resources such as multiple multirotors flying at the same time, or predefined flights with a vertical take-off and landing UAV (VTOL) containing a very high resolution camera. If you are limited by the resources, let's say, by only having one battery for your UAV, the time you will be able to spend acquiring data will be low, and you will either not cover the entire area that you want, or collect general images ending up having a low-resolution model.
Therefore, when acquiring data in the field, it is important that you evaluate the resolution of the model you want to get, the resources you have, the time you can spend flying to find the balance to get the best data as possible.

```{figure} content\lessons\data_acquisition\assets/triangle.png
:name: triangle

The principle of the triangle suggests that of the three points, you can only have two at a time, not three.
```

The data acquisition stage also contains processes during which we collect additional data, for example, [Ground Control Points (GCPs)](https://unisvalbard.github.io/Geo-SfM/content/lessons/l2/gcps.html).







The data that we will acquire for processing structure-from-motion are images.

DJI UAV come with a transparent cover to protect the camera from scratches. Make sure to remove that cover before starting up the UAV. This will help acquiring a better image quality and will allow the gimbal to move freely.
