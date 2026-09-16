# Host systems -- chunk 061 of 73

Ranks 3001-3050 by sample count. These 50 host systems cover 50 samples (0.10% of the TE set); cumulative through this chunk: 98.85%.

Assign each host system a structural prototype from `data/annotated/taxonomy/prototypes_seed_v3.json`, or propose a new one in `taxonomy/prototypes_proposed.jsonl` first. Append results to `data/annotated/annotations/family_assignments.jsonl`.

The hand-entered MaterialFamily labels are deliberately NOT shown here -- they are held out in `df_host_systems.parquet` to validate this classification later. Decide from the compositions.

A "seed hypothesis" line means the taxonomy already names this host under that prototype. Confirm it against the compositions rather than accepting it; two or more listed means the host is mixed and needs splitting per composition.

Evidence follows the project precedence. Your judgement about the thermoelectric chemistry decides the prototype. [ref 1] is TEDesignLab, ICSD-backed and thermoelectric-specific -- prefer it. [ref 2] is Materials Project. Within a formula, polymorphs are ranked by ICSD reference count and the top one is marked PRIMARY -- not by e_above_hull, which is unusable for layered chalcogenides in the 2019 dump (Sb2Te3 R-3m carries 26 ICSD refs at hull 1.02). A primary resting on fewer than 5 ICSD references is flagged weak; the ambient phase may simply be absent from the snapshot, as it is for Bi2Se3.

While you have the host in view, also record what each minor element DOES, in `dopant_roles` -- the role follows from the prototype and cannot be judged without it. A median host has 2 such elements. Not everything listed is a dopant: O, C, N and H are usually milling or pressing residue, and an element just under 5 at.% may be an alloying end member rather than dilute doping. The doping LEVEL is computed later from the parsed fractions -- do not work it out by hand here.

A polymorph list is NOT a thermal sequence. SnSe has three known structures but only Pnma -> Cmcm happens on heating; rocksalt SnSe is metastable (2 icsd refs against 32). Put thermally reached phases in `phases` with their transition temperatures, and everything else in `other_polymorphs` with an occurrence reason. hull and icsd counts are shown to help you tell them apart.

A host may need MORE THAN ONE prototype. Transport is measured across a wide window and many thermoelectrics transform inside it, so where a "MEASUREMENT CROSSES A TRANSITION" line appears, record each phase with its own temperature range in the `phases` field. Transition temperatures shown are approximate and composition-dependent.

Both references describe which phases EXIST in a chemistry, not which phase this paper made. Al-O-Zn is best attested as ZnAl2O4 spinel (227) while almost every sample in it is Al-doped wurtzite ZnO (186). Weigh them against the compositions; do not follow them blindly.

## Co-Sb-Si-Ti
- rank 3001 | 1 samples | 1 papers | 1 compositions
- compositions: TiCoSb0.8Si0.2 (1)
- sample form: Bulk (1)
- measured range: 319-870 K (5th-95th pct of 4 curves)
- papers: https://doi.org/10.1007/s11664-019-07486-y (Enhanced Thermoelectric Performance in Hf-Free p-Type (Ti, Zr)CoSb Hal...)

## Co-Sb-Si-Zr
- rank 3002 | 1 samples | 1 papers | 1 compositions
- compositions: ZrCoSb0.8Si0.2 (1)
- sample form: Bulk (1)
- measured range: 320-869 K (5th-95th pct of 4 curves)
- papers: https://doi.org/10.1007/s11664-019-07486-y (Enhanced Thermoelectric Performance in Hf-Free p-Type (Ti, Zr)CoSb Hal...)

## Co-Sb-Sm
- rank 3003 | 1 samples | 1 papers | 1 compositions
- compositions: Sm0.9Co4Sb12 (1)
- sample form: Bulk (1)
- measured range: 299-741 K (5th-95th pct of 4 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): SmCoSb2 P4/nmm (129) mp-1079833 [hull=0.049, icsd=2, PRIMARY]
- papers: https://doi.org/10.1016/j.matlet.2014.12.019 (Structural and thermoelectric characterizations of samarium filled CoS...)

