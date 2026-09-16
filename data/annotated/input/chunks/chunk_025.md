# Host systems -- chunk 025 of 73

Ranks 1201-1250 by sample count. These 50 host systems cover 250 samples (0.48% of the TE set); cumulative through this chunk: 91.65%.

Assign each host system a structural prototype from `data/annotated/taxonomy/prototypes_seed_v3.json`, or propose a new one in `taxonomy/prototypes_proposed.jsonl` first. Append results to `data/annotated/annotations/family_assignments.jsonl`.

The hand-entered MaterialFamily labels are deliberately NOT shown here -- they are held out in `df_host_systems.parquet` to validate this classification later. Decide from the compositions.

A "seed hypothesis" line means the taxonomy already names this host under that prototype. Confirm it against the compositions rather than accepting it; two or more listed means the host is mixed and needs splitting per composition.

Evidence follows the project precedence. Your judgement about the thermoelectric chemistry decides the prototype. [ref 1] is TEDesignLab, ICSD-backed and thermoelectric-specific -- prefer it. [ref 2] is Materials Project. Within a formula, polymorphs are ranked by ICSD reference count and the top one is marked PRIMARY -- not by e_above_hull, which is unusable for layered chalcogenides in the 2019 dump (Sb2Te3 R-3m carries 26 ICSD refs at hull 1.02). A primary resting on fewer than 5 ICSD references is flagged weak; the ambient phase may simply be absent from the snapshot, as it is for Bi2Se3.

While you have the host in view, also record what each minor element DOES, in `dopant_roles` -- the role follows from the prototype and cannot be judged without it. A median host has 2 such elements. Not everything listed is a dopant: O, C, N and H are usually milling or pressing residue, and an element just under 5 at.% may be an alloying end member rather than dilute doping. The doping LEVEL is computed later from the parsed fractions -- do not work it out by hand here.

A polymorph list is NOT a thermal sequence. SnSe has three known structures but only Pnma -> Cmcm happens on heating; rocksalt SnSe is metastable (2 icsd refs against 32). Put thermally reached phases in `phases` with their transition temperatures, and everything else in `other_polymorphs` with an occurrence reason. hull and icsd counts are shown to help you tell them apart.

A host may need MORE THAN ONE prototype. Transport is measured across a wide window and many thermoelectrics transform inside it, so where a "MEASUREMENT CROSSES A TRANSITION" line appears, record each phase with its own temperature range in the `phases` field. Transition temperatures shown are approximate and composition-dependent.

Both references describe which phases EXIST in a chemistry, not which phase this paper made. Al-O-Zn is best attested as ZnAl2O4 spinel (227) while almost every sample in it is Al-doped wurtzite ZnO (186). Weigh them against the compositions; do not follow them blindly.

## F-H-I-S
- rank 1201 | 5 samples | 1 papers | 1 compositions
- compositions: STF2I3 (5)
- measured range: 12-300 K (5th-95th pct of 7 curves)
- papers: https://doi.org/10.3390/cryst10040270 (Band Structure and Physical Properties of α-STF2I3: Dirac Electrons in...)

## Fe-Ga-Ge
- rank 1202 | 5 samples | 2 papers | 5 compositions
- compositions: FeGa2.75Ge0.25 (1); FeGa2.65Ge0.35 (1); Fe0.85Co0.15Ga2.65Ge0.35 (1); Fe0.90Co0.10Ga2.65Ge0.35 (1); FeGa2.80Ge0.20 (1)
- dopant candidates (<5% at.): Co (2)
- sample form: Bulk (5)
- measured range: 85-874 K (5th-95th pct of 28 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): GaFeGe Fddd (70) mp-1225119 [hull=0.048, PRIMARY]
- papers: https://doi.org/10.1063/1.4938474 (Improved thermoelectric properties in heavily doped FeGa3) | https://doi.org/10.1007/s11664-013-2888-1 (Substitution Solid Solutions FeGa3−x E x and Their Thermoelectric Prop...)

## Fe-Hf-Nb-Sb-Ti-V
- rank 1203 | 5 samples | 2 papers | 3 compositions
- compositions: FeV0.24Nb0.40Hf0.16Ti0.2Sb (2); FeV0.39Nb0.25Hf0.16Ti0.2Sb (2); FeV0.24Nb0.4Hf0.16Ti0.2Sb (1)
- sample form: Polycrystal (4); Bulk (1)
- measured range: 298-800 K (5th-95th pct of 27 curves)
- papers: https://doi.org/10.1016/j.jallcom.2021.161838 (Transport and thermoelectric properties of Nb-doped FeV0.64Hf0.16Ti0.2...) | https://doi.org/10.1016/j.jallcom.2021.161308 (Mechanical and thermoelectric properties of FeVSb-based half-Heusler a...)

## Fe-In-O-Zn
- rank 1204 | 5 samples | 1 papers | 5 compositions
- compositions: InFeZnO4 (1); InFeO3(ZnO)4 (1); InFeO3(ZnO)2 (1); InFeO3(ZnO)3 (1); InFeO3(ZnO)5 (1)
- sample form: Bulk (5)
- measured range: 291-1273 K (5th-95th pct of 5 curves)
- papers: https://doi.org/10.1016/j.actamat.2017.07.012 (Investigation on thermal transport and structural properties of InFeO ...)

## Fe-Pb-Te
- rank 1205 | 5 samples | 1 papers | 5 compositions
- compositions: Pb0.85Fe0.15Te0.99I0.01 (1); Pb0.85Fe0.15Te0.992I0.008 (1); Pb0.85Fe0.15Te0.996I0.004 (1); Pb0.85Fe0.15Te0.994I0.006 (1); Pb0.85Fe0.15Te0.998I0.002 (1)
- dopant candidates (<5% at.): I (5)
- measured range: 295-852 K (5th-95th pct of 25 curves)
- papers: https://doi.org/10.1007/s11664-016-4857-y (Preparation and Thermoelectric Properties of Pb1–x Fe x Te Alloys Dope...)

