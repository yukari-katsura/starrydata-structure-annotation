# Host systems -- chunk 036 of 73

Ranks 1751-1800 by sample count. These 50 host systems cover 150 samples (0.29% of the TE set); cumulative through this chunk: 95.32%.

Assign each host system a structural prototype from `data/annotated/taxonomy/prototypes_seed_v3.json`, or propose a new one in `taxonomy/prototypes_proposed.jsonl` first. Append results to `data/annotated/annotations/family_assignments.jsonl`.

The hand-entered MaterialFamily labels are deliberately NOT shown here -- they are held out in `df_host_systems.parquet` to validate this classification later. Decide from the compositions.

A "seed hypothesis" line means the taxonomy already names this host under that prototype. Confirm it against the compositions rather than accepting it; two or more listed means the host is mixed and needs splitting per composition.

Evidence follows the project precedence. Your judgement about the thermoelectric chemistry decides the prototype. [ref 1] is TEDesignLab, ICSD-backed and thermoelectric-specific -- prefer it. [ref 2] is Materials Project. Within a formula, polymorphs are ranked by ICSD reference count and the top one is marked PRIMARY -- not by e_above_hull, which is unusable for layered chalcogenides in the 2019 dump (Sb2Te3 R-3m carries 26 ICSD refs at hull 1.02). A primary resting on fewer than 5 ICSD references is flagged weak; the ambient phase may simply be absent from the snapshot, as it is for Bi2Se3.

While you have the host in view, also record what each minor element DOES, in `dopant_roles` -- the role follows from the prototype and cannot be judged without it. A median host has 2 such elements. Not everything listed is a dopant: O, C, N and H are usually milling or pressing residue, and an element just under 5 at.% may be an alloying end member rather than dilute doping. The doping LEVEL is computed later from the parsed fractions -- do not work it out by hand here.

A polymorph list is NOT a thermal sequence. SnSe has three known structures but only Pnma -> Cmcm happens on heating; rocksalt SnSe is metastable (2 icsd refs against 32). Put thermally reached phases in `phases` with their transition temperatures, and everything else in `other_polymorphs` with an occurrence reason. hull and icsd counts are shown to help you tell them apart.

A host may need MORE THAN ONE prototype. Transport is measured across a wide window and many thermoelectrics transform inside it, so where a "MEASUREMENT CROSSES A TRANSITION" line appears, record each phase with its own temperature range in the `phases` field. Transition temperatures shown are approximate and composition-dependent.

Both references describe which phases EXIST in a chemistry, not which phase this paper made. Al-O-Zn is best attested as ZnAl2O4 spinel (227) while almost every sample in it is Al-doped wurtzite ZnO (186). Weigh them against the compositions; do not follow them blindly.

## K
- rank 1751 | 3 samples | 1 papers | 1 compositions
- compositions: K (3)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): K I4/mcm (140) mp-1078640 [hull=0.160, icsd=10, PRIMARY]; K Im-3m (229) mp-58 [hull=0.000, icsd=6]; K Pnma (62) mp-1080043 [hull=0.070, icsd=2]; K Fm-3m (225) mp-10157 [hull=0.010, icsd=1]; K P6_3/mmc (194) mp-1184755 [hull=0.011, icsd=1]
- papers: https://doi.org/10.1103/physrevb.20.3970 (Thermomagnetic and thermoelectric properties of potassium)

## K-O-Os
- rank 1752 | 3 samples | 2 papers | 1 compositions
- compositions: KOs2O6 (3)
- measured range: 11-680 K (5th-95th pct of 3 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): K(OsO3)2 Fd-3m (227) mp-4788 [hull=0.012, icsd=7, PRIMARY]; K2OsO6 I4/m (87) mp-1080446 [hull=0.264, icsd=1, PRIMARY]; K2OsO5 P-6 (174) mp-762088 [hull=0.000, PRIMARY, AMBIGUOUS]; KOsO3 Pm-3m (221) mp-1185009 [hull=0.041, PRIMARY]; K(OsO3)2 R3m (160) mp-675028 [hull=0.012]
- papers: https://doi.org/10.1103/physrevb.75.172501 (Manifestations of fine features of the density of states in the transp...) | https://doi.org/10.1016/j.physc.2007.03.023 (Chemical trends of superconducting properties in pyrochlore oxides)

## K-O-V
- rank 1753 | 3 samples | 1 papers | 3 compositions
- compositions: KVO3 (1); (K0.80Cs0.20)VO3 (1); (K0.80Li0.20)VO3 (1)
- dopant candidates (<5% at.): Cs (1), Li (1)
- measured range: 473-658 K (5th-95th pct of 3 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): KV3O8 P2_1/m (11) mp-19172 [hull=0.000, icsd=5, PRIMARY]; KVO3 Pbcm (57) mp-18815 [hull=0.000, icsd=3, PRIMARY]; KV6O11 P6_3/mmc (194) mp-25159 [hull=0.027, icsd=2, PRIMARY]; KV4O8 I4/m (87) mp-32412 [hull=0.031, icsd=2, PRIMARY]; K2V3O8 P4bm (100) mp-19596 [hull=0.000, icsd=2, PRIMARY]
- papers: https://doi.org/10.1007/bf02746039 (Thermoelectric power of ferroelectric potassium vanadate, cesium vanad...)

