# Installing required software
## ISIS
Install following the instructions from [this link](https://isis.astrogeology.usgs.gov/documents/InstallGuide/index.html). (<u>Install with Voyager 2 kernels!</u>)

The $ISISROOT environment variable must be added to Bash config file [info](https://isis.astrogeology.usgs.gov/documents/InstallGuide/index.html#UnixEnvironment).

The $NEPTUPY is also required: `export NEPTUPY=/route/to/your/local/copy/from/this/repo`

## AstroPy
[Install](http://www.astropy.org/index.html)

## DS9
[Install](http://ds9.si.edu/site/Download.html)

XPA service is required in order to correct functionality with NeptuPy, sure this environment variable is added to your Bash config file:
`export XPA_METHOD=local`

## PhotUtils
[Install](http://photutils.readthedocs.io/en/stable/photutils/install.html)

## SpicePy (and SPICE included)
[Install](http://spiceypy.readthedocs.io/en/master/installation.html)