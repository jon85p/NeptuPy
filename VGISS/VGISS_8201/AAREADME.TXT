PDS_VERSION_ID                  = PDS3
RECORD_TYPE                     = STREAM

DATA_SET_ID                     = "VG2-N-ISS-2/3/4/6-PROCESSED-V1.0"

OBJECT                          = TEXT
  PUBLICATION_DATE              = 2013-10-25
  NOTE                          = "General overview of the calibrated Voyager
image data set from the Neptune encounters."
END_OBJECT                      = TEXT
END

             CALIBRATED VOYAGER IMAGES FROM THE NEPTUNE ENCOUNTERS
             -----------------------------------------------------

1. INTRODUCTION

This data set contains raw, calibrated and geometrically corrected versions of
all the Voyager images from the Neptune encounters. It has been derived from
the compressed raw images that were archived previously by the PDS.

Images have been processed following standardized procedures using the VICAR
software, as provided by the Multi-mission Image Processing Laboratory at JPL.
For more information about the processing procedures, see the file
DOCUMENT/PROCESSING.TXT. For details on how to use the images, see
DOCUMENT/TUTORIAL.TXT.

This data set is far easier to use than the raw, compressed files and is
recommended for essentially all scientific purposes. Scientific users should
however, heed the comments about calibration accuracy as found in the
TUTORIAL.TXT document mentioned above. Intermediate steps in the processing
are included for any users who might wish to re-calibrate the data themselves.

If you reference this data set in a publication, please cite the work of the
PDS Rings Node, as follows:
    Showalter, M.R., M.K. Gordon, and D. Olson, VG2 NEPTUNE ISS
    PROCESSED IMAGES V1.0, VGISS_8201-8210, NASA Planetary Data
    System, 2013.

It would also be appropriate to acknowledge the work of the Voyager imaging
team, as led by Dr. Brad Smith. For example see this paper:
  Smith, B. A., L. A. Soderblom, D. Banfield, C. Barnet, A. T. Basilevsky,
  R. F. Beebe, K. Bollinger, J. M. Boyce, A. Brahic, G. A. Briggs, R. H.
  Brown, C. Chyba, S. A. Collins, T. Colvin, A. F. Cook II, D. Crisp, S. K.
  Croft, D. Cruikshank, J. N. Cuzzi, G. E. Danielson, M.E. Davies, E. De Jong,
  L. Dones, D. Godfrey, J. Goguen, I. Grenier, V. R. Haemmerle, H. Hammel,
  C. J. Hansen, C. P. Helfenstein, C. Howell, G. E. Hunt, A. P. Ingersoll,
  T. V. Johnson, J. Kargel, R. Kirk, D. I. Kuehn, S. Limaye, H. Masursky,
  A. McEwen, D. Morrison, T. Owen, W. Owen, J. B. Pollack, C. C. Porco,
  K. Rages, P. Rogers, D. Rudy, C. Sagan, J. Schwartz, E. M. Shoemaker,
  M. Showalter, B. Sicardy, D. Simonelli, J. Spencer, L. A. Sromovsky,
  C. Stoker, R. G. Strom, V. E. Suomi, S. P. Synott, R. J. Terrile, P. Thomas,
  W. R. Thompson, A. Verbiscer, and J. Veverka, Voyager 2 at Neptune: Imaging
  science results, Science, 246, 1422-1449, 1989. [SMITHETAL1989]

2. VOLUME FORMAT

This is a virtual volume, which is too large to fit on current hard storage
media such as DVD-ROM. It is currently only available as a directory tree
stored on a hard drive.

3. FILE FORMATS

3.1 FILE EXTENSIONS

Files on this volume are named according to PDS standards, where the
characters after the period indicate the file type. The file types used on
this volume are:

ASCII text files:
    PDS detached labels                     *.LBL
    ASCII tables and indices                *.TAB
    PDS catalog files                       *.CAT
    Text documentation files                *.ASC, *.TXT
    HTML documents                          *.HTM

Binary files
    Binary images                           *.IMG
    Binary data files                       *.DAT
    Browse images                           *.JPG
    Graphical images for documents          *.GIF
    Adobe Acrobat documentation files       *.PDF

3.2 PDS LABELS

Every file in this data set is described by an associated PDS label. Most
files are described by a detached label, which has the same name as the
corresponding file but an extension ".LBL". Most text files (*.TXT, *.CAT)
have attached labels.

