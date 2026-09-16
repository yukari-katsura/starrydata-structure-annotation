# Host systems -- chunk 041 of 73

Ranks 2001-2050 by sample count. These 50 host systems cover 100 samples (0.19% of the TE set); cumulative through this chunk: 96.30%.

Assign each host system a structural prototype from `data/annotated/taxonomy/prototypes_seed_v3.json`, or propose a new one in `taxonomy/prototypes_proposed.jsonl` first. Append results to `data/annotated/annotations/family_assignments.jsonl`.

The hand-entered MaterialFamily labels are deliberately NOT shown here -- they are held out in `df_host_systems.parquet` to validate this classification later. Decide from the compositions.

A "seed hypothesis" line means the taxonomy already names this host under that prototype. Confirm it against the compositions rather than accepting it; two or more listed means the host is mixed and needs splitting per composition.

Evidence follows the project precedence. Your judgement about the thermoelectric chemistry decides the prototype. [ref 1] is TEDesignLab, ICSD-backed and thermoelectric-specific -- prefer it. [ref 2] is Materials Project. Within a formula, polymorphs are ranked by ICSD reference count and the top one is marked PRIMARY -- not by e_above_hull, which is unusable for layered chalcogenides in the 2019 dump (Sb2Te3 R-3m carries 26 ICSD refs at hull 1.02). A primary resting on fewer than 5 ICSD references is flagged weak; the ambient phase may simply be absent from the snapshot, as it is for Bi2Se3.

While you have the host in view, also record what each minor element DOES, in `dopant_roles` -- the role follows from the prototype and cannot be judged without it. A median host has 2 such elements. Not everything listed is a dopant: O, C, N and H are usually milling or pressing residue, and an element just under 5 at.% may be an alloying end member rather than dilute doping. The doping LEVEL is computed later from the parsed fractions -- do not work it out by hand here.

A polymorph list is NOT a thermal sequence. SnSe has three known structures but only Pnma -> Cmcm happens on heating; rocksalt SnSe is metastable (2 icsd refs against 32). Put thermally reached phases in `phases` with their transition temperatures, and everything else in `other_polymorphs` with an occurrence reason. hull and icsd counts are shown to help you tell them apart.

A host may need MORE THAN ONE prototype. Transport is measured across a wide window and many thermoelectrics transform inside it, so where a "MEASUREMENT CROSSES A TRANSITION" line appears, record each phase with its own temperature range in the `phases` field. Transition temperatures shown are approximate and composition-dependent.

Both references describe which phases EXIST in a chemistry, not which phase this paper made. Al-O-Zn is best attested as ZnAl2O4 spinel (227) while almost every sample in it is Al-doped wurtzite ZnO (186). Weigh them against the compositions; do not follow them blindly.

## Bi-Ho-O-Sb
- rank 2001 | 2 samples | 1 papers | 2 compositions
- compositions: Ho2Sb0.6Bi0.4O3 (1); Ho2Sb0.4Bi0.6O3 (1)
- measured range: 10-394 K (5th-95th pct of 2 curves)
- papers: https://doi.org/10.1021/acs.chemmater.7b03996 (Rare-Earth Pnictide Oxides (RE,Ca)mPnnOm (Pn = Sb, Bi): A Review of Cr...)

## Bi-I-Rh
- rank 2002 | 2 samples | 1 papers | 1 compositions
- compositions: Bi1.4Rh3I9 (2)
- sample form: Bulk (2)
- measured range: 10-552 K (5th-95th pct of 7 curves)
- papers: https://doi.org/10.1002/adfm.201600718 (Minimum Thermal Conductivity in Weak Topological Insulators with Bismu...)

## Bi-K-O
- rank 2003 | 2 samples | 1 papers | 1 compositions
- compositions: Bi0.62K0.38BiO3 (2)
- sample form: Bulk (1)
- measured range: 22-297 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): KBiO2 C2/c (15) mp-30988 [hull=0.000, icsd=2, PRIMARY]; KBiO3 Pn-3 (201) mp-29799 [hull=0.000, icsd=2, PRIMARY]; K8BiO3 Pm-3m (221) mp-1102773 [hull=0.222, icsd=1, PRIMARY]; K3BiO3 I-43m (217) mp-29524 [hull=0.000, icsd=1, PRIMARY]; K3BiO4 P-1 (2) mp-30120 [hull=0.000, icsd=1, PRIMARY]
- papers: https://doi.org/10.1016/0921-4534(94)90462-6 (Thermoelectric power of superconducting Ba-K-Bi-O crystals)

