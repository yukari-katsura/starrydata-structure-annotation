# Host systems -- chunk 019 of 73

Ranks 901-950 by sample count. These 50 host systems cover 343 samples (0.66% of the TE set); cumulative through this chunk: 88.50%.

Assign each host system a structural prototype from `data/annotated/taxonomy/prototypes_seed_v3.json`, or propose a new one in `taxonomy/prototypes_proposed.jsonl` first. Append results to `data/annotated/annotations/family_assignments.jsonl`.

The hand-entered MaterialFamily labels are deliberately NOT shown here -- they are held out in `df_host_systems.parquet` to validate this classification later. Decide from the compositions.

A "seed hypothesis" line means the taxonomy already names this host under that prototype. Confirm it against the compositions rather than accepting it; two or more listed means the host is mixed and needs splitting per composition.

Evidence follows the project precedence. Your judgement about the thermoelectric chemistry decides the prototype. [ref 1] is TEDesignLab, ICSD-backed and thermoelectric-specific -- prefer it. [ref 2] is Materials Project. Within a formula, polymorphs are ranked by ICSD reference count and the top one is marked PRIMARY -- not by e_above_hull, which is unusable for layered chalcogenides in the 2019 dump (Sb2Te3 R-3m carries 26 ICSD refs at hull 1.02). A primary resting on fewer than 5 ICSD references is flagged weak; the ambient phase may simply be absent from the snapshot, as it is for Bi2Se3.

While you have the host in view, also record what each minor element DOES, in `dopant_roles` -- the role follows from the prototype and cannot be judged without it. A median host has 2 such elements. Not everything listed is a dopant: O, C, N and H are usually milling or pressing residue, and an element just under 5 at.% may be an alloying end member rather than dilute doping. The doping LEVEL is computed later from the parsed fractions -- do not work it out by hand here.

A polymorph list is NOT a thermal sequence. SnSe has three known structures but only Pnma -> Cmcm happens on heating; rocksalt SnSe is metastable (2 icsd refs against 32). Put thermally reached phases in `phases` with their transition temperatures, and everything else in `other_polymorphs` with an occurrence reason. hull and icsd counts are shown to help you tell them apart.

A host may need MORE THAN ONE prototype. Transport is measured across a wide window and many thermoelectrics transform inside it, so where a "MEASUREMENT CROSSES A TRANSITION" line appears, record each phase with its own temperature range in the `phases` field. Transition temperatures shown are approximate and composition-dependent.

Both references describe which phases EXIST in a chemistry, not which phase this paper made. Al-O-Zn is best attested as ZnAl2O4 spinel (227) while almost every sample in it is Al-doped wurtzite ZnO (186). Weigh them against the compositions; do not follow them blindly.