Some pairs of files have the same name but different extensions, e.g.
Cnnnnnnn_RESLOC.TAB and .DAT. These files have combined-detached labels,
where a single label file Cnnnnnnn_RESLOC.LBL describes both files.

See the PDS Standards Reference (JPL D-7669) for a complete description of the
PDS label format. This document can also be found on line at
    http://pds.nasa.gov/tools/standards-reference.shtml

3.3 ASCII TEXT FILES

Different popular operating systems use different standards for how ASCII text
files are formatted. On Unix systems and modern Macintosh computers, lines are
terminated by a <LF> (linefeed character, control-J, ASCII 10). On older
Macintosh computers, lines are terminated by a <CR> (carriage return
character, control-M, ASCII 13). On PCs, lines are terminated by a <CR><LF>
pair. PDS standards require all text files to use <CR><LF> line termination.
If the PDS label indicates INTERCHANGE_FORMAT = ASCII or RECORD_TYPE = STREAM,
then this line termination is in use.

On occasion, users on Unix and Macintosh computers may need to change the line
termination on some text files before they can use them. This can be handled
via text editors or a variety of utilities. For example, the Unix tr
(translate) command can be used to change carriage returns to blanks:
    tr "\015" " " <oldfile.txt >newfile.txt

Some ASCII tables indicate RECORD_TYPE = FIXED_LENGTH and include an
additional parameter RECORD_BYTES, which indicates the length in bytes of each
record in the file. It should be noted that all ASCII files still include the
<CR><LF> line terminators, and these two bytes are included in the byte count.
For this reason, it is unwise to convert the line terminator to a single
character (<LF> on Unix or <CR> on Macintosh) because this can change the
number of bytes per record and make it incompatible with the label. In these
situations, it is recommended that the line terminator be replaced by a space
plus <LF> or a space plus <CR> instead.

3.4 BINARY FILES

The binary files on this volume are provided in VICAR format. This is a
relatively simple fixed-length file format consisting of an ASCII header
followed by consecutive rows of the image as binary integers. See
  http://www-mipl.jpl.nasa.gov/external/VICAR_file_fmt.pdf
a complete description of the VICAR file format. This information can also be
found on this volume in DOCUMENTS/VICAR.ASC and DOCUMENTS/VICAR.HTML.

Some binary files contain two-byte integers. All two-byte binary integers are
in least-significant-byte (LSB) format. This is the native format for
Intel-based computers. For computers from Sun and for Macintosh PowerPC-based
computers, users may need to perform a pair-wise swap of the bytes prior to
using these data files.

Floating-point (REAL) binary numbers are in the native Vax D-floating format.
This format is no longer widely used so most of these files have also been
converted to ASCII text format for convenience.

Browse images are provided in JPG format.

4. VOLUME CONTENTS

4.1 VOLUME NAMES

The PDS originally released raw, compressed "EDR" versions of all the Voyager
images on a set of CD-ROMs identified VG_0001 through VG_0038. The
organization of that series is as follows:

  VG_0001-0003: The complete Uranus images
  VG_0004-0005: Selected Saturn images
  VG_0006-0008: Selected Jupiter images
  VG_0009-0012: The complete Neptune images
  VG_0013-0025: The complete Jupiter images
  VG_0026-0038: The complete Saturn images

This derived set of volumes has been derived from VG_0009-0012. The boundaries
between the new volumes are chronological, as defined by Voyager's Flight Data
System ("FDS") clock. Within the Neptune data set, boundaries between volumes
are as follows

  Volume      Vgr  FDS range

  VGISS_8201   2   8966.31 --  9499.00
  VGISS_8202   2   9500.00 --  9999.59
  VGISS_8203   2  10000.00 -- 10399.59
  VGISS_8204   2  10400.00 -- 10799.59
  VGISS_8205   2  10800.00 -- 10999.59
  VGISS_8206   2  11000.00 -- 11199.59
  VGISS_8207   2  11200.00 -- 11399.59
  VGISS_8208   2  11400.00 -- 11599.59
  VGISS_8209   2  11600.00 -- 11999.59
  VGISS_8210   2  12000.00 -- 12457.33

4.2 FILE NAMING CONVENTIONS

All files are named by the associated seven-digit FDS clock count (without a
decimal point) at the time the image was read out of the vidicon. For example,
a file named C3456712*.* is associated with the image read out at FDS time
34567.12. For most images, this corresponds to the time when an exposure
ended; however, in some circumstances (modes "BOTSIM" and "BSIMAN") both the
wide-angle and narrow-angle cameras were triggered simultaneously; under these
circumstances, the narrow-angle camera was read out first and the wide-angle
image has an FDS number a few digits higher.