## Co-Sb-Th
- rank 3004 | 1 samples | 1 papers | 1 compositions
- compositions: Th3Co3Sb4 (1)
- sample form: pellets (1)
- measured range: 301-568 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Th3Co3Sb4 I-43d (220) mp-22708 [hull=0.000, PRIMARY]
- papers: https://doi.org/10.1006/jssc.2001.9206 (Th3Co3Sb4: A New Room Temperature Magnet)

## Co-Sb-Ti-V
- rank 3005 | 1 samples | 1 papers | 1 compositions
- compositions: V0.755Ti0.2CoSb (1)
- sample form: Bulk (1)
- measured range: 299-974 K (5th-95th pct of 5 curves)
- papers: https://doi.org/10.1002/andp.201900440 (Titanium Doping to Enhance Thermoelectric Performance of 19‐Electron V...)

## Co-Sb-Yb
- rank 3006 | 1 samples | 1 papers | 1 compositions
- compositions: YbCo4Sb12 (1)
- sample form: Bulk (1)
- measured range: 296-834 K (5th-95th pct of 4 curves)
- papers: https://doi.org/10.1103/physrevb.80.115329 (Solubility study of Yb inn-type skutteruditesYbxCo4Sb12and their enhan...)

## Co-Si-U
- rank 3007 | 1 samples | 1 papers | 1 compositions
- compositions: U2Co3Si5 (1)
- measured range: 11-95 K (5th-95th pct of 2 curves; full span incl. outliers 11-162 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): U(CoSi)2 I4/mmm (139) mp-21429 [hull=0.000, icsd=2, PRIMARY]; U2Co3Si5 Ibam (72) mp-21178 [hull=0.000, icsd=2, PRIMARY]; U2Co3Si P6_3/mmc (194) mp-1102105 [hull=0.000, icsd=1, PRIMARY]; U3Co2Si7 Cmmm (65) mp-1103185 [hull=0.000, icsd=1, PRIMARY]; UCoSi Pnma (62) mp-20811 [hull=0.082, icsd=1, PRIMARY]
- papers: https://doi.org/10.1016/0304-8853(93)90477-j (Transport and magnetic properties of U2M3Si5 silicides (M = Co, Rh, Ru))

## Co-Si-Yb
- rank 3008 | 1 samples | 1 papers | 1 compositions
- compositions: YbCo2Si2 (1)
- sample form: SingleCrystal (1)
- measured range: 11-306 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Yb(CoSi)2 I4/mmm (139) mp-5326 [hull=0.000, icsd=2, PRIMARY]; Yb5(Co2Si7)2 P2_1/c (14) mp-1202639 [hull=0.024, icsd=1, PRIMARY]
- papers: https://doi.org/10.1007/s10909-019-02187-6 (Thermopower Evolution in Yb(\n                \n                  \n  ...)

## Co-Sn-Ta
- rank 3009 | 1 samples | 1 papers | 1 compositions
- compositions: TaCoSn (1)
- measured range: 299-974 K (5th-95th pct of 5 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): TaCoSn2 F-43m (216) mp-631635 [hull=0.713, PRIMARY]
- papers: https://doi.org/10.1021/acsami.9b13603 (n-Type TaCoSn-Based Half-Heuslers as Promising Thermoelectric Materials)

