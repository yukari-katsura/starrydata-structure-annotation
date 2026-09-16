# Host systems -- chunk 013 of 73

Ranks 601-650 by sample count. These 50 host systems cover 528 samples (1.01% of the TE set); cumulative through this chunk: 83.88%.

Assign each host system a structural prototype from `data/annotated/taxonomy/prototypes_seed_v3.json`, or propose a new one in `taxonomy/prototypes_proposed.jsonl` first. Append results to `data/annotated/annotations/family_assignments.jsonl`.

The hand-entered MaterialFamily labels are deliberately NOT shown here -- they are held out in `df_host_systems.parquet` to validate this classification later. Decide from the compositions.

A "seed hypothesis" line means the taxonomy already names this host under that prototype. Confirm it against the compositions rather than accepting it; two or more listed means the host is mixed and needs splitting per composition.

Evidence follows the project precedence. Your judgement about the thermoelectric chemistry decides the prototype. [ref 1] is TEDesignLab, ICSD-backed and thermoelectric-specific -- prefer it. [ref 2] is Materials Project. Within a formula, polymorphs are ranked by ICSD reference count and the top one is marked PRIMARY -- not by e_above_hull, which is unusable for layered chalcogenides in the 2019 dump (Sb2Te3 R-3m carries 26 ICSD refs at hull 1.02). A primary resting on fewer than 5 ICSD references is flagged weak; the ambient phase may simply be absent from the snapshot, as it is for Bi2Se3.

While you have the host in view, also record what each minor element DOES, in `dopant_roles` -- the role follows from the prototype and cannot be judged without it. A median host has 2 such elements. Not everything listed is a dopant: O, C, N and H are usually milling or pressing residue, and an element just under 5 at.% may be an alloying end member rather than dilute doping. The doping LEVEL is computed later from the parsed fractions -- do not work it out by hand here.

A polymorph list is NOT a thermal sequence. SnSe has three known structures but only Pnma -> Cmcm happens on heating; rocksalt SnSe is metastable (2 icsd refs against 32). Put thermally reached phases in `phases` with their transition temperatures, and everything else in `other_polymorphs` with an occurrence reason. hull and icsd counts are shown to help you tell them apart.

A host may need MORE THAN ONE prototype. Transport is measured across a wide window and many thermoelectrics transform inside it, so where a "MEASUREMENT CROSSES A TRANSITION" line appears, record each phase with its own temperature range in the `phases` field. Transition temperatures shown are approximate and composition-dependent.

Both references describe which phases EXIST in a chemistry, not which phase this paper made. Al-O-Zn is best attested as ZnAl2O4 spinel (227) while almost every sample in it is Al-doped wurtzite ZnO (186). Weigh them against the compositions; do not follow them blindly.

## C-Ti
- rank 601 | 11 samples | 6 papers | 7 compositions
- compositions: TiC (4); TiC0.96 (2); C84Ti16 (1); C91.5Ti8.5 (1); TiC0.93 (1); TiC0.88 (1)
- seed hypothesis (confirm): rocksalt_nitride_carbide
- measured range: 12-1073 K (5th-95th pct of 11 curves; full span incl. outliers 12-1312 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): TiC Fm-3m (225) mp-631 [hull=0.000, icsd=37, PRIMARY]; Ti8C5 R-3m (166) mp-27919 [hull=0.000, icsd=2, PRIMARY]; Ti2C Fd-3m (227) mp-10721 [hull=0.000, icsd=1, PRIMARY]; Ti3C2 P6_3/mmc (194) mp-1094034 [hull=0.061, PRIMARY]; Ti3C Pm-3m (221) mp-1187454 [hull=0.863, PRIMARY]
- papers: Thermal diffusivity/conductivity of doped graphites | Microstructure and thermal conductivity of Mo–TiC cermets processed by hot isostatic pressing | Densification and Thermal Properties of TiC-Ni3Al Composites Materials.

## Ca-In-Sb
- rank 602 | 11 samples | 4 papers | 8 compositions
- compositions: Ca5In2Sb6 (4); Ca5In0.98Zn0.02Sb6 (1); Ca5In0.95Zn0.05Sb6 (1); Ca5In0.8Zn0.2Sb6 (1); Ca5In0.9Zn0.1Sb6 (1); Ca5Al0.2In1.7Zn0.1Sb6 (1)
- dopant candidates (<5% at.): Zn (6), Al (2)
- measured range: 293-976 K (5th-95th pct of 37 curves)
- [ref 1] TEDesignLab / ICSD: Ca5(InSb3)2 Pbam (55) mp-649479 [hull=0.000, icsd=1, PRIMARY]
- [ref 2] MP, ranked by ICSD evidence: Ca11InSb9 Iba2 (45) mp-29722 [hull=0.000, icsd=1, PRIMARY]
- papers: Thermoelectric properties of Zn-doped Ca5In2Sb6 | Thermoelectric properties of the Ca5Al2−xInxSb6solid solution | Thermoelectric properties and electronic structure of the Zintl phase Sr5In2Sb6 and the Ca5−xSrxIn2Sb6 solid solution