## Bi-La-Mn-O-Sr-Ti
- rank 2004 | 2 samples | 1 papers | 1 compositions
- compositions: (La0.7Sr0.3MnO3)86(SrBi4Ti4O15)14 (2)
- sample form: Bulk (2)
- measured range: 299-805 K (5th-95th pct of 8 curves)
- papers: https://doi.org/10.1016/j.jallcom.2020.157001 (Colossal seebeck coefficient in Aurivillius phase-perovskite oxide com...)

## Bi-La-Pd
- rank 2005 | 2 samples | 2 papers | 1 compositions
- compositions: LaPdBi (2)
- sample form: Bulk (1)
- measured range: 300-958 K (5th-95th pct of 8 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): LaBiPd F-43m (216) mp-1206717 [hull=0.000, PRIMARY]; LaBiPd2 Immm (71) mp-1093906 [hull=1.734, PRIMARY]
- papers: https://doi.org/10.2320/matertrans.e-mra2007807 (Thermoelectric Properties of Half-Heusler Type LaPdBi and GdPdBi) | https://doi.org/10.1023/a:1004409706821 (Electrical properties of some (1,1,1) intermetallic compounds)

## Bi-La-Pt
- rank 2006 | 2 samples | 2 papers | 2 compositions
- compositions: LaBiPt (1); La3Bi4Pt3 (1)
- sample form: SingleCrystal (1)
- measured range: 13-292 K (5th-95th pct of 3 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): La3Bi4Pt3 I-43d (220) mp-1189173 [hull=0.026, icsd=1, PRIMARY]; LaBiPt F-43m (216) mp-1018136 [hull=0.000, icsd=1, PRIMARY]
- papers: https://doi.org/10.1063/1.1357864 (Thermoelectric and transport properties of CeBiPt and LaBiPt) | https://doi.org/10.1103/physrevb.50.18142 (Substitutional effects on the electronic transport of the Kondo semico...)