## Gd-S
- rank 901 | 7 samples | 3 papers | 3 compositions
- compositions: Gd2S3 (3); GdS1.48 (2); GdS1.43 (2)
- sample form: Bulk (1)
- measured range: 233-957 K (5th-95th pct of 19 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Gd2S3 Pnma (62) mp-608146 [hull=0.000, icsd=5, PRIMARY]; Gd3S4 I-43d (220) mp-20036 [hull=0.012, icsd=2, PRIMARY]; GdS2 P2_1/c (14) mp-1095479 [hull=0.000, icsd=1, PRIMARY]; Gd10S19 P4_2/n (86) mp-646008 [hull=0.000, icsd=1, PRIMARY]; GdS2 P4/nmm (129) mp-1018706 [hull=0.058, icsd=1]
- papers: https://doi.org/10.1016/j.jallcom.2007.04.078 (Thermoelectric properties of Th3P4-type rare-earth sulfides Ln2S3 (Ln=...) | https://doi.org/10.1016/j.jallcom.2009.04.076 (Synthesis of multinary rare-earth sulfides PrGdS3, NdGdS3, and SmEuGdS...) | https://doi.org/10.1016/j.jallcom.2008.05.003 (Corrigendum to “Thermoelectric properties of Th3P4-type rare-earth sul...)

## Ge-La-Pt-Sb
- rank 902 | 7 samples | 1 papers | 7 compositions
- compositions: LaPt4Ge7Sb5 (1); LaPt4(Ge7.3Sb4.7) (1); LaPt4(Ge6.7Sb5.3) (1); LaPt4Ge6.9Sb5.1 (1); LaPt4Ge8Sb4 (1); LaPt4(Ge7.1Sb4.9) (1)
- measured range: 10-978 K (5th-95th pct of 9 curves)
- papers: https://doi.org/10.1007/978-94-007-4984-9_9 (From Superconductivity Towards Thermoelectricity: Ge-Based Skutterudites)

## Ge-Pb-Sb-Te
- rank 903 | 7 samples | 2 papers | 7 compositions
- compositions: Ge0.76Pb0.1Sb0.1Te (1); Ge0.745Al0.015Pb0.1Sb0.1Te (1); Ge0.74Al0.02Pb0.1Sb0.1Te (1); Ge0.75Al0.01Pb0.1Sb0.1Te (1); Ge0.73Al0.03Pb0.1Sb0.1Te (1); Ge0.72Al0.04Pb0.1Sb0.1Te (1)
- dopant candidates (<5% at.): Al (5)
- sample form: Bulk (6); Polycrystal (1)
- measured range: 297-801 K (5th-95th pct of 35 curves)
- papers: https://doi.org/10.1016/j.mtphys.2021.100497 (Lone-Pair Engineering: Achieving Ultralow Lattice Thermal Conductivity...) | https://doi.org/10.1126/science.abq5815 (High figure-of-merit and power generation in high-entropy GeTe-based t...)

## Ge-Pd-Ru-U
- rank 904 | 7 samples | 1 papers | 7 compositions
- compositions: URu0.5Pd0.5Ge (1); URu0.3Pd0.7Ge (1); URu0.8Pd0.2Ge (1); URu0.7Pd0.3Ge (1); URu0.6Pd0.4Ge (1); URu0.4Pd0.6Ge (1)
- sample form: Bulk (7)
- measured range: 12-301 K (5th-95th pct of 7 curves)
- papers: https://doi.org/10.12693/aphyspola.127.287 (Thermoelectric Power of the URu1-xPdxGe System)

## Hf-Pt-Sn
- rank 905 | 7 samples | 3 papers | 4 compositions
- compositions: HfPtSn (4); Hf(Pt0.99Co0.01)Sn (1); Hf(Pt0.995Ir0.005)Sn (1); Hf(Pt0.99Ir0.01)Sn (1)
- dopant candidates (<5% at.): Ir (2), Co (1)
- sample form: SingleCrystal (3); Bulk (1)
- measured range: 217-1072 K (5th-95th pct of 25 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): HfSnPt F-43m (216) mp-20889 [hull=0.493, icsd=2, PRIMARY]
- papers: https://doi.org/10.1063/1.2364721 (Thermoelectric properties of p-type half-Heusler compound HfPtSn and i...) | https://doi.org/10.1007/s11837-014-1233-3 (Ordered Structures and Thermoelectric Properties of MNiSn (M = Ti, Zr,...) | https://doi.org/10.1109/ict.2006.331294 (Thermoelectric Properties of P-type Half-Heusler Compounds HfPtSn and ...)

## Hg-In-Se
- rank 906 | 7 samples | 1 papers | 7 compositions
- compositions: Hg3In2Se6M0.02 (1); Hg3In2Se6 (1); Hg3In2Se6Fe0.03 (1); Hg3In2Se6Fe0.02 (1); Hg3In2Se6Mn0.03 (1); Hg3In2Se6M0.01 (1)
- dopant candidates (<5% at.): Fe (3), M0+ (2), Mn (1)
- sample form: SingleCrystal (7)
- measured range: 75-304 K (5th-95th pct of 14 curves)
- [ref 1] TEDesignLab / ICSD: In2HgSe4 I-4 (82) mp-20731 [hull=0.000, icsd=1, PRIMARY]
- papers: https://doi.org/10.1134/s0020168514050070 (Charge transport and mechanisms of electron scattering in (HgSe)3(In2S...)

## Hg-Se
- rank 907 | 7 samples | 2 papers | 5 compositions
- compositions: HgSe (3); (Hg3Se)0.9(Al2Se3)0.1Mn0.001 (1); (Hg3Se)0.9(Al2Se3)0.1Mn0.0001 (1); (Hg3Se)0.9(Al2Se3)0.1Mn0.002 (1); (Hg3Se)0.9(Al2Se3)0.1Mn0.0015 (1)
- dopant candidates (<5% at.): Al (4), Mn (4)
- sample form: SingleCrystal (3)
- measured range: 78-425 K (5th-95th pct of 6 curves; full span incl. outliers 78-478 K)
- [ref 1] TEDesignLab / ICSD: HgSe P3_221 (154) mp-1018722 [hull=0.037, icsd=1]
- [ref 2] MP, ranked by ICSD evidence: HgSe F-43m (216) mp-820 [hull=0.000, icsd=12, PRIMARY]; HgSe Fm-3m (225) mp-957 [hull=0.160, icsd=4]
- papers: https://doi.org/10.1134/s0020168510050043 (Electrical and optical properties of manganese-doped (3HgSe)1 − x (Al2...) | https://doi.org/10.1063/1.1777052 (Electrical and Optical Properties of Mercury Selenide (HgSe))

## I-Pb-Te
- rank 908 | 7 samples | 2 papers | 5 compositions
- compositions: Pb1.09Cr0.009Te1I0.2 (2); Pb1.045Cr0.009Te1I0.11 (2); Pb47.60Te47.35I5.05 (1); Pb47.09Te47.07I5.03 (1); Pb47.24Te47.34I5.42 (1)
- dopant candidates (<5% at.): Cr (4)
- measured range: 147-599 K (5th-95th pct of 15 curves)
- papers: https://doi.org/10.1063/1.3603962 (Dramatic enhancement of thermoelectric power factor in PbTe:Cr co-dope...) | https://doi.org/10.1021/nl403677k (The Effects of the Size and the Doping Concentration on the Power Fact...)

## In-Ni
- rank 909 | 7 samples | 2 papers | 2 compositions
- compositions: In3Ni2 (6); In46Ni54 (1)
- measured range: 12-1379 K (5th-95th pct of 8 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): InNi P6/mmm (191) mp-19876 [hull=0.000, icsd=9, PRIMARY]; In3Ni2 P-3m1 (164) mp-21385 [hull=0.000, icsd=5, PRIMARY]; InNi2 P6_3/mmc (194) mp-21092 [hull=0.107, icsd=5, PRIMARY]; InNi3 P6_3/mmc (194) mp-1080093 [hull=0.028, icsd=4, PRIMARY]; In9Ni13 C2/m (12) mp-641509 [hull=0.043, icsd=2, PRIMARY]
- papers: https://doi.org/10.1088/0953-8984/11/15/010 (Electrical resistivity and absolute thermoelectric power of liquid ind...) | https://doi.org/10.1002/zaac.202000035 (Anisotropic Electrical, Magnetic, and Thermal Properties of In3\nNi2\n...)

## Ir-O-Sn
- rank 910 | 7 samples | 1 papers | 5 compositions
- compositions: Ir0.8Sn0.2O2 (2); Ir0.7Sn0.3O2 (2); Ir0.6Sn0.4O2 (1); Ir0.5Sn0.5O2 (1); Ir0.4Sn0.6O2 (1)
- measured range: 10-302 K (5th-95th pct of 7 curves)
- papers: https://doi.org/10.1002/adfm.201806754 (Toward the Optimized Spintronic Response of Sn‐Doped IrO\n            ...)

## K-La-Mn-O
- rank 911 | 7 samples | 4 papers | 5 compositions
- compositions: La0.7K0.3MnO3 (2); La0.75K0.25MnO3 (2); La0.67K0.33MnO3 (1); La0.7Na0.05K0.25MnO3 (1); La0.65K0.35MnO3 (1)
- dopant candidates (<5% at.): Na (1)
- sample form: pellets (1)
- measured range: 10-350 K (5th-95th pct of 7 curves; full span incl. outliers 10-402 K)
- papers: https://doi.org/10.1016/j.matchemphys.2013.10.033 (Influence of rare-earth ion doping on magnetotransport behavior of pot...) | https://doi.org/10.1063/5.0097996 (La<sub>0.7</sub>Na<sub>0.3−</sub><sub><i>x</i></sub>K<sub><i>x</i></su...) | https://doi.org/10.1016/j.apsusc.2022.152905 (Adjusting the K-doping of La1-K MnO3 (0.1 ≤ x ≤ 0.35) films to obtain ...)

## K-Na-Nb-O
- rank 912 | 7 samples | 1 papers | 1 compositions
- compositions: (K0.5Na0.5)NbO3 (7)
- measured range: 321-1006 K (5th-95th pct of 7 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): K2NaNb3O9 Pm (6) mp-1224011 [hull=0.011, PRIMARY]; K4NaNb5O15 Pm (6) mp-1224551 [hull=0.009, PRIMARY]; K5Na3Nb7WO20 P1 (1) mp-1076894 [hull=0.226, PRIMARY]; K5Na3Nb7WO24 Cm (8) mp-1099622 [hull=0.018, PRIMARY]; K5Na3Nb8O20 P1 (1) mp-1076768 [hull=0.157, PRIMARY]
- papers: https://doi.org/10.1016/j.matlet.2015.09.124 (Thermoelectric properties of oxygen deficient (K0.5Na0.5)NbO3 ceramics)

## La-Mn-O-Pr
- rank 913 | 7 samples | 2 papers | 3 compositions
- compositions: La0.54Pr0.36Te0.1MnO3 (3); La0.36Pr0.54Te0.1MnO3 (3); (La0.7Pb0.3)0.5(Pr0.63Ca0.37)0.5MnO3 (1)
- dopant candidates (<5% at.): Te (6), Ca (1), Pb (1)
- sample form: Bulk (1)
- measured range: 12-379 K (5th-95th pct of 7 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): La3PrMn4O12 Pm (6) mp-1223133 [hull=0.006, PRIMARY]; LaPr3Mn4O12 Pm (6) mp-1222923 [hull=0.006, PRIMARY]; LaPrMn2O6 Pmc2_1 (26) mp-1222975 [hull=0.005, PRIMARY]
- papers: https://doi.org/10.1063/1.2188029 (Ferro-antiferromagnetic coupling and unusual transport properties of f...) | https://doi.org/10.1016/j.ssc.2006.06.010 (Electrical and thermal transport properties of the Pr-doped La0.9−xPrx...)

## La-Te-Tl
- rank 914 | 7 samples | 2 papers | 5 compositions
- compositions: Tl9LaTe6 (3); Tl8.85La1.15Te6 (1); Tl9.1La0.9Te6 (1); Tl9.05La0.95Te6 (1); Tl8.95La1.05Te6 (1)
- sample form: Bulk (7)
- measured range: 303-605 K (5th-95th pct of 33 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): La(Tl3Te2)3 I4/m (87) mp-1223306 [hull=0.000, PRIMARY]; La5TlTe8 I-4 (82) mp-35907 [hull=0.000, PRIMARY]
- papers: https://doi.org/10.1039/c0dt01151g (Crystal structures and thermoelectric properties of the series Tl10−xL...) | https://doi.org/10.1016/j.jallcom.2015.01.025 (Thermoelectric properties of hot-pressed Tl9LnTe6 (Ln=La, Ce, Pr, Nd, ...)

## Li-Nb-O
- rank 915 | 7 samples | 2 papers | 6 compositions
- compositions: Li0.6NbO2 (2); Li0.68NbO2 (1); LiNbO2 (1); Li0.95NbO2 (1); Li0.9NbO2 (1); Li0.8NbO2 (1)
- measured range: 297-965 K (5th-95th pct of 6 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): LiNbO3 R3c (161) mp-3731 [hull=0.000, icsd=32, PRIMARY]; LiNbO2 P6_3/mmc (194) mp-3924 [hull=0.000, icsd=6, PRIMARY]; Li3NbO4 I-43m (217) mp-31488 [hull=0.000, icsd=2, PRIMARY]; LiNb3O8 P2_1/c (14) mp-3368 [hull=0.000, icsd=2, PRIMARY]; Li8Nb2O9 P-1 (2) mp-28030 [hull=0.000, icsd=1, PRIMARY]
- papers: https://doi.org/10.1103/physrevb.74.012504 (Evidence of<mml:math xmlns:mml=\"http://www.w3.org/1998/Math/MathML\" ...) | https://doi.org/10.1039/c7ra10557f (Localized double phonon scattering and DOS induced thermoelectric enha...)

## Mn-Sb-Yb-Zn
- rank 916 | 7 samples | 3 papers | 5 compositions
- compositions: YbZn1.6Mn0.4Sb2 (2); YbZn1.7Mn0.3Sb2 (2); Yb9Mn1.2Zn3Sb9 (1); Yb9Mn2.2Zn2Sb9 (1); YbZn1.75Mn0.25Sb2 (1)
- measured range: 296-974 K (5th-95th pct of 28 curves)
- papers: https://doi.org/10.1063/1.2939372 (Improved thermoelectric performance in the Zintl phase compounds YbZn2...) | https://doi.org/10.1039/c4ta00539b (Thermoelectric properties of the Yb9Mn4.2−xZnxSb9 solid solutions) | https://doi.org/10.1007/s11664-009-0667-9 (Thermoelectric Properties of Zintl Compound YbZn2Sb2 with Mn Substitut...)

## Mn-Sn
- rank 917 | 7 samples | 2 papers | 7 compositions
- compositions: Mn3.26Sn0.74 (1); Mn3.21Sn0.79 (1); Mn3.51Sn0.49 (1); Mn3.42Sn0.58 (1); Mn3.18Sn0.82 (1); Mn3.1Sn0.9 (1)
- dopant candidates (<5% at.): In (1)
- measured range: 46-849 K (5th-95th pct of 9 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): MnSn2 I4/mcm (140) mp-20086 [hull=0.011, icsd=7, PRIMARY]; Mn2Sn P6_3/mmc (194) mp-22514 [hull=0.164, icsd=4, PRIMARY]; Mn3Sn P6_3/mmc (194) mp-1095178 [hull=0.173, icsd=3, PRIMARY]; Mn3Sn2 Pnma (62) mp-600428 [hull=0.074, icsd=3, PRIMARY]; MnSn P6_3/mmc (194) mp-999507 [hull=0.149, icsd=1, PRIMARY]
- papers: https://doi.org/10.1126/sciadv.abc1977 (Kondo physics in antiferromagnetic Weyl semimetal Mn3+xSn1−x films) | https://doi.org/10.1039/d3ta05468c (Unravelling the need for balancing band convergence and resonant level...)

## Mo-Nb-Te
- rank 918 | 7 samples | 2 papers | 7 compositions
- compositions: Mo0.2Nb0.8Te2 (1); Mo0.8Nb0.2Te2 (1); Mo0.6Nb0.4Te2 (1); Mo0.4Nb0.6Te2 (1); Mo0.88Nb0.12Te (1); Mo0.78Nb0.22Te (1)
- sample form: Bulk (4)
- measured range: 10-301 K (5th-95th pct of 31 curves)
- papers: https://doi.org/10.1063/1.4913967 (Rich structural phase diagram and thermoelectric properties of layered...) | https://doi.org/10.1126/sciadv.1601378 (Critical enhancement of thermopower in a chemically tuned polar semime...)

## Mo-O-Sr-Ti
- rank 919 | 7 samples | 3 papers | 5 compositions
- compositions: Sr2TiMoO6 (3); Ba0.1Sr1.9TiMoO6 (1); La0.3Sr1.7TiMoO6 (1); La0.15Sr1.85TiMoO6 (1); La0.25Sr1.75TiMoO6 (1)
- dopant candidates (<5% at.): La (3), Ba (1)
- measured range: 332-1235 K (5th-95th pct of 7 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Sr2TiMoO6 I4/m (87) mp-1078580 [hull=0.003, icsd=1, PRIMARY]; Sr2TiMoO6 Fm-3m (225) mp-1218376 [hull=0.031]
- papers: https://doi.org/10.1016/j.scriptamat.2016.11.033 (Environmental friendly Sr2TiMoO6 double perovskite for high temperatur...) | https://doi.org/10.1016/j.jallcom.2017.03.264 (Effect of Ba-doping on high temperature thermoelectric properties of S...) | https://doi.org/10.1039/c7dt00848a (Metal-like electrical conductivity in La<sub>x</sub>Sr<sub>2−x</sub>Ti...)

## Mo-O-Te
- rank 920 | 7 samples | 2 papers | 7 compositions
- compositions: (MoO3)0.15(TeO2)0.05 (1); (MoO3)0.05(TeO2)0.15 (1); (MoO3)0.1(TeO2)0.1 (1); (MoO3)3(TeO2)7 (1); (MoO3)3(TeO2)2 (1); (MoO3)2(TeO2)3 (1)
- solid-solution axis: O/(O+Te) spans 0.75-0.92 (median 0.83) over 7 compositions
     CHECK: same periodic group, but oxygen often occupies its own sublattice (BiCuSeO, LaFeAsO) rather than substituting for the heavier chalcogen. Confirm the two share a site before treating this as a substitution axis.
- measured range: 82-520 K (5th-95th pct of 10 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Te2MoO7 P2_1/c (14) mp-19453 [hull=0.000, icsd=4, PRIMARY]; TeMo5O16 Pc (7) mp-1217495 [hull=0.013, PRIMARY]
- papers: https://doi.org/10.1016/j.physb.2020.412141 (Investigation of structural, optical and thermoelectric properties of ...) | https://doi.org/10.1063/1.1935137 (Low-temperature metallic behavior of amorphous MoO3–TeO2 thin films)

## Mo-Se-Ti
- rank 921 | 7 samples | 2 papers | 7 compositions
- compositions: Ti0.9Mo6Se8 (1); Cu0.05Ti1.25Mo6Se8 (1); Cu0.2Ti1.0Mo6Se8 (1); Ti1.3Mo6Se8 (1); Cu0.1Ti1.2Mo6Se8 (1); Cu0.5Ti0.8Mo6Se8 (1)
- dopant candidates (<5% at.): Cu (5)
- sample form: Bulk (6)
- measured range: 297-1095 K (5th-95th pct of 23 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ti(Mo3Se4)2 R-3 (148) mp-1104333 [hull=0.133, icsd=1, PRIMARY]; Ti2(Mo3Se4)5 P-1 (2) mp-685942 [hull=0.029, PRIMARY]
- papers: https://doi.org/10.1016/j.jssc.2006.04.022 (Thermoelectric and structural properties of a new Chevrel phase: Ti0.3...) | https://doi.org/10.1109/ict.2003.1287497 (Thermoelectric properties of Mo/sub 6/Se/sub 8/-based chevrel phase wi...)

## N-Nb
- rank 922 | 7 samples | 2 papers | 1 compositions
- compositions: NbN (7)
- measured range: 10-300 K (5th-95th pct of 6 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): NbN Fm-3m (225) mp-1580 [hull=0.202, icsd=22, PRIMARY]; Nb4N5 I4/m (87) mp-7927 [hull=0.024, icsd=2, PRIMARY]; Nb2N P-31m (162) mp-1079585 [hull=0.000, icsd=1, PRIMARY]; Nb5N6 P6_3/mcm (193) mp-7234 [hull=0.000, icsd=1, PRIMARY]; Nb2N3 Pnma (62) mp-1188869 [hull=0.017, icsd=1, PRIMARY]
- papers: https://doi.org/10.9714/PSAC.2015.17.3.009 (Transition temperatures and upper critical fields of NbN thin films fa...) | https://doi.org/10.1103/physrevb.37.3970 (Electrical resistivity of polycrystalline niobium nitride films)

## N-Pu-U
- rank 923 | 7 samples | 2 papers | 2 compositions
- compositions: (U0.8Pu0.2)N (6); (U)81.26(PuN)18.74 (1)
- measured range: 410-1975 K (5th-95th pct of 7 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): PuU4N5 I4/mmm (139) mp-1219808 [hull=0.009, PRIMARY]; PuUN2 R-3m (166) mp-1219668 [hull=0.000, PRIMARY]; PuUN2 P4/mmm (123) mp-1219671 [hull=0.022]
- papers: https://doi.org/10.1016/j.jnucmat.2017.11.010 (U-PuO2, U-PuC, U-PuN cermet fuel for fast reactor) | https://doi.org/10.1016/s0925-8388(01)00875-1 (A molecular dynamics study on uranium–plutonium mixed nitride)

## Nb-O-Sr-Ti
- rank 924 | 7 samples | 2 papers | 7 compositions
- compositions: (NbO)12(SrTiNb0.2O3)12 (1); (NbO)12(SrTiNb0.2O3)6 (1); (NbO)1(SrTiNb0.2O3)12 (1); (NbO)9(SrTiNb0.2O3)12 (1); (NbO)9(SrTiNb0.2O3)6 (1); (NbO)9(SrTiNb0.2O3)3 (1)
- dopant candidates (<5% at.): La (1)
- sample form: Film (4); multilayer film (2); Bulk (1)   <-- film/epitaxial samples present: a metastable polymorph may be reachable here that never forms in bulk
- measured range: 297-1003 K (5th-95th pct of 22 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Sr2LaTi2Nb3O15 Pbam (55) mp-1218793 [hull=0.067, PRIMARY]; Sr3TiNb4O15 Pc (7) mp-1218661 [hull=0.049, PRIMARY]; Sr4Ti3Nb2O15 R-3m (166) mp-1218495 [hull=0.030, PRIMARY]
- papers: https://doi.org/10.1021/cm500646f (Thermoelectric Properties of Strontium Titanate Superlattices Incorpor...) | https://doi.org/10.1007/s11664-014-3560-0 (High-Temperature Thermoelectric Properties of (1 − x) SrTiO3 − (x) La1...)

## Ni-O-Sm
- rank 925 | 7 samples | 4 papers | 2 compositions
- compositions: SmNiO3 (6); Sm0.8Sr0.2NiO3 (1)
- dopant candidates (<5% at.): Sr (1)
- sample form: pellets (1); rod-shaped (1)
- measured range: 10-483 K (5th-95th pct of 7 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): SmNiO3 Pnma (62) mp-25588 [hull=0.000, icsd=27, PRIMARY]; Sm2Ni2O5 Ima2 (46) mp-1099625 [hull=0.118, PRIMARY]; SmNiO3 Pm-3m (221) mp-1099668 [hull=0.121]
- papers: https://doi.org/10.1021/acsami.9b12609 (A d-Band Electron Correlated Thermoelectric Thermistor Established in ...) | https://doi.org/10.1088/1361-648x/abfb90 (Synthesis and physical properties of perovskite Sm<sub>1−x\n          ...) | https://doi.org/10.1016/j.ceramint.2023.12.273 (Regulating the resistivity of rare-earth nickelates electronic phase t...)

## Ni-Pb-Zr
- rank 926 | 7 samples | 1 papers | 7 compositions
- compositions: ZrNiPb (1); ZrNiPb0.995Bi0.005 (1); ZrNiPb0.980Bi0.020 (1); ZrNiPb0.993Bi0.007 (1); ZrNiPb0.990Bi0.010 (1); ZrNiPb0.985Bi0.015 (1)
- dopant candidates (<5% at.): Bi (6)
- sample form: SingleCrystal (7)
- measured range: 300-873 K (5th-95th pct of 35 curves)
- papers: https://doi.org/10.1021/acs.chemmater.6b04898 (Thermoelectric Properties of n-type ZrNiPb-Based Half-Heuslers)

## Ni-Sb-Ti
- rank 927 | 7 samples | 4 papers | 5 compositions
- compositions: NiTiSb (3); TiCo0.1Ni0.9Sb (1); TiNiSb (1); NiTi0.9Mn0.1Sb (1); TiFe0.1Ni1.0Sb (1)
- dopant candidates (<5% at.): Co (1), Mn (1), Fe (1)
- sample form: pellets (1)
- measured range: 14-970 K (5th-95th pct of 15 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): TiNiSb F-43m (216) mp-20952 [hull=0.000, icsd=3, PRIMARY]; TiNi2Sb Fm-3m (225) mp-10261 [hull=0.100, icsd=1, PRIMARY]
- papers: https://doi.org/10.1016/s0925-8388(01)01618-8 (Electric transport and magnetic properties of TiCo1−xNixSb solid solution) | https://doi.org/10.1016/s0304-8853(98)00125-5 (Physical properties of the weak itinerant ferromagnet CoVSb and relate...) | https://doi.org/10.1007/s100510070055 (Galvanomagnetic properties of disordered Mn semi-Heusler phases with A...)

## O-Sb-Sm
- rank 928 | 7 samples | 3 papers | 3 compositions
- compositions: Sm2SbO2 (5); Sm3SbO3 (1); Sm8Sb3O8 (1)
- measured range: 11-392 K (5th-95th pct of 6 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Sm3Sb5O12 I-43m (217) mp-3154 [hull=0.000, icsd=2, PRIMARY]; Sm3SbO7 Cmcm (63) mp-1191139 [hull=0.000, icsd=1, PRIMARY, AMBIGUOUS]; Sm3SbO3 C2/m (12) mp-983597 [hull=0.022, icsd=1, PRIMARY]; SmSbO4 P2_1/c (14) mp-13196 [hull=0.000, icsd=1, PRIMARY]; Sm2SbO2 I4/mmm (139) mp-1219180 [hull=0.000, PRIMARY]
- papers: https://doi.org/10.1021/ja1027698 (Synthesis, Crystal and Electronic Structures of New Narrow-Band-Gap Se...) | https://doi.org/10.1021/ja209652d (Decoupling the Electrical Conductivity and Seebeck Coefficient in theR...) | https://doi.org/10.1021/acs.chemmater.7b03996 (Rare-Earth Pnictide Oxides (RE,Ca)mPnnOm (Pn = Sb, Bi): A Review of Cr...)

## O-Sm-Zr
- rank 929 | 7 samples | 5 papers | 1 compositions
- compositions: Sm2Zr2O7 (7)
- sample form: Bulk (2)
- measured range: 293-1272 K (5th-95th pct of 7 curves; full span incl. outliers 293-1673 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Sm2Zr2O7 Fd-3m (227) mp-4408 [hull=0.000, icsd=3, PRIMARY]; Sm2Zr8O19 P-4m2 (115) mp-1173100 [hull=0.016, PRIMARY]; Sm4ZrO8 Immm (71) mp-1173349 [hull=0.216, PRIMARY]; SmZr4O9 Imm2 (44) mp-760533 [hull=0.099, PRIMARY]; Sm2Zr2O7 P2_1 (4) mp-772758 [hull=0.022]
- papers: https://doi.org/10.1016/j.scriptamat.2019.12.006 (Multicomponent high-entropy zirconates with comprehensive properties f...) | https://doi.org/10.31349/revmexfis.67.255 (Electrical and thermal conductivities of rare-earth A2Zr2O7 (A = Pr, N...) | https://doi.org/10.1002/adem.200700153 (Preparation and Thermophysical Properties of Sm2(Ce0.3Zr0.7)2O7 Ceramic)

## O-Sn-Zn
- rank 930 | 7 samples | 3 papers | 6 compositions
- compositions: ZnSnO (2); Zn2SnO4 (1); Sn0.5ZnO1.5 (1); Sn0.15ZnO1.15 (1); Sn0.2ZnO1.2 (1); Sn0.3ZnO1.3 (1)
- sample form: Powder (2); Bulk (1)
- measured range: 303-1073 K (5th-95th pct of 8 curves)
- [ref 1] TEDesignLab / ICSD: ZnSnO3 R3c (161) mp-13334 [hull=0.041, icsd=2, PRIMARY]; ZnSnO3 R-3 (148) mp-14628 [hull=0.055, icsd=1]
- [ref 2] MP, ranked by ICSD evidence: Zn2SnO4 Fd-3m (227) mp-1103830 [hull=0.117, icsd=1, PRIMARY]; Zn3Sn2O7 Cmc2_1 (36) mp-1118152 [hull=0.063, PRIMARY]; ZnSnO3 Pm-3m (221) mp-1016902 [hull=0.713]; Zn2SnO4 Imma (74) mp-35493 [hull=0.017]
- papers: https://doi.org/10.1016/j.materresbull.2007.02.018 (Influence of SnO2 addition on the thermoelectric properties of Zn1−xSn...) | https://doi.org/10.1016/j.tsf.2013.12.010 (Thermoelectric and photoconductivity properties of zinc oxide–tin oxid...) | https://doi.org/10.1016/j.ceramint.2020.03.031 (Improved thermoelectric performance of Al and Sn doped ZnO nano partic...)

## O-Sr
- rank 931 | 7 samples | 3 papers | 3 compositions
- compositions: Sr(Fe0.2Ti0.2Mo0.2Nb0.2Cr0.2)O3 (5); Sr0.95La0.05Ti0.02Mn0.0126O3 (1); Sr20.995Ti0.005O4 (1)
- dopant candidates (<5% at.): Ti (7), Fe (5), Mo (5), Nb (5), Cr (5), La (1), Mn (1)
- sample form: Bulk (1)
- measured range: 10-1091 K (5th-95th pct of 11 curves)
- [ref 1] TEDesignLab / ICSD: SrO Fm-3m (225) mp-2472 [hull=0.000, icsd=12, PRIMARY]; SrO2 I4/mmm (139) mp-2697 [hull=0.000, icsd=2, PRIMARY, AMBIGUOUS]; SrO Pm-3m (221) mp-1009819 [hull=0.415, icsd=3]
- [ref 2] MP, ranked by ICSD evidence: SrO10 P4/mcc (124) mp-1179236 [hull=0.036, icsd=2, PRIMARY]; SrO6 C2/c (15) mp-1179143 [hull=0.090, icsd=1, PRIMARY]; Sr2O3 Pm-3m (221) mp-1187089 [hull=0.615, PRIMARY]; SrO3 Pmc2_1 (26) mp-1206311 [hull=0.374, PRIMARY]; SrO2 Pnma (62) mp-1179089 [hull=0.010, icsd=2]
- papers: https://doi.org/10.1088/1742-6596/568/2/022035 (Effects of Mn substitution on the thermoelectric properties of the ele...) | https://doi.org/10.1021/acssuschemeng.0c03849 (High-Entropy Perovskites: An Emergent Class of Oxide Thermoelectrics w...) | https://doi.org/10.1016/s0921-4526(01)01208-x (Effect of Ti substitution on the residual resistivity in the spin-trip...)

## O-Te-V
- rank 932 | 7 samples | 2 papers | 7 compositions
- compositions: Sb10(V2O5)50(TeO2)40 (1); Sb12(V2O5)48(TeO2)40 (1); Sb12(V2O5)45(TeO2)40 (1); (V2O5)60(TeO2)40 (1); Sb5(V2O5)55(TeO2)40 (1); Sb8(V2O5)52(TeO2)40 (1)
- dopant candidates (<5% at.): Sb (5)
- sample form: SingleCrystal (1)
- solid-solution axis: O/(O+Te) spans 0.33-0.90 (median 0.89) over 7 compositions
     CHECK: same periodic group, but oxygen often occupies its own sublattice (BiCuSeO, LaFeAsO) rather than substituting for the heavier chalcogen. Confirm the two share a site before treating this as a substitution axis.
- measured range: 13-438 K (5th-95th pct of 7 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): V2Te2O9 Fdd2 (43) mp-649905 [hull=0.014, icsd=1, PRIMARY]; VTeO4 P2_1/c (14) mp-32482 [hull=0.000, icsd=1, PRIMARY]; V(TeO3)4 P1 (1) mp-762679 [hull=0.076, PRIMARY]
- papers: https://doi.org/10.1007/s11664-015-4071-3 (Thermoelectric Power Measurements of xSb-(60-x)V2O5-40TeO2 Glasses) | https://doi.org/10.1021/acs.inorgchem.8b02280 (V2Te2O: A Two-Dimensional van der Waals Correlated Metal)

## Pb-Se-Ti
- rank 933 | 7 samples | 1 papers | 5 compositions
- compositions: PbTiSe3 (2); PbTi2Se5 (2); PbTi3Se7 (1); PbTi4Se9 (1); PbTi6Se13 (1)
- measured range: 19-287 K (5th-95th pct of 7 curves)
- papers: https://doi.org/10.1039/c5tc01570g (Carrier dilution in TiSe2based intergrowth compounds for enhanced ther...)

## Pb-Sr-Te
- rank 934 | 7 samples | 2 papers | 7 compositions
- compositions: Pb0.196Sr0.784Na0.02Te (1); (Pb0.8Sr0.2)0.98Na0.02Te (1); Pb0.588Sr0.392Na0.02Te (1); Pb0.392Sr0.588Na0.02Te (1); Pb0.8624Sr0.1176Na0.02Te (1); Pb0.88Na0.02TeSr0.1 (1)
- dopant candidates (<5% at.): Na (7)
- measured range: 297-919 K (5th-95th pct of 29 curves)
- papers: https://doi.org/10.1016/j.jallcom.2016.06.172 (Enhanced thermoelectric performance in PbSe-SrSe solid solution by Mn ...) | https://doi.org/10.1038/ncomms12167 (Non-equilibrium processing leads to record high thermoelectric figure ...)

## Pd-Y
- rank 935 | 7 samples | 3 papers | 5 compositions
- compositions: YPd3 (3); Y0.9U0.1Pd3 (1); Y0.95U0.05Pd3 (1); U0.1Y0.9Pd3 (1); U0.05Y0.95Pd3 (1)
- dopant candidates (<5% at.): U (4)
- sample form: Bulk (3); Polycrystal (3)
- measured range: 11-295 K (5th-95th pct of 7 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): YPd3 Pm-3m (221) mp-559 [hull=0.000, icsd=8, PRIMARY]; Y3Pd2 R-3 (148) mp-1104388 [hull=0.000, icsd=1, PRIMARY]; Y3Pd4 R-3 (148) mp-1104019 [hull=0.000, icsd=1, PRIMARY]; YPd Cmcm (63) mp-1066136 [hull=0.000, icsd=1, PRIMARY]; YPd2 I4/mmm (139) mp-1062893 [hull=0.278, icsd=1, PRIMARY]
- papers: https://doi.org/10.1016/0304-8853(87)90669-x (Thermoelectric power investigation of the (Ce, Y)Pd3 system) | https://doi.org/10.1103/physrevb.49.6400 (Evidence for the Kondo effect and crossover in transport behavior forx...) | https://doi.org/10.1016/0921-4526(94)91847-3 (Evidence for Kondo effect and crossover in electronic structure for x ...)

## Pr-Te
- rank 936 | 7 samples | 1 papers | 7 compositions
- compositions: Pr2.9Te4 (1); Pr2.78Te4 (1); Pr2.74Te4 (1); Pr2.70Te4 (1); Pr2.67Te4 (1); Pr3Te4 (1)
- sample form: compact (7)
- measured range: 295-1280 K (5th-95th pct of 25 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): PrTe Fm-3m (225) mp-2532 [hull=0.000, icsd=6, PRIMARY]; Pr3Te4 I-43d (220) mp-2127 [hull=0.009, icsd=2, PRIMARY]; PrTe2 P4/nmm (129) mp-975652 [hull=0.000, icsd=2, PRIMARY]; PrTe3 Cmcm (63) mp-12351 [hull=0.000, icsd=2, PRIMARY]; Pr2Te5 Cmcm (63) mp-1104180 [hull=0.003, icsd=1, PRIMARY]
- papers: https://doi.org/10.1016/j.joule.2018.01.013 (Praseodymium Telluride: A High-Temperature, High-ZT Thermoelectric Mat...)

## Pt-Sb-Ti
- rank 937 | 7 samples | 1 papers | 7 compositions
- compositions: TiPtSb (1); Ti0.85PtSb (1); Ti0.84PtSb (1); Ti0.83PtSb (1); Ti0.82PtSb (1); Ti0.75PtSb (1)
- measured range: 299-1125 K (5th-95th pct of 35 curves)
- papers: https://doi.org/10.1016/j.mtphys.2020.100200 (A new defective 19-electron TiPtSb half-Heusler thermoelectric compoun...)

## Pt-U
- rank 938 | 7 samples | 4 papers | 1 compositions
- compositions: UPt3 (7)
- sample form: Bulk (2); Polycrystal (1)
- measured range: 13-349 K (5th-95th pct of 2 curves; full span incl. outliers 13-1010 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): UPt3 P6_3/mmc (194) mp-30855 [hull=0.000, icsd=4, PRIMARY]; UPt5 F-43m (216) mp-1077375 [hull=0.000, icsd=3, PRIMARY]; UPt2 Cmcm (63) mp-30854 [hull=0.000, icsd=1, PRIMARY]; U3Pt Fm-3m (225) mp-1187724 [hull=0.051, PRIMARY]
- papers: https://doi.org/10.1063/1.335166 (Transport and magnetic measurements on UPt3) | https://doi.org/10.1007/bf00681319 (Thermodynamic and transport properties of UPt3) | https://doi.org/10.1007/bf01325377 (Specific heat and transport properties of UPt3)

## Ru-Sb-Te
- rank 939 | 7 samples | 2 papers | 5 compositions
- compositions: RuSb2Te (2); Ru0.95Fe0.05Sb2Te (2); Yb0.05RuSb2Te (1); RuSb2Sn0.1Te0.9 (1); Ru0.95Sn0.1Sb2Te0.9 (1)
- dopant candidates (<5% at.): Fe (2), Sn (2), Yb (1)
- sample form: Bulk (5)
- measured range: 91-706 K (5th-95th pct of 18 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): SbTeRu P2_1/c (14) mp-1102857 [hull=0.358, icsd=2, PRIMARY]; Sb2TeRu Immm (71) mp-1219496 [hull=0.381, PRIMARY]
- papers: https://doi.org/10.1140/epjb/e2013-40335-5 (Theoretical investigation on the electronic and thermoelectric propert...) | https://doi.org/10.1007/s11664-012-2451-5 (Thermoelectric Properties of RuSb2Te Ternary Skutterudites)

## S-Ta
- rank 940 | 7 samples | 1 papers | 6 compositions
- compositions: TaS2 (2); TaS2.004 (1); TaS2.002 (1); TaS2.003 (1); TaS2.005 (1); TaS2.008 (1)
- measured range: 12-299 K (5th-95th pct of 7 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): TaS2 Fmm2 (42) mp-1411 [hull=0.002, icsd=8, PRIMARY]; TaS3 P2_1/m (11) mp-30527 [hull=0.000, icsd=2, PRIMARY]; Ta3S2 Aem2 (39) mp-1826 [hull=0.000, icsd=1, PRIMARY]; Ta6S C2/c (15) mp-27467 [hull=0.004, icsd=1, PRIMARY]; TaS P-6m2 (187) mp-10628 [hull=0.211, icsd=1, PRIMARY]
- papers: https://doi.org/10.1023/a:1014749121869 ([])

## Sb-Se
- rank 941 | 7 samples | 3 papers | 2 compositions
- compositions: Sb2Se3Te0.01 (5); Sb2Se3 (2)
- dopant candidates (<5% at.): Te (5)
- sample form: Bulk (1)
- measured range: 300-540 K (5th-95th pct of 9 curves; full span incl. outliers 300-800 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Sb2Se3 Pnma (62) mp-2160 [hull=0.000, icsd=11, PRIMARY]
- papers: https://doi.org/10.1039/c5tc01364j (Self-assisted nucleation and growth of [010]-oriented Sb2Se3 whiskers:...) | https://doi.org/10.1007/s11051-013-1541-5 (Preparation and electrical transport properties of nanostructured Sb2S...) | https://doi.org/10.1002/adfm.201806558 (Intrinsically Low Thermal Conductivity in BiSbSe3\n: A Promising Therm...)

## Se-Sn-V
- rank 942 | 7 samples | 1 papers | 7 compositions
- compositions: ((SnSe1.15))(V1.12Se) (1); ((SnSe)1.15)(V1.14Se)2 (1); ((SnSe)1.15)(V1.22Se)3 (1); ((SnSe1.15))(V1.42Se)4 (1); ((SnSe1.15))(V1.38Se)5 (1); ((SnSe1.15))(V1.28Se)6 (1)
- measured range: 21-298 K (5th-95th pct of 7 curves)
- papers: https://doi.org/10.1016/j.jssc.2015.08.013 (Influence of interstitial V on structure and properties of ferecrystal...)

## Si-Yb
- rank 943 | 7 samples | 4 papers | 6 compositions
- compositions: YbSi (2); Yb5Si3 (1); YbSi5 (1); YbCo0.15Si4.85 (1); YbCo0.1Si4.9 (1); YbCo0.2Si4.8 (1)
- dopant candidates (<5% at.): Co (3)
- sample form: Polycrystal (5); Bulk (1)
- measured range: 10-814 K (5th-95th pct of 24 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): YbSi2 P6/mmm (191) mp-1671 [hull=0.058, icsd=4, PRIMARY]; Yb3Si5 P-62m (189) mp-349 [hull=0.032, icsd=4, PRIMARY]; Yb5Si3 P6_3/mcm (193) mp-1188257 [hull=0.121, icsd=3, PRIMARY]; Yb5Si4 Pnma (62) mp-20101 [hull=0.034, icsd=2, PRIMARY]; YbSi Cmcm (63) mp-10651 [hull=0.000, icsd=2, PRIMARY]
- papers: https://doi.org/10.7567/1347-4065/ab5b85 (Thermoelectric properties of Yb5Si3) | https://doi.org/10.1063/1.335167 (Two-band model and ground state of heavy fermion compounds) | https://doi.org/10.1023/a:1021801903961 (Thermopower of Yb Heavy Fermion Compounds at High Pressure)

## Ag-Ba-Ge
- rank 944 | 6 samples | 2 papers | 4 compositions
- compositions: Ba8Ag5Ga1Ge40 (2); Ba8Ag5Ge41 (2); Ba8Ag6Ge40 (1); Ba8Ag5Ga2Ge39 (1)
- dopant candidates (<5% at.): Ga (3)
- measured range: 19-474 K (5th-95th pct of 13 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ba(AgGe)2 I4/mmm (139) mp-13910 [hull=0.000, icsd=1, PRIMARY]
- papers: https://doi.org/10.1109/ict.2007.4569463 (An exploration of noble metal substitution in germanium based clathrates) | https://doi.org/10.1007/s11664-016-4669-0 (Theoretical and Experimental Study on Thermoelectric Properties of Ba8...)

## Ag-Ba-Se-Sn
- rank 945 | 6 samples | 2 papers | 5 compositions
- compositions: BaAg2SnSe4 (2); Ba0.98Ag2SnSe4 (1); BaAg1.98SnSe4 (1); Ba0.92Na0.08Ag2SnSe4 (1); BaAg2Sn0.9In0.1Se4 (1)
- dopant candidates (<5% at.): Na (1), In (1)
- sample form: Bulk (6)
- measured range: 190-650 K (5th-95th pct of 10 curves)
- [ref 1] TEDesignLab / ICSD: BaAg2SnSe4 (23) [PRIMARY]
- papers: https://doi.org/10.1109/ict.2005.1519948 (Exploratory synthesis of new heavy main group chalcogenides) | https://doi.org/10.1039/c8ta09660k (Origins of ultralow thermal conductivity in 1-2-1-4 quaternary selenides)

## Ag-Bi-Sb-Te
- rank 946 | 6 samples | 3 papers | 6 compositions
- compositions: Ag0.4Bi0.5Sb1.1Te3 (1); (Ag2Te)0.25(Bi0.5Sb1.5Te3)0.75 (1); (Ag2Te)0.5(Bi0.5Sb1.5Te3)0.5 (1); Ag0.20Bi0.5Sb0.30Te3 (1); Ag0.30Bi0.5Sb0.20Te3 (1); Ag0.40Bi0.5Sb1.10Te3 (1)
- sample form: Bulk (6)
- solid-solution axis: Bi/(Bi+Sb) spans 0.25-0.71 (median 0.31) over 6 compositions
     ISOELECTRONIC SERIES: the parent compound depends on the composition, not on this host. Near either end the minor element is a dilute substituent; in the middle it is a genuine alloy. Record the axis, not one parent -- and note the 5% split used the whole formula, not the sublattice, so its cut lands at a different level on each site.
- measured range: 296-558 K (5th-95th pct of 17 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ag2BiSbTe4 I-4m2 (119) mp-1229125 [hull=0.457, PRIMARY]
- papers: https://doi.org/10.1016/j.matlet.2006.03.080 (Microstructures and thermoelectric properties of p-type pseudo-binary ...) | https://doi.org/10.3724/sp.j.1077.2010.00583 (Influence of Ag<SUB>2</SUB>Te Doping on the Thermoelectric Properties ...) | https://doi.org/10.1016/j.matlet.2005.05.039 (Transport properties of quaternary Ag–Bi–Sb–Te alloys prepared by pres...)

## Ag-Br-Te
- rank 947 | 6 samples | 1 papers | 6 compositions
- compositions: Ag10Te3.8S0.2Br3 (1); Ag10Te4Br2.6Cl0.4 (1); Ag10Te4Br3 (1); Ag10Te4Br2.4Cl0.6 (1); Ag10Te4Br2.8Cl0.2 (1); Ag10Te3.9Se0.1Br3 (1)
- dopant candidates (<5% at.): Cl (3), S (1), Se (1)
- sample form: Bulk (6)
- measured range: 289-524 K (5th-95th pct of 9 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ag5Te2Br Pnma (62) mp-1215016 [hull=0.005, PRIMARY]; Ag9Te4Br3 P1 (1) mp-676260 [hull=0.062, PRIMARY]
- papers: https://doi.org/10.1016/j.solidstatesciences.2011.02.012 (A conceptional approach to materials for resistivity switching and the...)

## Ag-Cl-Te
- rank 948 | 6 samples | 3 papers | 5 compositions
- compositions: Ag5Te2Cl (2); Ag5Te1.9S0.1Cl (1); Ag5Te2Cl0.8Br0.2 (1); Ag5Te1.7S0.3Cl (1); Ag5Te1.8Se0.2Cl (1)
- dopant candidates (<5% at.): S (2), Br (1), Se (1)
- sample form: Bulk (6)
- measured range: 297-505 K (5th-95th pct of 11 curves)
- papers: https://doi.org/10.1021/cm100269a (Reversible Property Switching, Thermoelectric Performance, and d10−d10...) | https://doi.org/10.1016/j.jssc.2011.01.031 (Effects of partial anion substitution on the thermoelectric properties...) | https://doi.org/10.1016/j.solidstatesciences.2011.02.012 (A conceptional approach to materials for resistivity switching and the...)

## Ag-Cu-S
- rank 949 | 6 samples | 1 papers | 1 compositions
- compositions: AgCuS (6)
- measured range: 291-542 K (5th-95th pct of 7 curves)
- [ref 1] TEDesignLab / ICSD: CuAg3S2 I4_1/amd (141) mp-5725 [hull=0.043, icsd=2, PRIMARY]; CuAgS Cmc2_1 (36) mp-1077811 [hull=0.032, icsd=2]; CuAgS Cmcm (63) mp-8911 [hull=0.024, icsd=1]; CuAg3S2 I4_1/a (88) mp-644883 [hull=0.037, icsd=1]; CuAgS (26)
- [ref 2] MP, ranked by ICSD evidence: CuAgS Pnma (62) mp-5014 [hull=0.024, icsd=2, PRIMARY, AMBIGUOUS]; CuAgS P4/nmm (129) mp-1205410 [hull=0.107, icsd=1]
- papers: https://doi.org/10.1039/c5sc02966j (The effect of order–disorder phase transitions and band gap evolution ...)

## Ag-Ge-Pb-Sb-Te
- rank 950 | 6 samples | 1 papers | 6 compositions
- compositions: (Ge0.62Ag0.11Sb0.13Pb0.12Cd0.05Te)Bi0.01 (1); (Ge0.62Ag0.11Sb0.13Pb0.12Mn0.05Te)Bi0.01 (1); (Ge0.62Ag0.11Sb0.13Pb0.12Sn0.05Te)Bi0.01 (1); Ge0.62Ag0.11Sb0.13Pb0.12Te (1); (Ge0.62Ag0.11Sb0.13Pb0.12Te)Bi0.01 (1); (Ge0.62Ag0.11Sb0.13Pb0.12Te)Bi0.01Cu0.003 (1)
- dopant candidates (<5% at.): Bi (5), Cd (1), Mn (1), Sn (1), Cu (1)
- sample form: Polycrystal (6)
- measured range: 299-801 K (5th-95th pct of 30 curves)
- papers: https://doi.org/10.1126/science.abq5815 (High figure-of-merit and power generation in high-entropy GeTe-based t...)
