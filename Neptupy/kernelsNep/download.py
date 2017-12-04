#!/usr/bin/env python3
# Download remain kernels (not included in this repo)
import os
import urllib.request as req
NR = os.environ["NEPTUPY"]

def main():
    urls = ["https://naif.jpl.nasa.gov/pub/naif/VOYAGER/kernels/ck/vgr2_super_v2.bc",
            "https://naif.jpl.nasa.gov/pub/naif/VOYAGER/kernels/ck/vgr2_super.xbc",
            "https://naif.jpl.nasa.gov/pub/naif/generic_kernels/spk/satellites/nep081.bsp",
            "https://naif.jpl.nasa.gov/pub/naif/generic_kernels/spk/satellites/nep086.bsp",
            "https://naif.jpl.nasa.gov/pub/naif/generic_kernels/spk/satellites/nep087.bsp",
            "https://naif.jpl.nasa.gov/pub/naif/generic_kernels/spk/satellites/nep088.bsp"]
    filenames = ["vgr2_super_v2.bc", "vgr2_super.xbc", "nep081.bsp", "nep086.bsp", "nep087.bsp",
                "nep088.bsp"]
    # For each file, verify and download
    for i, kern in enumerate(filenames):
        if not os.path.exists(NR + 'Neptupy/kernelsNep/' + kern):
            # Download
            print("Downloading", kern,'...')
            req.urlretrieve(urls[i], NR + 'Neptupy/kernelsNep/' + kern)
        else:
            print(kern, "already exists.")

if __name__ == '__main__':
    main()
