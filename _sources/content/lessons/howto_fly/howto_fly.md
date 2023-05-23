# How to fly a multirotor UAV
Flying a multirotor UAV for the first time can be challenging for anyone. There is a learning curve to it. The goal of this section is to help you fly your UAV safely and efficiently during your acquisition campaign.
When creating your flight plan, you will need to decide if you want to fly manually or plan an automatic flight.

```{admonition} Fly manual in Svalbard
:class: warning
In Svalbard we highly recommend flying your UAV manually. There are multiple reasons for this:

1. Low terrain model resolution. The Digital Elevation Model (DEM) in Svalbard has a maximum resolution of tens of meters.
2. Changing environment. Glaciers, morraines, coastal fjord's morphology significatively altering every year. This means that the base map in your controller may not include all the morphological changes that have taken place since the time of your flight. If you plan your flight solely based on this map, there is a high risk of crashing your UAV into a newly formed and changed morphological feature.
```

## Manual
As we discussed, manual flight is the preferred method in Svalbard.

When operating the UAV, it is advised to keep your focus on the controller screen. Initially, you may be inclined to look at the UAV in flight. However, please note that the controls will be reversed depending on whether the drone is facing towards you or away from you. To avoid confusion, utilizing a First Person View (FPV) allows for better visualization of the UAV's movements, rather than its orientation towards you, resulting in a smoother flight.

### UAV controls
As you continue to fly for a few hours, you will become more familiar with how the controls work together to provide a complete flying experience. When you first begin, it's best to gently push the sticks to create small movements. As you become more confident, you can increase the intensity of your movements for sharper turns and maneuvers.

There are four main drone controls:
- Roll: Roll moves your drone left or right. It's done by pushing the right stick on your controller to the left or to the right. It's called "roll" because it literally rolls the drone.
- Pitch: Pitch is done by pushing the right stick on your controller forwards or backward. This will tilt the drone, resulting in forwards or backward movement.
- Yaw: Done by pushing the left stick to the left or to the right. Rotates the drone left or right. Points the front of the copter in different directions and helps with changing directions while flying.
- Throttle: Throttle gives the propellers on your drone enough power to get airborne. When flying, you will have the throttle engaged constantly. To engage the throttle, push the left stick forward. To disengage, pull it backwards.

### Position of the antennas
For optimal signal reception, ensure that the remote controller's antennas are directed towards the UAV.
In case of weak reception, try rotating the antennas 90 degrees.

### How to take-off
To launch your UAV, the only control you need to use is the throttle. We suggest gradually pushing up the throttle (left stick) multiple times until you feel at ease with its sensitivity. When you are comfortable, you can increase the throttle to lift the multirotor off the ground.

```{admonition} Flying DJI UAV multirotor
:class: note
To take-off with DJI UAVs you need to pull both sticks towards the center. This will start the propellers.
DJI UAVs are programmed so that you don't need to push the throttle continuously. In other words, if you want to hover the UAV in mid-air, you simply need to leave the throttle.
```

### How to land your UAV
To land the UAV you need to cut back throttle slowly. It is important that you practice and get comfortable landing gently to avoid damage to the UAV.

```{admonition} Flying DJI UAV multirotor
:class: note
When landing a DJI UAV, simply pull the throttle towards you. These drones come equipped with sensors that regulate their distance from the ground. As the drone approaches a height of 20 cm from the ground, it will stop automatically to prevent any collisions. If you wish to land the drone directly on a specific spot below its position, you can pull the throttle to the maximum and the drone will land automatically.
```

#### Return to home (RTH)
The DJI Return to Home feature ensures the safe landing of your drone by bringing it back to either a pre-selected home point or a safe landing spot. In the event of a communication loss between the controller and the drone, the feature will automatically activate, causing the UAV to fly up to a predetermined height before returning to the home point. To avoid any obstacles on the way home, it's crucial to set the height high enough. It's recommended to set the height each time instead of setting it to a very high number and forgetting about it, as running out of battery on the way home could cause a forced landing.

```{admonition} User recommendations
:class: warning
It is advisable to avoid using the Return to Home feature to land your UAV. As per regulations, pilots with an A1/A3 license certificate have to fly within line of sight, and it is advisable to land the UAV manually for better control.
```

### Move left/right and forward/backward
To fly a UAV left, right, forwards, and backwards, you will need to hold the throttle at a steady rate (do not touch it when using DJI UAVs) to keep it airborne. You will then use the right stick to maneuver the drone in the direction you want it to go.

### How to rotate the UAV
To rotate the UAV you will need to move the throttle stick right to move clockwise and left to move anti-clockwise. You can rotate the UAV 360 degrees.

## Automatic
```{admonition} Under construction!
:class: warning
The Geo-UAV module of on how automatically fly a multirotor UAV is still under construction.
```
Many apps and survey design software are available to automate surveys. They allow for planning the survey in the lab and executing it in the field with a simple command, maximizing flight efficiency, reducing pilot and observer workloads and in some situations, minimizing equipment risk. These tools work best for mapping planar surfaces or simple structures like buildings.

```{admonition} Explore more
:class: tip

[PIX4D](https://www.pix4d.com/product/pix4dmapper-photogrammetry-software/) is a photogrammetry software to help you plan and capture your UAV mapping survey.
```

