# Geo-UAV

<a rel="license" href="http://creativecommons.org/licenses/by-nc/4.0/"><img alt="Creative Commons Licence" style="border-width:0" src="https://i.creativecommons.org/l/by-nc/4.0/88x31.png" /></a> [![Build and Deploy](https://github.com/UNISvalbard/Geo-UAV/actions/workflows/build%20and%20deploy.yml/badge.svg)](https://github.com/UNISvalbard/Geo-UAV/actions/workflows/build%20and%20deploy.yml) [![Zenodo DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.11173398.svg)](https://doi.org/10.5281/zenodo.11173398)

[Geo-UAV](https://unisvalbard.github.io/Geo-UAV/landing-page.html) is an open-source reference work for the UAV-based data acquisition in the field.

Unmanned Aerial Vehicles, also known as UAVs, are being used extensively for recreational, commercial, academic, and government purposes. They are particularly useful in geosciences to survey large areas accurately and efficiently. This course offers guidelines on how to acquire scientifically publishable data using UAVs in a safe and legal manner.

The reference work is primarily developed as a class-room aid. Best practices and tutorials are based on the experience acquired as part of the [Svalbox project](https://svalbox.no), which aims to digitize as many outcrops as possible in Svalbard (Norwegian Arctic).

### Contribute or improve the resource
```{admonition} Under construction
Geo-UAV is still in development, with additional tutorials and how-tos added continously to keep the work up-to-date with recent developments and evolving best practices.
```

Notice some unclear sections? A typo in the text? Want to add a cool tutorial or how-to on processing? Get in touch and let's make thing happen!

### Compile it

The minimal Python environment to compile this tutorial can be created as follows:

```
mamba env create --file geomod_environment.yaml
```

Subsequently, one may build the pages by using the following command from the root folder:

```
jupyter book build .
```


### Acknowledgements and licensing
Geo-UAV is implemented through Jupyter Book and the Executable Book Project.
This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc/4.0/">Creative Commons Attribution-NonCommercial 4.0 International License</a>.

The developement of Geo-UAV is funded by [iEarth](https://www.iearth.no/), a Norwegian Center of Excellence for Integrated Earth Science Education.