## Co-Sn-Te
- rank 3010 | 1 samples | 1 papers | 1 compositions
- compositions: CoSn1.5Te1.5 (1)
- sample form: Bulk (1)
- measured range: 77-878 K (5th-95th pct of 4 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Co2(SnTe)3 R-3 (148) mp-866481 [hull=0.000, icsd=1, PRIMARY]
- papers: https://doi.org/10.1063/1.4926479 (Electronic structure and thermoelectric properties of pnictogen-substi...)

## Co-Sn-Ti-V
- rank 3011 | 1 samples | 1 papers | 1 compositions
- compositions: Co2Ti0.6V0.4Sn (1)
- measured range: 14-302 K (5th-95th pct of 1 curves)
- papers: https://doi.org/10.1103/physrevapplied.10.044037 (Anomalous Hall and Nernst Effects in \n<mml:math xmlns:mml=\"http://ww...)

## Co-Sn-V
- rank 3012 | 1 samples | 1 papers | 1 compositions
- compositions: CoVSn (1)
- sample form: Bulk (1)
- measured range: 301-824 K (5th-95th pct of 4 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): VCo2Sn Fm-3m (225) mp-21469 [hull=0.067, icsd=4, PRIMARY]; VCoSn F-43m (216) mp-1018119 [hull=0.589, icsd=1, PRIMARY]
- papers: https://doi.org/10.3390/en13061459 (Experimental Realization of Heavily p-doped Half-Heusler CoVSn Compound)

## Co-Sn-Yb
- rank 3013 | 1 samples | 1 papers | 1 compositions
- compositions: Yb3Co4Sn13 (1)
- sample form: Bulk (1)
- measured range: 240-380 K (5th-95th pct of 4 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Yb3Co4Sn13 Pm-3n (223) mp-1198658 [hull=0.000, icsd=1, PRIMARY]; Yb3(Co2Sn)4 P6_3mc (186) mp-1207700 [hull=0.054, PRIMARY]; Yb9Co13Sn38 Pmmm (47) mp-1217734 [hull=0.017, PRIMARY]
- papers: https://doi.org/10.1016/j.jallcom.2012.09.024 (Thermoelectric properties of Pr3Rh4Sn13-type Yb3Co4Ge13 and Yb3Co4Sn13...)

## Cr-Cu-Fe-Ni
- rank 3014 | 1 samples | 1 papers | 1 compositions
- compositions: Ni2CuCrFe (1)
- sample form: Bulk (1)
- measured range: 10-1124 K (5th-95th pct of 6 curves)
- papers: https://doi.org/10.1088/2053-1591/ab7d5a (Thermoelectric behaviour with high lattice thermal conductivity of Nic...)

## Cr-Cu-Mg-O
- rank 3015 | 1 samples | 1 papers | 1 compositions
- compositions: CuCr0.7Mg0.3O2 (1)
- sample form: Bulk (1)
- measured range: 305-772 K (5th-95th pct of 5 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Mg14CrCuO16 Pmmm (47) mp-1035284 [hull=0.044, PRIMARY, AMBIGUOUS]; Mg30CrCuO32 P4/mmm (123) mp-1037287 [hull=0.022, PRIMARY]; Mg6CrCuO8 P4/mmm (123) mp-1032334 [hull=0.087, PRIMARY]; Mg14CrCuO16 P4/mmm (123) mp-1035311 [hull=0.050]
- papers: https://doi.org/10.1016/j.jallcom.2020.156119 (Effects of multi-scale defects on the thermoelectric properties of del...)

## Cr-Cu-S-Sb
- rank 3016 | 1 samples | 1 papers | 1 compositions
- compositions: CuCr1.5Sb0.5S4 (1)
- sample form: Bulk (1)
- measured range: 324-872 K (5th-95th pct of 5 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Cr3Cu2SbS8 R-3m (166) mp-1226326 [hull=0.001, PRIMARY]
- papers: https://doi.org/10.1021/acs.chemmater.6b05344 (Sb Doping of Metallic CuCr2S4as a Route to Highly Improved Thermoelect...)

## Cr-Cu-Se-V
- rank 3017 | 1 samples | 1 papers | 1 compositions
- compositions: CuCr1.49V0.45Se4 (1)
- sample form: Bulk (1)
- measured range: 78-433 K (5th-95th pct of 1 curves)
- papers: https://doi.org/10.1016/j.jpcs.2011.10.032 (Thermoelectric power of CuCrxVySe4 p-type spinel semiconductors)

## Cr-Fe-Nd-O-Sr
- rank 3018 | 1 samples | 1 papers | 1 compositions
- compositions: Nd0.3Sr0.7Fe0.7Cr0.3O3 (1)
- measured range: 423-1173 K (5th-95th pct of 1 curves)
- papers: https://doi.org/10.1016/j.materresbull.2018.05.031 (Property optimization for strontium-rich lanthanum chromium ferrite ca...)

## Cr-Fe-Ni
- rank 3019 | 1 samples | 1 papers | 1 compositions
- compositions: Ni0.08Cr0.18Fe0.76 (1)
- measured range: 63-1365 K (5th-95th pct of 3 curves)
- papers: https://doi.org/10.2355/tetsutohagane1955.82.9_789 (Thermal Conductivities of SUS304/PSZ Composite Materials)

## Cr-Fe-O-Pr-Sr
- rank 3020 | 1 samples | 1 papers | 1 compositions
- compositions: Pr0.3Sr0.7Fe0.7Cr0.3O3 (1)
- measured range: 423-1173 K (5th-95th pct of 1 curves)
- papers: https://doi.org/10.1016/j.materresbull.2018.05.031 (Property optimization for strontium-rich lanthanum chromium ferrite ca...)

## Cr-Fe-O-Sm-Sr
- rank 3021 | 1 samples | 1 papers | 1 compositions
- compositions: Sm0.3Sr0.7Fe0.7Cr0.3O3 (1)
- measured range: 423-1173 K (5th-95th pct of 1 curves)
- papers: https://doi.org/10.1016/j.materresbull.2018.05.031 (Property optimization for strontium-rich lanthanum chromium ferrite ca...)

## Cr-Ga-N
- rank 3022 | 1 samples | 1 papers | 1 compositions
- compositions: GaNCr3 (1)
- sample form: Polycrystal (1)
- measured range: 10-331 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Cr3GaN Pm-3m (221) mp-3000 [hull=0.022, icsd=2, PRIMARY]; Cr2GaN P6_3/mmc (194) mp-10371 [hull=0.029, icsd=1, PRIMARY]
- papers: https://doi.org/10.1016/j.jssc.2013.10.034 (Synthesis and characterization of antiperovskite nitrides GaNCr3−xMnx)

## Cr-Gd-O
- rank 3023 | 1 samples | 1 papers | 1 compositions
- compositions: (SrRuO3)0.2(GdCrO3)0.8 (1)
- dopant candidates (<5% at.): Sr (1), Ru (1)
- measured range: 113-300 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): GdCrO3 Pnma (62) mp-19598 [hull=0.000, icsd=3, PRIMARY]; GdCrO4 I4_1/amd (141) mp-24916 [hull=0.000, icsd=2, PRIMARY]; GdCrO5 P2_1/c (14) mp-1198487 [hull=0.052, icsd=1, PRIMARY]; Gd2Cr2O5 P4/mmm (123) mp-1184487 [hull=0.318, PRIMARY]; GdCrO3 Pm-3m (221) mp-1147577 [hull=0.235]
- papers: https://doi.org/10.1088/1361-648x/aa9728 (Effect of Gd and Cr substitution on the structural, electronic and mag...)

## Cr-Ge
- rank 3024 | 1 samples | 1 papers | 1 compositions
- compositions: GeCr3 (1)
- measured range: 11-299 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Cr3Ge Pm-3n (223) mp-20685 [hull=0.000, icsd=8, PRIMARY]; CrGe P2_13 (198) mp-20861 [hull=0.091, icsd=5, PRIMARY]
- papers: https://doi.org/10.1016/j.jallcom.2013.09.086 (Synthesis and characterization of Ge–Cr-based intermetallic compounds:...)

## Cr-Ge-N
- rank 3025 | 1 samples | 1 papers | 1 compositions
- compositions: GeNCr3 (1)
- measured range: 12-299 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Cr3GeN P-42_1m (113) mp-637918 [hull=0.008, icsd=2, PRIMARY]
- papers: https://doi.org/10.1016/j.jallcom.2013.09.086 (Synthesis and characterization of Ge–Cr-based intermetallic compounds:...)

## Cr-I-S
- rank 3026 | 1 samples | 1 papers | 1 compositions
- compositions: Cr0.33SI0.67 (1)
- sample form: Film (1)   <-- film/epitaxial samples present: a metastable polymorph may be reachable here that never forms in bulk
- measured range: 333-847 K (5th-95th pct of 3 curves)
- papers: https://doi.org/10.1016/j.jallcom.2012.12.088 (Enhancement of thermoelectric properties in nanocrystalline M–Si thin ...)

## Cr-La-Mn-O
- rank 3027 | 1 samples | 1 papers | 1 compositions
- compositions: La(Cr0.6Mn0.4)O3 (1)
- sample form: Unknown (1)
- measured range: 310-496 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): La2MnCrO6 P2_1/c (14) mp-1223342 [hull=0.022, PRIMARY]; LaMn3Cr4O12 Im-3 (204) mp-1211359 [hull=0.018, PRIMARY]
- papers: https://doi.org/10.2109/jcersj2.15316 (Development and electrical properties of wurtzite (Al,Ti)N materials f...)

## Cr-La-Mn-O-Y
- rank 3028 | 1 samples | 1 papers | 1 compositions
- compositions: YLaMnCrO6 (1)
- curator composition details (from the paper): polycrystalline (1)
- measured range: 180-299 K (5th-95th pct of 1 curves)
- papers: https://doi.org/10.1016/j.jallcom.2015.05.158 (Effects of La-doping on the ferrimagnetism in double perovskite Y2MnCrO6)

## Cr-La-Ni
- rank 3029 | 1 samples | 1 papers | 1 compositions
- compositions: LaNi4Cr (1)
- sample form: Bulk (1)
- measured range: 11-298 K (5th-95th pct of 3 curves)
- papers: https://doi.org/10.1140/epjb/e2011-20159-1 (Thermal transport in the intermetallic compound CeNi4Cr)

## Cr-La-O-Zn
- rank 3030 | 1 samples | 1 papers | 1 compositions
- compositions: LaCr0.7Zn0.3O3 (1)
- measured range: 299-774 K (5th-95th pct of 1 curves)
- papers: https://doi.org/10.1007/s10971-016-4170-5 (Preparation by sol–gel method and characterization of Zn-doped LaCrO3 ...)

## Cr-Mg-O
- rank 3031 | 1 samples | 1 papers | 1 compositions
- compositions: MgCr2O4 (1)
- sample form: Bulk (1)
- measured range: 324-698 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): MgCr2O4 Fd-3m (227) mp-19202 [hull=0.000, icsd=14, PRIMARY]; MgCrO9 P-1 (2) mp-1180584 [hull=0.570, icsd=1, PRIMARY]; MgCrO4 Cmcm (63) mp-19120 [hull=0.000, icsd=1, PRIMARY]; Mg3CrO4 Pm-3m (221) mp-1024044 [hull=0.107, PRIMARY]; MgCrO2 P2_1/m (11) mp-1118395 [hull=0.117, PRIMARY]
- papers: https://doi.org/10.1016/j.solidstatesciences.2009.09.005 (Effect of sintering temperature and thermoelectric power studies of th...)

## Cr-Mn-Ru-Si
- rank 3032 | 1 samples | 1 papers | 1 compositions
- compositions: Mn0.65Cr0.2Ru0.15Si1.74 (1)
- measured range: 80-912 K (5th-95th pct of 4 curves; full span incl. outliers 80-973 K)
- papers: https://doi.org/10.1016/j.jallcom.2013.07.136 (The role of simultaneous substitution of Cr and Ru on the thermoelectr...)

## Cr-Mo
- rank 3033 | 1 samples | 1 papers | 1 compositions
- compositions: (Cr0.98Si0.02)0.91Mo0.09 (1)
- dopant candidates (<5% at.): Si (1)
- sample form: Bulk (1)
- measured range: 10-238 K (5th-95th pct of 2 curves; full span incl. outliers 10-345 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Cr3Mo Cmmm (65) mp-1226288 [hull=0.092, PRIMARY]; CrMo Cmmm (65) mp-1226200 [hull=0.115, PRIMARY]; CrMo3 R3m (160) mp-1226250 [hull=0.454, PRIMARY]
- papers: https://doi.org/10.1063/1.3536667 (Evidence for a possible quantum critical point in a Cr-Si alloy doped ...)

## Cr-Mo-N
- rank 3034 | 1 samples | 1 papers | 1 compositions
- compositions: Cr0.9Mo0.1N (1)
- sample form: Bulk (1)
- measured range: 11-396 K (5th-95th pct of 1 curves)
- papers: https://doi.org/10.1063/1.4861845 (Thermoelectric properties of heavy-element doped CrN)

## Cr-Mo-O-Sr
- rank 3035 | 1 samples | 1 papers | 1 compositions
- compositions: Sr2CrMoO6 (1)
- measured range: 82-322 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Sr2CrMoO6 Fm-3m (225) mp-1205606 [hull=0.044, PRIMARY]
- papers: https://doi.org/10.1063/1.1728294 (Effect of alkaline-earth and transition metals on the electrical trans...)

## Cr-Mo-S
- rank 3036 | 1 samples | 1 papers | 1 compositions
- compositions: Cr1.3Mo6S8 (1)
- sample form: Bulk (1)
- measured range: 302-958 K (5th-95th pct of 4 curves)
- [ref 1] TEDesignLab / ICSD: Cr(MoS2)2 (9) [PRIMARY]
- papers: https://doi.org/10.1007/s11664-009-0975-0 (Thermoelectric Properties of Chevrel-Phase Sulfides M x Mo6S8 (M: Cr, ...)

## Cr-O-Pb
- rank 3037 | 1 samples | 1 papers | 1 compositions
- compositions: Pb2CrO5 (1)
- sample form: SingleCrystal (1)
- measured range: 300-490 K (5th-95th pct of 2 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): CrPb2O5 C2/m (12) mp-24901 [hull=0.000, icsd=4, PRIMARY]; CrPbO4 P2_1/c (14) mp-19146 [hull=0.000, icsd=4, PRIMARY]; CrPbO3 Pm-3m (221) mp-24913 [hull=0.151, icsd=2, PRIMARY]; Cr6CuSi2(Pb5O17)2 P-1 (2) mp-1204438 [hull=0.037, icsd=1, PRIMARY]; CrPb5O8 P2_1/c (14) mp-705034 [hull=0.007, icsd=1, PRIMARY]
- papers: https://doi.org/10.1063/1.4902248 (Photo-transport properties of Pb2CrO5 single crystals)

## Cr-O-Pb-V
- rank 3038 | 1 samples | 1 papers | 1 compositions
- compositions: PbV0.70Cr0.30O3 (1)
- measured range: 58-479 K (5th-95th pct of 1 curves)
- papers: https://doi.org/10.1021/acs.chemmater.8b04680 (Melting of d<i><sub>xy</sub></i> Orbital Ordering Accompanied by Suppr...)

## Cr-O-Pd
- rank 3039 | 1 samples | 1 papers | 1 compositions
- compositions: PdCrO2 (1)
- measured range: 12-298 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): CrPdO2 R-3m (166) mp-1063607 [hull=0.000, icsd=3, PRIMARY]
- papers: https://doi.org/10.1038/ncomms15001 (Simultaneous loss of interlayer coherence and long-range magnetism in ...)

## Cr-O-Re
- rank 3040 | 1 samples | 1 papers | 1 compositions
- compositions: CrReO4 (1)
- measured range: 13-299 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): CrReO4 C2/m (12) mp-31628 [hull=0.023, icsd=1, PRIMARY]; Cr(ReO3)2 P4_2/mnm (136) mp-1226109 [hull=0.064, PRIMARY]; Cr2ReO6 P4_2/mnm (136) mp-31625 [hull=0.042, PRIMARY]; CrReO4 Cmmm (65) mp-1226239 [hull=0.086]
- papers: https://doi.org/10.1103/physrevb.97.014426 (High-pressure synthesis and structural, transport, and magnetic proper...)

