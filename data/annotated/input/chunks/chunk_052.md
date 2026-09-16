# Host systems -- chunk 052 of 73

Ranks 2551-2600 by sample count. These 50 host systems cover 50 samples (0.10% of the TE set); cumulative through this chunk: 97.99%.

Assign each host system a structural prototype from `data/annotated/taxonomy/prototypes_seed_v3.json`, or propose a new one in `taxonomy/prototypes_proposed.jsonl` first. Append results to `data/annotated/annotations/family_assignments.jsonl`.

The hand-entered MaterialFamily labels are deliberately NOT shown here -- they are held out in `df_host_systems.parquet` to validate this classification later. Decide from the compositions.

A "seed hypothesis" line means the taxonomy already names this host under that prototype. Confirm it against the compositions rather than accepting it; two or more listed means the host is mixed and needs splitting per composition.

Evidence follows the project precedence. Your judgement about the thermoelectric chemistry decides the prototype. [ref 1] is TEDesignLab, ICSD-backed and thermoelectric-specific -- prefer it. [ref 2] is Materials Project. Within a formula, polymorphs are ranked by ICSD reference count and the top one is marked PRIMARY -- not by e_above_hull, which is unusable for layered chalcogenides in the 2019 dump (Sb2Te3 R-3m carries 26 ICSD refs at hull 1.02). A primary resting on fewer than 5 ICSD references is flagged weak; the ambient phase may simply be absent from the snapshot, as it is for Bi2Se3.

While you have the host in view, also record what each minor element DOES, in `dopant_roles` -- the role follows from the prototype and cannot be judged without it. A median host has 2 such elements. Not everything listed is a dopant: O, C, N and H are usually milling or pressing residue, and an element just under 5 at.% may be an alloying end member rather than dilute doping. The doping LEVEL is computed later from the parsed fractions -- do not work it out by hand here.

A polymorph list is NOT a thermal sequence. SnSe has three known structures but only Pnma -> Cmcm happens on heating; rocksalt SnSe is metastable (2 icsd refs against 32). Put thermally reached phases in `phases` with their transition temperatures, and everything else in `other_polymorphs` with an occurrence reason. hull and icsd counts are shown to help you tell them apart.

A host may need MORE THAN ONE prototype. Transport is measured across a wide window and many thermoelectrics transform inside it, so where a "MEASUREMENT CROSSES A TRANSITION" line appears, record each phase with its own temperature range in the `phases` field. Transition temperatures shown are approximate and composition-dependent.

Both references describe which phases EXIST in a chemistry, not which phase this paper made. Al-O-Zn is best attested as ZnAl2O4 spinel (227) while almost every sample in it is Al-doped wurtzite ZnO (186). Weigh them against the compositions; do not follow them blindly.

## As-Zn
- rank 2551 | 1 samples | 1 papers | 1 compositions
- compositions: ZnAs (1)
- measured range: 11-394 K (5th-95th pct of 3 curves)
- [ref 1] TEDesignLab / ICSD: ZnAs Pbca (61) mp-7372 [hull=0.019, icsd=3, PRIMARY]
- [ref 2] MP, ranked by ICSD evidence: Zn3As2 P4_2/nmc (137) mp-15700 [hull=0.001, icsd=2, PRIMARY, AMBIGUOUS]; ZnAs2 P2_1/c (14) mp-7262 [hull=0.000, icsd=2, PRIMARY]; Zn2As Pn-3m (224) mp-1207458 [hull=0.389, PRIMARY]; ZnAs3 Fm-3m (225) mp-971701 [hull=0.483, PRIMARY]; Zn3As2 I4_1cd (110) mp-1203368 [hull=0.004, icsd=2]
- papers: https://doi.org/10.1021/ic501308q (Synthesis, Structure, and Properties of the Electron-Poor II–V Semicon...)