## Cd-Fe-O
- rank 603 | 11 samples | 5 papers | 8 compositions
- compositions: CdFe2O4 (4); CdFe1.9Gd0.1O4 (1); Li0.2Cd0.6Fe2.2O4 (1); Li0.1Cd0.8Fe2.1O4 (1); Li0.3Cd0.4Fe2.3O4 (1); Cd0.8Ni0.2Fe2O4 (1)
- dopant candidates (<5% at.): Li (3), Gd (1), Ni (1), Mn (1), Cu (1)
- seed hypothesis (confirm): spinel
- measured range: 292-928 K (5th-95th pct of 17 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Cd(FeO2)2 Fd-3m (227) mp-24940 [hull=0.000, icsd=1, PRIMARY]; CdFeO3 Pnma (62) mp-777146 [hull=0.078, PRIMARY]; Cd(FeO2)2 P3m1 (156) mp-705824 [hull=0.027]; Cd(FeO2)2 Pnma (62) mp-772600 [hull=0.069]
- papers: Thermoelectric power in Gd3+-substituted Cu-Cd ferrites | Electrical conductivity and thermoelectric power of lithium-cadmium ferrites | []

## Ce-Cu-Sb
- rank 604 | 11 samples | 4 papers | 3 compositions
- compositions: Ce3Cu3Sb4 (8); Ce5CuSb3 (2); Ce3Cu2.75Ni0.25Sb4 (1)
- dopant candidates (<5% at.): Ni (1)
- measured range: 10-398 K (5th-95th pct of 38 curves; full span incl. outliers 10-458 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): CeCuSb2 P4/nmm (129) mp-672238 [hull=0.000, icsd=2, PRIMARY]; Ce(CuSb)2 P4/nmm (129) mp-1006321 [hull=0.133, icsd=1, PRIMARY]; Ce3Cu3Sb4 I-43d (220) mp-1189165 [hull=0.000, icsd=1, PRIMARY]; Ce2Cu3Sb4 P4mm (99) mp-1227069 [hull=0.089, PRIMARY]; Ce4Cu5Sb8 P4mm (99) mp-1227972 [hull=0.058, PRIMARY]
- papers: Semiconducting behaviour of Ce3 Cu3 Sb4 revisited | Low-temperature properties of the heavy-fermion antiferromagnetCe5CuSb3 | Impact of microstructure on the thermoelectric properties of the ternary compound Ce 3 Cu 3 Sb 4

## Ce-Ni-Pd-Si
- rank 605 | 11 samples | 3 papers | 7 compositions
- compositions: Ce(Ni0.3Pd0.7)2Si2 (2); Ce(Ni0.4Pd0.6)2Si2 (2); Ce(Ni0.2Pd0.8)2Si2 (2); Ce(Ni0.6Pd0.4)2Si2 (2); Ce2Ni2.5Pd0.5Si (1); Ce2Ni2PdSi (1)
- seed hypothesis (confirm): thcr2si2_122
- solid-solution axis: Ni/(Ni+Pd) spans 0.15-0.83 (median 0.40) over 7 compositions
     ISOELECTRONIC SERIES: the parent compound depends on the composition, not on this host. Near either end the minor element is a dilute substituent; in the middle it is a genuine alloy. Record the axis, not one parent -- and note the 5% split used the whole formula, not the sublattice, so its cut lands at a different level on each site.
- measured range: 10-298 K (5th-95th pct of 18 curves)
- papers: Thermoelectric properties of the intermediate valent cerium intermetallic Ce2Ni3Si5 doped with Pd, Co, and Cu | Heavy fermion behavior in Ce(NixPd1−x)2Si2 | Transport properties of Ce(NixPd1−x)2Si2

## Ce-Sb
- rank 606 | 11 samples | 5 papers | 2 compositions
- compositions: CeSb (9); Ce4Sb3 (2)
- measured range: 10-1233 K (5th-95th pct of 12 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): CeSb Fm-3m (225) mp-387 [hull=0.000, icsd=15, PRIMARY]; Ce4Sb3 I-43d (220) mp-20680 [hull=0.002, icsd=6, PRIMARY]; Ce2Sb I4/mmm (139) mp-22678 [hull=0.000, icsd=2, PRIMARY]; Ce5Sb3 P6_3/mcm (193) mp-1188999 [hull=0.013, icsd=1, PRIMARY]; CeSb2 Cmce (64) mp-1102986 [hull=0.000, icsd=1, PRIMARY]
- papers: High-temperature transport properties of complex antimonides with anti-Th3P4structure | High-Temperature Transport Properties of Yb4−x Sm x Sb3 | Possible Weyl fermions in the magnetic Kondo system CeSb

## Co-O-Sm
- rank 607 | 11 samples | 6 papers | 5 compositions
- compositions: SmCoO3 (4); Sm0.9Sr0.1CoO3 (2); Sm0.9Ca0.1CoO3 (2); Sm0.8Sr0.2CoO3 (2); SmCo0.95Ni0.05O3 (1)
- dopant candidates (<5% at.): Sr (4), Ca (2), Ni (1)
- seed hypothesis (confirm): perovskite
- measured range: 89-1210 K (5th-95th pct of 15 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): SmCoO3 Pnma (62) mp-24877 [hull=0.000, icsd=2, PRIMARY]; Sm2Co2O5 Ima2 (46) mp-1076063 [hull=0.105, PRIMARY]; Sm2CoO3 P1 (1) mp-1173620 [hull=0.672, PRIMARY]; SmCoO3 Pm-3m (221) mp-24865 [hull=0.151, icsd=1]
- papers: High-temperature thermoelectric properties of Ln(Co, Ni)O3 (Ln=La, Pr, Nd, Sm, Gd and Dy) compounds | Influence of ionic size of rare-earth site on the thermoelectric properties of RCoO3-type perovskite cobalt oxides | Thermoelectric properties of the SmCoO3 and NdCoO3 cobalt oxides

## Co-O-Sr-Ti
- rank 608 | 11 samples | 3 papers | 11 compositions
- compositions: Sr1.6La0.4CoTiO6 (1); Sr2CoTiO6 (1); Sr1.8La0.2CoTiO6 (1); Sr2TiCoO6 (1); Ba0.15Sr1.85TiCoO6 (1); Ba0.1Sr1.9TiCoO6 (1)
- dopant candidates (<5% at.): Ba (3), La (2)
- measured range: 67-1232 K (5th-95th pct of 27 curves)
- papers: Structural and semiconductor-to-metal transitions of double-perovskite cobalt oxide Sr2−xLaxCoTiO6−δ with enhanced thermoelectric capability | Enhanced thermoelectric figure-of-merit in environmentally benign BaxSr2-xTiCoO6 double perovskites | Structural, Magnetic, and Transport Properties of the SrTi<sub>1</sub><sub>-</sub><i><sub>x</sub></i>Co<i><sub>x</sub></i>O<sub>3</sub><sub>-</sub><sub>δ</sub> Perovskite (0 ≤ <i>x</i> ≤ 0.9)

## Co-Sb-Sn-Ti-V
- rank 609 | 11 samples | 2 papers | 2 compositions
- compositions: Ti0.7V0.3Co.85Fe0.15Sb0.7Sn0.3 (6); Ti0.7V0.3CoSb0.7Sn0.3 (5)
- dopant candidates (<5% at.): Fe (6)
- measured range: 299-910 K (5th-95th pct of 36 curves)
- papers: Thermoelectric properties and high-temperature stability of the Ti1−xVxCoSb1−xSnx half-Heusler alloys | Substitution Versus Full-Heusler Segregation in TiCoSb

## Cu-Mo-Se
- rank 610 | 11 samples | 4 papers | 4 compositions
- compositions: Cu4Mo6Se8 (4); Cu2Mo6Se8 (4); Cu1.38Fe0.66Mo6Se8 (2); CuMo6Se8 (1)
- dopant candidates (<5% at.): Fe (2)
- measured range: 290-1262 K (5th-95th pct of 15 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Cu(Mo3Se4)2 R-3 (148) mp-1104894 [hull=0.094, icsd=1, PRIMARY]
- papers: Promising thermoelectric properties in AgxMo9Se11 compounds (3.4≤x≤3.9) | Yb14MnSb11:  New High Efficiency Thermoelectric Material for Power Generation | Synthesis and thermoelectric properties of alloys

## Cu-Si-Yb
- rank 611 | 11 samples | 7 papers | 5 compositions
- compositions: YbCu2Si2 (7); YbCu1Si2 (1); Yb(Cu0.151Si0.849)1.883 (1); Yb(Cu0.145Si0.855)1.833 (1); Yb(Cu0.132Si0.868)1.844 (1)
- seed hypothesis (confirm): thcr2si2_122
- measured range: 10-350 K (5th-95th pct of 17 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Yb(CuSi)2 I4/mmm (139) mp-5934 [hull=0.000, icsd=3, PRIMARY]; Yb3(CuSi)4 Immm (71) mp-1205488 [hull=0.037, icsd=1, PRIMARY]; YbCuSi P6_3/mmc (194) mp-8124 [hull=0.007, icsd=1, PRIMARY]; Yb3Cu11Si4 P6_3/mmc (194) mp-1207653 [hull=0.072, PRIMARY]
- papers: Influence of rare earth doping on thermoelectric properties of SrTiO3 ceramics | Interplay of chemical expansion, Yb valence, and low temperature thermoelectricity in the YbCu2Si2−xGex solid solution | Demagnetization due to interconfiguration fluctuations in the RE-Cu2Si2 compounds

## Cu-Sn-Te
- rank 612 | 11 samples | 3 papers | 10 compositions
- compositions: (Sn0.95Cd0.05Te)0.93(Cu2Te)0.07 (2); (SnTe)0.94(Cu2Te)0.06 (1); Cu5Sn2Te7 (1); (Sn0.95Cd0.05Te)0.93(Cu2Te)0.07I0.0025 (1); (Sn0.95Cd0.05Te)0.93(Cu2Te)0.07I0.01 (1); (Sn0.95Cd0.05Te)0.93(Cu2Te)0.07I0.015 (1)
- dopant candidates (<5% at.): Cd (9), I (6)
- measured range: 15-826 K (5th-95th pct of 54 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Cu2SnTe3 Imm2 (44) mp-13089 [hull=0.000, icsd=1, PRIMARY]; Cu5Sn2Te7 C2 (5) mp-1103821 [hull=0.000, icsd=1, PRIMARY]; Cu2SnTe3 Cc (9) mp-675880 [hull=0.001]; Cu2SnTe3 Fdd2 (43) mp-1226087 [hull=0.026]
- papers: Interstitial Point Defect Scattering Contributing to High Thermoelectric Performance in SnTe | Metallic Ternary Telluride with Sphalerite Superstructure | Eutectoid nano-precipitates inducing remarkably enhanced thermoelectric performance in (Sn1−xCdxTe)1−y(Cu2Te)y

## Fe-Mg-O
- rank 613 | 11 samples | 4 papers | 6 compositions
- compositions: MgFe2O4 (6); Li0.15Mg0.7Fe2.15O4 (1); Li0.05Mg0.9Fe2.05O4 (1); Li0.25Mg0.5Fe2.25O4 (1); MgSm0.1Fe1.9O4 (1); MgSm0.050Fe1.950O4 (1)
- dopant candidates (<5% at.): Li (3), Sm (2)
- seed hypothesis (confirm): spinel
- measured range: 300-996 K (5th-95th pct of 22 curves; full span incl. outliers 294-1095 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Mg(FeO2)2 Pbcm (57) mp-630714 [hull=0.101, icsd=1, PRIMARY]; Mg(Fe5O8)2 R3m (160) mp-773318 [hull=0.215, PRIMARY]; Mg10(Fe3O8)3 P1 (1) mp-34015 [hull=0.093, PRIMARY]; Mg10FeO11 P-1 (2) mp-761768 [hull=0.000, PRIMARY]; Mg11(Fe15O28)2 P1 (1) mp-705780 [hull=0.058, PRIMARY]
- papers: Effect of sintering temperature and thermoelectric power studies of the system MgFe2−xCrxO4 | Thermoelectric power studies of polycrystalline magnesium substituted lithium ferrites | Effect of spark plasma sintering (SPS) on the thermoelectric properties of magnesium ferrite

## Ga-O
- rank 614 | 11 samples | 4 papers | 11 compositions
- compositions: (Ti)0.00182(Ga2O3)0.99818 (1); Ga2O3 (1); (Al0.1Ga0.9)2O3 (1); Sn0.0008Ga2O3 (1); Sn0.0002Ga2O3 (1); Sn0.01Ga2O3 (1)
- dopant candidates (<5% at.): Si (5), Sn (3), Ti (1), Al (1)
- measured range: 14-451 K (5th-95th pct of 11 curves; full span incl. outliers 14-572 K)
- [ref 1] TEDesignLab / ICSD: Ga2O3 C2/m (12) mp-886 [hull=0.000, icsd=5, PRIMARY]; Ga2O3 R-3c (167) mp-1243 [hull=0.029, icsd=4]; Ga2O3 Cmcm (63) mp-13134 [hull=0.285, icsd=1]
- [ref 2] MP, ranked by ICSD evidence: Ga11NO17 P6_3/mmc (194) mp-1200059 [hull=0.250, icsd=2, PRIMARY]; GaO3 Im-3 (204) mp-1181293 [hull=0.604, icsd=1, PRIMARY]; GaO2 Fddd (70) mp-1181290 [hull=0.376, icsd=1, PRIMARY]; NaGa11O18 P2_1/m (11) mp-1200040 [hull=0.052, icsd=1, PRIMARY]; Ga11NO15 P1 (1) mp-676333 [hull=0.044, PRIMARY]
- papers: Ti-Doped β-Ga2O3: A Promising Material for Ultrafast and Tunable Lasers | Significantly reduced thermal conductivity in β-(Al0.1Ga0.9)2O3/Ga2O3 superlattices | Electrical, optical, and magnetic properties of Sn doped α-Ga2O3 thin films

## Ge-Sn-Te
- rank 615 | 11 samples | 5 papers | 11 compositions
- compositions: Ge0.2Sn0.8Te (1); Ge0.1Sn0.9Te (1); (Bi2Te3)0.05Sn0.2Ge0.8Te (1); Sn14Ge47Te39 (1); Sn26Ge40Te34 (1); Sn29Ge38Te33 (1)
- dopant candidates (<5% at.): Bi (1)
- seed hypothesis (confirm): gete_rhombohedral
- solid-solution axis: Ge/(Ge+Sn) spans 0.10-0.80 (median 0.50) over 11 compositions
     ISOELECTRONIC SERIES: the parent compound depends on the composition, not on this host. Near either end the minor element is a dilute substituent; in the middle it is a genuine alloy. Record the axis, not one parent -- and note the 5% split used the whole formula, not the sublattice, so its cut lands at a different level on each site.
- measured range: 49-809 K (5th-95th pct of 32 curves)
  !! MEASUREMENT CROSSES A TRANSITION: gete_rhombohedral -> rocksalt at ~700 K (R3m -> Fm-3m, ~700 K; shifts with Ge vacancy content and doping.)
     Record each phase with its own temperature range, not a single prototype.
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Sn2GeTe3 P-3m1 (164) mp-1218976 [hull=0.019, PRIMARY]; Sn2GeTe3 Pm (6) mp-1219050 [hull=0.047]
- papers: Thermoelectric properties of Ge1−xSnxTe crystals grown by vertical Bridgman method | Phase transitions of p-type (Pb,Sn,Ge)Te-based alloys for thermoelectric applications | Thermoelectric properties of Sn doped GeTe thin films

## H-Li
- rank 616 | 11 samples | 2 papers | 1 compositions
- compositions: LiH (11)
- measured range: 11-794 K (5th-95th pct of 10 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): LiH Fm-3m (225) mp-23703 [hull=0.000, icsd=20, PRIMARY]
- papers: Nonmetallic crystals with high thermal conductivity | Isotope scattering and phonon thermal conductivity in light atom compounds: LiH and LiF

## In-Mn-Ni
- rank 617 | 11 samples | 3 papers | 7 compositions
- compositions: Ni50Mn34In16 (4); Ni50Mn35In15 (2); In46 (Ni0.8Mn0.2)54 (1); In46 (Ni0.9Mn0.1)54 (1); In46 (Ni0.7Mn0.3)54 (1); In46 (Ni0.5Mn0.5)54 (1)
- seed hypothesis (confirm): full_heusler
- measured range: 13-1433 K (5th-95th pct of 16 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): MnInNi2 Fm-3m (225) mp-22731 [hull=0.044, icsd=6, PRIMARY]
- papers: Electrical resistivity and absolute thermoelectric power of liquid indium-nickel-manganese ternary alloys | Temperature dependence of thermoelectric power and thermal conductivity in ferromagnetic shape memory alloyNi50Mn34In16in magnetic fields | Effect of Crystalline Structure on Some Physical Properties of Bulk and Thin Film Ni$_{50}$Mn$_{35}$In$_{15}$ Alloy Samples

## La-Mn-Na-O
- rank 618 | 11 samples | 6 papers | 4 compositions
- compositions: La0.67Na0.33MnO3 (4); La0.7Na0.3MnO3 (3); La0.75Na0.25MnO3 (3); La0.6Na0.4MnO3 (1)
- measured range: 13-1468 K (5th-95th pct of 17 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): NaLa2Mn3O9 P-3m1 (164) mp-1220767 [hull=0.042, PRIMARY]
- papers: Influence of sintering temperature and oxygen stoichiometry on electrical transport properties of La0.67Na0.33MnO3 manganite | Thermoelectric power of Na-doped La0.7Ca0.3−yNayMnO3 both in the presence and the absence of magnetic field | Magnetoelectric behavior of sodium doped lanthanum manganites

## La-Nb-S
- rank 619 | 11 samples | 3 papers | 5 compositions
- compositions: (LaS)1.14NbS2 (4); La1.083S1.083NbS2 (2); La1.14S1.14NbS2 (2); La1.197S1.197NbS2 (2); (La2S2)2NbS2 (1)
- seed hypothesis (confirm): misfit_layered_chalcogenide
- measured range: 13-965 K (5th-95th pct of 53 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): La8Nb7S22 Ccc2 (37) mp-28507 [hull=0.000, icsd=1, PRIMARY]
- papers: Microstructural Control and Thermoelectric Properties of Misfit Layered Sulfides (LaS)1+mTS2(T = Cr, Nb): The Natural Superlattice Systems | Nanostructural and Microstructural Ordering and Thermoelectric Property Tuning in Misfit Layered Sulfide [(LaS)x]1.14NbS2 | Crystal Structure and Thermoelectric Properties of Misfit-Layered Sulfides [Ln2S2] p NbS2 (Ln = Lanthanides)

## N-O
- rank 620 | 11 samples | 2 papers | 1 compositions
- compositions: N2O (11)
- measured range: 10-139 K (5th-95th pct of 9 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): NO C2/c (15) mp-1079684 [hull=0.866, icsd=6, PRIMARY]; N2O3 Pmmn (59) mp-1079708 [hull=1.163, icsd=4, PRIMARY]; NO2 Im-3 (204) mp-2789 [hull=0.000, icsd=4, PRIMARY]; NO6 P2_12_12_1 (19) mp-1180438 [hull=0.357, icsd=3, PRIMARY]; N4O9 P2_1 (4) mp-1180808 [hull=0.527, icsd=2, PRIMARY]
- papers: High thermal conductivity of solid nitrous oxide at low temperatures | Low-temperature thermal conductivity of cryocrystals formed by linear three-atom molecules

## Nb-Sb-Te
- rank 621 | 11 samples | 2 papers | 10 compositions
- compositions: Nb3Sb2Te5 (2); Nb3Sb1.5Te5.5 (1); Nb3Sb3.05Te3.95 (1); Nb3Sb2.95Te4.05 (1); Nb3Sb3.5Te3.5 (1); Nb3Sb6Te1 (1)
- measured range: 11-772 K (5th-95th pct of 22 curves)
- papers: Thermoelectric properties of Nb3Sb2Te5 | Thermoelectric properties of Nb/sub 3/Sb/sub x/Te/sub 7-x/ compounds

## O-Pb-V
- rank 622 | 11 samples | 2 papers | 10 compositions
- compositions: (PbO)50(V2O5)50 (2); (ZnO)0.1(PbO)0.4(V2O5)0.5 (1); (PbO)0.5(V2O5)0.5 (1); (ZnO)0.05(PbO)0.45(V2O5)0.5 (1); (ZnO)0.15(PbO)0.35(V2O5)0.5 (1); (Ag2O)5(PbO)45(V2O5)50 (1)
- dopant candidates (<5% at.): Zn (3), Cd (3), Ag (2)
- measured range: 298-500 K (5th-95th pct of 11 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): VPbO3 P4mm (99) mp-25119 [hull=0.026, icsd=6, PRIMARY]; V3Pb5ClO12 P6_3/m (176) mp-628782 [hull=0.000, icsd=6, PRIMARY]; V2Pb3O8 C2 (5) mp-25142 [hull=0.003, icsd=4, PRIMARY]; V6PbO11 P6_3/mmc (194) mp-25790 [hull=0.032, icsd=2, PRIMARY]; V3Pb5O12F P6_3/m (176) mp-1207903 [hull=0.000, icsd=2, PRIMARY]
- papers: Transport properties of ZnO substituted lead vanadate glass system at eutectic composition | Anomalous temperature variation of thermoelectric power in CdO and Ag2O substituted lead vanadate glass system

## O-Rh
- rank 623 | 11 samples | 3 papers | 5 compositions
- compositions: Sr0.22Rh2O4 (3); Ba1.2Rh8O16 (2); Sr0.11Rh2O4 (2); Sr0.17Rh2O4 (2); Sr0.14Rh2O4 (2)
- dopant candidates (<5% at.): Sr (9), Ba (2)
- measured range: 23-991 K (5th-95th pct of 12 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Rh2O3 Pbcn (60) mp-1716 [hull=0.025, icsd=4, PRIMARY]; RhO2 P4_2/mnm (136) mp-725 [hull=0.000, icsd=2, PRIMARY]; RhO3 R32 (155) mp-1219486 [hull=0.545, PRIMARY]; Rh2O3 Pbca (61) mp-613620 [hull=0.027, icsd=1]; Rh2O3 Pnma (62) mp-1179690 [hull=0.173, icsd=1]
- papers: Thermal Conductivity of Thermoelectric Rhodium Oxides Measured by a Modified Harman Method | Thermal Conductivity and Dimensionless Figure of Merit of Thermoelectric Rhodium Oxides Measured by a Modified Harman Method | Correlated Metallic Phase in a Doped Band Insulator Sr1-xRh2O4

## Rh-Sb
- rank 624 | 11 samples | 3 papers | 6 compositions
- compositions: Rh4Sb12 (3); In0.1Rh4Sb12 (3); RhSb3 (2); In0.15Rh4Sb12 (1); In0.2Rh4Sb12 (1); In0.05Rh4Sb12 (1)
- dopant candidates (<5% at.): In (6)
- measured range: 302-625 K (5th-95th pct of 42 curves; full span incl. outliers 21-760 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Sb2Rh P2_1/c (14) mp-2682 [hull=0.000, icsd=5, PRIMARY]; SbRh Pnma (62) mp-20619 [hull=0.000, icsd=4, PRIMARY]; Sb3Rh Im-3 (204) mp-2395 [hull=0.000, icsd=3, PRIMARY]; SbRh2 Pnma (62) mp-21359 [hull=0.000, icsd=2, PRIMARY]; SbRh3 Pm-3m (221) mp-973342 [hull=0.011, PRIMARY]
- papers: Thermoelectric properties of indium-filled InxRh4Sb12 skutterudites | Thermoelectric properties of CoSb3and related alloys | Study of transport properties of the Co1−xRhxSb3

## Ru-Sb
- rank 625 | 11 samples | 6 papers | 6 compositions
- compositions: RuSb2 (6); Ru0.95Fe0.05Sb2 (1); Ru0.85Fe0.15Sb2 (1); Ru0.99Fe0.01Sb2 (1); Co0.1Ru0.9Sb2 (1); Cr0.1Ru0.9Sb2 (1)
- dopant candidates (<5% at.): Fe (3), Co (1), Cr (1)
- seed hypothesis (confirm): marcasite
- measured range: 10-621 K (5th-95th pct of 28 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Sb2Ru Pnnm (58) mp-20928 [hull=0.000, icsd=6, PRIMARY]; SbRu Pnma (62) mp-7565 [hull=0.051, icsd=1, PRIMARY]
- papers: Correlated evolution of colossal thermoelectric effect and Kondo insulating behavior | Huge Thermoelectric Power Factor: FeSb2versus FeAs2and RuSb2 | Thermoelectric properties of the narrow-gap semiconductors FeSb2and RuSb2: A comparative study

## Sc-Zn
- rank 626 | 11 samples | 1 papers | 1 compositions
- compositions: Zn6Sc_IAC_1_1 (11)
- measured range: 15-299 K (5th-95th pct of 11 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): ScZn Pm-3m (221) mp-11566 [hull=0.000, icsd=1, PRIMARY]; ScZn12 I4/mmm (139) mp-11567 [hull=0.000, icsd=1, PRIMARY]; ScZn2 P6_3/mmc (194) mp-13503 [hull=0.000, icsd=1, PRIMARY]; ScZn3 P6_3/mmc (194) mp-862260 [hull=0.000, PRIMARY]; ScZn6 Immm (71) mp-1219746 [hull=0.004, PRIMARY]
- papers: Experimental evidence for a phase transition in aZn6Sc1/1 cubic approximant

## Te-Zn
- rank 627 | 11 samples | 3 papers | 2 compositions
- compositions: ZnTe (10); Zn0.95Al0.05Te (1)
- dopant candidates (<5% at.): Al (1)
- seed hypothesis (confirm): sphalerite
- measured range: 11-601 K (5th-95th pct of 30 curves; full span incl. outliers 10-674 K)
- [ref 1] TEDesignLab / ICSD: ZnTe F-43m (216) mp-2176 [hull=0.000, icsd=27, PRIMARY]; ZnTe P3_121 (152) mp-1071319 [hull=0.159, icsd=5]; ZnTe P6_3mc (186) mp-8884 [hull=0.006, icsd=1]; ZnTe (144)
- [ref 2] MP, ranked by ICSD evidence: ZnTe2 P-3m1 (164) mp-1206914 [hull=0.257, PRIMARY]; ZnTe P6_422 (181) mp-9281 [hull=0.151, icsd=6]; ZnTe Fm-3m (225) mp-948 [hull=0.288, icsd=5]
- papers: Transport properties of ZnTe:N thin films | Low thermal conductivity and enhanced thermoelectric performance of nanostructured Al-doped ZnTe | Annealing effect on the thermal conductivity of thermoelectric ZnTe nanowires

## Te-Zr
- rank 628 | 11 samples | 6 papers | 3 compositions
- compositions: ZrTe5 (8); ZrTe4.75Se0.25 (2); Zr0.9Ti0.1Te5 (1)
- dopant candidates (<5% at.): Se (2), Ti (1)
- measured range: 10-379 K (5th-95th pct of 14 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): ZrTe3 P2_1/m (11) mp-2089 [hull=0.000, icsd=7, PRIMARY]; ZrTe5 Cmcm (63) mp-605 [hull=0.000, icsd=6, PRIMARY]; Zr5Te4 I4/m (87) mp-350 [hull=0.001, icsd=4, PRIMARY]; ZrTe P-6m2 (187) mp-1539 [hull=0.000, icsd=4, PRIMARY]; Zr3Te I-4 (82) mp-1793 [hull=0.000, icsd=3, PRIMARY]
- papers: Effect of Ti substitution on the thermoelectric properties of the pentatelluride materials M1−xTixTe5 (M=Hf, Zr) | Thermoelectric power of HfTe5 and ZrTe5 | Enhancement of the power factor of the transition metal pentatelluride HfTe5 by rare-earth doping

## Al-Au-Gd
- rank 629 | 10 samples | 2 papers | 9 compositions
- compositions: Au49Al37Gd14 (2); Au52Al34Gd14 (1); Au68Al18Gd14 (1); Au55Al31Gd14 (1); Au72Al14Gd14 (1); Au64Al22Gd14 (1)
- seed hypothesis (confirm): quasicrystal_approximant
- measured range: 372-871 K (5th-95th pct of 32 curves; full span incl. outliers 294-871 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): GdAl7Au3 R-3c (167) mp-22711 [hull=0.000, icsd=1, PRIMARY]
- papers: Thermoelectric properties of Tsai-type Au–Al–RE (RE: Yb, Tm, Gd) quasicrystals and approximants | Probing of the pseudogap via thermoelectric properties in the Au-Al-Gd quasicrystal approximant

## Al-C-Zr
- rank 630 | 10 samples | 3 papers | 7 compositions
- compositions: Zr2Al3C4 (2); Zr2Al3.56Si0.44C5 (2); Zr3Al3C5 (2); (ZrC)3Al3C2 (1); Zr3Al3.56Si0.44C6 (1); (ZrC)2Al3C2 (1)
- dopant candidates (<5% at.): Si (4)
- measured range: 346-1263 K (5th-95th pct of 30 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Zr2AlC P6_3/mmc (194) mp-3886 [hull=0.012, icsd=2, PRIMARY]; Zr5Al3C P6_3/mcm (193) mp-972176 [hull=0.039, icsd=1, PRIMARY]; Zr2Al3C4 P-3m1 (164) mp-1215737 [hull=0.225, PRIMARY]; Zr(AlC)4 P-3m1 (164) mp-1207385 [hull=0.021, PRIMARY]
- papers: Synthesis, crystal structure, and thermoelectric properties of a new layered carbide (ZrC)3[Al3.56Si0.44]C3 | Synthesis, crystal structure and thermoelectric properties of a new carbide Zr2[Al3.56Si0.44]C5 | Crystal Structure and Thermoelectric Properties of YAl3C3

## Al-Ce-Cu-La
- rank 631 | 10 samples | 2 papers | 2 compositions
- compositions: Ce0.6La0.4Cu4Al (5); Ce0.4La0.6Cu4Al (5)
- measured range: 10-300 K (5th-95th pct of 10 curves)
- papers: Thermopower of Ce1−xLaxCu4Al intermetallic compounds | Thermopower of Ce1–xLaxCu4Al in applied magnetic fields

## Al-Co-Cu
- rank 632 | 10 samples | 4 papers | 4 compositions
- compositions: Al62Si3Cu20Co15 (4); Al65Cu20Co15 (3); Al64.34Cu17.34Co18.25Fe0.07_DQC (2); Al65Cu20Co12.5Fe2.5 (1)
- dopant candidates (<5% at.): Si (4), Fe (3)
- measured range: 10-301 K (5th-95th pct of 10 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Al12Co4Cu C2/m (12) mp-17017 [hull=0.000, icsd=1, PRIMARY]; Al7CoCu2 P4/mnc (128) mp-17856 [hull=0.003, icsd=1, PRIMARY]; Al6CoCu3 P3m1 (156) mp-1228194 [hull=0.000, PRIMARY]
- papers: New stable icosahedral quasicrystal in the system Al–Cu–Co–Fe | Electron transport in Al65Cu20Co15−xFex quasicrystals | Low-Temperature Thermodynamic and Thermal-Transport Properties of Decagonal A<mml:math xmlns:mml=\"http://www.w3.org/1998/Math/MathML\" display=\"inline\"><mml:mrow><mml:msub><mml:mrow><mml:mi mathvariant=\"normal\">l</mml:mi></mml:mrow><mml:mrow><mml:mn>65</mml:mn></mml:mrow></mml:msub></mml:mrow></mml:math>C<mml:math xmlns:mml=\"http://www.w3.org/1998/Math/MathML\" display=\"inline\"><mml:mrow><mml:msub><mml:mrow><mml:mi mathvariant=\"normal\">u</mml:mi></mml:mrow><mml:mrow><mml:mn>20</mml:mn></mml:mrow></mml:msub></mml:mrow></mml:math>C<mml:math xmlns:mml=\"http://www.w3.org/1998/Math/MathML\" display=\"inline\"><mml:mrow><mml:msub><mml:mrow><mml:mi mathvariant=\"normal\">o</mml:mi></mml:mrow><mml:mrow><mml:mn>15</mml:mn></mml:mrow></mml:msub></mml:mrow></mml:math>

## As-Fe-La-O-Ru
- rank 633 | 10 samples | 1 papers | 4 compositions
- compositions: LaFe0.78Ru0.22AsO0.89F0.11 (3); LaFe0.7Ru0.3AsO0.89F0.11 (3); LaFe0.5Ru0.5AsO0.89F0.11 (3); LaFe0.3Ru0.7AsO0.89F0.11 (1)
- dopant candidates (<5% at.): F (10)
- seed hypothesis (confirm): zrcusias_1111
- solid-solution axis: Fe/(Fe+Ru) spans 0.30-0.78 (median 0.70) over 4 compositions
     ISOELECTRONIC SERIES: the parent compound depends on the composition, not on this host. Near either end the minor element is a dilute substituent; in the middle it is a genuine alloy. Record the axis, not one parent -- and note the 5% split used the whole formula, not the sublattice, so its cut lands at a different level on each site.
- measured range: 10-300 K (5th-95th pct of 10 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): La2FeAs2RuO2 P-4m2 (115) mp-1223264 [hull=0.112, PRIMARY]; La4FeAs4Ru3O4 P-42m (111) mp-1223053 [hull=0.001, PRIMARY]; La4FeAs4Ru3O4 P-4m2 (115) mp-1223024 [hull=0.005]
- papers: Superconducting Transition Temperatures and Transport Properties of LaFe1-yRuyAsO0.89F0.11and LaFeAsO0.89-xF0.11+x

## B-Co
- rank 634 | 10 samples | 2 papers | 10 compositions
- compositions: Co60B40 (1); Co65B35 (1); Co75B25 (1); Co70B30 (1); Co80B20 (1); CoB (1)
- dopant candidates (<5% at.): Ni (3), Fe (1)
- measured range: 80-949 K (5th-95th pct of 10 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Co2B I4/mcm (140) mp-1071320 [hull=0.025, icsd=7, PRIMARY]; Co3B Pnma (62) mp-20373 [hull=0.022, icsd=6, PRIMARY]; CoB Pnma (62) mp-20857 [hull=0.000, icsd=3, PRIMARY]; Co5B16 Pmma (51) mp-1194572 [hull=0.031, icsd=2, PRIMARY]; Co23B6 Fm-3m (225) mp-639154 [hull=0.017, icsd=2, PRIMARY]
- papers: Thermoelectric power of amorphous Co100−xBx alloys | Seebeck coefficients of iron group elements borides

## B-Fe-Ni-Si
- rank 635 | 10 samples | 2 papers | 7 compositions
- compositions: Fe40Ni40B10Si10 (2); Fe20Ni60B10Si10 (2); Fe50Ni30B10Si10 (2); Fe60Ni20B10Si10 (1); Fe40Ni40Mo2Si10B8 (1); Fe38.5Ni38.5C3Mo2Si10B8 (1)
- dopant candidates (<5% at.): Mo (3), C (2)
- seed hypothesis (confirm): metallic_glass
- measured range: 39-947 K (5th-95th pct of 10 curves)
- papers: Thermoelectric power singularities of FeNiBSi amorphous alloys | Thermopower of amorphous Fe-Ni-Cr-Mo-Si-B in the temperature range 40–700 K

## B-Fe-Si
- rank 636 | 10 samples | 3 papers | 3 compositions
- compositions: Fe78Si9B13 (7); (FeSi2)0.875(TiB2)0.125 (2); (FeSi2)0.9(TiB2)0.1 (1)
- dopant candidates (<5% at.): Ti (3)
- measured range: 117-860 K (5th-95th pct of 29 curves; full span incl. outliers 116-1102 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Fe5SiB2 I4/mcm (140) mp-1105372 [hull=0.007, icsd=3, PRIMARY]; Fe5Si2B I4/mcm (140) mp-1188610 [hull=0.037, icsd=1, PRIMARY]; Fe6SiB Pmc2_1 (26) mp-1225187 [hull=0.116, PRIMARY]
- papers: The effect of titanium diboride addition on the thermoelectric properties of β-FeSi2 semiconductors | Thermoelectric properties of β-FeSi/sub 2/-TiB/sub 2/ composites | Effect of nanocrystallization of magnetic amorphous ribbon on thermoelectric and magnetic properties

## B-Fe-Si-Ti
- rank 637 | 10 samples | 2 papers | 5 compositions
- compositions: (FeSi2)0.85(TiB2)0.15 (2); (FeSi2)0.8(TiB2)0.2 (2); (FeSi2)0.745(TiB2)0.255 (2); (FeSi2)0.825(TiB2)0.175 (2); (FeSi2)0.7(TiB2)0.3 (2)
- seed hypothesis (confirm): beta_fesi2, composite_multiphase  <-- MIXED, split per composition
- measured range: 121-1100 K (5th-95th pct of 35 curves)
- papers: The effect of titanium diboride addition on the thermoelectric properties of β-FeSi2 semiconductors | Thermoelectric properties of β-FeSi/sub 2/-TiB/sub 2/ composites

## Ba-Ce-O
- rank 638 | 10 samples | 5 papers | 8 compositions
- compositions: BaCeO3 (2); BaCe0.95Tb0.05O3 (2); BaCe0.85Tb0.05Co0.1O3 (1); BaCe0.85Tb0.05Y0.1O3 (1); BaCe0.85Tb0.05Zr0.1O3 (1); BaCe0.85Tb0.15O3 (1)
- dopant candidates (<5% at.): Tb (8), Co (1), Y (1), Zr (1), Fe (1), Mn (1)
- measured range: 285-1123 K (5th-95th pct of 10 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): BaCeO3 Pnma (62) mp-3187 [hull=0.000, icsd=14, PRIMARY]; BaCe2O4 Pnma (62) mp-778873 [hull=0.014, icsd=1, PRIMARY]; Ba2Ce2O5 Pbam (55) mp-769656 [hull=0.006, PRIMARY]; Ba4Ce2O7 Cmce (64) mp-770465 [hull=0.036, PRIMARY]; Ba3Ce2O6 I4/mmm (139) mp-1178568 [hull=0.034, PRIMARY]
- papers: Thermoelectric properties of perovskite type barium molybdate | Thermoelectric properties of perovskite type strontium ruthenium oxide | Preparation and characterization of BaCe0.95Tb0.05O3−α hollow fibre membranes for hydrogen permeation

## Ba-Co-O-Yb
- rank 639 | 10 samples | 2 papers | 3 compositions
- compositions: YbBaCo4O7 (6); YbBaCo4O8 (3); BaYbCo4O7 (1)
- seed hypothesis (confirm): swedenborgite
- measured range: 56-855 K (5th-95th pct of 12 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): BaYbCo4O7 P31c (159) mp-25738 [hull=0.029, icsd=3, PRIMARY]; BaYbCo4O7 Cc (9) mp-1182402 [hull=0.007, icsd=1]; BaYbCo4O7 P1 (1) mp-1182211 [hull=0.007]; BaYbCo4O7 P6_3mc (186) mp-1182188 [hull=0.038]
- papers: Structural and thermoelectric properties of BaRCo4O7 (R = Dy, Ho, Er, Tm, Yb, and Lu) | Spin, charge, and lattice coupling in triangular and Kagomé sublattices ofCoO4tetrahedra:YbBaCo4O7+δ(δ=0,1)

## Ba-Cu-Ir-La-O
- rank 640 | 10 samples | 1 papers | 5 compositions
- compositions: Ba0.6La1.4CuIrO6 (2); Ba0.8La1.2CuIrO6 (2); BaLaCuIrO6 (2); Ba0.5La1.5CuIrO6 (2); Ba0.7La1.3CuIrO6 (2)
- measured range: 320-775 K (5th-95th pct of 10 curves)
- papers: Iridium valence variation and carrier sign tuning in \n(Ca,Ba)xLa2−xCuIrO6\n double perovskites

## Ba-Ga-Ge-Sn
- rank 641 | 10 samples | 2 papers | 6 compositions
- compositions: Ba8Ga16.4Sn25.0Ge4.6 (2); Ba8Ga16.9Sn19.8Ge9.3 (2); Ba8Ga17.2Sn24.2Ge4.6 (2); Ba8Ga18.1Sn23.3Ge4.6 (2); Ba8Ga16.1Sn25.1Ge4.8 (1); Ba7.8Ga19Sn21Ge8 (1)
- seed hypothesis (confirm): clathrate_i
- solid-solution axis: Ge/(Ge+Sn) spans 0.16-0.32 (median 0.16) over 6 compositions
     ISOELECTRONIC SERIES: the parent compound depends on the composition, not on this host. Near either end the minor element is a dilute substituent; in the middle it is a genuine alloy. Record the axis, not one parent -- and note the 5% split used the whole formula, not the sublattice, so its cut lands at a different level on each site.
- measured range: 98-720 K (5th-95th pct of 28 curves)
- papers: Effect of Ge substitution on carrier mobilities and thermoelectric properties of sintered p-type Ba8Ga16+xSn30−x−yGeywith the type-VIII clathrate structure | Power generation characteristics of thermoelectric conversion module using type-II (K,Ba)24(Ga,Sn)136 and type-VIII Ba8Ga16(Sn,Ge)30 clathrates

## Ba-Mn-O
- rank 642 | 10 samples | 3 papers | 5 compositions
- compositions: Ba0.98La0.02MnO3 (5); Ba3Mn2O8 (2); (La0.67Ba0.33MnO3)0.17(BaMnO3)0.83 (1); (La0.67Ba0.33MnO3)0.2(BaMnO3)0.8 (1); (La0.67Ba0.33MnO3)0.35(BaMnO3)0.65 (1)
- dopant candidates (<5% at.): La (8)
- measured range: 10-1173 K (5th-95th pct of 10 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): BaMnO3 P6_3/mmc (194) mp-19156 [hull=0.008, icsd=5, PRIMARY]; Ba5Mn3ClO12 P6_3/m (176) mp-650764 [hull=0.000, icsd=3, PRIMARY]; Ba4Mn3O10 Cmce (64) mp-18791 [hull=0.000, icsd=3, PRIMARY]; BaMnO2 Pnma (62) mp-1199857 [hull=0.034, icsd=3, PRIMARY]; Ba5Mn3O12F P6_3/m (176) mp-1214575 [hull=0.000, icsd=2, PRIMARY]
- papers: Low-temperature heat transport in the layered spin-dimer compound Ba3Mn2O8 | Electrical transport and percolation in structural phase-separated manganites La1−xBaxMnO3 | The effect of alkaline earth metal substitution on thermoelectric properties of A0.98La0.02MnO3-δ (A=Ca,Ba)

## Ba-Nb-O-Sr
- rank 643 | 10 samples | 4 papers | 4 compositions
- compositions: Sr0.5Ba0.5Nb2O6 (7); BaSrNb4O12 (1); BaSrNb4O12(TiC)0.05 (1); Ba3Sr3Nb10O30 (1)
- dopant candidates (<5% at.): Ti (1), C (1)
- seed hypothesis (confirm): tungsten_bronze
- measured range: 300-1069 K (5th-95th pct of 25 curves; full span incl. outliers 10-1072 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ba3SrNb2O9 P-3m1 (164) mp-1103862 [hull=0.021, icsd=1, PRIMARY]; Ba2Sr3Nb10O30 P1 (1) mp-1228768 [hull=0.036, PRIMARY]; Ba2Sr3Nb10O30 P2 (3) mp-1228700 [hull=0.043]
- papers: Semiconducting large bandgap oxides as potential thermoelectric materials for high-temperature power generation? | Thermoelectric Properties of Reduced Polycrystalline Sr0.5Ba0.5Nb2O6Fabricated Via Solution Combustion Synthesis | Thermal conductivity and thermoelectric performance of SrxBa1−xNb2O6 ceramics at high temperatures

## Be-O
- rank 644 | 10 samples | 4 papers | 1 compositions
- compositions: BeO (10)
- measured range: 10-1499 K (5th-95th pct of 10 curves; full span incl. outliers 10-2000 K)
- [ref 1] TEDesignLab / ICSD: BeO P6_3mc (186) mp-2542 [hull=0.000, icsd=32, PRIMARY]
- [ref 2] MP, ranked by ICSD evidence: BeO2 P2_12_12_1 (19) mp-1182269 [hull=0.508, PRIMARY]; BeO Fm-3m (225) mp-1794 [hull=0.482, icsd=7]; BeO F-43m (216) mp-1778 [hull=0.007, icsd=6]; BeO P4_2/mnm (136) mp-7599 [hull=0.012, icsd=2]; BeO2 P2_1 (4) mp-1214291 [hull=0.622]
- papers: Nonmetallic crystals with high thermal conductivity | Steady-state thermal conductivity measurements of AlN and SiC substrate materials | Anharmonic interactions in beryllium oxide

## Bi-Ca-Mn-O
- rank 645 | 10 samples | 4 papers | 7 compositions
- compositions: Bi0.3Ca0.7MnO3 (3); Bi0.25Ca0.75MnO3 (2); Ca0.98Bi0.92MnO3 (1); Ca1.6Bi0.4MnO4 (1); Ca0.95Bi0.95MnO3 (1); Bi0.25Gd0.05Ca0.7MnO3 (1)
- dopant candidates (<5% at.): Gd (2)
- measured range: 45-1152 K (5th-95th pct of 17 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ca3Mn4BiO12 Pm (6) mp-1227724 [hull=0.029, PRIMARY]
- papers: Thermoelectric properties of n-type Ca1-xBixMnO3-δ (0.00, 0.02, and 0.05) system | Structure and High-Temperature Thermoelectric Properties of the n-Type Layered Oxide Ca2−x Bi x−δ MnO4−γ | Transport properties of manganese perovskites Bi1−xCaxMnO3(0.7 ⩽x⩽ 0.95)

## Bi-Ce-Pt
- rank 646 | 10 samples | 5 papers | 3 compositions
- compositions: Ce3Bi4Pt3 (8); CeBiPt (1); (Ce0.9La0.1)3Bi4Pt3 (1)
- dopant candidates (<5% at.): La (1)
- measured range: 10-302 K (5th-95th pct of 13 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ce3Bi4Pt3 I-43d (220) mp-1105392 [hull=0.000, icsd=1, PRIMARY]; CeBiPt F-43m (216) mp-1018162 [hull=0.000, icsd=1, PRIMARY]
- papers: Thermoelectric and transport properties of CeBiPt and LaBiPt | Substitutional effects on the electronic transport of the Kondo semiconductorCe3Bi4Pt3 | Low-temperature conducting state in two candidate topological Kondo insulators:SmB6andCe3Bi4Pt3

## Bi-Pb-Se
- rank 647 | 10 samples | 5 papers | 8 compositions
- compositions: Pb5Bi6Se14 (3); Pb7Bi4Se13 (1); K1.25Pb3.5Bi7.25Se15 (1); Pb5Bi12Se23 (1); Pb5Bi18Se32 (1); Pb5Bi6Se13.975I0.025 (1)
- dopant candidates (<5% at.): I (2), K (1)
- seed hypothesis (confirm): bi_chalcogenide_complex
- measured range: 11-763 K (5th-95th pct of 42 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Bi4Pb7Se13 C2/m (12) mp-1190436 [hull=0.012, icsd=2, PRIMARY]; Bi2PbSe4 R-3m (166) mp-675543 [hull=0.001, PRIMARY]
- papers: Pb7Bi4Se13: A Lillianite Homologue with Promising Thermoelectric Properties | Low lattice thermal conductivity in Pb5Bi6Se14, Pb3Bi2S6, and PbBi2S4: promising thermoelectric materials in the cannizzarite, lillianite, and galenobismuthite homologous series | Modular Construction of A1+xM4-2xM‘7+xSe15(A = K, Rb; M = Pb, Sn; M‘ = Bi, Sb):  A New Class of Solid State Quaternary Thermoelectric Compounds

## C-H-S
- rank 648 | 10 samples | 4 papers | 6 compositions
- compositions: C4H2S (3); (CH3Cl)7.69(C)86.18(C2S4Ni)6.13 (2); C5H4S (2); C36H32Cl4GaS24 (1); C36H32AuBr2S24 (1); C6H2S2 (1)
- dopant candidates (<5% at.): Cl (3), Ni (2), Ga (1), Br (1), Au (1)
- measured range: 10-340 K (5th-95th pct of 34 curves; full span incl. outliers 10-381 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): CuH12C5S4N P-42_1c (114) mp-698375 [hull=0.108, icsd=1, PRIMARY]; H2CS3 P2_1/c (14) mp-709098 [hull=0.174, icsd=1, PRIMARY]; AgH12C4S5N Cc (9) mp-698405 [hull=0.081, icsd=1, PRIMARY]; H10PbC6S2IN P-1 (2) mp-1194627 [hull=0.109, icsd=1, PRIMARY]; FeH21C7S3N P2_1/c (14) mp-1201806 [hull=0.131, icsd=1, PRIMARY]
- papers: Novel Hybrid Organic Thermoelectric Materials:Three-Component Hybrid Films Consisting of a Nanoparticle Polymer Complex, Carbon Nanotubes, and Vinyl Polymer | Dimerization Effect on the Physical Properties in New One-Dimensional Organic Conductors: (ChTM-TTP)2AuBr2, (ChTM-TTP)2GaCl4, and (ChTM-TTP)ReO4 | Thermoelectric Performances of Free-Standing Polythiophene and Poly(3-Methylthiophene) Nanofilms

## Ca-Co-H-O
- rank 649 | 10 samples | 5 papers | 5 compositions
- compositions: (Ca0.85OH)1.16CoO2 (4); (CaOH)1.14CoO2 (3); (Ca0.85OH) 1.16CoO2 (1); (Ca0.8Nd0.05OH) 1.16CoO2 (1); (Ca0.75Nd0.1OH) 1.16CoO2 (1)
- dopant candidates (<5% at.): Nd (2)
- seed hypothesis (confirm): misfit_cobaltite
- measured range: 11-574 K (5th-95th pct of 21 curves)
- papers: Hydrothermal synthesis, characterization, electronic structure, and thermoelectric properties of (Ca0.85OH)1.16CoO2 | Hydrothermal Synthesis and Thermoelectric Properties of New Oxides (Ca<SUB>0.85-<I>x</I></SUB>Nd<SUB><I>x</I></SUB>OH) <SUB>1.16</SUB>CoO<SUB>2</SUB> | Monoclinic phase of the misfit-layered cobalt oxide (Ca0.85OH)1.16CoO2

## Ca-Co-O-Pr
- rank 650 | 10 samples | 4 papers | 6 compositions
- compositions: (Pr0.875Y0.125)0.7Ca0.3CoO3 (3); Pr0.7Ca0.3CoO3 (2); Pr0.5Ca0.5CoO3 (2); (Pr0.8Sm0.2)0.7Ca0.3CoO3 (1); (Pr0.9375Y0.0625)0.7Ca0.3CoO3 (1); (Pr0.825Y0.125)0.7Ca0.3CoO3 (1)
- dopant candidates (<5% at.): Y (5), Sm (1)
- measured range: 10-326 K (5th-95th pct of 10 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): CaPr3(CoO3)4 Pm (6) mp-1227199 [hull=0.011, PRIMARY]; CaPrCoO4 I4mm (107) mp-1227079 [hull=0.042, PRIMARY]
- papers: Transport and Magnetic Properties of R1-xAxCoO3(R = La, Pr and Nd; A = Ba, Sr and Ca) | Thermal conductivity of (Pr1-xREx0.7Ca0.3CoO3(RE=Sm, Gd) around metal-insulator - spin-state transition | Suppression of the metal-insulator transition by magnetic field in (Pr<sub>1−</sub><sub><i>y</i></sub>Y<sub><i>y</i></sub>)<sub>0.7</sub>Ca<sub>0.3</sub>CoO<sub>3</sub> (<i>y</i> = 0.0625)