## Fe-Sb-Zr
- rank 1206 | 5 samples | 1 papers | 5 compositions
- compositions: Zr6FeSb2 (1); Zr5Fe0.44Sb2.56 (1); Zr5Fe0.63Sb3.21 (1); ZrFe0.7Sb (1); ZrFe0.5Sb (1)
- sample form: Bulk (5)
- measured range: 11-296 K (5th-95th pct of 8 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Zr5FeSb3 P6_3/mcm (193) mp-1189764 [hull=0.000, icsd=1, PRIMARY]; Zr6FeSb2 P-62m (189) mp-12962 [hull=0.000, icsd=1, PRIMARY]; Zr3Fe2Sb3 Pm (6) mp-1216223 [hull=0.044, PRIMARY]; ZrFeSb F-43m (216) mp-961652 [hull=0.040, PRIMARY]
- papers: https://doi.org/10.1016/s0925-8388(99)00537-x (Thermoelectric properties of ternary transition metal antimonides)

## Fe-Si-Zr
- rank 1207 | 5 samples | 1 papers | 5 compositions
- compositions: Fe0.76Zr0.24Si2 (1); Fe0.73Zr0.27Si2 (1); Fe0.81Zr0.18Si2 (1); Fe0.79Zr0.21Si2 (1); Fe0.7Zr0.3Si2 (1)
- sample form: Bulk (5)
- measured range: 295-1173 K (5th-95th pct of 12 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Zr4Fe4Si7 I4/mmm (139) mp-17435 [hull=0.000, icsd=3, PRIMARY]; Zr3Fe2Si3 Cmcm (63) mp-1105799 [hull=0.013, icsd=2, PRIMARY]; Zr(Fe2Si)2 P4_2/mnm (136) mp-19792 [hull=0.000, icsd=1, PRIMARY]; Zr2Fe3Si P6_3/mmc (194) mp-16336 [hull=0.000, icsd=1, PRIMARY]; Zr6Fe16Si7 Fm-3m (225) mp-1192960 [hull=0.000, icsd=1, PRIMARY]
- papers: https://doi.org/10.1063/1.1502202 (Effects of Zr substitution on phase transformation and thermoelectric ...)

## Ga-In-O-Sn
- rank 1208 | 5 samples | 1 papers | 5 compositions
- compositions: Ga2.7In5.3Sn2O16 (1); Ga2In6Sn2O16 (1); Ga1.4In6.6Sn2O16 (1); Ga2.4In5.6Sn2O16 (1); Ga1.7In6.3Sn2O16 (1)
- sample form: Bulk (5)
- solid-solution axis: Ga/(Ga+In) spans 0.18-0.34 (median 0.25) over 5 compositions
     ISOELECTRONIC SERIES: the parent compound depends on the composition, not on this host. Near either end the minor element is a dilute substituent; in the middle it is a genuine alloy. Record the axis, not one parent -- and note the 5% split used the whole formula, not the sublattice, so its cut lands at a different level on each site.
- measured range: 322-1024 K (5th-95th pct of 25 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): InGaSnO5 P2/m (10) mp-1212081 [hull=0.004, PRIMARY]
- papers: https://doi.org/10.1063/1.3495797 (Synthesis and thermoelectric properties of oxygen deficient fluorite d...)

## Ga-In-Sb
- rank 1209 | 5 samples | 2 papers | 4 compositions
- compositions: In0.28Ga0.72Sb (2); In0.12Ga0.88Sb (1); In0.85Ga0.15Sb (1); In0.90Ga0.10Sb (1)
- sample form: Bulk (2)
- solid-solution axis: Ga/(Ga+In) spans 0.10-0.88 (median 0.72) over 4 compositions
     ISOELECTRONIC SERIES: the parent compound depends on the composition, not on this host. Near either end the minor element is a dilute substituent; in the middle it is a genuine alloy. Record the axis, not one parent -- and note the 5% split used the whole formula, not the sublattice, so its cut lands at a different level on each site.
- measured range: 103-586 K (5th-95th pct of 15 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): InGa4Sb5 R3m (160) mp-1223963 [hull=0.030, PRIMARY]; InGaSb2 P-4m2 (115) mp-1223638 [hull=0.026, PRIMARY]; InGaSb2 R3m (160) mp-1223646 [hull=0.037]
- papers: https://doi.org/10.1002/adma.201100449 (Semimetal/Semiconductor Nanocomposites for Thermoelectrics) | https://doi.org/10.1021/acs.inorgchem.9b01430 (An Approach to Optimize the Thermoelectric Properties of III–V Ternary...)

## Ga-Mn-Ni
- rank 1210 | 5 samples | 3 papers | 4 compositions
- compositions: Ni2MnGa (2); Ni50Mn25Ga25 (1); Ni49.4Mn30Ga20.6 (1); Ni47.3Mn30.6Ga22.1 (1)
- sample form: Bulk (2)
- measured range: 24-326 K (5th-95th pct of 4 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): MnGaNi2 Fm-3m (225) mp-20228 [hull=0.005, icsd=17, PRIMARY]; Mn3Ga4Ni9 Pm-3m (221) mp-1189147 [hull=0.016, icsd=2, PRIMARY]; Mn2GaNi I-4m2 (119) mp-1222026 [hull=0.009, PRIMARY]; MnGa2Ni Fm-3m (225) mp-1206866 [hull=0.126, PRIMARY]; MnGa2Ni9 P4/mmm (123) mp-1222110 [hull=0.000, PRIMARY]
- papers: https://doi.org/10.1016/j.jmmm.2005.11.018 (Electrical transport and thermal properties of ferromagnetic shape mem...) | https://doi.org/10.1016/j.jmmm.2017.01.024 (Magnetocaloric effect in Ni2MnGa single crystal in the vicinity of the...) | https://doi.org/10.1103/physrevb.102.064413 (Anomalous Hall effect in \n<mml:math xmlns:mml=\"http://www.w3.org/199...)

## Ga-Nd-O
- rank 1211 | 5 samples | 4 papers | 2 compositions
- compositions: NdGaO3 (3); Nd3Ga5SiO14 (2)
- dopant candidates (<5% at.): Si (2)
- sample form: SingleCrystal (2)
- measured range: 10-298 K (5th-95th pct of 6 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): NdGaO3 Pnma (62) mp-3196 [hull=0.033, icsd=21, PRIMARY]; Nd3GaO6 Cmc2_1 (36) mp-11773 [hull=0.000, icsd=2, PRIMARY]; Nd3Ga5O12 Ia-3d (230) mp-15239 [hull=0.000, icsd=1, PRIMARY]; Nd3Ga5SiO14 P3 (143) mp-1220307 [hull=0.020, PRIMARY]; NdGaO3 Pm-3m (221) mp-9834 [hull=1.467, icsd=1]
- papers: https://doi.org/10.1002/aenm.201301927 (Enhanced Thermoelectric Power Factor of NaxCoO2Thin Films by Structura...) | https://doi.org/10.1103/physrevb.85.174438 (Paramagnetic ground state with field-induced partial order in Nd3Ga5Si...) | https://doi.org/10.1021/acsami.8b21301 (Strain Effect on Oxygen Evolution Reaction Activity of Epitaxial NdNiO...)

## Ga-Pd
- rank 1212 | 5 samples | 1 papers | 2 compositions
- compositions: GaPd2 (4); GaPd (1)
- measured range: 11-389 K (5th-95th pct of 11 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ga3Pd5 Pbam (55) mp-2408 [hull=0.012, icsd=4, PRIMARY]; GaPd P2_13 (198) mp-1078526 [hull=0.000, icsd=4, PRIMARY]; GaPd2 Pnma (62) mp-1869 [hull=0.000, icsd=3, PRIMARY]; Ga7Pd3 Im-3m (229) mp-1106289 [hull=0.000, icsd=2, PRIMARY]; Ga2Pd5 Pnma (62) mp-405 [hull=0.000, icsd=1, PRIMARY]
- papers: https://doi.org/10.1016/j.intermet.2015.07.010 (Physical properties of the GaPd 2 intermetallic catalyst in bulk and n...)

## Ga-Sb-Zn
- rank 1213 | 5 samples | 1 papers | 5 compositions
- compositions: (ZnSb)70(GaSb)30 (1); (ZnSb)60(GaSb)40 (1); (ZnSb)90(GaSb)10 (1); (ZnSb)80(GaSb)20 (1); (ZnSb)50(GaSb)50 (1)
- sample form: Other (5)
- measured range: 321-625 K (5th-95th pct of 18 curves)
- papers: https://doi.org/10.3365/eml.2010.12.193 (Thermoelectric Properties of (ZnSb)1-x-(MSb)x Binary Systems)

## Gd-O-Sb
- rank 1214 | 5 samples | 2 papers | 1 compositions
- compositions: Gd2SbO2 (5)
- measured range: 12-392 K (5th-95th pct of 5 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Gd3SbO3 C2/m (12) mp-1104777 [hull=0.028, icsd=1, PRIMARY]; Gd3SbO7 Cmcm (63) mp-1191117 [hull=0.000, icsd=1, PRIMARY]; Gd8Sb3O8 C2 (5) mp-1224996 [hull=0.000, PRIMARY]; GdSbO4 P-1 (2) mp-1213602 [hull=0.021, PRIMARY]; Gd3SbO7 C222_1 (20) mp-755404 [hull=0.000]
- papers: https://doi.org/10.1021/ja209652d (Decoupling the Electrical Conductivity and Seebeck Coefficient in theR...) | https://doi.org/10.1021/acs.chemmater.7b03996 (Rare-Earth Pnictide Oxides (RE,Ca)mPnnOm (Pn = Sb, Bi): A Review of Cr...)

## Gd-O-U
- rank 1215 | 5 samples | 1 papers | 5 compositions
- compositions: (UO2.00)(Gd2.00) (1); (UO2.06)(GdO2.06) (1); (UO2.11)(GdO2.11) (1); (UO2.08)(GdO2.08) (1); (UO2.15)(GdO2.15) (1)
- solid-solution axis: Gd/(Gd+U) spans 0.50-0.67 (median 0.50) over 5 compositions
     ISOELECTRONIC SERIES: the parent compound depends on the composition, not on this host. Near either end the minor element is a dilute substituent; in the middle it is a genuine alloy. Record the axis, not one parent -- and note the 5% split used the whole formula, not the sublattice, so its cut lands at a different level on each site.
- measured range: 288-1408 K (5th-95th pct of 5 curves; full span incl. outliers 288-1505 K)
- papers: https://doi.org/10.1016/s0022-3115(97)00105-0 (The effects of oxidation on the thermal conductivity of (U, M)O2 pelle...)

## Gd-Te-Tl
- rank 1216 | 5 samples | 3 papers | 4 compositions
- compositions: Tl9GdTe6 (2); Tl8.83Gd1.17Te6 (1); Tl9Gd1.0Te6 (1); TlGdTe2 (1)
- sample form: Bulk (5)
- measured range: 295-590 K (5th-95th pct of 21 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Gd(Tl3Te2)3 I4/m (87) mp-1188567 [hull=0.022, icsd=1, PRIMARY]; GdTlTe2 R-3m (166) mp-1065609 [hull=0.000, icsd=1, PRIMARY]
- papers: https://doi.org/10.1016/j.jallcom.2012.09.023 (Thermoelectric properties of Tl10−xLnxTe6, with Ln=Ce, Pr, Nd, Sm, Gd,...) | https://doi.org/10.1016/j.jallcom.2015.01.025 (Thermoelectric properties of hot-pressed Tl9LnTe6 (Ln=La, Ce, Pr, Nd, ...) | https://doi.org/10.1007/s11664-011-1846-z (Thermoelectric Properties of TlGdQ2 (Q = Se, Te) and Tl9GdTe6)

## Ge-In-Te
- rank 1217 | 5 samples | 3 papers | 5 compositions
- compositions: In0.1Ge0.9Te (1); In0.15Ge0.85Te (1); (In2Te3)0.15(GeTe)2.55 (1); (In2Te3)0.2(GeTe)2.4 (1); Ge12In2Te15 (1)
- sample form: Bulk (5)
- measured range: 32-823 K (5th-95th pct of 24 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): InGeTe2 R-3m (166) mp-1223647 [hull=0.040, PRIMARY]
- papers: https://doi.org/10.1007/s11664-014-3507-5 (Thermoelectric Properties of In\n                x\n            Ge1−x\...) | https://doi.org/10.1039/c4cp01294a (Highly efficient (In2Te3)x(GeTe)3−3x thermoelectric materials: a subst...) | https://doi.org/10.1016/j.solidstatesciences.2013.08.013 (The solid solution series Ge12M2Te15 (M = Sb, In): Nanostructures and ...)

## Ge-La-Ni
- rank 1218 | 5 samples | 3 papers | 4 compositions
- compositions: LaNi2Ge2 (2); La2Ni3Ge5 (1); La3NiGe2 (1); La2NiGe3 (1)
- sample form: SingleCrystal (2); Polycrystal (1)
- measured range: 10-346 K (5th-95th pct of 10 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): La(NiGe)2 I4/mmm (139) mp-19979 [hull=0.000, icsd=4, PRIMARY]; LaNiGe2 Cmcm (63) mp-21077 [hull=0.000, icsd=3, PRIMARY]; La11(Ni2Ge3)2 C2/m (12) mp-627405 [hull=0.000, icsd=1, PRIMARY]; LaNi9Ge4 I4/mcm (140) mp-1194233 [hull=0.000, icsd=1, PRIMARY]; La5NiGe3 P6_3/mcm (193) mp-1211722 [hull=0.054, PRIMARY]
- papers: https://doi.org/10.1016/j.jallcom.2016.08.045 (Thermal and electron transport properties of Ce2Ni3Ge5 and Ce3NiGe2: E...) | https://doi.org/10.1016/0304-8853(94)01422-1 (Anisotropic transport and magnetic properties of CeNi2Ge2) | https://doi.org/10.1103/physrevb.64.224405 (Electric, magnetic, and thermal properties of<mml:math xmlns:mml=\"htt...)

## Ge-La-Pt
- rank 1219 | 5 samples | 2 papers | 5 compositions
- compositions: LaPt4Ge11.5Sb0.5 (1); LaPt4Ge11.75Sb0.25 (1); LaPt4Ge12 (1); La1Pt4Ge12. (1); La1Pt4Ge12 (1)
- dopant candidates (<5% at.): Sb (2)
- measured range: 10-293 K (5th-95th pct of 9 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): La(GePt)2 P2_1/m (11) mp-21218 [hull=0.011, icsd=2, PRIMARY]; La(Ge3Pt)4 Im-3 (204) mp-1188305 [hull=0.007, icsd=1, PRIMARY]; LaGePt I4_1md (109) mp-1077797 [hull=0.000, icsd=1, PRIMARY]; La(GePt)2 P2_1/c (14) mp-606511 [hull=0.000, icsd=1]; La(GePt)2 P4/nmm (129) mp-1080546 [hull=0.018, icsd=1]
- papers: https://doi.org/10.1007/978-94-007-4984-9_9 (From Superconductivity Towards Thermoelectricity: Ge-Based Skutterudites) | https://doi.org/10.1103/physrevb.94.094501 (Superconducting and normal state properties of the systemsLa1−xMxPt4Ge...)

## Ge-Mn-Pb-Sn-Te
- rank 1220 | 5 samples | 1 papers | 5 compositions
- compositions: Ga0.02(Sn0.25Pb0.25Mn0.25Ge0.25)0.98Te (1); Sn0.25Pb0.25Mn0.25Ge0.25Te (1); Ga0.015(Sn0.25Pb0.25Mn0.25Ge0.25)0.985Te (1); Ga0.025(Sn0.25Pb0.25Mn0.25Ge0.25)0.975Te (1); Ga0.03(Sn0.25Pb0.25Mn0.25Ge0.25)0.97Te (1)
- dopant candidates (<5% at.): Ga (4)
- sample form: Polycrystal (5)
- measured range: 299-824 K (5th-95th pct of 25 curves)
- papers: https://doi.org/10.1021/acsami.1c00221 (Enhanced Thermoelectric Performance in High Entropy Alloys Sn0.25Pb0.2...)

## Ge-Mn-Sb-Te
- rank 1221 | 5 samples | 2 papers | 2 compositions
- compositions: Ge3MnSb2Te7 (4); Ge0.8Mn0.1Sb0.1Te (1)
- sample form: Bulk (5)
- measured range: 299-823 K (5th-95th pct of 21 curves)
- papers: https://doi.org/10.1016/j.jallcom.2015.08.170 (The influence of Mn doping on the properties of Ge4Sb2Te7) | https://doi.org/10.1021/jacs.7b13611 (Rhombohedral to Cubic Conversion of GeTe via MnTe Alloying Leads to Ul...)

## Ge-N-W
- rank 1222 | 5 samples | 1 papers | 1 compositions
- compositions: GeNW (5)
- measured range: 39-300 K (5th-95th pct of 5 curves)
- papers: https://doi.org/10.1063/1.4794821 (Contribution of radial dopant concentration to the thermoelectric prop...)

## Ge-O-Si
- rank 1223 | 5 samples | 3 papers | 3 compositions
- compositions: SiGeO (3); (SiO2)80(GeO2)20B2.8 (1); Sr2.24Ti2.24O6.72Si80Ge20P1 (1)
- dopant candidates (<5% at.): B (1), Sr (1), Ti (1), P (1)
- sample form: Film (3); Bulk (1)   <-- film/epitaxial samples present: a metastable polymorph may be reachable here that never forms in bulk
- measured range: 80-1050 K (5th-95th pct of 11 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): SiGeO3 Pbca (61) mp-769171 [hull=0.106, PRIMARY]
- papers: https://doi.org/10.1021/cm401990c (Silicon-Based Thermoelectrics Made from a Boron-Doped Silicon Dioxide ...) | https://doi.org/10.1021/acsami.9b20090 (Enhanced Thermoelectric Performance in n-Type SrTiO3/SiGe Composite) | https://doi.org/10.1063/1.4773204 (Large reduction in thermal conductivity for Ge quantum dots embedded i...)

## H-Ni
- rank 1224 | 5 samples | 2 papers | 4 compositions
- compositions: Ni0.98Ti0.02H0.9 (2); Ni0.98Ti0.02H0.5 (1); Ni0.95Cr0.05H0.96 (1); Ni0.95Cr0.05H0.14 (1)
- dopant candidates (<5% at.): Ti (3), Cr (2)
- measured range: 82-288 K (5th-95th pct of 5 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ni2H P-3m1 (164) mp-753890 [hull=0.023, icsd=2, PRIMARY]; NiH Fm-3m (225) mp-24719 [hull=0.000, icsd=1, PRIMARY]; Ni3H P6_3/mmc (194) mp-976948 [hull=0.519, PRIMARY]; NiH3 P6_3/mmc (194) mp-973963 [hull=0.230, PRIMARY]; Ni2H R-3m (166) mp-1220079 [hull=0.019]
- papers: https://doi.org/10.1016/j.jallcom.2004.11.126 (Transport properties of some hydrogenated nickel-based alloys) | https://doi.org/10.1016/s0925-8388(02)00048-8 (Effect of dissolved hydrogen on electron transport in nickel–chromium ...)

## Hg-S-Te
- rank 1225 | 5 samples | 1 papers | 5 compositions
- compositions: HgS0.2Te0.8 (1); HgS0.1Te0.9 (1); HgS0.3Te0.7 (1); HgS0.44Te0.56 (1); HgS0.9Te0.1 (1)
- solid-solution axis: S/(S+Te) spans 0.10-0.90 (median 0.30) over 5 compositions
     ISOELECTRONIC SERIES: the parent compound depends on the composition, not on this host. Near either end the minor element is a dilute substituent; in the middle it is a genuine alloy. Record the axis, not one parent -- and note the 5% split used the whole formula, not the sublattice, so its cut lands at a different level on each site.
- measured range: 56-394 K (5th-95th pct of 6 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Hg2TeS R3m (160) mp-1223955 [hull=0.044, PRIMARY]
- papers: https://doi.org/10.1007/bf00549999 (Galvanomagnetic and thermoelectric properties of HgSx Te1?x solid solu...)

## I-Mg-S
- rank 1226 | 5 samples | 2 papers | 5 compositions
- compositions: Mg2SI0.8Ge0.2Ag0.01 (1); Mg2SI0.8Ge0.2Ag0.008 (1); Mg2SI0.8Ge0.2Ag0.016 (1); Mg2SI0.8Ge0.2Ag0.012 (1); Mg2SI (1)
- dopant candidates (<5% at.): Ge (4), Ag (4)
- sample form: Bulk (4)
- measured range: 303-815 K (5th-95th pct of 13 curves; full span incl. outliers 303-872 K)
- papers: https://doi.org/10.4028/0-87849-997-0.177 (Solid State Reaction Synthesis and Thermoelectric Properties of Ag-Dop...) | https://doi.org/10.1016/j.jallcom.2013.11.092 (Synthesis of Mg2Si for thermoelectric applications using magnesium all...)

## In-La
- rank 1227 | 5 samples | 3 papers | 4 compositions
- compositions: LaIn3 (2); (Ce0.1La0.9)In3 (1); (Ce0.01La0.99)In3 (1); (Ce0.2La0.8)In3.12 (1)
- dopant candidates (<5% at.): Ce (3)
- sample form: Bulk (1)
- measured range: 10-291 K (5th-95th pct of 7 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): La3In Pm-3m (221) mp-20909 [hull=0.000, icsd=6, PRIMARY]; LaIn3 Pm-3m (221) mp-20729 [hull=0.000, icsd=6, PRIMARY]; La2In P6_3/mmc (194) mp-20760 [hull=0.012, icsd=1, PRIMARY]; LaIn Pm-3m (221) mp-20582 [hull=0.000, icsd=1, PRIMARY]; LaIn2 Imma (74) mp-22282 [hull=0.000, icsd=1, PRIMARY]
- papers: https://doi.org/10.1016/0304-8853(85)90291-4 (Thermoelectric power and electrical resistivity of Ce(In1-xSnx)3 and (...) | https://doi.org/10.1016/0038-1098(89)90423-7 (Thermoelectric power of the REIn3 single crystals where RE = La, Ce, P...) | https://doi.org/10.1016/0304-8853(87)90671-8 (Thermoelectric power of some Ce compounds of the dilute Kondo type)

## In-Sb-Sr
- rank 1228 | 5 samples | 2 papers | 4 compositions
- compositions: Sr5In2Sb6 (2); Sr5In1.9Zn0.1Sb6 (1); Sr5In1.975Zn0.025Sb6 (1); Sr5In1.95Zn0.05Sb6 (1)
- dopant candidates (<5% at.): Zn (3)
- sample form: Other (4); Bulk (1)
- measured range: 298-776 K (5th-95th pct of 19 curves)
- [ref 1] TEDesignLab / ICSD: Sr5(InSb3)2 Pbam (55) mp-649033 [hull=0.000, icsd=1, PRIMARY]
- papers: https://doi.org/10.1039/c5ta01967b (Enhanced thermoelectric properties of Sr5In2Sb6via Zn-doping) | https://doi.org/10.1088/0953-8984/27/1/015801 (Thermoelectric properties and electronic structure of the Zintl phase ...)

## K-N-O
- rank 1229 | 5 samples | 1 papers | 1 compositions
- compositions: KNO3 (5)
- measured range: 611-679 K (5th-95th pct of 5 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): KN3O4 P2_1/c (14) mp-3768 [hull=0.169, icsd=6, PRIMARY]; KNO3 Pnma (62) mp-5158 [hull=0.000, icsd=5, PRIMARY, AMBIGUOUS]; K2CuPb(NO2)6 Fm-3 (202) mp-19863 [hull=0.085, icsd=4, PRIMARY]; K2BaCo(NO2)6 Fm-3 (202) mp-24872 [hull=0.097, icsd=2, PRIMARY]; K2PrN5O17 Fdd2 (43) mp-1196176 [hull=0.174, icsd=2, PRIMARY]
- papers: https://doi.org/10.1299/kikaib.52.940 (Thermal conductivity measurement of molten salts by the transient hot-...)

## La-Ni-Si
- rank 1230 | 5 samples | 2 papers | 2 compositions
- compositions: La5Ni2Si3 (4); LaNi9Si4 (1)
- measured range: 13-728 K (5th-95th pct of 3 curves; full span incl. outliers 13-799 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): La(SiNi)2 I4/mmm (139) mp-5898 [hull=0.000, icsd=2, PRIMARY]; LaSi2Ni Cmcm (63) mp-1079037 [hull=0.000, icsd=2, PRIMARY]; LaSiNi4 Cmmm (65) mp-1071627 [hull=0.000, icsd=1, PRIMARY]; LaSiNi I4_1md (109) mp-7030 [hull=0.000, icsd=1, PRIMARY]; LaSi4Ni9 I4/mcm (140) mp-11726 [hull=0.000, icsd=1, PRIMARY]
- papers: https://doi.org/10.1007/s10909-017-1794-y (Inhomogeneous Superconducting Behaviour in \n                $$\\hbox ...) | https://doi.org/10.1103/physrevb.67.224428 (Crystal structure and Kondo lattice behavior of<mml:math xmlns:mml=\"h...)

## Mn-Mo-O-Sr
- rank 1231 | 5 samples | 2 papers | 5 compositions
- compositions: Sr1.8La0.2MnMoO6 (1); Sr1.7La0.3MnMoO6 (1); Sr2MnMoO6 (1); Sr1.9La0.1MnMoO6 (1); Sr3MnMo2O9 (1)
- dopant candidates (<5% at.): La (3)
- sample form: Bulk (4)
- measured range: 85-1246 K (5th-95th pct of 16 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Sr2MnMoO6 P4_2/n (86) mp-705116 [hull=0.007, icsd=1, PRIMARY, AMBIGUOUS]; Sr2MnMoO6 I4/m (87) mp-1095141 [hull=0.008, icsd=1]
- papers: https://doi.org/10.1016/j.jascer.2013.06.006 (La doped effects on structure and thermoelectric properties of Sr2MnMo...) | https://doi.org/10.1016/j.jallcom.2015.11.204 (Electronic properties in intrinsically disordered double perovskites: ...)

## Mn-Ni-Sn
- rank 1232 | 5 samples | 3 papers | 3 compositions
- compositions: Ni50Mn36Sn14 (2); Ni50Mn37Sn13 (2); Ni2MnSn (1)
- sample form: Bulk (2)
- measured range: 14-400 K (5th-95th pct of 5 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): MnNi2Sn Fm-3m (225) mp-20440 [hull=0.010, icsd=12, PRIMARY]; Mn2NiSn F-43m (216) mp-1221821 [hull=0.197, PRIMARY]; Mn3Ni3Sn2 R3m (160) mp-1221922 [hull=0.070, PRIMARY]; Mn3Ni4Sn R-3m (166) mp-1221827 [hull=0.033, PRIMARY]; Mn5Ni8Sn3 R-3m (166) mp-1221389 [hull=0.023, PRIMARY]
- papers: https://doi.org/10.1016/j.jmmm.2006.10.1040 (Magnetic and thermoelectric properties of Ni50Mn36Sn14 in high-magneti...) | https://doi.org/10.1063/1.4930592 (Magnetic field dependence of electrical resistivity and thermopower in...) | https://doi.org/10.1088/0305-4608/11/7/017 (The transport properties of Heusler alloys: 'ideal' local moment ferro...)

## Mo-O-Sr-V
- rank 1233 | 5 samples | 3 papers | 5 compositions
- compositions: Sr1.9VMoO6 (1); Sr2VMoO6 (1); Sr1.8VMoO6 (1); Sr(V0.5Mo0.5)O3 (1); SrV0.5Mo0.5O3 (1)
- sample form: rod-shaped (1)
- measured range: 300-1123 K (5th-95th pct of 5 curves; full span incl. outliers 300-1173 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Sr2VMoO6 P4/mmm (123) mp-1218447 [hull=0.034, PRIMARY]
- papers: https://doi.org/10.1063/1.4811715 (Electrical conductivity of Sr<sub>2−x</sub>VMoO<sub>6−y</sub>(x = 0.0,...) | https://doi.org/10.1002/fuce.201000070 (Study of the Crystal Structure, Thermal Stability and Conductivity of ...) | https://doi.org/10.1021/acsami.9b15584 (Vanadium-Doped Strontium Molybdate with Exsolved Ni Nanoparticles as A...)

## Mo-O-Tl
- rank 1234 | 5 samples | 3 papers | 3 compositions
- compositions: Tl0.3Mo0.96W0.04O3 (2); Tl0.3MoO3 (2); Tl0.24K0.06MoO3 (1)
- dopant candidates (<5% at.): W (2), K (1)
- measured range: 25-298 K (5th-95th pct of 5 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Tl2MoO4 C2 (5) mp-18938 [hull=0.000, icsd=2, PRIMARY]; HfTl8(MoO4)6 C2/m (12) mp-645513 [hull=0.000, icsd=1, PRIMARY]; TlMo6O17 P-3m1 (164) mp-32096 [hull=0.009, icsd=1, PRIMARY]; Tl(MoO3)3 C2/m (12) mp-615697 [hull=0.042, icsd=1, PRIMARY]; Tl2Mo7O22 C2/c (15) mp-704535 [hull=0.016, icsd=1, PRIMARY]
- papers: https://doi.org/10.1016/s0375-9601(03)00688-1 (Transverse thermoelectric power in the molybdenum blue bronze K0.3MoO3) | https://doi.org/10.1016/0038-1098(93)90513-m (Effect of impurities on thermoelectric power in thallium blue bronze T...) | https://doi.org/10.1016/0038-1098(85)90863-4 (Charge-density wave instability and nonlinear transport in Tl0.3MoO3 a...)

## N-O-Ti
- rank 1235 | 5 samples | 3 papers | 5 compositions
- compositions: (TiO2)0.8(TiN)0.2 (1); N0.2TiO2 (1); Ti34O34N33 (1); Ti33O29N37 (1); Ti41O12N47 (1)
- sample form: Bulk (1)
- measured range: 80-1065 K (5th-95th pct of 8 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ti(NO3)4 P2_1/c (14) mp-30998 [hull=0.000, icsd=1, PRIMARY]; Ti17(NO4)6 Pmmn (59) mp-779712 [hull=0.030, PRIMARY, AMBIGUOUS]; Ti2N2O P1 (1) mp-776280 [hull=0.053, PRIMARY]; Ti3N2O3 Cm (8) mp-754790 [hull=0.005, PRIMARY, AMBIGUOUS]; Ti3NO4 Cmcm (63) mp-755920 [hull=0.036, PRIMARY]
- papers: https://doi.org/10.2497/jjspm.60.60 (Study of Phases and Thermoelectric Properties of TiO2-TiN Compacts Fab...) | https://doi.org/10.1016/j.physb.2012.06.019 (Physical properties of NxTiO2 prepared by sol–gel route) | https://doi.org/10.1116/1.580516 (Study of TiO<i>x</i>N<i>y</i> thin film selective surfaces produced by...)

## Na-O-Sb-Ti
- rank 1236 | 5 samples | 1 papers | 1 compositions
- compositions: Na2Ti2Sb2O (5)
- measured range: 10-297 K (5th-95th pct of 5 curves; full span incl. outliers 10-349 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Na2Ti2Sb2O I4/mmm (139) mp-6328 [hull=0.000, icsd=20, PRIMARY]
- papers: https://doi.org/10.1103/physrevb.80.144516 (Physical properties of the layered pnictide oxidesNa2Ti2P2O(P=As,Sb))

## Na-Pb-Sb-Te
- rank 1237 | 5 samples | 1 papers | 3 compositions
- compositions: NaPbSbTe3 (2); NaPb6SbTe8 (2); Na1.10Pb5.90Sb0.85Te8 (1)
- sample form: Bulk (3); Polycrystal (2)
- measured range: 299-914 K (5th-95th pct of 17 curves)
- papers: https://doi.org/10.1021/jacs.8b04193 (Absence of Nanostructuring in NaPbmSbTem+2: Solid Solutions with High ...)

## Nb-O-Ti
- rank 1238 | 5 samples | 3 papers | 5 compositions
- compositions: Ti0.83Nb0.17(O0.955N0.045)2 (1); Nb0.2Ti0.8O2 (1); Ti0.80Nb0.20O2 (1); Ti0.60Nb0.40O2 (1); Ti0.40Nb0.60O2 (1)
- dopant candidates (<5% at.): N (1)
- sample form: Bulk (4)
- measured range: 102-1057 K (5th-95th pct of 18 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): TiNb3O6 R-3 (148) mp-29699 [hull=0.000, icsd=1, PRIMARY]; Li2Ti7Nb6O30 P3 (143) mp-759382 [hull=0.055, PRIMARY]; Ti3NbO8 P-1 (2) mp-758428 [hull=0.032, PRIMARY, AMBIGUOUS]; Ti15NbO32 P-4m2 (115) mp-1099073 [hull=0.003, PRIMARY]; Ti5Nb2O14 Cmmm (65) mp-758324 [hull=0.033, PRIMARY]
- papers: https://doi.org/10.1021/jp401132g (Chemical Tuning of TiO2Nanoparticles and Sintered Compacts for Enhance...) | https://doi.org/10.1063/1.2362990 (Carrier generation and transport properties of heavily Nb-doped anatas...) | https://doi.org/10.1016/j.ceramint.2017.08.091 (Thermoelectric properties of Nb-doped TiO2- ceramics reduced at elevat...)

## Nd-Ni
- rank 1239 | 5 samples | 1 papers | 1 compositions
- compositions: NdNi5 (5)
- measured range: 76-280 K (5th-95th pct of 5 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): NdNi5 P6/mmm (191) mp-1824 [hull=0.000, icsd=10, PRIMARY]; NdNi2 Fd-3m (227) mp-1343 [hull=0.012, icsd=5, PRIMARY]; Nd2Ni7 P6_3/mmc (194) mp-1202657 [hull=0.001, icsd=3, PRIMARY]; NdNi3 R-3m (166) mp-1095561 [hull=0.000, icsd=3, PRIMARY]; NdNi Cmcm (63) mp-999339 [hull=0.000, icsd=2, PRIMARY]
- papers: https://doi.org/10.1038/s41598-020-70646-2 (Magnetotransport and magnetic properties of amorphous $$\\mathrm{NdNi}...)

## Nd-O-Sb
- rank 1240 | 5 samples | 2 papers | 1 compositions
- compositions: Nd2SbO2 (5)
- measured range: 12-392 K (5th-95th pct of 5 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Nd3Sb5O12 I-43m (217) mp-3782 [hull=0.000, icsd=2, PRIMARY]; Nd3SbO7 Cmcm (63) mp-769366 [hull=0.000, icsd=1, PRIMARY]; Nd2SbO2 Pmmn (59) mp-1105626 [hull=0.000, icsd=1, PRIMARY]; NdSbO4 P2_1/c (14) mp-13195 [hull=0.000, icsd=1, PRIMARY]; NdSbO3 Pm-3m (221) mp-1206341 [hull=0.768, PRIMARY]
- papers: https://doi.org/10.1021/ja209652d (Decoupling the Electrical Conductivity and Seebeck Coefficient in theR...) | https://doi.org/10.1021/acs.chemmater.7b03996 (Rare-Earth Pnictide Oxides (RE,Ca)mPnnOm (Pn = Sb, Bi): A Review of Cr...)

## Ni-O-Pr
- rank 1241 | 5 samples | 4 papers | 5 compositions
- compositions: Pr2Ni0.75Cu0.25Ga0.05O4 (1); Pr0.82Sr0.18NiO3 (1); Pr0.82Sr0.18NiO2 (1); Pr4Ni3O10 (1); Pr2NiO4 (1)
- dopant candidates (<5% at.): Sr (2), Cu (1), Ga (1)
- measured range: 12-1123 K (5th-95th pct of 5 curves; full span incl. outliers 12-1532 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): PrNiO3 Pnma (62) mp-25590 [hull=0.000, icsd=14, PRIMARY]; Pr2NiO4 Cmce (64) mp-19434 [hull=0.048, icsd=1, PRIMARY]; Pr10Ni5O22 P1 (1) mp-1173634 [hull=0.458, PRIMARY]; Pr8Ni4O17 P1 (1) mp-1173645 [hull=0.203, PRIMARY]; PrNiO3 R-3c (167) mp-19170 [hull=0.004, icsd=2]
- papers: https://doi.org/10.1016/j.ceramint.2015.06.028 (Electrochemical characterization of B-site cation-excess Pr2Ni0.75Cu0....) | https://doi.org/10.1038/s41467-022-32065-x (Pressure-induced monotonic enhancement of Tc to over 30 K in supercond...) | https://doi.org/10.1006/jssc.1995.1269 (Synthesis, Structure, and Properties of Ln4Ni3O10-δ (Ln = La, Pr, and Nd))

## Ni-Pd-Sn-Zr
- rank 1242 | 5 samples | 3 papers | 4 compositions
- compositions: ZrNi0.8Pd0.2Sn0.99Sb0.01 (2); ZrNi0.7Pd0.3Sn (1); ZrNi0.8Pd0.2Sn (1); ZrNi0.5Pd0.5Sn0.99Sb0.01 (1)
- dopant candidates (<5% at.): Sb (3)
- solid-solution axis: Ni/(Ni+Pd) spans 0.50-0.80 (median 0.80) over 4 compositions
     ISOELECTRONIC SERIES: the parent compound depends on the composition, not on this host. Near either end the minor element is a dilute substituent; in the middle it is a genuine alloy. Record the axis, not one parent -- and note the 5% split used the whole formula, not the sublattice, so its cut lands at a different level on each site.
- measured range: 294-1006 K (5th-95th pct of 20 curves)
- papers: https://doi.org/10.2320/matertrans.47.1453 (Substitution Effect on Thermoelectric Properties of ZrNiSn Based Half-...) | https://doi.org/10.1063/1.1425459 (Effects of partial substitution of Ni by Pd on the thermoelectric prop...) | https://doi.org/10.1023/a:1017928800031 (Thermoelectric properties of ZrNiSn-based half-Heusler compounds by so...)

## Ni-Sb-U
- rank 1243 | 5 samples | 2 papers | 3 compositions
- compositions: UNi0.5Sb2 (2); U3Ni3Sb4 (2); U3Ni2.9Co0.1Sb4 (1)
- dopant candidates (<5% at.): Co (1)
- sample form: Polycrystal (3); SingleCrystal (2)
- measured range: 11-345 K (5th-95th pct of 23 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): UNiSb2 P4/nmm (129) mp-1080551 [hull=0.027, icsd=1, PRIMARY]; U2NiSb4 P-4m2 (115) mp-1216654 [hull=0.000, PRIMARY]
- papers: https://doi.org/10.1016/j.intermet.2015.01.008 (Low-temperature hysteresis in transport properties of UNi0.5Sb2) | https://doi.org/10.1063/1.5128593 (Uranium-based materials for thermoelectric applications)

## Ni-Ti-Zr
- rank 1244 | 5 samples | 3 papers | 4 compositions
- compositions: Ti45Zr38Ni17 (2); Ti45Zr35Ni17Cu (1); Ti53Zr27Ni20 (1); Ti54Zr26Ni20 (1)
- dopant candidates (<5% at.): Cu (1)
- measured range: 20-415 K (5th-95th pct of 3 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): ZrTi2Ni9 R-3m (166) mp-1095547 [hull=0.020, icsd=1, PRIMARY]; Zr12Ti4Ni8O R-3m (166) mp-1215809 [hull=0.907, PRIMARY]; ZrTiNi Amm2 (38) mp-1215337 [hull=0.061, PRIMARY]; ZrTiNi2 Amm2 (38) mp-1215191 [hull=0.041, PRIMARY]; ZrTi2Ni9 R3m (160) mp-1215266 [hull=0.018]
- papers: https://doi.org/10.1016/j.physb.2007.01.018 (Preparation and transport properties of a bulk icosahedral quasicrysta...) | https://doi.org/10.1016/s0375-9601(02)01227-6 (Superconductivity of TiZrNi alloys containing quasicrystals) | https://doi.org/10.1557/proc-478-321 (Measurement of the Thermoelectric Properties of Quasicrystalline AlPdR...)

## O-P-Te
- rank 1245 | 5 samples | 1 papers | 1 compositions
- compositions: Te2P2O9 (5)
- sample form: Polycrystal (4); FoamedBulk (1)
- measured range: 299-573 K (5th-95th pct of 5 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Te3P2O11 P2_1/c (14) mp-3764 [hull=0.000, icsd=2, PRIMARY]; Te2PO7 Pca2_1 (29) mp-1198178 [hull=0.090, icsd=2, PRIMARY]; Te4P2O13 P2_1/c (14) mp-29215 [hull=0.000, icsd=1, PRIMARY]; Te2P2O9 Cc (9) mp-1193939 [hull=0.000, icsd=1, PRIMARY]; Te2(PO4)3 R-3 (148) mp-766504 [hull=0.000, PRIMARY]
- papers: https://doi.org/10.1021/acs.cgd.8b00680 (Czochralski Growth and Characterization of a Novel Nonlinear Optical C...)

## O-Si-Y-Yb
- rank 1246 | 5 samples | 2 papers | 5 compositions
- compositions: YbYSiO5 (1); (Y0.6Yb0.4)2SiO5 (1); (Y0.8Yb0.2)2SiO5 (1); (Y0.4Yb0.6)2SiO5 (1); (Y0.2Yb0.8)2SiO5 (1)
- sample form: Bulk (5)
- solid-solution axis: Y/(Y+Yb) spans 0.20-0.80 (median 0.50) over 5 compositions
     ISOELECTRONIC SERIES: the parent compound depends on the composition, not on this host. Near either end the minor element is a dilute substituent; in the middle it is a genuine alloy. Record the axis, not one parent -- and note the 5% split used the whole formula, not the sublattice, so its cut lands at a different level on each site.
- measured range: 293-1274 K (5th-95th pct of 5 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Yb3Y(Si2O7)2 P1 (1) mp-1215859 [hull=0.010, PRIMARY]
- papers: https://doi.org/10.1016/j.actamat.2020.06.012 (Tailoring thermal properties of multi-component rare earth monosilicates) | https://doi.org/10.1016/j.jeurceramsoc.2021.07.029 (Improved thermophysical properties of rare-earth monosilicates applied...)

## O-W-Zr
- rank 1247 | 5 samples | 1 papers | 1 compositions
- compositions: ZrW2O8 (5)
- measured range: 10-386 K (5th-95th pct of 5 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Zr(WO4)2 P2_13 (198) mp-18778 [hull=0.074, icsd=7, PRIMARY]; Zr9W4O3 P6_3/mmc (194) mp-1207430 [hull=0.588, PRIMARY]; ZrW2O11 I4_1cd (110) mp-1207524 [hull=0.439, PRIMARY]
- papers: https://doi.org/10.1016/j.ssc.2005.01.031 (Unusual thermal conductivity of the negative thermal expansion materia...)

## P
- rank 1248 | 5 samples | 3 papers | 2 compositions
- compositions: P (4); PP (1)
- sample form: Bulk (1); SingleCrystal (1)
- measured range: 11-365 K (5th-95th pct of 8 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): P Cmce (64) mp-157 [hull=0.030, icsd=25, PRIMARY]; P Pm-3m (221) mp-53 [hull=0.141, icsd=5]; P R-3m (166) mp-130 [hull=0.079, icsd=4]; P P-1 (2) mp-1198724 [hull=0.000, icsd=2]; P Imma (74) mp-7245 [hull=0.089, icsd=1]
- papers: https://doi.org/10.1016/0379-6779(93)90918-m (Thermoelectric power in reticulate doped polymers) | https://doi.org/10.1063/1.4905636 (Thermoelectric power of bulk black-phosphorus) | https://doi.org/10.1063/1.4943084 (Large anisotropic thermal transport properties observed in bulk single...)

## Pb-S-Sb
- rank 1249 | 5 samples | 2 papers | 4 compositions
- compositions: FePb4Sb6S14 (2); Sn0.04FePb4Sb5.96S14 (1); Sn0.08FePb4Sb5.92S14 (1); Pb0.9Cl0.1Sb2S3 (1)
- dopant candidates (<5% at.): Fe (4), Sn (2), Cl (1)
- measured range: 165-735 K (5th-95th pct of 9 curves)
- [ref 1] TEDesignLab / ICSD: Sb6Pb4S13 P1 (1) mp-27907 [hull=0.020, icsd=1, PRIMARY]; Sb2Pb2S5 (62) [PRIMARY]
- [ref 2] MP, ranked by ICSD evidence: Sb8(PbS5)3 C2/c (15) mp-22737 [hull=0.000, icsd=3, PRIMARY]; Sb8Pb7S19 C2/c (15) mp-641987 [hull=0.012, icsd=2, PRIMARY]; Sb4Pb5S11 P2_1/c (14) mp-638022 [hull=0.009, icsd=1, PRIMARY]; MnSb6(Pb2S7)2 P2_1/c (14) mp-683891 [hull=0.008, icsd=1, PRIMARY]
- papers: https://doi.org/10.1016/j.jallcom.2004.08.041 (Electronic structure and thermoelectric properties of the thioantimona...) | https://doi.org/10.1016/j.jallcom.2015.10.052 (High performance thermoelectrics from earth-abundant materials: Enhanc...)

## Ru-Sn-U
- rank 1250 | 5 samples | 3 papers | 3 compositions
- compositions: U2Ru2Sn (3); URuSn3 (1); 	U2Ru2Sn (1)
- sample form: Bulk (2); Polycrystal (2); SingleCrystal (1)
- measured range: 10-399 K (5th-95th pct of 14 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): USnRu P-62m (189) mp-19811 [hull=0.003, icsd=6, PRIMARY]; U2SnRu2 P4/mbm (127) mp-20705 [hull=0.000, icsd=1, PRIMARY]
- papers: https://doi.org/10.1016/s0921-4526(01)01087-0 (U2Ru2Sn: a new Kondo insulator?) | https://doi.org/10.1016/s0921-4526(90)81072-v (Magnetic and transport properties of new uranium compounds U3Sn5 and U...) | https://doi.org/10.1103/physrevb.67.075111 (Magnetic, thermodynamic, NMR, and transport properties of the heavy-fe...)