## As-Zr
- rank 2552 | 1 samples | 1 papers | 1 compositions
- compositions: ZrAs (1)
- measured range: 15-304 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): ZrAs P6_3/mmc (194) mp-1682 [hull=0.000, icsd=2, PRIMARY]; ZrAs2 Pnma (62) mp-27606 [hull=0.000, icsd=2, PRIMARY]; Zr14As9 Pnnm (58) mp-1203256 [hull=0.000, icsd=1, PRIMARY]; Zr3As2 Pnma (62) mp-972228 [hull=0.000, icsd=1, PRIMARY]; Zr3As P4_2/n (86) mp-1200894 [hull=0.000, icsd=1, PRIMARY]
- papers: https://doi.org/10.1088/0953-2048/25/8/084016 (Properties of binary transition-metal arsenides (TAs))

## Au-Cd-Eu-Sb
- rank 2553 | 1 samples | 1 papers | 1 compositions
- compositions: Eu9Cd3.82Au1.24Sb9 (1)
- measured range: 301-770 K (5th-95th pct of 4 curves)
- papers: https://doi.org/10.1021/acs.chemmater.5b03808 (Coinage-Metal-Stuffed Eu9Cd4Sb9: Metallic Compounds with Anomalous Low...)

## Au-Cr-Te
- rank 2554 | 1 samples | 1 papers | 1 compositions
- compositions: CrAuTe4 (1)
- measured range: 13-300 K (5th-95th pct of 6 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): CrTe4Au P2/m (10) mp-12743 [hull=0.000, icsd=1, PRIMARY]
- papers: https://doi.org/10.1016/j.jssc.2004.04.029 (Thermoelectric properties and antiferromagnetism of the new ternary tr...)

## Au-Cu-Lu
- rank 2555 | 1 samples | 1 papers | 1 compositions
- compositions: LuCu4Au (1)
- measured range: 13-279 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Lu2CuAu Fm-3m (225) mp-1185452 [hull=0.009, PRIMARY]
- papers: https://doi.org/10.1007/bf02570277 (Low temperature hall effect and thermopower of YbCu4Au and YbCu4Pd)

## Au-Cu-Pr
- rank 2556 | 1 samples | 1 papers | 1 compositions
- compositions: PrCu2Au3 (1)
- measured range: 11-300 K (5th-95th pct of 3 curves)
- papers: https://doi.org/10.1016/j.jallcom.2020.156015 (Crystal electric field effects and heavy-fermion behavior in cubic PrC...)

## Au-Gd-Ge
- rank 2557 | 1 samples | 1 papers | 1 compositions
- compositions: Gd14.34Au67.16Ge18.5 (1)
- measured range: 10-391 K (5th-95th pct of 4 curves)
- papers: https://doi.org/10.1088/0953-8984/25/13/135402 (Syntheses optimization, structural and thermoelectric properties of 1/...)