## Cr-O-Sm-Sr
- rank 3041 | 1 samples | 1 papers | 1 compositions
- compositions: Sm0.6Sr0.4CrO3 (1)
- sample form: rod-shaped (1)
- measured range: 524-1223 K (5th-95th pct of 1 curves)
- papers: https://doi.org/10.1016/j.memsci.2011.12.027 (Design and experimental investigation of oxide ceramic dual-phase memb...)

## Cr-Se-Tl
- rank 3042 | 1 samples | 1 papers | 1 compositions
- compositions: TlCr5Se8 (1)
- sample form: Bulk (1)
- measured range: 11-872 K (5th-95th pct of 5 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): TlCr5Se8 C2/m (12) mp-3407 [hull=0.000, icsd=3, PRIMARY]; TlCr3Se5 C2/m (12) mp-1190043 [hull=0.000, icsd=1, PRIMARY]; TlCrSe2 R3m (160) mp-998927 [hull=0.132, icsd=1, PRIMARY]; TlCrSe2 R-3m (166) mp-1208019 [hull=0.057]
- papers: https://doi.org/10.1021/cm400365q (Transport Properties of an Intermetallic with Pseudo-hollandite Struct...)

## Cs-Cu-Fe-N-Se
- rank 3043 | 1 samples | 1 papers | 1 compositions
- compositions: CuFeSe2 NCs (1)
- sample form: Bulk (1)
- measured range: 316-653 K (5th-95th pct of 1 curves)
- papers: https://doi.org/10.3390/nano8010008 (Colloidal Synthesis and Thermoelectric Properties of CuFeSe2 Nanocrystals)