In the original raw, compressed volumes, files were named
    Cnnnnnnn.IMQ
where 'nnnnnnn' is the FDS count and "IMQ" indicates that the file is a
compressed image.

In this data set, the associated files have the following names:
    Cnnnnnnn_RAW.IMG:     uncompressed, raw image.
    Cnnnnnnn_RAW.LBL:     detached PDS label for the above.

    Cnnnnnnn_CLEANED.IMG: cleaned version of the image, with spikes and reseau
                          markings erased.
    Cnnnnnnn_CLEANED.LBL: detached PDS label for the above.

    Cnnnnnnn_RESLOC.DAT:  binary table of reseau marking locations.
    Cnnnnnnn_RESLOC.TAB:  ASCII table of reseau marking locations.
    Cnnnnnnn_RESLOC.LBL:  combined-detached PDS label for both of the above.

    Cnnnnnnn_CALIB.IMG:   calibrated image.
    Cnnnnnnn_CALIB.LBL:   detached PDS label for the above. Included in the
                          label is the rough conversion factor from pixel
                          values to absolute reflectivity.

    Cnnnnnnn_GEOMA.DAT:   binary table of tie points for modeling the
                          geometric distortion.
    Cnnnnnnn_GEOMA.TAB:   ASCII table containing the same information as the
                          above.
    Cnnnnnnn_GEOMA.LBL:   combined-detached PDS label for both of the above.

    Cnnnnnnn_GEOMED.IMG:  geometrically corrected version of the calibrated
                          image.
    Cnnnnnnn_GEOMED.LBL:  detached PDS label for the above.

4.3 DARK CURRENT FILE NAMING CONVENTIONS

The CALIB/DARKS subdirectory contains the dark current files generated for the
calibration process. They are named as follows:

    DC2_aa_bb{_BS}_X100.IMG

where

    aa = WA for the wide-angle camera;
         NA for the narrow-angle camera.

    bb = 11 for scan rate 1:1
         21 for scan rate 2:1
         31 for scan rate 3:1
         51 for scan rate 5:1
         101 for scan rate 10:1

    "_BS" appears in the file name for wide-angle images taken in BOTSIM or
         BSIMAN mode; this text does not appear for other images.

    "X100" indicates that all dark current images have been scaled by a factor
         of 100 for enhanced precision.

For further details about these images, see DOCUMENTS/PROCESSING.TXT.

4.4 DIRECTORY STRUCTURE

The directory structure matches that of the original Voyager image volumes.

FILE                    CONTENTS