## La-Li-Nb-O
- rank 1754 | 3 samples | 1 papers | 2 compositions
- compositions: La0.33Li0.59NbO3 (2); La0.33Li0.44NbO3 (1)
- measured range: 24-295 K (5th-95th pct of 3 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Li2LaNb6O18 Pmmm (47) mp-1210870 [hull=0.099, PRIMARY]; Li4La3Nb12O36 C2/m (12) mp-762374 [hull=0.080, PRIMARY]; Li5La3Nb14O42 C2/m (12) mp-768083 [hull=0.086, PRIMARY]; Li5La3Nb2O12 P1 (1) mp-761986 [hull=0.054, PRIMARY, AMBIGUOUS]; Li5La4TiNb7O28 P1 (1) mp-781824 [hull=0.051, PRIMARY]
- papers: https://doi.org/10.1016/j.materresbull.2004.05.005 (Metallization of La1/3NbO3 by lithium incorporation)

## La-Mn-O-Sr-Ti
- rank 1755 | 3 samples | 2 papers | 2 compositions
- compositions: La0.5Sr0.5Mn0.5Ti0.5O3 (2); La0.7Sr0.3Mn0.7Ti0.3O3 (1)
- sample form: pellets (1)
- measured range: 108-1173 K (5th-95th pct of 3 curves; full span incl. outliers 108-1223 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Sr3La7Ti2Mn8O30 P1 (1) mp-694976 [hull=0.011, PRIMARY]; Sr3La7Ti3Mn7O30 P1 (1) mp-694908 [hull=0.018, PRIMARY]; Sr3LaTi2Mn2O12 R-3m (166) mp-1218525 [hull=0.022, PRIMARY]; Sr6La14Ti3Mn17O60 P1 (1) mp-1173230 [hull=0.018, PRIMARY]; SrLaTiMnO6 P2/c (13) mp-691117 [hull=0.017, PRIMARY]
- papers: https://doi.org/10.1063/1.4798364 (Neutron structural characterization and transport properties of <i>oxi...) | https://doi.org/10.1002/pssc.200304425 (Magnetism and giant magnetoresistance in La\n            <sub>0.7</sub...)

## La-Nd-Ni-O
- rank 1756 | 3 samples | 1 papers | 3 compositions
- compositions: Nd0.7La0.3NiO3 (1); Nd0.4La0.6NiO3 (1); Nd0.6La0.4NiO3 (1)
- measured range: 18-297 K (5th-95th pct of 3 curves)
- papers: https://doi.org/10.1088/1361-648x/accd38 (Metal–insulator transition in composition-tuned nickel oxide films)

## La-O
- rank 1757 | 3 samples | 2 papers | 2 compositions
- compositions: LaO (2); La2O3 (1)
- measured range: 12-302 K (5th-95th pct of 3 curves; full span incl. outliers 12-1386 K)
- [ref 1] TEDesignLab / ICSD: La2O3 P-3m1 (164) mp-1968 [hull=0.024, icsd=13, PRIMARY]; La2O3 (12); La2O3 (150)
- [ref 2] MP, ranked by ICSD evidence: LaO3 P6_3/m (176) mp-1078452 [hull=0.388, icsd=11, PRIMARY]; LaO2 P2_1/m (11) mp-1206559 [hull=0.135, icsd=1, PRIMARY]; LaO Fm-3m (225) mp-1206710 [hull=0.027, PRIMARY]; La9ErO15 P1 (1) mp-766452 [hull=0.040, PRIMARY]; La2O3 Ia-3 (206) mp-2292 [hull=0.000, icsd=4]
- papers: https://doi.org/10.1016/0375-9601(80)90035-3 (Transport properties of SmO) | https://doi.org/10.1016/j.tsf.2008.02.032 (Experimental determination of La2O3 thermal conductivity and its appli...)

## La-Os-Sb
- rank 1758 | 3 samples | 2 papers | 1 compositions
- compositions: LaOs4Sb12 (3)
- sample form: SingleCrystal (1)
- measured range: 11-291 K (5th-95th pct of 5 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): La(Sb3Os)4 Im-3 (204) mp-1106066 [hull=0.000, icsd=2, PRIMARY]
- papers: https://doi.org/10.1016/j.physb.2006.03.067 (Roles of spin fluctuations and rattling in magnetic and thermoelectric...) | https://doi.org/10.1103/physrevb.72.014519 (Transport properties of the heavy-fermion superconductorPrOs4Sb12)

## La-Pd-Si
- rank 1759 | 3 samples | 2 papers | 3 compositions
- compositions: Ce0.1La0.9Pd2Si2 (1); LaPd2Si2 (1); La2Pd3Si5 (1)
- dopant candidates (<5% at.): Ce (1)
- sample form: Bulk (2); Polycrystal (1)
- measured range: 12-286 K (5th-95th pct of 4 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): La(SiPd)2 I4/mmm (139) mp-4954 [hull=0.000, icsd=4, PRIMARY]; La3(Si3Pd10)2 Fm-3m (225) mp-1211466 [hull=0.000, PRIMARY]; LaSiPd P2_1/c (14) mp-1211246 [hull=0.000, PRIMARY]
- papers: https://doi.org/10.1016/0921-4526(93)90623-e (Thermoelectric power on Ce1−xLaxPd2Si2) | https://doi.org/10.1103/physrevb.65.144450 (Antiferromagnetism in the Kondo lattice compound<mml:math xmlns:mml=\"...)

## La-Ru-Sn
- rank 1760 | 3 samples | 2 papers | 1 compositions
- compositions: LaRuSn3 (3)
- sample form: Polycrystal (3)
- measured range: 10-298 K (5th-95th pct of 7 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): LaSn3Ru Pm-3n (223) mp-30756 [hull=0.000, icsd=3, PRIMARY]; La3Sn13Ru4 Pm-3n (223) mp-1196992 [hull=0.000, icsd=3, PRIMARY]; La2Sn4Ru Amm2 (38) mp-1223248 [hull=0.037, PRIMARY]; La(Sn3Ru2)2 I-42m (121) mp-1206665 [hull=0.000, PRIMARY]
- papers: https://doi.org/10.1088/0953-8984/1/40/023 (Electronic and magnetic properties of a new heavy-fermion compound, Ce...) | https://doi.org/10.1088/0953-8984/3/45/014 (Transport and magnetic properties of RERuSn3(RE=La, Ce, Pr, Nd, Sm): a...)

## La-Sb
- rank 1761 | 3 samples | 3 papers | 2 compositions
- compositions: La4Sb3 (2); LaSb (1)
- sample form: Bulk (1)
- measured range: 20-874 K (5th-95th pct of 3 curves; full span incl. outliers 20-988 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): LaSb Fm-3m (225) mp-1065 [hull=0.000, icsd=6, PRIMARY]; La4Sb3 I-43d (220) mp-1223 [hull=0.000, icsd=5, PRIMARY]; La2Sb I4/mmm (139) mp-759 [hull=0.000, icsd=4, PRIMARY]; LaSb2 Cmce (64) mp-1101942 [hull=0.000, icsd=2, PRIMARY]; La5Sb3 P6_3/mcm (193) mp-1106084 [hull=0.000, icsd=1, PRIMARY]
- papers: https://doi.org/10.1039/b914712h (High-temperature transport properties of complex antimonides with anti...) | https://doi.org/10.1007/s11664-010-1274-5 (High-Temperature Transport Properties of Yb4−x Sm x Sb3) | https://doi.org/10.1038/s41535-017-0038-3 (Possible Weyl fermions in the magnetic Kondo system CeSb)

## La-Sb-Te
- rank 1762 | 3 samples | 1 papers | 3 compositions
- compositions: La3Te3.20Sb0.80 (1); La3Te3.40Sb0.60 (1); La3Te3.35Sb0.65 (1)
- sample form: Bulk (3)
- measured range: 291-1274 K (5th-95th pct of 13 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): LaSbTe P4/nmm (129) mp-1018747 [hull=0.053, icsd=2, PRIMARY]; La4SbTe7 P-4m2 (115) mp-1223110 [hull=0.149, PRIMARY]; LaSbTe Pnma (62) mp-1185210 [hull=0.056]
- papers: https://doi.org/10.1103/physrevb.81.125205 (Electron and phonon scattering in the high-temperature thermoelectricL...)

## Li-Mo-O
- rank 1763 | 3 samples | 1 papers | 1 compositions
- compositions: Li0.33MoO3 (3)
- sample form: SingleCrystal (3)
- measured range: 96-507 K (5th-95th pct of 9 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): LiMoO2 R-3m (166) mp-19338 [hull=0.011, icsd=3, PRIMARY]; Li2MoO4 R-3 (148) mp-25080 [hull=0.000, icsd=1, PRIMARY, AMBIGUOUS]; Li12Mo5O17 P-1 (2) mp-1199885 [hull=0.018, icsd=1, PRIMARY]; Li4Mo3O8 R-3m (166) mp-690551 [hull=0.059, icsd=1, PRIMARY]; Li4MoO5 P-1 (2) mp-19117 [hull=0.000, icsd=1, PRIMARY]
- papers: https://doi.org/10.1063/1.4943071 (Anisotropic transport in the quasi-one-dimensional semiconductor Li0.3...)

## Li-Nd-O-Ti
- rank 1764 | 3 samples | 1 papers | 3 compositions
- compositions: (Nd0.55Li0.36)(Ti0.95Nb0.05)O3 (1); (Nd0.55Li0.36)TiO3 (1); (Nd0.55Li0.36)(Ti0.90Nb0.10)O3 (1)
- dopant candidates (<5% at.): Nb (2)
- sample form: Bulk (3)
- measured range: 300-651 K (5th-95th pct of 9 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): LiNdTi2O6 Pmc2_1 (26) mp-1105497 [hull=0.011, icsd=2, PRIMARY]; LiNdTiO4 P4/nmm (129) mp-10520 [hull=0.023, icsd=1, PRIMARY]; LiNdTi2O6 Pm (6) mp-1105323 [hull=0.036, icsd=1]; LiNdTi2O6 P4/nbm (125) mp-756581 [hull=0.077]
- papers: https://doi.org/10.1016/j.jallcom.2015.12.231 (Thermoelectric properties of Nb-doped (Nd 0.55 Li 0.36 )TiO 3 bulk cer...)

## Mg-Mn-Si
- rank 1765 | 3 samples | 1 papers | 3 compositions
- compositions: Mg1.7Mn0.3Si (1); Mg1.6Mn0.4Si (1); Mg1.8Mn0.2Si (1)
- measured range: 11-298 K (5th-95th pct of 12 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Mg14MnSi Amm2 (38) mp-1028099 [hull=0.123, PRIMARY, AMBIGUOUS]; Mg6MnSi Amm2 (38) mp-1023005 [hull=0.232, PRIMARY]; Mg14MnSi P-6m2 (187) mp-1028096 [hull=0.131]
- papers: https://doi.org/10.1016/j.jallcom.2016.08.095 (Correlation between the magnetic and thermoelectric properties in Mg2−...)

## Mg-Sb-Sn
- rank 1766 | 3 samples | 1 papers | 3 compositions
- compositions: Mg1.94Sn0.8Sb0.2 (1); Mg2.06Sn0.60Sb0.40 (1); Mg2.06Sn0.70Sb0.30 (1)
- sample form: Bulk (3)
- measured range: 302-775 K (5th-95th pct of 15 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Mg14SnSb P-6m2 (187) mp-1026621 [hull=0.043, PRIMARY]; Mg6SnSb Amm2 (38) mp-1021391 [hull=0.097, PRIMARY]; Mg14SnSb Amm2 (38) mp-1026644 [hull=0.056]
- papers: https://doi.org/10.1016/j.mtphys.2020.100327 (Thermodynamic criterions of the thermoelectric performance enhancement...)

## Mg-Sb-Yb
- rank 1767 | 3 samples | 1 papers | 1 compositions
- compositions: YbMg2Sb2 (3)
- measured range: 298-650 K (5th-95th pct of 3 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Yb(MgSb)2 P-3m1 (164) mp-10996 [hull=0.000, PRIMARY]
- papers: https://doi.org/10.1016/s1002-0721(12)60398-6 (Zintl phase compounds AM2Sb2 (A=Ca, Sr, Ba, Eu, Yb; M=Zn, Cd) and thei...)

## Mn-Ni-Sb
- rank 1768 | 3 samples | 1 papers | 2 compositions
- compositions: NiMnSb (2); NiTi0.1Mn0.9Sb (1)
- dopant candidates (<5% at.): Ti (1)
- measured range: 270-300 K (5th-95th pct of 4 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): MnNiSb F-43m (216) mp-600124 [hull=0.000, icsd=8, PRIMARY]; MnNi2Sb Fm-3m (225) mp-5124 [hull=0.067, icsd=3, PRIMARY]; Mn2NiSb F-43m (216) mp-1206364 [hull=0.223, PRIMARY]; Mn3Ni4Sb R-3m (166) mp-1221776 [hull=0.062, PRIMARY]; MnNiSb2 P-3m1 (164) mp-1221333 [hull=0.042, PRIMARY]
- papers: https://doi.org/10.1007/s100510070055 (Galvanomagnetic properties of disordered Mn semi-Heusler phases with A...)

## Mo-N-O-Sr
- rank 1769 | 3 samples | 1 papers | 3 compositions
- compositions: SrMoO1.81N1.19 (1); SrMoO1.95N1.05 (1); SrMoO1.73N1.27 (1)
- sample form: Bulk (3)
- measured range: 318-636 K (5th-95th pct of 9 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Sr4MoN4O P2_1/m (11) mp-19649 [hull=0.175, icsd=2, PRIMARY]
- papers: https://doi.org/10.1016/j.jssc.2007.06.035 (Synthesis, Mo-valence state, thermal stability and thermoelectric prop...)

## N-Nb-Sc
- rank 1770 | 3 samples | 1 papers | 3 compositions
- compositions: Sc0.87Nb0.13N (1); Sc0.82Nb0.18N (1); Sc0.75Nb0.25N (1)
- measured range: 298-805 K (5th-95th pct of 3 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): ScNbN P-3m1 (164) mp-1219256 [hull=0.312, PRIMARY]
- papers: https://doi.org/10.1063/1.4993913 (Reduction of the thermal conductivity of the thermoelectric material S...)

## N-Np-U
- rank 1771 | 3 samples | 1 papers | 3 compositions
- compositions: (UN)25(NpN)75 (1); (UN)75(NpN)25 (1); (UN)50(NpN)50 (1)
- measured range: 760-1628 K (5th-95th pct of 3 curves)
- papers: https://doi.org/10.1016/s0925-8388(98)00168-6 (Thermal conductivity of actinide mononitride solid solutions)

## N-O-Ta
- rank 1772 | 3 samples | 1 papers | 1 compositions
- compositions: TaON (3)
- measured range: 11-299 K (5th-95th pct of 3 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): TaNO P2_1/c (14) mp-4165 [hull=0.000, icsd=6, PRIMARY]; Ta2N3O P6/mmm (191) mp-1019262 [hull=0.969, icsd=1, PRIMARY]; Ta3NO6 Cm (8) mp-1193678 [hull=0.000, icsd=1, PRIMARY]; TaN3O8 I-42m (121) mp-1208577 [hull=2.165, PRIMARY]; TaNO C2/m (12) mp-5813 [hull=0.012, icsd=5]
- papers: https://doi.org/10.1021/cm402720d (High-Mobility Electron Conduction in Oxynitride: Anatase TaON)

## N-Si-Ta
- rank 1773 | 3 samples | 1 papers | 3 compositions
- compositions: Ta0.914Si0.086N0.56 (1); Ta0.89Si0.11N0.56 (1); Ta0.87Si0.13N0.56 (1)
- measured range: 21-305 K (5th-95th pct of 3 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ta5Si3N P6_3/mcm (193) mp-1208335 [hull=0.036, PRIMARY]
- papers: https://doi.org/10.1063/1.4766904 (Electrical and optical properties of Ta-Si-N thin films deposited by r...)

## N-Th
- rank 1774 | 3 samples | 3 papers | 1 compositions
- compositions: ThN (3)
- sample form: compact (1)
- measured range: 76-860 K (5th-95th pct of 4 curves; full span incl. outliers 76-1701 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): ThN Fm-3m (225) mp-834 [hull=0.000, icsd=24, PRIMARY]; Th3N4 R-3m (166) mp-467 [hull=0.000, icsd=5, PRIMARY]; Th2N3 P-3m1 (164) mp-1940 [hull=0.118, icsd=4, PRIMARY]; ThN2 Fm-3m (225) mp-1072204 [hull=0.622, icsd=1, PRIMARY]
- papers: https://doi.org/10.1016/j.jnucmat.2019.151760 (Thermophysical properties of thorium mononitride from 298 to 1700 K) | https://doi.org/10.1016/j.nucengdes.2019.110317 (Reactor performance and safety characteristics of ThN-UN fuel concepts...) | https://doi.org/10.1016/0022-3697(67)90224-7 (Electrical properties of thorium nitrides)

## N-Th-U
- rank 1775 | 3 samples | 1 papers | 3 compositions
- compositions: (ThN)40.58(UN)59.42 (1); (ThN)20.39(UN)79.61 (1); (ThN)66.54(UN)33.46 (1)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): ThUN2 P4/mmm (123) mp-1217284 [hull=0.077, PRIMARY]
- papers: https://doi.org/10.1016/j.nucengdes.2019.110317 (Reactor performance and safety characteristics of ThN-UN fuel concepts...)

## Na-Pb-Te
- rank 1776 | 3 samples | 2 papers | 2 compositions
- compositions: Pb0.90Na0.10Te0.450 (2); Na1.06Pb7.94Sb0.85Te10 (1)
- dopant candidates (<5% at.): Sb (1)
- sample form: Bulk (1)
- measured range: 312-885 K (5th-95th pct of 14 curves)
- papers: https://doi.org/10.1021/jacs.8b04193 (Absence of Nanostructuring in NaPbmSbTem+2: Solid Solutions with High ...) | https://doi.org/10.1021/acs.chemmater.7b05091 (Sodium Substitution in Lead Telluride)

## Na-Sb-Sn-Te
- rank 1777 | 3 samples | 1 papers | 3 compositions
- compositions: NaSn4SbTe6 (1); NaSn5SbTe7 (1); NaSn3SbTe5 (1)
- sample form: Bulk (3)
- measured range: 301-873 K (5th-95th pct of 15 curves)
- papers: https://doi.org/10.1021/jacs.0c05650 (Contrasting SnTe–NaSbTe2 and SnTe–NaBiTe2 Thermoelectric Alloys: High ...)

## Nb-Te
- rank 1778 | 3 samples | 3 papers | 2 compositions
- compositions: NbTe2 (2); Nb3Te4 (1)
- sample form: SingleCrystal (2); Bulk (1)
- measured range: 10-303 K (5th-95th pct of 6 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): NbTe4 P4/mcc (124) mp-20196 [hull=0.013, icsd=14, PRIMARY]; Nb3Te4 P6_3/m (176) mp-7564 [hull=0.000, icsd=2, PRIMARY]; NbTe2 C2/m (12) mp-11675 [hull=0.000, icsd=2, PRIMARY]; Nb5Te4 I4/m (87) mp-30797 [hull=0.000, icsd=2, PRIMARY]; Nb12TlTe15As P-6 (174) mp-1220809 [hull=0.015, PRIMARY]
- papers: https://doi.org/10.1063/1.4913967 (Rich structural phase diagram and thermoelectric properties of layered...) | https://doi.org/10.1209/0295-5075/109/17003 (Structural, electrical, and thermoelectric properties of distorted 1T-...) | https://doi.org/10.1143/jjap.23.851 (Electrical Properties of a Quasi-One-Dimensional Nb3Te4Single Crystal)

## Nd-Ni-O-Sm
- rank 1779 | 3 samples | 1 papers | 1 compositions
- compositions: Sm0.75Nd0.25NiO3 (3)
- measured range: 299-483 K (5th-95th pct of 3 curves)
- papers: https://doi.org/10.1021/acsami.9b12609 (A d-Band Electron Correlated Thermoelectric Thermistor Established in ...)

## Nd-O-Sn-Yb-Zr
- rank 1780 | 3 samples | 1 papers | 3 compositions
- compositions: (Yb2Zr2O7)0.6(Nd2Sn2O7)0.4 (1); (Yb2Zr2O7)0.5(Nd2Sn2O7)0.5 (1); (Yb2Zr2O7)0.4(Nd2Sn2O7)0.6 (1)
- sample form: Bulk (3)
- measured range: 298-1273 K (5th-95th pct of 3 curves)
- papers: https://doi.org/10.1111/jace.13979 (Low Thermal Conductivity of Rare-Earth Zirconate-Stannate Solid Soluti...)

## Nd-O-Sr-Ti
- rank 1781 | 3 samples | 1 papers | 3 compositions
- compositions: Nd0.3Sr0.7TiO3 (1); Nd0.7Sr0.3TiO3 (1); Nd0.5Sr0.5TiO3 (1)
- measured range: 78-308 K (5th-95th pct of 3 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): SrNd2Ti4O12 P4/mmm (123) mp-1218162 [hull=0.099, PRIMARY]
- papers: https://doi.org/10.1016/j.jallcom.2003.11.021 (Band filling dependence of the electrical transport of Nd1−xAxTiO3 (A=...)

## Nd-Pr
- rank 1782 | 3 samples | 1 papers | 1 compositions
- compositions: Nd0.5Pr0.5 (3)
- measured range: 10-18 K (5th-95th pct of 3 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Pr3Nd I4/mmm (139) mp-1186724 [hull=0.019, PRIMARY]; PrNd P6_3/mmc (194) mp-1219716 [hull=0.000, PRIMARY]; PrNd3 I4/mmm (139) mp-975887 [hull=0.012, PRIMARY]; PrNd P-6m2 (187) mp-1186753 [hull=0.049]
- papers: https://doi.org/10.1038/ncomms15515 (Magnetic-field induced multiple topological phases in pyrochlore irida...)

## Ni-O-Si
- rank 1783 | 3 samples | 1 papers | 3 compositions
- compositions: Ni0.55(SiO2)0.45 (1); Ni0.26(SiO2)0.74 (1); Ni0.22(SiO2)0.78 (1)
- measured range: 10-253 K (5th-95th pct of 3 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Si(NiO2)2 Fd-3m (227) mp-18766 [hull=0.024, icsd=16, PRIMARY]; KNaCaSi8Ni5O24 P1 (1) mp-1223575 [hull=0.000, PRIMARY]; Li2Si12(NiO6)5 P-62c (190) mp-773694 [hull=0.064, PRIMARY]; Si(NiO2)2 Pnma (62) mp-19072 [hull=0.000, icsd=8]
- papers: https://doi.org/10.1103/physrevb.94.094202 (Resistivity minimum in granular composites and thin metallic films)

## Ni-Pt-Sb-Zr
- rank 1784 | 3 samples | 1 papers | 3 compositions
- compositions: Zr3Ni2.3Pt0.6Co0.1Sb4 (1); Zr3Ni1.7Pt0.6Co0.1Sb4 (1); Zr3Ni1.7Pt1.2Co0.1Sb4 (1)
- dopant candidates (<5% at.): Co (3)
- sample form: Other (3)
- measured range: 321-867 K (5th-95th pct of 10 curves)
- papers: https://doi.org/10.1063/1.4928168 (Thermoelectric properties and electronic transport analysis of Zr3Ni3S...)

## Ni-Sb-Sc-Tm
- rank 1785 | 3 samples | 1 papers | 3 compositions
- compositions: Sc0.75Tm0.25NiSb (1); Sc0.5Tm0.5NiSb (1); Sc0.25Tm0.75NiSb (1)
- sample form: Bulk (3)
- measured range: 13-917 K (5th-95th pct of 12 curves)
- papers: https://doi.org/10.1016/j.matchemphys.2019.01.056 (Enhanced thermoelectric power factor of half-Heusler solid solution Sc...)

## Np-Pd-Sn
- rank 1786 | 3 samples | 1 papers | 1 compositions
- compositions: NpPdSn (3)
- sample form: Polycrystal (3)
- measured range: 10-296 K (5th-95th pct of 6 curves)
- papers: https://doi.org/10.1103/physrevmaterials.2.074401 (Magnetic and electronic properties of NpPdSn)

## O-Pb-Ru
- rank 1787 | 3 samples | 2 papers | 3 compositions
- compositions: Pb2Ru2O7 (1); Pb1.8Eu0.2Ru2O7 (1); Pb2Ru2O6.5 (1)
- dopant candidates (<5% at.): Eu (1)
- measured range: 19-247 K (5th-95th pct of 4 curves; full span incl. outliers 19-296 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ru4Pb4O13 F-43m (216) mp-674149 [hull=0.000, PRIMARY]; RuPbO3 Pm-3m (221) mp-974337 [hull=0.177, PRIMARY]
- papers: https://doi.org/10.2497/jjspm.65.249 (Metal-insulator Crossover in Pb-Ru Based Oxides with Pyrochlore-type S...) | https://doi.org/10.1016/j.jcrysgro.2004.08.002 (Flux growth and physical properties of pyrochlore Pb2Ru2O6.5 single cr...)

## O-Rb-Te-V
- rank 1788 | 3 samples | 1 papers | 1 compositions
- compositions: Rb0.83V2Te2O (3)
- measured range: 11-300 K (5th-95th pct of 3 curves)
- papers: https://doi.org/10.1103/physrevb.97.214517 (Weak metal-metal transition in the vanadium oxytelluride \n<mml:math x...)

## O-Si-Yb
- rank 1789 | 3 samples | 3 papers | 2 compositions
- compositions: Yb2SiO5 (2); Yb2Si2O7 (1)
- sample form: Bulk (2)
- measured range: 293-1272 K (5th-95th pct of 3 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Yb2Si2O7 C2/m (12) mp-4300 [hull=0.000, icsd=5, PRIMARY]; BaYb6Si7O24 P2_1/m (11) mp-1201554 [hull=0.010, icsd=1, PRIMARY]; SrYb4Si5O17 P2_1/m (11) mp-1195911 [hull=0.011, icsd=1, PRIMARY]; Yb2SiO5 C2/c (15) mp-17702 [hull=0.197, icsd=1, PRIMARY]; Yb5Si3SO12 P6_3/m (176) mp-17648 [hull=0.098, icsd=1, PRIMARY]
- papers: https://doi.org/10.1111/jace.12618 (Theoretical Prediction and Experimental Investigation on the Thermal a...) | https://doi.org/10.1016/j.actamat.2020.06.012 (Tailoring thermal properties of multi-component rare earth monosilicates) | https://doi.org/10.1016/j.jeurceramsoc.2021.07.029 (Improved thermophysical properties of rare-earth monosilicates applied...)

## O-Sm-Sn-Yb-Zr
- rank 1790 | 3 samples | 1 papers | 3 compositions
- compositions: (Yb2Zr2O7)0.6(Sm2Sn2O7)0.4 (1); (Yb2Zr2O7)0.4(Sm2Sn2O7)0.6 (1); (Yb2Zr2O7)0.5(Sm2Sn2O7)0.5 (1)
- sample form: Bulk (3)
- measured range: 298-1272 K (5th-95th pct of 3 curves)
- papers: https://doi.org/10.1111/jace.13979 (Low Thermal Conductivity of Rare-Earth Zirconate-Stannate Solid Soluti...)

## O-Sr-Ti-V
- rank 1791 | 3 samples | 1 papers | 3 compositions
- compositions: SrTi0.33V0.67O3 (1); SrTi0.5V0.5O3 (1); SrTi0.67V0.33O3 (1)
- measured range: 10-298 K (5th-95th pct of 3 curves)
- papers: https://doi.org/10.1063/1.4836576 (Metal-insulator transition in SrTi<sub>1−</sub><sub><i>x</i></sub>V<su...)

## O-Y
- rank 1792 | 3 samples | 2 papers | 2 compositions
- compositions: Y2O3 (2); (Y2O3)99.5(CeO2)0.5 (1)
- dopant candidates (<5% at.): Ce (1)
- sample form: Bulk (1)
- measured range: 300-2078 K (5th-95th pct of 3 curves)
- [ref 1] TEDesignLab / ICSD: Y2O3 P-3m1 (164) mp-13061 [hull=0.071, icsd=3]; Y2O3 Pnma (62) mp-1178770 [hull=0.122, icsd=1]; Y2O3 (12)
- [ref 2] MP, ranked by ICSD evidence: Y2O3 Ia-3 (206) mp-2652 [hull=0.000, icsd=44, PRIMARY]; YO2 P2_1/m (11) mp-1206610 [hull=0.178, icsd=1, PRIMARY]; YO3 Pnma (62) mp-1189335 [hull=0.452, icsd=1, PRIMARY, AMBIGUOUS]; Y15TmO24 C2 (5) mp-757001 [hull=0.001, PRIMARY]; SmY15O24 C2 (5) mp-757791 [hull=0.001, PRIMARY]
- papers: https://doi.org/10.2109/jcersj1950.86.997_424 (Measurement of Thermal Diffusivity for Y<sub>2</sub>O<sub>3</sub> Sint...) | https://doi.org/10.1039/c9tc00506d (Thermally self-managing YAG:Ce–Al2O3color converters enabling high-bri...)

## O-Yb-Zr
- rank 1793 | 3 samples | 1 papers | 3 compositions
- compositions: Yb2Zr2O7 (1); (Yb2Zr2O7)0.8(Nd2Sn2O7)0.2 (1); (Yb2Zr2O7)0.8(Sm2Sn2O7)0.2 (1)
- dopant candidates (<5% at.): Sn (2), Nd (1), Sm (1)
- sample form: Bulk (3)
- measured range: 298-1272 K (5th-95th pct of 4 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Yb2Zr2O7 Pmma (51) mp-676382 [hull=0.132, PRIMARY]; Yb2Zr8O19 P-4m2 (115) mp-676389 [hull=0.100, PRIMARY]; Yb4Zr3O12 P-1 (2) mp-675744 [hull=0.039, PRIMARY]
- papers: https://doi.org/10.1111/jace.13979 (Low Thermal Conductivity of Rare-Earth Zirconate-Stannate Solid Soluti...)

## Pd-Sb-U
- rank 1794 | 3 samples | 3 papers | 3 compositions
- compositions: UPdSb (1); UPd2Sb (1); U3Pd3Sb4 (1)
- sample form: Polycrystal (2); Bulk (1)
- measured range: 10-327 K (5th-95th pct of 8 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): USb2Pd P4/nmm (129) mp-4207 [hull=0.000, icsd=2, PRIMARY]; USbPd P6_3/mmc (194) mp-1077418 [hull=0.005, icsd=1, PRIMARY]; U3Sb4Pd3 I-43d (220) mp-1189990 [hull=0.000, icsd=1, PRIMARY]; U2Sb4Pd P-4m2 (115) mp-1216580 [hull=0.000, PRIMARY]; USbPd2 Fm-3m (225) mp-1207137 [hull=0.070, PRIMARY]
- papers: https://doi.org/10.1088/0953-8984/18/15/030 (On the magnetic and electrical behaviour of UPdSb) | https://doi.org/10.1016/j.ssc.2005.01.007 (Magnetic and transport properties of UPd2Sb) | https://doi.org/10.1063/1.5128593 (Uranium-based materials for thermoelectric applications)

## Pd-Si-U
- rank 1795 | 3 samples | 2 papers | 2 compositions
- compositions: Pd58.8SU20.6Si20.6 (2); Pd58.8U20.6Si20.6 (1)
- dopant candidates (<5% at.): S (2)
- measured range: 12-296 K (5th-95th pct of 2 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): U(SiPd)2 I4/mmm (139) mp-4793 [hull=0.000, icsd=6, PRIMARY]; U3(Si3Pd10)2 Fm-3m (225) mp-630265 [hull=0.025, icsd=2, PRIMARY]; USiPd Pnma (62) mp-21191 [hull=0.043, icsd=1, PRIMARY]; U2Si3Pd Pmm2 (25) mp-1216905 [hull=0.044, PRIMARY]
- papers: https://doi.org/10.1103/physrevb.34.7371 (Transport and magnetic properties of icosahedral and glassy Pd-U-Si al...) | https://doi.org/10.1103/physrevb.35.2451 (Low-temperature thermal conductivity of glassy and icosahedral Pd-U-Si...)

## Pd-Zr
- rank 1796 | 3 samples | 1 papers | 1 compositions
- compositions: Zr70Pd30 (3)
- measured range: 308-948 K (5th-95th pct of 4 curves; full span incl. outliers 308-992 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Zr2Pd I4/mmm (139) mp-266 [hull=0.000, icsd=6, PRIMARY]; ZrPd3 P6_3/mmc (194) mp-30842 [hull=0.000, icsd=3, PRIMARY]; ZrPd Cmcm (63) mp-13495 [hull=0.000, icsd=2, PRIMARY]; Zr3Pd4 R-3 (148) mp-12712 [hull=0.005, icsd=2, PRIMARY]; ZrPd2 I4/mmm (139) mp-1018102 [hull=0.006, icsd=2, PRIMARY]
- papers: https://doi.org/10.1016/j.jallcom.2010.03.243 (Influence of quasicrystalline phase on transport processes in Zr70Pd30...)

## Pt
- rank 1797 | 3 samples | 2 papers | 3 compositions
- compositions: Pt98Ir2 (1); Pt96.1Ir3.9 (1); Pt (1)
- dopant candidates (<5% at.): Ir (2)
- measured range: 10-117 K (5th-95th pct of 3 curves; full span incl. outliers 10-797 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Pt Fm-3m (225) mp-126 [hull=0.000, icsd=22, PRIMARY]
- papers: https://doi.org/10.1007/bf00655330 (Comments upon ?the thermoelectric power of someThCe alloys? and an alt...) | https://doi.org/10.1103/physrevmaterials.1.065002 (Phonon and electron contributions to the thermal conductivity of \nVNx...)

## Re-Si
- rank 1798 | 3 samples | 1 papers | 3 compositions
- compositions:  ReSi1.7125Al0.05 (1); ReSi1.675Al0.10 (1); ReSi1.75 (1)
- dopant candidates (<5% at.): Al (2)
- sample form: Bulk (3)
- measured range: 297-973 K (5th-95th pct of 12 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): ReSi2 I4/mmm (139) mp-12605 [hull=0.130, icsd=5, PRIMARY]; ReSi P2_13 (198) mp-7948 [hull=0.000, icsd=3, PRIMARY]; Re5Si3 I4/mcm (140) mp-1105959 [hull=0.132, icsd=1, PRIMARY]; Re2Si P2_1/c (14) mp-669547 [hull=0.310, icsd=1, PRIMARY]; Re3Si P6_3/mmc (194) mp-974425 [hull=0.296, PRIMARY]
- papers: https://doi.org/10.1002/ejic.201600792 (Tuning Crystal Structures and Thermoelectric Properties through Al Dop...)

## Re-Te
- rank 1799 | 3 samples | 1 papers | 3 compositions
- compositions: Re6Te15 (1); Re6Ga0.5Te15 (1); Re6GaTe15 (1)
- dopant candidates (<5% at.): Ga (2)
- sample form: Bulk (3)
- measured range: 92-318 K (5th-95th pct of 3 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): ReTe P6_3mc (186) mp-974469 [hull=0.899, PRIMARY]; ReTe2 P-1 (2) mp-1102447 [hull=0.059, PRIMARY]
- papers: https://doi.org/10.1016/j.matchemphys.2009.08.061 (Thermoelectric properties of Re6GaxSeyTe15−y (0≤x≤2; 0≤y≤7.5))

## Ru-Se
- rank 1800 | 3 samples | 1 papers | 2 compositions
- compositions: RuSe2 (2); Ru0.9Ir0.1Se2 (1)
- dopant candidates (<5% at.): Ir (1)
- sample form: Bulk (3)
- measured range: 10-1026 K (5th-95th pct of 4 curves)
- [ref 1] TEDesignLab / ICSD: RuSe2 Pa-3 (205) mp-1922 [hull=0.000, icsd=7, PRIMARY]
- papers: https://doi.org/10.1063/1.4913919 (Enhanced thermoelectric power and electronic correlations in RuSe2)
