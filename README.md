# NAMD-analysis-tools
_Python scripts for identification of coordinates defining reactivity of nonadiabatic molecular dynamics (NAMD) trajectories._

This repository contains two complimentary tools, namely **"Cluster-Analysis"** and **"RMSD-Analysis"**, which are located in two corresponding folders.

**Cluster-Analysis**

_Cluster-analysis.py_ allows you to quickly establish whether the surface hop points along particular coordinate (in our example we test various torsion angles) and the velocity along corresponding coordinate has a clear separation in group of productive and unproductive trajectories. In our example cluster approach identifies that surface hop points are clearly separate in group of productive and unproductive surface hop points along torsion angle tau. Hence the tau coordinate is the coordinate determining the reactivity of trajectories in our example system.

_Cluster-Analysis_ folder contains four scripts: _Combine-angle.py_, _Combine-velo.py_, _Plot-actual-angle-and-velo.py_, and _Cluster-analysis.py_

_Combine-angle.py_ and _Combine-velo.py_ can be used to combine surface hop points of reactive and unreactive trajectories into the same file, so that _Cluster-analysis.py_ can be used on them.

_Plot-actual-angle-and-velo.py_ can be used to verify that actual distribution of productive and unproductive surface hop points has the same number of clusters as predicted by _Cluster-analysis.py_

The main purpose of the _Cluster-analysis.py_ is elimination of need for manual visualization of hop points along all coordinates that potentially define reactivity of the system. _Cluster-analysis.py_ allows to automatically find most promising coordinates, which can be subsequently visualized with _Plot-actual-angle-and-velo.py_.

**RMSD-Analysis**

_RMSD-Analysis.py_ is the tool that could be used after _Cluster-analysis.py_ identified most promising reaction coordinate (in our example it is tau). _RMSD-Analysis.py_ calculates the RMSD between the average velocity of a selected coordinate and the velocities of all other coordinates provided by user. In addition the _RMSD-Analysis.py_ identifies if inverted velocity of particular coordinate has close correlation with coordinate selected by user (in some instances the associated coordinate might have an opposite phase).

The main purpose of the _RMSD-Analysis.py_ is to elucidate what other coordinates might be coupled with the coordinate that defines the reactivity of the given system.