(root)                  Root directory for this PDS Volume.
|
|-AAREADME.TXT          This file.
|
|-ERRATA.TXT            A file describing any known errors or deviations from
|                       PDS standards.
|
|-VOLDESC.CAT           A PDS volume object, providing a high-level
|                       description of the volume and its contents.
|
|-BROWSE/               A directory containing full-resolution JPEG previews
| |                     of each image.
| |
| |-CnnnnnXX/           Subdirectory that divides the the data files, based on
|   |                   the first five digits of the spacecraft clock (FDS)
|   |                   count.
|   |
|   |-Cnnnnnnn_*.JPG    JPEG image.
|   |-Cnnnnnnn_*.LBL    A detached PDS label for the above.
|
|-CALIB/                A directory containing calibration data and support
| |                     files. Only found on volume VGISS_8210.
| |
| |-CALINFO.TXT         A brief description of the subdirectories.
| |
| |-DARKS/              A subdirectory containing the dark current files used
| | |                   in the calibration of these images.
| | |
| | |-CALINFO.TXT       A brief description of the files in this directory.
| | |
| | |-DC*.IMG           A dark current image in VICAR format.
| | |-DC*.LBL           A detached label for each of the above.
| |
| |-MIPL/               A directory containing the support files obtained from
|   |                   JPL's Multi-mission Image Processing Laboratory.
|   |
|   |-DATAINFO.TXT      Description of the files in this directory.
|   |
|   |-FICOR77_VGRSCF.DAT  File of calibration correction factors.
|   |-FICOR77_VGRSCF.LBL  Detached PDS label for the above.
|   |
|   |-FICOR77_VGn_camera_filter.DAT       Calibration file for each Voyager
|   |                                     spacecraft, camera and filter.
|   |-FICOR77_VGn_camera_filter.LBL       Detached PDS label for the above.
|   |
|   |-RESSAR77_VGn_camera.DAT             Default blemish location files for
|   |                                     each Voyager spacecraft and camera.
|   |-RESSAR77_VGn_camera.LBL             Detached PDS label for the above.
|
|-CATALOG/              A directory containing PDS catalog information,
| |                     providing high-level descriptions of the data,
| |                     instruments, etc.
| |
| |-CATINFO.TXT         Description of the files in this directory.
| |
| |-*.CAT               PDS catalog files describing this data set.
|
|-DATA/                 A directory containing the data files.
| |
| |-CnnnnnXX/           Subdirectory that divides the the data files, based on
|   |                   the first five digits of the spacecraft clock (FDS)
|   |                   count.
|   |
|   |-Cnnnnnnn_*.IMG    Image files named as described above.
|   |-Cnnnnnnn_*.DAT    Binary tables named as described above.
|   |-Cnnnnnnn_*.TAB    ASCII tables named as described above.
|   |-Cnnnnnnn_*.LBL    Detached or combined-detached PDS labels.
|
|-DOCUMENT/             A directory containing documentation.
| |
| |-DOCINFO.TXT         A description of the files in this directory.
| |
| |-*.ASC               Documentation in ASCII text format.
| |-*.HTM               Documentation in HTML text format.
| |-*.GIF               Documentation in the form of images in GIF format.
| |-*.TXT               Documentation in ASCII text format.
| |-*.LBL               A detached PDS label for any of the above.
| |
| |-FILTERS/            A subdirectory containing filter information in HTML
| | |                   and GIF format.
| | |
| | |-DOCINFO.TXT       A description of the files in this directory.
| | |
| | |-INDEX.HTM         The starting point of some HTML pages containing
| | |                   filter and calibration information.
| | |
| | |-VG*.HTM           An HTML page describing a filter.
| | |-VG*.GIF           If available, a plot of the filter bandpass.
| | |
| | |-FILTERS.LBL       A PDS label for all of the above HTML and GIF files.
| |
| |-REPORTS/            Calibration reports and memos associated with the
|   |                   Voyager cameras.
|   |
|   |-DOCINFO.TXT       A description of the files in this directory.
|   |
|   |-*.ASC             Documents in ASCII text format.
|   |-*.GIF             GIF images of associated figures.
|   |-*.PDF             Documents in Adobe Acrobat format.
|   |-*.LBL             A detached PDS label for each of the above.
|
|-INDEX/                A directory containing an index of all the data files
  |                     on this volume.
  |
  |-INDXINFO.TXT        Description of the files in this directory.
  |
  |-INDEX.TAB           An index of all the data files on the volume.
  |-INDEX.LBL           A detached PDS label for the above.
  |
  |-CUMINDEX.TAB        An cumulative index of all the data files in this data
  |                     set.
  |-CUMINDEX.LBL        A detached PDS label for the above.

5. METADATA

A note about TARGET_NAMEs. Many images contain more than one target. The
targets indicated in the label files were nominal targets at the time of
observation. Many images missed their intended targets. The values, which are
the same as the directory name in the original voyager archive, provides
nothing more than general guidance about which images may be of interest.

OPUS, the Rings Node's search tool provides a wide range of parameters to use
to find images with specific content:
    http://pds-rings.seti.org/search/

6. CONTACT INFORMATION

    Mark Showalter
    SETI Institute
    189 Bernardo Ave
    Mountain View, CA 94043
    650-810-0234
    mshowalter@seti.org

    Mitch Gordon
    276-393-8822
    mgordon@seti.org

    http://pds-rings.seti.org/

==============================================================================
ACKNOWLEDGMENTS
==============================================================================

We recognize the contribution of Brad Smith and the Voyager Imaging Team for
their work in obtaining this extraordinary data set.

Mark Showalter acknowledges James Pollack and Jeff Cuzzi for teaching him so
many of the ins and outs of Voyager image calibration and processing. We thank
JPL's Multimission Instrument Processing Laboratory for writing and
maintaining the VICAR software. Gary Yagi of JPL provided updates and helpful
advice on several VICAR routines. The PDS Imaging Node provided additional
guidance and support. At the Rings Node, Danny Olson provided extensive
archiving support.

==============================================================================
DISCLAIMER
==============================================================================

Although considerable care has gone into making this volume, errors are both
possible and likely. Users of the data are advised to exercise the same
caution as they would when dealing with any other unknown data set.

Reports of errors or difficulties would be appreciated. Please contact Mark
Showalter or Mitch Gordon at the addresses listed above.
