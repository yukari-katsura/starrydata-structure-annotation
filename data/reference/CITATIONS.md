# Citing the reference datasets

## TEDesignLab

Source: <https://www.prashungorai.org/tedesignlab/> (formerly tedesignlab.org).

The database paper, to be cited whenever these data are used:

> Gorai, P.; Gao, D.; Ortiz, B.; Miller, S.; Barnett, S. A.; Mason, T.; Lv, Q.;
> Stevanović, V.; Toberer, E. S.
> **TE Design Lab: A virtual laboratory for thermoelectric material design.**
> *Computational Materials Science* **112**, 368–376 (2016).
> <https://doi.org/10.1016/j.commatsci.2015.11.006>

```bibtex
@article{gorai2016tedesignlab,
  author  = {Gorai, Prashun and Gao, Duanfeng and Ortiz, Brenden and Miller, Sam
             and Barnett, Scott A. and Mason, Thomas and Lv, Qin and
             Stevanovi{\'c}, Vladan and Toberer, Eric S.},
  title   = {{TE} {D}esign {L}ab: A virtual laboratory for thermoelectric material design},
  journal = {Computational Materials Science},
  volume  = {112},
  pages   = {368--376},
  year    = {2016},
  doi     = {10.1016/j.commatsci.2015.11.006}
}
```

### The `cite` column: markers [1]-[5] resolved

Every row of the spreadsheet carries a marker in its `cite` column identifying
which paper produced that row's computed quantities. The reference list is
rendered on the TEDesignLab page but is not included in the download; it is
reproduced here, with all five verified against Crossref.

| marker | rows | reference |
|---:|---:|---|
| [1] | 735 | Miller, S. A.; Gorai, P.; Aydemir, U.; Mason, T. O.; Stevanović, V.; Toberer, E. S.; Snyder, G. J. **SnO as a potential oxide thermoelectric candidate.** *J. Mater. Chem. C* **5**, 8854–8861 (2017). [10.1039/c7tc01623a](https://doi.org/10.1039/c7tc01623a) |
| [2] | 477 | Gorai, P.; Gao, D.; Ortiz, B.; Miller, S.; Barnett, S. A.; Mason, T. O.; Lv, Q.; Stevanović, V.; Toberer, E. S. **TE Design Lab: A virtual laboratory for thermoelectric material design.** *Comput. Mater. Sci.* **112**, 368–376 (2016). [10.1016/j.commatsci.2015.11.006](https://doi.org/10.1016/j.commatsci.2015.11.006) |
| [3] | 616 | Yan, J.; Gorai, P.; Ortiz, B.; Miller, S.; Barnett, S. A.; Mason, T. O.; Stevanović, V.; Toberer, E. S. **Material descriptors for predicting thermoelectric performance.** *Energy Environ. Sci.* **8**, 983–994 (2015). [10.1039/c4ee03157a](https://doi.org/10.1039/c4ee03157a) |
| [4] | 795 | Gorai, P.; Toberer, E. S.; Stevanović, V. **Thermoelectricity in transition metal compounds: the role of spin disorder.** *Phys. Chem. Chem. Phys.* **18**, 31777–31786 (2016). [10.1039/c6cp06943f](https://doi.org/10.1039/c6cp06943f) |
| [5] | 78 | Ortiz, B. R.; Peng, W.; Gomes, L. C.; Gorai, P.; Zhu, T.; Smiadak, D. M.; Snyder, G. J.; Stevanović, V.; Ertekin, E.; Zevalkink, A.; Toberer, E. S. **Ultralow thermal conductivity in diamond-like semiconductors: selective scattering of phonons from antisite defects.** *Chem. Mater.* **30**, 3395–3409 (2018). [10.1021/acs.chemmater.8b00890](https://doi.org/10.1021/acs.chemmater.8b00890) |

The marker is carried through the pipeline as `tedl_cite` in
`data/annotated/input/df_structure_refs.parquet` and
`df_structure_candidates.parquet`, so any space group or descriptor taken from
TEDesignLab can be traced to the paper that produced it.

Note that [4] (spin disorder, 795 rows) is the single largest contributor —
magnetic transition-metal compounds, where the reported transport quantities
depend on how spin disorder was treated. Worth knowing before comparing a
descriptor across markers.

### Redistribution

The TEDesignLab page states no licence or redistribution terms. This repository
currently tracks `tedesignlab-complete-data.xlsx`; see the pre-publication
checklist in the root README before making the repository public.

## Materials Project

Dump of 2019-08-22, `mp_190822.csv` (untracked; 35 MB).

> Jain, A.; Ong, S. P.; Hautier, G.; Chen, W.; Richards, W. D.; Dacek, S.;
> Cholia, S.; Gunter, D.; Skinner, D.; Ceder, G.; Persson, K. A.
> **Commentary: The Materials Project: A materials genome approach to
> accelerating materials innovation.**
> *APL Materials* **1**, 011002 (2013).
> <https://doi.org/10.1063/1.4812323>

Materials Project data are released under CC BY 4.0.

## ICSD

ICSD collection codes appear as identifiers only; no ICSD structure data is
redistributed here. ICSD is a licensed product of FIZ Karlsruhe.