## Au-Gd-Si
- rank 2558 | 1 samples | 1 papers | 1 compositions
- compositions: Gd14.4Au69.9Si15.7 (1)
- measured range: 11-390 K (5th-95th pct of 4 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Gd(SiAu)2 I4/mmm (139) mp-22615 [hull=0.000, icsd=3, PRIMARY]
- papers: https://doi.org/10.1088/0953-8984/25/13/135402 (Syntheses optimization, structural and thermoelectric properties of 1/...)

## Au-Ge-Si
- rank 2559 | 1 samples | 1 papers | 1 compositions
- compositions: Si0.5Ge0.5Au0.07 (1)
- measured range: 326-703 K (5th-95th pct of 1 curves)
- papers: https://doi.org/10.1143/jjap.50.041301 (Nano Structural and Thermoelectric Properties of SiGeAu Thin Films)

## Au-Ge-Yb
- rank 2560 | 1 samples | 1 papers | 1 compositions
- compositions: Yb15.78Au65.22Ge19 (1)
- measured range: 10-391 K (5th-95th pct of 4 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Yb2GeAu Fm-3m (225) mp-1187891 [hull=0.000, PRIMARY]; Yb4Ge3Au5 Cm (8) mp-1215781 [hull=0.004, PRIMARY]; YbGeAu P-6m2 (187) mp-1215498 [hull=0.042, PRIMARY]; YbGeAu C2/m (12) mp-1215621 [hull=0.058]
- papers: https://doi.org/10.1088/0953-8984/25/13/135402 (Syntheses optimization, structural and thermoelectric properties of 1/...)

## Au-In-Yb
- rank 2561 | 1 samples | 1 papers | 1 compositions
- compositions: YbInAu2 (1)
- measured range: 10-295 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Yb(In2Au)2 P2_1/m (11) mp-1104570 [hull=0.090, icsd=1, PRIMARY]; Yb2In5Au3 Cmc2_1 (36) mp-1188123 [hull=0.000, icsd=1, PRIMARY]; YbIn2Au Cmcm (63) mp-20746 [hull=0.000, icsd=1, PRIMARY]
- papers: https://doi.org/10.1023/a:1021801903961 (Thermopower of Yb Heavy Fermion Compounds at High Pressure)

## Au-Sb-Tl
- rank 2562 | 1 samples | 1 papers | 1 compositions
- compositions: AuTlSb (1)
- measured range: 79-300 K (5th-95th pct of 2 curves)
- papers: https://doi.org/10.1016/j.jallcom.2006.01.020 (Crystal structure, electronic structure, and thermoelectric properties...)

## Au-Se-Sn-Tl
- rank 2563 | 1 samples | 1 papers | 1 compositions
- compositions: Tl2Au4Sn2Se6 (1)
- measured range: 81-301 K (5th-95th pct of 1 curves)
- papers: https://doi.org/10.1021/cm050412c (Exploring Thallium Compounds as Thermoelectric Materials:  Seventeen N...)

## Au-Te
- rank 2564 | 1 samples | 1 papers | 1 compositions
- compositions: AuTe2 (1)
- measured range: 319-609 K (5th-95th pct of 5 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Te2Au P-3m1 (164) mp-1662 [hull=0.011, icsd=22, PRIMARY]; Te3Au2 P1 (1) mp-645449 [hull=0.030, icsd=1, PRIMARY]; Te3Au P4/mmm (123) mp-1217358 [hull=0.064, PRIMARY]; Te2Au Pma2 (28) mp-20123 [hull=0.000, icsd=2]
- papers: https://doi.org/10.1016/j.jallcom.2010.02.030 (Thermoelectric properties of gold telluride: AuTe2)

## B-Ba-Ca
- rank 2565 | 1 samples | 1 papers | 1 compositions
- compositions: Ca0.5Ba0.5B6 (1)
- measured range: 325-1040 K (5th-95th pct of 2 curves)
- papers: https://doi.org/10.1016/j.jssc.2014.10.001 (High-pressure densified solid solutions of alkaline earth hexaborides ...)

## B-Ba-Ni-S-Sn
- rank 2566 | 1 samples | 1 papers | 1 compositions
- compositions: Ba0.92Ni4SB6.7Sn5.3 (1)
- measured range: 10-294 K (5th-95th pct of 2 curves; full span incl. outliers 10-723 K)
- papers: https://doi.org/10.1039/c6dt01298a (Ba-filled Ni–Sb–Sn based skutterudites with anomalously high lattice t...)

## B-Ba-Sr
- rank 2567 | 1 samples | 1 papers | 1 compositions
- compositions: Sr0.5Ba0.5B6 (1)
- measured range: 325-1040 K (5th-95th pct of 2 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ba2SrB18 P4/mmm (123) mp-1228370 [hull=0.003, PRIMARY]
- papers: https://doi.org/10.1016/j.jssc.2014.10.001 (High-pressure densified solid solutions of alkaline earth hexaborides ...)

## B-C-Cr-Fe
- rank 2568 | 1 samples | 1 papers | 1 compositions
- compositions: (Fe)41.59(Cr)17.52(Mo)2.37(W)2.48(C)7.58(Mn)4.15(Si)3.24(B)21.06 (1)
- dopant candidates (<5% at.): Mn (1), Si (1), W (1), Mo (1)
- measured range: 573-873 K (5th-95th pct of 1 curves)
- papers: https://doi.org/10.1007/s11666-017-0681-z (Intermetallic Al-, Fe-, Co- and Ni-Based Thermal Barrier Coatings Prep...)

## B-C-Cu
- rank 2569 | 1 samples | 1 papers | 1 compositions
- compositions: (B4C)40.48(Cu)59.52 (1)
- measured range: 293-871 K (5th-95th pct of 1 curves)
- papers: https://doi.org/10.1080/18811248.1999.9726221 (Fabrication and Thermal Conductivity of Boron Carbide/Copper Cermet)

## B-C-Fe-Ni-Si
- rank 2570 | 1 samples | 1 papers | 1 compositions
- compositions: Fe37.5Ni37.5C5Mo2Si10B8 (1)
- dopant candidates (<5% at.): Mo (1)
- measured range: 42-579 K (5th-95th pct of 1 curves)
- papers: https://doi.org/10.1016/0304-8853(86)90575-5 (Thermopower of amorphous Fe-Ni-Cr-Mo-Si-B in the temperature range 40–...)

## B-C-Hf-Si
- rank 2571 | 1 samples | 1 papers | 1 compositions
- compositions: (La2O3)0.012(SiC)0.5HfB2 (1)
- dopant candidates (<5% at.): O (1), La (1)
- measured range: 295-2173 K (5th-95th pct of 1 curves)
- papers: https://doi.org/10.1016/j.jeurceramsoc.2013.06.009 (Thermal properties of La2O3-doped ZrB2- and HfB2-based ultra-high temp...)

## B-C-Ho-Ni
- rank 2572 | 1 samples | 1 papers | 1 compositions
- compositions: HoNi2B2C (1)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): HoNi2B2C I4/mmm (139) mp-6646 [hull=0.000, icsd=6, PRIMARY]
- papers: https://doi.org/10.1103/physrevb.54.3062 (Thermal conductivity ofRNi2B2C (R=Y,Ho) single crystals)

## B-C-N
- rank 2573 | 1 samples | 1 papers | 1 compositions
- compositions: Y0.74B21.5C2.12N1.5 (1)
- dopant candidates (<5% at.): Y (1)
- measured range: 324-961 K (5th-95th pct of 2 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): BC2N Pmm2 (25) mp-629458 [hull=0.537, icsd=2, PRIMARY, AMBIGUOUS]; B2CN Pmma (51) mp-1079333 [hull=0.224, icsd=1, PRIMARY]; B3C10N3 Pmma (51) mp-642462 [hull=0.583, icsd=1, PRIMARY]; B2(CN2)3 R-3c (167) mp-989472 [hull=0.171, PRIMARY, AMBIGUOUS]; B2CN2 R3m (160) mp-1228638 [hull=0.461, PRIMARY]
- papers: https://doi.org/10.1016/j.jpcs.2013.03.007 (Structural and thermoelectric properties of Y1−xB22+yC2−yN)

## B-C-N-O
- rank 2574 | 1 samples | 1 papers | 1 compositions
- compositions: C82.3B6.11N5.52O6 (1)
- measured range: 327-562 K (5th-95th pct of 2 curves)
- papers: https://doi.org/10.1016/j.carbon.2016.07.054 (C/BCN core/shell nanotube films with improved thermoelectric properties)

## B-Ce-La
- rank 2575 | 1 samples | 1 papers | 1 compositions
- compositions: Ce0.5La0.5B6 (1)
- measured range: 10-96 K (5th-95th pct of 2 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): La(CeB8)3 Pmmm (47) mp-1223276 [hull=0.002, PRIMARY, AMBIGUOUS]; LaCeB12 Fm-3m (225) mp-1222899 [hull=0.001, PRIMARY, AMBIGUOUS]; La(CeB8)3 P4/mmm (123) mp-1223281 [hull=0.003]; LaCeB12 P4/mmm (123) mp-1222912 [hull=0.003]
- papers: https://doi.org/10.1016/0304-8853(92)91396-b (Thermoelectric power in Ce1−xLaxB6 Kondo systems)

## B-Ce-N-Ni
- rank 2576 | 1 samples | 1 papers | 1 compositions
- compositions: Ce3Ni2B2N3 (1)
- measured range: 15-291 K (5th-95th pct of 2 curves; full span incl. outliers 15-765 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ce3Ni2B2N3 I4/mmm (139) mp-21136 [hull=0.000, icsd=1, PRIMARY]
- papers: https://doi.org/10.1103/physrevb.83.115131 (Anderson lattice in the intermediate valence compound Ce3Ni2B2N3−δ)

## B-Ce-Ni
- rank 2577 | 1 samples | 1 papers | 1 compositions
- compositions: Ce2NiB9.7 (1)
- measured range: 11-298 K (5th-95th pct of 3 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ce(Ni2B)6 Cmc2_1 (36) mp-21695 [hull=0.000, icsd=2, PRIMARY]; Ce2Ni5B4 C2/m (12) mp-1095458 [hull=0.027, icsd=1, PRIMARY]; Ce2NiB10 Pbam (55) mp-21169 [hull=0.000, icsd=1, PRIMARY]; Ce3Ni13B2 P6/mmm (191) mp-1106339 [hull=0.000, icsd=1, PRIMARY]; CeNi4B P6/mmm (191) mp-1095459 [hull=0.000, icsd=1, PRIMARY]
- papers: https://doi.org/10.1143/jpsj.72.2344 (Magnetic and Thermoelectric Properties of Ce2NiB10-δ(\\(\\delta\\cong ...)

## B-Ce-Re
- rank 2578 | 1 samples | 1 papers | 1 compositions
- compositions: CeReB4 (1)
- measured range: 10-336 K (5th-95th pct of 3 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ce2(ReB2)3 C2/c (15) mp-1190580 [hull=0.000, icsd=1, PRIMARY]; Ce8Re13B12 R-3m (166) mp-1202101 [hull=0.000, icsd=1, PRIMARY]; CeReB4 Pbam (55) mp-22361 [hull=0.000, icsd=1, PRIMARY]
- papers: https://doi.org/10.1002/ejic.201501038 (Crystal Structure, Magnetic, Electronic, and Thermal Transport Propert...)

## B-Co-Cr
- rank 2579 | 1 samples | 1 papers | 1 compositions
- compositions: Co37.5Cr7.5B25 (1)
- measured range: 79-400 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): CrCoB Fmmm (69) mp-1226217 [hull=0.084, PRIMARY]
- papers: https://doi.org/10.1016/0022-3093(90)90955-l (Thermoelectric power of amorphous Co100−xBx alloys)

## B-Co-Cr-Fe
- rank 2580 | 1 samples | 1 papers | 1 compositions
- compositions: Fe74Co5Cr5B16 (1)
- measured range: 312-579 K (5th-95th pct of 2 curves)
- papers: https://doi.org/10.1007/bf01794613 (Electrical resistivity and thermoelectric power of Fe74Co10−x Cr x B16...)

## B-Co-Mn
- rank 2581 | 1 samples | 1 papers | 1 compositions
- compositions: Co67.5Mn7.5B25 (1)
- measured range: 80-397 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Mn2(Co7B2)3 Fm-3m (225) mp-1194187 [hull=0.046, icsd=1, PRIMARY]; Mn3(Co10B3)2 Fm-3m (225) mp-1193450 [hull=0.068, icsd=1, PRIMARY]; MnCoB Fmmm (69) mp-1221661 [hull=0.030, PRIMARY]; MnCoB2 Pmc2_1 (26) mp-1221680 [hull=0.082, PRIMARY]
- papers: https://doi.org/10.1016/0022-3093(90)90955-l (Thermoelectric power of amorphous Co100−xBx alloys)

## B-Co-N-O
- rank 2582 | 1 samples | 1 papers | 1 compositions
- compositions: N0.7Co0.5B0.5O2 (1)
- measured range: 15-300 K (5th-95th pct of 4 curves)
- papers: https://doi.org/10.1007/s00339-015-9089-0 (Magnetic and thermoelectric properties of B-substituted NaCoO2)

## B-Co-Ru-Ti
- rank 2583 | 1 samples | 1 papers | 1 compositions
- compositions: Ti9Co2Ru18B8 (1)
- measured range: 301-974 K (5th-95th pct of 5 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ti9Co2(B4Ru9)2 P4/mbm (127) mp-1200174 [hull=0.033, icsd=1, PRIMARY]
- papers: https://doi.org/10.1007/s11664-014-3423-8 (Thermoelectric Properties of Pseudogap Ti10Ru19B8 \tand Ti9TM2Ru18B8 (...)

## B-Co-Si
- rank 2584 | 1 samples | 1 papers | 1 compositions
- compositions: CoSi0.9B0.1 (1)
- measured range: 80-299 K (5th-95th pct of 2 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Co19(Si2B)4 C2 (5) mp-1226660 [hull=0.028, PRIMARY]
- papers: https://doi.org/10.1063/1.3671066 (The role of boron segregation in enhanced thermoelectric power factor ...)

## B-Cr-Gd
- rank 2585 | 1 samples | 1 papers | 1 compositions
- compositions: GdCrB4 (1)
- measured range: 310-1057 K (5th-95th pct of 1 curves)
- papers: https://doi.org/10.1016/j.jallcom.2010.05.110 (Applying an electron counting rule to screen prospective thermoelectri...)

## B-Cr-Ho
- rank 2586 | 1 samples | 1 papers | 1 compositions
- compositions: HoCrB4 (1)
- measured range: 323-986 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): HoCrB4 Pbam (55) mp-1191543 [hull=0.000, icsd=2, PRIMARY]; Ho3CrB7 Cmcm (63) mp-31046 [hull=0.000, icsd=1, PRIMARY]
- papers: https://doi.org/10.1016/j.jallcom.2010.05.110 (Applying an electron counting rule to screen prospective thermoelectri...)

## B-Cr-Ni-Si
- rank 2587 | 1 samples | 1 papers | 1 compositions
- compositions: (Fe)2.65(Cr)6.65(Si)7.21(B)13.71(Ni)69.78 (1)
- dopant candidates (<5% at.): Fe (1)
- measured range: 573-873 K (5th-95th pct of 1 curves)
- papers: https://doi.org/10.1007/s11666-017-0681-z (Intermetallic Al-, Fe-, Co- and Ni-Based Thermal Barrier Coatings Prep...)

## B-Cr-Ru-Ti
- rank 2588 | 1 samples | 1 papers | 1 compositions
- compositions: Ti9Cr2Ru18B8 (1)
- measured range: 298-975 K (5th-95th pct of 5 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ti8Cr3(B4Ru9)2 Cmmm (65) mp-1217552 [hull=0.006, PRIMARY]
- papers: https://doi.org/10.1007/s11664-014-3423-8 (Thermoelectric Properties of Pseudogap Ti10Ru19B8 \tand Ti9TM2Ru18B8 (...)

## B-Cu-O-Sr
- rank 2589 | 1 samples | 1 papers | 1 compositions
- compositions: SrCu2(BO3)2 (1)
- measured range: 14-275 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): SrCu2(BO3)2 I-42m (121) mp-6602 [hull=0.051, icsd=10, PRIMARY]; Sr2Cu(BO3)2 P2_1/c (14) mp-9660 [hull=0.016, icsd=1, PRIMARY]; BaSr3Cu8(BO3)8 P222 (16) mp-1228284 [hull=0.054, PRIMARY]; SrCu2(BO3)2 I4cm (108) mp-1191148 [hull=0.052, icsd=1]
- papers: https://doi.org/10.1103/physrevlett.87.047202 (Strong Damping of Phononic Heat Current by Magnetic Excitations inSrCu...)

## B-Cu-Ru-Ti
- rank 2590 | 1 samples | 1 papers | 1 compositions
- compositions: Ti9Cu2Ru18B8 (1)
- measured range: 300-974 K (5th-95th pct of 5 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ti9Cu2(B4Ru9)2 P4/mbm (127) mp-1201135 [hull=0.033, icsd=1, PRIMARY]
- papers: https://doi.org/10.1007/s11664-014-3423-8 (Thermoelectric Properties of Pseudogap Ti10Ru19B8 \tand Ti9TM2Ru18B8 (...)

## B-F-H-P
- rank 2591 | 1 samples | 1 papers | 1 compositions
- compositions: (BTBT)2PF6 (1)
- measured range: 100-300 K (5th-95th pct of 4 curves)
- papers: https://doi.org/10.1016/j.synthmet.2019.116217 (Low-temperature properties of thermoelectric generators using molecula...)

## B-Fe-Ni-S
- rank 2592 | 1 samples | 1 papers | 1 compositions
- compositions: Pr0.42Fe3NiSB12 (1)
- dopant candidates (<5% at.): Pr (1)
- measured range: 14-684 K (5th-95th pct of 1 curves)
- papers: https://doi.org/10.1109/ict.2003.1287456 (Ground state properties and thermoelectric behavior of PrFe/sub 4-x/TM...)

## B-Fe-Ru-Ti
- rank 2593 | 1 samples | 1 papers | 1 compositions
- compositions: Ti9Fe2Ru18B8 (1)
- measured range: 302-974 K (5th-95th pct of 5 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ti9Fe2(B4Ru9)2 P4/mbm (127) mp-684003 [hull=0.010, icsd=1, PRIMARY]
- papers: https://doi.org/10.1007/s11664-014-3423-8 (Thermoelectric Properties of Pseudogap Ti10Ru19B8 \tand Ti9TM2Ru18B8 (...)

## B-Fe-S
- rank 2594 | 1 samples | 1 papers | 1 compositions
- compositions: Ce0.32Yb0.36Fe3.32Ni0.68SB12 (1)
- dopant candidates (<5% at.): Ni (1), Yb (1), Ce (1)
- measured range: 116-295 K (5th-95th pct of 1 curves)
- papers: https://doi.org/10.1109/ict.2003.1287450 (Thermoelectric properties of the new skutterudites (Ce-Yb)/sub y/Fe/su...)

## B-Fe-Sb
- rank 2595 | 1 samples | 1 papers | 1 compositions
- compositions: FeBSb (1)
- measured range: 298-799 K (5th-95th pct of 5 curves)
- papers: https://doi.org/10.1016/j.jallcom.2021.161308 (Mechanical and thermoelectric properties of FeVSb-based half-Heusler a...)

## B-Gd
- rank 2596 | 1 samples | 1 papers | 1 compositions
- compositions: GdB6 (1)
- measured range: 11-99 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): GdB6 Pm-3m (221) mp-22266 [hull=0.000, icsd=9, PRIMARY]; GdB2 P6/mmm (191) mp-425 [hull=0.069, icsd=4, PRIMARY]; Gd2B5 P2_1/c (14) mp-28366 [hull=0.000, icsd=2, PRIMARY]; GdB4 P4/mbm (127) mp-1105563 [hull=0.000, icsd=2, PRIMARY]; GdB12 Fm-3m (225) mp-1006223 [hull=0.004, icsd=1, PRIMARY]
- papers: https://doi.org/10.1103/physrevb.54.r5207 (Thermal conductivity ofRB6(R=Ce,Pr,Nd,Sm,Gd) single crystals)

## B-Ge-Ni-P-Si
- rank 2597 | 1 samples | 1 papers | 1 compositions
- compositions: NiSi2Ge0.6B0.4P4 (1)
- measured range: 11-770 K (5th-95th pct of 7 curves)
- papers: https://doi.org/10.1063/1.4794992 (Thermoelectric properties of polycrystalline NiSi3P4)

## B-Ho-Re
- rank 2598 | 1 samples | 1 papers | 1 compositions
- compositions: HoReB4 (1)
- measured range: 13-348 K (5th-95th pct of 3 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): HoReB4 Pbam (55) mp-975064 [hull=0.000, icsd=2, PRIMARY]; Ho2ReB6 Pbam (55) mp-1204735 [hull=0.000, icsd=1, PRIMARY]; Ho3ReB7 Cmcm (63) mp-973395 [hull=0.000, icsd=1, PRIMARY]
- papers: https://doi.org/10.1002/ejic.201501038 (Crystal Structure, Magnetic, Electronic, and Thermal Transport Propert...)

## B-I
- rank 2599 | 1 samples | 1 papers | 1 compositions
- compositions: BI0.905Sb0.095 (1)
- dopant candidates (<5% at.): Sb (1)
- measured range: 11-303 K (5th-95th pct of 2 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): BI3 P6_3/m (176) mp-23189 [hull=0.000, icsd=3, PRIMARY]; B5I C2/c (15) mp-1182499 [hull=0.653, PRIMARY]
- papers: https://doi.org/10.1016/0022-3697(95)00148-4 (Transport properties of Bi-RICH Bi-Sb alloys)

## B-I-Te
- rank 2600 | 1 samples | 1 papers | 1 compositions
- compositions: BI2Te3 (1)
- measured range: 302-518 K (5th-95th pct of 5 curves)
- papers: https://doi.org/10.1016/j.scriptamat.2012.04.005 (Thermoelectric properties of hydrothermally synthesized Bi2Te3−xSex na...)