## Bi-Li
- rank 2007 | 2 samples | 1 papers | 2 compositions
- compositions: Bi80Li20 (1); Bi86Li14 (1)
- measured range: 10-297 K (5th-95th pct of 4 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Li3Bi Fm-3m (225) mp-23222 [hull=0.000, icsd=2, PRIMARY]; LiBi P4/mmm (123) mp-22902 [hull=0.000, icsd=2, PRIMARY]
- papers: https://doi.org/10.1007/s11664-011-1861-0 (Lithium as an Interstitial Donor in Bismuth and Bismuth–Antimony Alloys)

## Bi-Lu-Pd
- rank 2008 | 2 samples | 2 papers | 1 compositions
- compositions: LuPdBi (2)
- measured range: 11-300 K (5th-95th pct of 5 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Lu5BiPd2 I4/mcm (140) mp-1210532 [hull=0.000, PRIMARY]; LuBiPd F-43m (216) mp-1207185 [hull=0.000, PRIMARY]; LuBiPd2 Fm-3m (225) mp-1185495 [hull=0.087, PRIMARY]
- papers: https://doi.org/10.1103/physrevb.93.115134 (Robust tunability of magnetoresistance in half-HeuslerRPtBi(R=Gd, Dy, ...) | https://doi.org/10.1023/a:1004409706821 (Electrical properties of some (1,1,1) intermetallic compounds)

## Bi-Mg-Sb-Yb
- rank 2009 | 2 samples | 2 papers | 2 compositions
- compositions: Mg2.725Yb0.4Sb1.5Bi.5Te0.01 (1); YbMg2Bi1.58Sb0.4 (1)
- dopant candidates (<5% at.): Te (1)
- sample form: Bulk (2)
- measured range: 298-872 K (5th-95th pct of 9 curves)
- papers: https://doi.org/10.1039/c9ta11328b (The importance of the Mg–Mg interaction in Mg3Sb2–Mg3Bi2 shown through...) | https://doi.org/10.1016/j.jmst.2020.04.052 (Enhanced thermoelectric properties of Zintl phase YbMg2Bi1.98 through ...)

## Bi-Mg-Sm
- rank 2010 | 2 samples | 1 papers | 2 compositions
- compositions: SmMg2Bi2 (1); Sm0.75Yb0.125Eu0.125Mg2Bi1.99 (1)
- dopant candidates (<5% at.): Yb (1), Eu (1)
- sample form: Bulk (2)
- measured range: 305-776 K (5th-95th pct of 10 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Sm(MgBi)2 P-3m1 (164) mp-1068021 [hull=0.105, icsd=1, PRIMARY]
- papers: https://doi.org/10.1039/c9ta13224d (Achieving high-performance p-type SmMg2Bi2 thermoelectric materials th...)

## Bi-Mn
- rank 2011 | 2 samples | 1 papers | 2 compositions
- compositions: Mn55Bi45 (1); Mn51Fe4Bi45 (1)
- dopant candidates (<5% at.): Fe (1)
- measured range: 23-294 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): MnBi P6_3/mmc (194) mp-1063902 [hull=0.214, icsd=13, PRIMARY]; Mn3Bi I4/mmm (139) mp-623452 [hull=0.467, icsd=1, PRIMARY]; MnBi3 Pm-3m (221) mp-1185989 [hull=0.400, PRIMARY]; MnBi Pmma (51) mp-1221736 [hull=0.226]; Mn3Bi R-3m (166) mp-669332 [hull=0.617]
- papers: https://doi.org/10.1063/1.3675615 (Structural, magnetic, and electron transport properties of MnBi:Fe thi...)

## Bi-Mn-Sr
- rank 2012 | 2 samples | 1 papers | 1 compositions
- compositions: SrMnBi2 (2)
- sample form: SingleCrystal (2)
- measured range: 11-320 K (5th-95th pct of 6 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): SrMnBi2 I4/mmm (139) mp-29207 [hull=0.176, icsd=1, PRIMARY]
- papers: https://doi.org/10.1063/1.3695155 (Large magnetothermopower effect in Dirac materials (Sr/Ca)MnBi2)

## Bi-Mo-Te
- rank 2013 | 2 samples | 2 papers | 1 compositions
- compositions: MoBi2Te5 (2)
- measured range: 303-497 K (5th-95th pct of 2 curves)
- papers: https://doi.org/10.1016/j.materresbull.2012.08.026 (Synthesis of fibrous reticulate nanocrystalline n-type MoBi2(Se1−xTex)...) | https://doi.org/10.1080/09500839.2012.700410 (Synthesis and characterization of nanocrystalline MoBi2Te5thin films f...)

## Bi-Nd-Pd
- rank 2014 | 2 samples | 2 papers | 1 compositions
- compositions: NdPdBi (2)
- measured range: 11-300 K (5th-95th pct of 5 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): NdBiPd F-43m (216) mp-1008858 [hull=0.000, icsd=1, PRIMARY]
- papers: https://doi.org/10.1103/physrevb.84.035208 (Magnetic and transport properties of rare-earth-based half-Heusler pha...) | https://doi.org/10.1023/a:1004409706821 (Electrical properties of some (1,1,1) intermetallic compounds)

## Bi-O-Rh
- rank 2015 | 2 samples | 1 papers | 1 compositions
- compositions: Bi2Rh2O7 (2)
- measured range: 30-294 K (5th-95th pct of 2 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Bi12Rh12O41 Imm2 (44) mp-760121 [hull=0.001, PRIMARY, AMBIGUOUS]; Bi8Rh8O27 R3m (160) mp-766286 [hull=0.009, PRIMARY]; CeBi2(Rh2O5)3 Pm (6) mp-1227635 [hull=0.015, PRIMARY]; Bi12Rh12O41 P3m1 (156) mp-686044 [hull=0.008]
- papers: https://doi.org/10.1063/5.0151959 (Impact of iso-structural template layer on stabilizing pyrochlore Bi2R...)

## Bi-Pd-Y
- rank 2016 | 2 samples | 2 papers | 1 compositions
- compositions: YPdBi (2)
- measured range: 14-292 K (5th-95th pct of 3 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): YBiPd F-43m (216) mp-1008624 [hull=0.000, icsd=1, PRIMARY]; YBiPd2 Fm-3m (225) mp-30465 [hull=0.070, icsd=1, PRIMARY]; Y5BiPd2 I4/mcm (140) mp-1207753 [hull=0.000, PRIMARY]
- papers: https://doi.org/10.1103/physrevb.72.094409 (Magnetic and transport properties of the rare-earth-based Heusler phas...) | https://doi.org/10.1103/physrevb.84.035208 (Magnetic and transport properties of rare-earth-based half-Heusler pha...)

## Bi-Pt-Yb
- rank 2017 | 2 samples | 2 papers | 2 compositions
- compositions: YbPtBi (1); YbBiPt (1)
- sample form: SingleCrystal (2)
- measured range: 12-299 K (5th-95th pct of 5 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): YbBiPt F-43m (216) mp-1018106 [hull=0.000, icsd=2, PRIMARY]
- papers: https://doi.org/10.1103/physrevb.87.075120 (Magnetic-field-tuned quantum criticality of the heavy-fermion system Y...) | https://doi.org/10.1103/physrevb.56.8098 (Electronic transport properties of the semimetallic heavy fermion YbBiPt)

## Bi-S-Se-Te
- rank 2018 | 2 samples | 1 papers | 1 compositions
- compositions: Bi2Te2.3Se0.3S0.4 (2)
- measured range: 297-599 K (5th-95th pct of 10 curves)
- papers: https://doi.org/10.1039/c2ee23549h (Studies on the Bi2Te3–Bi2Se3–Bi2S3system for mid-temperature thermoele...)

## Bi-Sb-Te-Zn
- rank 2019 | 2 samples | 1 papers | 2 compositions
- compositions: (Zn4Sb3)0.12Bi0.5Sb1.5Te3 (1); (Zn4Sb3)0.19Bi0.5Sb1.5Te3 (1)
- sample form: Bulk (2)
- measured range: 310-608 K (5th-95th pct of 6 curves)
- papers: https://doi.org/10.1016/j.jallcom.2010.04.006 (Synthesis and thermoelectric properties of Zn4Sb3/Bi0.5Sb1.5Te3 bulk n...)

## Bi-Sb-Yb
- rank 2020 | 2 samples | 2 papers | 2 compositions
- compositions: Yb4Sb2.4Bi0.6 (1); Yb4Bi0.6Sb2.4 (1)
- sample form: pellets (1)
- measured range: 298-1249 K (5th-95th pct of 3 curves)
- papers: https://doi.org/10.1007/s11664-011-1564-6 (Antimony-Based Compounds with the Anti-Th3P4 Structure as Potential Hi...) | https://doi.org/10.1039/d2dt00412g (Materials design, synthesis, and transport properties of disordered ra...)

## Bi-Te-Y
- rank 2021 | 2 samples | 1 papers | 2 compositions
- compositions: Y0.25Bi1.75Te3 (1); Y0.3Bi1.7Te3 (1)
- sample form: Bulk (2)
- measured range: 307-533 K (5th-95th pct of 8 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): YBiTe3 R3m (160) mp-1215930 [hull=0.139, PRIMARY]
- papers: https://doi.org/10.1007/s11664-014-3220-4 (Preparation and Thermoelectric Properties of Yttrium-Doped Bi2Te3 Flow...)

## Br-Cs-Sn
- rank 2022 | 2 samples | 1 papers | 1 compositions
- compositions: CsSnBr3 (2)
- sample form: SingleCrystal (2)
- measured range: 332-585 K (5th-95th pct of 8 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): CsSn2Br5 I4/mcm (140) mp-23467 [hull=0.000, icsd=2, PRIMARY]; Cs2SnBr6 Fm-3m (225) mp-641923 [hull=0.000, icsd=1, PRIMARY]; CsSnBr3 Pm-3m (221) mp-27214 [hull=0.000, icsd=1, PRIMARY]
- papers: https://doi.org/10.1016/j.cplett.2020.137637 (Thermoelectric properties of all-inorganic perovskite CsSnBr3: A combi...)

## C-Ca-Co-O
- rank 2023 | 2 samples | 1 papers | 2 compositions
- compositions: Ca3Co4O9C1.3 (1); Ca3Co4O9C2.7 (1)
- measured range: 31-352 K (5th-95th pct of 6 curves)
- papers: https://doi.org/10.1016/j.ceramint.2014.09.015 (Ultralow thermal conductivity and thermoelectric properties of carbon ...)

## C-Ca-Co-O-Si
- rank 2024 | 2 samples | 1 papers | 2 compositions
- compositions: (Ca3Co4O9)51.59(SiC)48.41 (1); (Ca3Co4O9)41.92(SiC)58.08 (1)
- measured range: 324-1066 K (5th-95th pct of 6 curves)
- papers: https://doi.org/10.1016/j.jallcom.2019.01.239 (Significant enhancement in Seebeck coefficient and power factor of Ca3...)

## C-Co-Na-O
- rank 2025 | 2 samples | 1 papers | 2 compositions
- compositions: C13.71O42.95Na15.9Co27.41 (1); C5.48O48.8Na19.03Co26.69 (1)
- sample form: Bulk (2)
- measured range: 399-901 K (5th-95th pct of 6 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): NaCo(CO)4 Pbcm (57) mp-609284 [hull=0.362, icsd=1, PRIMARY]; Na4Co2C4SO16 Fddd (70) mp-1176472 [hull=0.034, PRIMARY, AMBIGUOUS]; Na4Co2P(CO4)4 Fddd (70) mp-771217 [hull=0.064, PRIMARY]; Na5Co2As(CO4)4 C2/c (15) mp-777426 [hull=0.055, PRIMARY, AMBIGUOUS]; Na5CoCO5 Pmm2 (25) mp-1221135 [hull=0.030, PRIMARY]
- papers: https://doi.org/10.1007/s11664-010-1316-z (Synthesis and Electrical Properties of γ-Na x Co2O4 via a Citrate Sol–...)

## C-Co-O
- rank 2026 | 2 samples | 1 papers | 1 compositions
- compositions: C3Co4O9 (2)
- sample form: Bulk (2)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Co(CO)4 P2_1/m (11) mp-609229 [hull=0.402, icsd=3, PRIMARY]; CoCO3 R-3c (167) mp-24854 [hull=0.000, icsd=3, PRIMARY]; Co3SnC12ClO12 P2_1/c (14) mp-1202020 [hull=0.368, icsd=2, PRIMARY]; Fe2Co4Ge2(CO)21 C2/c (15) mp-652793 [hull=0.510, icsd=2, PRIMARY]; Co3C10O9 P3_121 (152) mp-647768 [hull=0.466, icsd=1, PRIMARY, AMBIGUOUS]
- papers: https://doi.org/10.1016/j.ssc.2003.11.045 (High-temperature thermoelectric properties of Ca3Co4O9+δ with Eu subst...)

## C-Co-O-Sr
- rank 2027 | 2 samples | 1 papers | 1 compositions
- compositions: Sr4Co2O6CO3 (2)
- measured range: 10-300 K (5th-95th pct of 2 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Sr2Co(CO)2 P4/mmm (123) mp-1147608 [hull=0.634, PRIMARY]
- papers: https://doi.org/10.1063/1.3624901 (Contribution of carriers in both the metallic and semiconducting phase...)

## C-Cr-Si
- rank 2028 | 2 samples | 1 papers | 2 compositions
- compositions: (Cr3C2)65.62(SiC)34.38 (1); (Cr3C2)52.68(SiC)47.32 (1)
- measured range: 295-873 K (5th-95th pct of 2 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Cr2SiC P6_3/mmc (194) mp-1078494 [hull=0.117, icsd=2, PRIMARY]; Cr5Si3C P6_3/mcm (193) mp-1105327 [hull=0.048, icsd=1, PRIMARY]
- papers: https://doi.org/10.1007/bf00356339 (Thermal conduction in Cr3C2/SiC composite)

## C-Fe
- rank 2029 | 2 samples | 1 papers | 1 compositions
- compositions: FeC0.1 (2)
- measured range: 107-421 K (5th-95th pct of 2 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Fe5C2 C2/c (15) mp-2794 [hull=0.053, icsd=6, PRIMARY]; Fe3C P6_322 (182) mp-13154 [hull=0.053, icsd=3, PRIMARY]; Fe7C3 Pnma (62) mp-21717 [hull=0.059, icsd=3, PRIMARY]; Fe2C Pnnm (58) mp-1871 [hull=0.057, icsd=3, PRIMARY]; Fe23C6 Fm-3m (225) mp-1192884 [hull=0.046, icsd=2, PRIMARY]
- papers: https://doi.org/10.1016/0001-6160(88)90094-6 (Effects of precipitation on the thermoelectric power of iron-carbon al...)

## C-Fe-Sn
- rank 2030 | 2 samples | 2 papers | 1 compositions
- compositions: SnCFe3 (2)
- measured range: 10-325 K (5th-95th pct of 5 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Fe3SnC Pm-3m (221) mp-21850 [hull=0.069, icsd=1, PRIMARY]
- papers: https://doi.org/10.1007/s13391-015-4425-2 (Thermoelectric properties of metallic antiperovskites AXD3 (A=Ge, Sn, ...) | https://doi.org/10.1021/ic500026t (Good Thermoelectric Performance in Strongly Correlated System SnCCo3wi...)

## C-Mo-Si
- rank 2031 | 2 samples | 1 papers | 1 compositions
- compositions: Mo5Si3C (2)
- sample form: Bulk (2)
- measured range: 13-1064 K (5th-95th pct of 6 curves)
- papers: https://doi.org/10.1016/j.intermet.2003.12.008 (Electrical and thermal properties of single crystalline Mo 5 X 3  (X=S...)

## C-N-Si
- rank 2032 | 2 samples | 1 papers | 2 compositions
- compositions: Si3N4C2 (1); Si3N4C0.5 (1)
- curator composition details (from the paper): Si3N4 with 17vol%GNP (1); Si3N4 with 4vol%rGO (1)
- sample form: Bulk (2)
- measured range: 97-315 K (5th-95th pct of 2 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Si(CN2)2 Pn-3m (224) mp-30160 [hull=0.029, icsd=1, PRIMARY]; SiCN F-43m (216) mp-8003 [hull=2.221, icsd=1, PRIMARY]; Si2CN4 Aea2 (41) mp-30161 [hull=0.000, icsd=1, PRIMARY]; LiZnSi3(C4N)4 P2_12_12_1 (19) mp-1182794 [hull=1.191, PRIMARY]; NdSi6(C6N)3 C2/c (15) mp-1180641 [hull=0.778, PRIMARY]
- papers: https://doi.org/10.1016/j.ceramint.2016.04.056 (Thermopower and hall effect in silicon nitride composites containing t...)

## C-Nb
- rank 2033 | 2 samples | 1 papers | 2 compositions
- compositions: NbC0.96 (1); NbC0.76 (1)
- measured range: 10-76 K (5th-95th pct of 2 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): NbC Fm-3m (225) mp-910 [hull=0.040, icsd=38, PRIMARY]; Nb6C5 C2/m (12) mp-2760 [hull=0.000, icsd=4, PRIMARY]; Nb2C P-3m1 (164) mp-2318 [hull=0.017, icsd=2, PRIMARY]; Nb4C3 Pm-3m (221) mp-15660 [hull=0.171, icsd=1, PRIMARY]; Nb10C7 C2/m (12) mp-32679 [hull=0.039, PRIMARY]
- papers: https://doi.org/10.1103/physrev.188.770 (Lattice Thermal Conductivity of Superconducting Niobium Carbide)

## C-O-Sr-Ti
- rank 2034 | 2 samples | 1 papers | 2 compositions
- compositions: SrTiO3C0.31 (1); SrTiO3C0.63 (1)
- curator composition details (from the paper): C:graphene oxide (2)
- sample form: Bulk (2)
- measured range: 295-775 K (5th-95th pct of 12 curves)
- papers: https://doi.org/10.1038/s41598-019-45162-7 (Grain Boundary Interfaces Controlled by Reduced Graphene Oxide in Nons...)

## C-Pu
- rank 2035 | 2 samples | 2 papers | 1 compositions
- compositions: PuC (2)
- measured range: 10-1273 K (5th-95th pct of 3 curves; full span incl. outliers 10-1574 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): PuC Fm-3m (225) mp-280 [hull=0.132, icsd=8, PRIMARY]; Pu2C3 I-43d (220) mp-19891 [hull=0.000, icsd=6, PRIMARY]; PuC2 I4/mmm (139) mp-1206675 [hull=0.046, PRIMARY]
- papers: https://doi.org/10.1016/0022-3115(86)90182-0 (Thermal conductivity of sintered plutonium carbide) | https://doi.org/10.1016/0022-3697(64)90144-1 (Etude de la structure electronique des carbures de thorium, d'uranium ...)

## C-Se-Sn
- rank 2036 | 2 samples | 1 papers | 2 compositions
- compositions: SnSeC0.12 (1); SnSeC0.17 (1)
- sample form: Bulk (2)
- measured range: 328-823 K (5th-95th pct of 10 curves)
- papers: https://doi.org/10.1021/acsami.0c00873 (Enhancing the Thermoelectric Performance of Polycrystalline SnSe by De...)

## Ca-Cd
- rank 2037 | 2 samples | 2 papers | 2 compositions
- compositions: Cd6Ca (1); Cd85Ca15 (1)
- measured range: 12-299 K (5th-95th pct of 2 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): CaCd2 P6_3/mmc (194) mp-1078 [hull=0.008, icsd=3, PRIMARY]; CaCd Pm-3m (221) mp-1073 [hull=0.000, icsd=2, PRIMARY]; Ca3AlCd17 R3 (146) mp-680394 [hull=0.000, icsd=1, PRIMARY]; Ca3Cd2 P4_2/mnm (136) mp-18167 [hull=0.002, icsd=1, PRIMARY]; Ca3Cd Pm-3m (221) mp-1183501 [hull=0.069, PRIMARY]
- papers: https://doi.org/10.1016/j.jallcom.2003.10.073 (Novel phase transition in the Cd6M intermetallics) | https://doi.org/10.1088/0953-8984/14/28/309 (Origin of the maximum in the temperature-dependent electrical resistiv...)

## Ca-Co-Fe-O
- rank 2038 | 2 samples | 1 papers | 2 compositions
- compositions: Ca0.6Co0.4Fe2O4 (1); Ca0.5Co0.5Fe2O4 (1)
- measured range: 311-658 K (5th-95th pct of 2 curves; full span incl. outliers 311-735 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ca2FeCoO5 Pbcm (57) mp-1203339 [hull=0.035, icsd=1, PRIMARY]; Ca12FeCo7O24 P2 (3) mp-1227684 [hull=0.032, PRIMARY]; Ca6Fe(CoO4)3 R32 (155) mp-1227494 [hull=0.000, PRIMARY]
- papers: https://doi.org/10.1016/j.jallcom.2003.08.073 (Thermoelectric power studies of Ca–Co ferrites)

## Ca-Co-Fe-O-Y
- rank 2039 | 2 samples | 1 papers | 2 compositions
- compositions: Ca0.5Y0.5Fe0.5Co0.5O3 (1); Ca0.3Y0.7Fe0.5Co0.5O3 (1)
- sample form: pellets (2)
- measured range: 823-1023 K (5th-95th pct of 2 curves)
- papers: https://doi.org/10.1016/j.jpowsour.2018.12.030 (Enhanced oxygen reduction reaction through Ca and Co Co-doped YFeO3 as...)

## Ca-Co-Ir-O
- rank 2040 | 2 samples | 2 papers | 2 compositions
- compositions: Ca3CoIrO6 (1); Ca3Co3.9Ir40.1O9 (1)
- sample form: Bulk (1)
- measured range: 110-1104 K (5th-95th pct of 3 curves)
- papers: https://doi.org/10.1063/1.2828575 (Magnetic and thermoelectric properties of quasi-one-dimensional oxides...) | https://doi.org/10.1111/jace.12676 (Strengthening of Thermoelectric Performance via Ir Doping in Layered C...)

## Ca-Co-O-Pb
- rank 2041 | 2 samples | 1 papers | 2 compositions
- compositions: Pb0.7Sr0.5Ca1.5Co0.3O3(CoO2)1.67 (1); Pb0.75Ca2Co0.3O3(CoO2)1.61 (1)
- dopant candidates (<5% at.): Sr (1)
- measured range: 10-789 K (5th-95th pct of 5 curves)
- papers: https://doi.org/10.1063/1.1494114 (Thermopower enhancement in misfit cobaltites)

## Ca-Co-O-Sr-Y
- rank 2042 | 2 samples | 1 papers | 1 compositions
- compositions: Sr1.8Ca1.2YCo4O10.5 (2)
- measured range: 57-300 K (5th-95th pct of 2 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Sr10CaY4(CoO3)10 I4/m (87) mp-1218919 [hull=0.025, PRIMARY]
- papers: https://doi.org/10.1143/jpsj.78.094711 (Chemical and Physical Pressure Effects on the Magnetic and Transport P...)

## Ca-Cr-La-Mn-O
- rank 2043 | 2 samples | 1 papers | 2 compositions
- compositions: La0.7Ca0.3Mn0.4Cr0.6O3 (1); La0.7Ca0.3Mn0.7Cr0.3O3 (1)
- sample form: Polycrystal (2)
- measured range: 82-301 K (5th-95th pct of 6 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ca3La5Mn7CrO24 P1 (1) mp-743745 [hull=0.003, PRIMARY]; Ca6La2Mn7CrO24 P-1 (2) mp-743861 [hull=0.022, PRIMARY]
- papers: https://doi.org/10.1063/1.1898438 (Spin-cluster effect and lattice-deformation-induced Kondo effect, spin...)

## Ca-Cr-O-Pr
- rank 2044 | 2 samples | 1 papers | 2 compositions
- compositions: Pr0.5Ca0.5CrO3 (1); Pr0.7Ca0.3CrO3 (1)
- measured range: 37-657 K (5th-95th pct of 6 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): CaPrCrO4 Cmc2_1 (36) mp-1227145 [hull=0.046, PRIMARY]
- papers: https://doi.org/10.1140/epjb/e2006-00349-8 (Transport and magnetic properties of Pr1-xCaxCrO3 (x = 0.0–0.5): effec...)

## Ca-Cu-Ir-La-O
- rank 2045 | 2 samples | 1 papers | 1 compositions
- compositions: Ca0.6La1.4CuIrO6 (2)
- measured range: 322-753 K (5th-95th pct of 2 curves)
- papers: https://doi.org/10.1103/physrevmaterials.5.054604 (Iridium valence variation and carrier sign tuning in \n(Ca,Ba)xLa2−xCu...)

## Ca-Cu-Mn-O
- rank 2046 | 2 samples | 2 papers | 2 compositions
- compositions: CaMn2CuMn4O12 (1); CaCu3Mn4O12 (1)
- measured range: 11-537 K (5th-95th pct of 3 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ca3MnCuO6 P2_1/c (14) mp-1214191 [hull=0.014, PRIMARY]
- papers: https://doi.org/10.1016/j.progsolidstchem.2007.01.013 (Thermoelectric properties of the AA′3B4O12-type ordered perovskite oxides) | https://doi.org/10.1103/physrevb.105.054409 (<mml:math xmlns:mml=\"http://www.w3.org/1998/Math/MathML\"><mml:mrow><...)

## Ca-Cu-O
- rank 2047 | 2 samples | 2 papers | 1 compositions
- compositions: CaCuO2 (2)
- measured range: 38-196 K (5th-95th pct of 2 curves; full span incl. outliers 38-301 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ca2CuO3 Immm (71) mp-5869 [hull=0.000, icsd=4, PRIMARY]; CaCuO2 P4/mmm (123) mp-4826 [hull=0.001, icsd=3, PRIMARY]; CaCu2O3 Pmmn (59) mp-7466 [hull=0.015, icsd=2, PRIMARY]; Ca5(CuO2)6 P2/c (13) mp-29917 [hull=0.017, icsd=1, PRIMARY]; Ca(Cu3O4)2 Fm-3m (225) mp-1147677 [hull=0.033, PRIMARY]
- papers: https://doi.org/10.1063/1.4767117 (Growth and interfacial properties of epitaxial CaCuO2 thin films) | https://doi.org/10.1016/0921-4534(95)00656-7 (and   superlattices prepared by laser ablation)

## Ca-Cu-O-Sr-Tl
- rank 2048 | 2 samples | 1 papers | 1 compositions
- compositions: TlSr2Ca2Cu3O9.4 (2)
- measured range: 30-293 K (5th-95th pct of 2 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Sr2CaTlCu2O7 P4/mmm (123) mp-20824 [hull=0.018, icsd=1, PRIMARY]
- papers: https://doi.org/10.1016/s0921-4534(99)00446-3 (Synthesis and characterization of single-phase TlSr2Ca2Cu3Oy)

## Ca-Cu-O-Y
- rank 2049 | 2 samples | 1 papers | 2 compositions
- compositions: YBa0.5Ca1.5Cu3O7 (1); YCa2Cu3O7 (1)
- dopant candidates (<5% at.): Ba (1)
- sample form: pellets (2)
- measured range: 18-299 K (5th-95th pct of 3 curves)
- papers: https://doi.org/10.1016/s0921-4534(97)01439-1 (Metal-insulator transition in YBa2−xCaxCu3O7−δ system)

## Ca-Eu-Mn-O
- rank 2050 | 2 samples | 1 papers | 2 compositions
- compositions: Ca0.7Eu0.3MnO3 (1); Ca0.6Eu0.4MnO3 (1)
- sample form: pellets (2)
- measured range: 299-895 K (5th-95th pct of 2 curves)
- papers: https://doi.org/10.1016/j.ssi.2009.10.017 (Synthesis and electrical properties of nanocrystalline Ca1−xEuxMnO3±δ ...)