## Cs-Cu-La-Te
- rank 3044 | 1 samples | 1 papers | 1 compositions
- compositions: Cs0.752La2Cu5.252Te6 (1)
- sample form: Bulk (1)
- measured range: 294-614 K (5th-95th pct of 4 curves)
- papers: https://doi.org/10.1021/cm201574a (Syntheses, Structures, and Magnetic and Thermoelectric Properties of D...)

## Cs-Cu-Mo-Se
- rank 3045 | 1 samples | 1 papers | 1 compositions
- compositions: Cu2Cs2Mo12Se14 (1)
- sample form: Bulk (1)
- measured range: 12-574 K (5th-95th pct of 2 curves; full span incl. outliers 12-615 K)
- papers: https://doi.org/10.1021/acs.inorgchem.6b00781

## Cs-Cu-Pr-Te
- rank 3046 | 1 samples | 1 papers | 1 compositions
- compositions: Cs0.732Pr2Cu5.272Te6 (1)
- sample form: Bulk (1)
- measured range: 292-689 K (5th-95th pct of 5 curves)
- papers: https://doi.org/10.1021/cm201574a (Syntheses, Structures, and Magnetic and Thermoelectric Properties of D...)

## Cs-Cu-Te
- rank 3047 | 1 samples | 1 papers | 1 compositions
- compositions: Cs2BaCu8Te10 (1)
- dopant candidates (<5% at.): Ba (1)
- sample form: Bulk (1)
- measured range: 82-307 K (5th-95th pct of 1 curves)
- papers: https://doi.org/10.1021/cm000390o (Thermoelectric Properties and Electronic Structure of the Cage Compoun...)

