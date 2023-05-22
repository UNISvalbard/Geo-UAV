# UAV flight regulations
The flying regulations in the European Union are established by EASA ([European Union Aviation Safety Agency](https://www.easa.europa.eu/en)). The main goal of EASA is to establish uniform safety standards for civil aviation operations across all Member States. They achieve this by creating common rules that apply to all states. To standardize regulations for Unmanned Aircraft Systems (UAS), they have developed Regulations (EU) 2019/947 and (EU) 2019/945.

As a member state of EASA, Norway adheres to the same safety standards and regulations as the rest of the EU member states.

````{admonition} Data source
:class: warning
This is a compilation of the standarised rules published by [European Union Aviation Safety Agency](https://www.easa.europa.eu/en/light/topics/drones).

```{figure} assets/easa.png
:name: easa
:class: m-auto
:width: 200px
:target: https://www.easa.europa.eu/en
```
````

## UAV operation categories
- OPEN: Low risk operation. No need of authorisation nor declaration.
- SPECIFIC: Higher risk. Need to declare the Standard Scenarios (STS) or authorization.
- CERTIFIED: High risk. Similar regulations to manned aviation.

```{figure} assets/dronecategories.png
:name: dronecategories

A visual representation of the adopted three categories of UAV operations. Figure published by Konert et al., 2020.
```


### Open Category
The open category has three subcategories: A1, A2 and A3. In A1 you can fly small UAVs, which can be used above and near individuals. In A2 you can fly medium-sized UAVs with a defined distance from individuals and crowds. Larger UAVs in the open category are flown in subcategory A3 and away from people, buildings and recreational areas.

For all three flight subcategories in the **open category**, there are specific general flight conditions that apply. These conditions are:
1. The remote pilot is required to maintain visual line of sight (**VLOS**) while flying, unless they are using follow me mode or an unmanned aircraft observer. In those cases, they may use first-person vision devices (FPV), also known as First-Person-View.

2. It is not permitted to fly a drone at a height exceeding **120 meters** from the nearest point on the surface. However, if the flight area is specified by the authorities, the maximum allowable height may be lower than 120 meters.
```{admonition} Case example
:class: note
If a UAV is flying within 50 m, measured horizontally, of an artificial obstacle (such as a building) higher than 105 m in height, the maximum height of the UAS operation may be increased up to 15 m above the height of the obstacle, accounting for a total height of 120 m.
```

3. If there is a conflict or encounter with a manned aircraft, the remote pilot must lower the flight height, make evasive maneuvers to avoid a possible collision, and land as quickly as possible.
```{admonition} Note
:class: note
In any case, the remote pilot must always interrupt the flight with UAS when its continuation could pose a risk to the manned aircraft.
```
 
4. It is prohibited to fly over areas where there are large groups of people, and it is necessary to keep a safe distance from individuals who are not involved in the operation.
```{admonition} Note
:class: note
The "safe distance" will depend on the subcategory of the operation. As a general rule, the heavier the unmanned aircraft, the farther it should be flown from nonparticipants to make the operation safer
```

5. If needed, an observer on an unmanned aircraft can assist the pilot. However, the observer must never extend the flight range of the UAS beyond the pilot's visual range. The observer will stand next to the pilot and aid in:
A. Maintaining a safe distance from obstacles and alert the pilot if the distance is reduced. 
B. Help the pilot stay aware of the surroundings and potential hazards.

**In any case, the remote pilot is always ultimately responsible for maintaining the safety of the UAS operation**.

6. In the open category, it is prohibited to transport dangerous goods with the UAS or to drop or project any material or object.


#### Subcategory A1
In addition to the general conditions described for the "open" category, in subcategory A1 the following condition
must be met:

- Flight over non-participants is allowed, without infringing the privacy and data protection of these people, except for operations with class C1 UAS with which it  ill not be possible to fly over non-participants.
```{admonition} Important
:class: tip
The flight ban on concentrations of people is maintained!
```

```{figure} assets/uav-a1.jpg
:name: uav-a1

Open category A1 flight regulations. Source: Direction de l'Aviation Civile Luxembourg.
```

#### Subcategory A2
In subcategory A2 the following condition must be met:
- Flight is permitted at a safe horizontal distance of at least 30 m from non-participants, which may be reduced to a minimum of 5 m when the low speed mode function is activated, and the height will be reduced in the same proportion as the safe horizontal distance to non-participants is reduced (1:1 rule) 
```{admonition} Important
:class: tip
The flight ban on concentrations of people is maintained!
```

```{figure} assets/uav-a2.jpg
:name: uav-a2

Open category A2 flight regulations. Source: Direction de l'Aviation Civile Luxembourg.
```

#### Subcategory A3
In subcategory A3 the following conditions must be met:
- Fly in areas where it is anticipated that no non-participating person will be endangered for the entire duration of the flight.
- Fly a minimum safe horizontal distance of 150 m from residential, commercial, industrial and recreational areas.
```{admonition} Important
:class: tip
The flight ban on concentrations of people is maintained!
```

```{figure} assets/uav-a3.jpg
:name: uav-a3

Open category A3 flight regulations. Source: Direction de l'Aviation Civile Luxembourg.
```

### Specific category
When the "open" or "certified" category requirements are not met, we would be within the "specific" category. Within this category there are the following options:

1. An operational authorization will be requested from the authority of the Member State in which it is registered, including a risk assessment with mitigation measures. Authorization may refer to:
- One or several operations.
- The approval of an LUC (Light UAS Operator Certificate).

2. If the operation conforms to a standard scenario, a responsible statement will be submitted through the UAS operator profile on the AESA website.

#### Standard Scenarios (STS)
Execution Regulation (EU) 2019/947 defines two standard scenarios in which certain requirements are indicated, some of which are not applicable today due to technical limitations.

European Standard Scenarios:
- STS-01: VLOS over a controlled ground area in a populated environment.
- STS-02: BVLOS operations with airspace observers over a controlled area on ground in a sparsely populated environment.

##### STS-01
The European Standard Scenario STS-01 refers to flight of a C5 UAS within visual line of sight (VLOS) over a controlled ground area in a populated environment.

Keep your flight below **120 m** and do not fly your unmanned aircraft more than **100 m away**. Additionally, ensure that your entire flight takes place in a _controlled area on ground_ where outsiders cannot access.

````{admonition} Controlled area on ground
:class: note
The UAS should only be used in an area where the operator can ensure that only participating individuals are present. A non-participant is someone who is not involved in the UAS operation or unaware of the operator's safety instructions. The operator must establish the boundary of the controlled area on land and monitor who enters. The controlled area includes the flight geography, contingency area, and a risk prevention zone on the ground.

```{figure} assets/sts01.png
:name: sts01

European Standard Scenario STS-01. Source: [EASA](https://www.easa.europa.eu/en/domains/civil-drones-rpas/specific-category-civil-drones/standard-scenario-sts)
```
````

````{sidebar}
```{admonition} UAS requirements
:class: tip
- The UAV cannot be a fixed-wing.
- MTOM < 10 kg
- Electric
- Low speed mode (max speed 5 m/s)
- UAS insurance
- Means to reduce the effect of impact dynamics
```
````

```{admonition} General requirements
:class: tip
- Operator Registration
- STS-01 Declaration
- Operator's Manual
- STS-01 Pilot license
- Coordination with Air Traffic Service Porviders if necessary
- EARO + FPL if necessary
```

##### STS-02
The European Standard Scenario STS-02 refers to flight of a C6 UAS beyond visual line of sight (BVLOS) with airspace observers over a controlled area on ground in a sparsely populated environment.

It is imperative that you comply with safety regulations:
- Keep your flight below **100 m** and ensure that takeoff and landing are within your visual line of sight (VLOS).
- All flights will take place in sparsely populated areas, and only authorized personnel will be present in a controlled land area.
- Access to the area must be strictly regulated without exception. 
- It is essential that you maintain a minimum visibility of **5 kilometers** and keep no more than **1 kilometer** distance between the pilot and aircraft if not using observers.
- These regulations are non-negotiable and must be followed at all times for the safety of all involved.

````{admonition} Flight zone
:class: note

When utilizing observers, there are several guidelines to follow to ensure safe operation of the UAS:
- The drone should not be flown more than 2 km away from the pilot
- It should be within 1 km of the nearest airspace observer
- The distance between the remote pilot and any observer should not exceed 1 km
- Reliable communication between the remote pilot and observers must be established
- Observers should be strategically positioned to adequately cover the operational volume.

```{figure} assets/sts02.png
:name: sts02

European Standard Scenario STS-02. Source: [EASA](https://www.easa.europa.eu/en/domains/civil-drones-rpas/specific-category-civil-drones/standard-scenario-sts)
```
````

````{sidebar}
```{admonition} UAS requirements
:class: tip
- MTOM < 25 kg
- Max dimension < 3 m
- Max speed < 50 m/s
- Max cruise speed < 33 m/s
- Independent emergency shutdown system
- Means for programming the trajectory of the aircraft
- UAS insurance
```
````

```{admonition} General requirements
:class: tip
- Operator Registration
- STS-02 Declaration
- Operator's Manual
- STS-02 Pilot license
- Coordination with Air Traffic Service Porviders if necessary
- EARO + FPL if necessary
```

### Certified Category
To operate in the "certified" category, certain requirements must be met as defined in the Execution Regulation (EU) 2019/947. These include:
- Not flying UAS with a dimension greater than 3 m over concentrations of people
- Transporting people
- Transporting dangerous goods with high risk for third parties in the event of an accident.

Additionally, if the necessary safety study shows that the risks of the operation cannot be mitigated without certification of the UAS, operator, and pilot licenses, it will also fall under the certified category.