## Cs-Fe-Se
- rank 3048 | 1 samples | 1 papers | 1 compositions
- compositions: Cs1.2Fe3.95Se4 (1)
- measured range: 10-298 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): CsFe2Se3 Cmcm (63) mp-662563 [hull=0.000, icsd=2, PRIMARY]; Cs3FeSe3 Cmce (64) mp-1194302 [hull=0.000, icsd=1, PRIMARY]; Cs9Fe2Se7 P2_13 (198) mp-1201016 [hull=0.000, icsd=1, PRIMARY]
- papers: https://doi.org/10.1103/physrevx.10.041008 (Unconventional Superconductivity Induced by Suppressing an Iron-Seleni...)

## Cs-Ga-Sb
- rank 3049 | 1 samples | 1 papers | 1 compositions
- compositions: (Ba0.025Cs0.975)1.05GaSb4 (1)
- dopant candidates (<5% at.): Ba (1)
- sample form: Bulk (1)
- measured range: 325-625 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Cs2GaSb2 Pnma (62) mp-29372 [hull=0.000, icsd=1, PRIMARY]; Cs6GaSb3 P2_1/m (11) mp-9697 [hull=0.000, icsd=1, PRIMARY]
- papers: https://doi.org/10.1021/acsaem.0c00048 (Discovery of n-Type Zintl Phases RbAlSb4, RbGaSb4, CsAlSb4, and CsGaSb4)

## Cs-Ga-Si
- rank 3050 | 1 samples | 1 papers | 1 compositions
- compositions: Cs8Ga8Si38 (1)
- measured range: 10-297 K (5th-95th pct of 3 curves)
- papers: https://doi.org/10.1021/cm504436v (Synthesis, Structure, Thermoelectric Properties, and Band Gaps of Alka...)
