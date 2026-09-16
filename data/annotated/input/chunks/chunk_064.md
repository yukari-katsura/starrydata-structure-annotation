# Host systems -- chunk 064 of 73

Ranks 3151-3200 by sample count. These 50 host systems cover 50 samples (0.10% of the TE set); cumulative through this chunk: 99.14%.

Assign each host system a structural prototype from `data/annotated/taxonomy/prototypes_seed_v3.json`, or propose a new one in `taxonomy/prototypes_proposed.jsonl` first. Append results to `data/annotated/annotations/family_assignments.jsonl`.

The hand-entered MaterialFamily labels are deliberately NOT shown here -- they are held out in `df_host_systems.parquet` to validate this classification later. Decide from the compositions.

A "seed hypothesis" line means the taxonomy already names this host under that prototype. Confirm it against the compositions rather than accepting it; two or more listed means the host is mixed and needs splitting per composition.

Evidence follows the project precedence. Your judgement about the thermoelectric chemistry decides the prototype. [ref 1] is TEDesignLab, ICSD-backed and thermoelectric-specific -- prefer it. [ref 2] is Materials Project. Within a formula, polymorphs are ranked by ICSD reference count and the top one is marked PRIMARY -- not by e_above_hull, which is unusable for layered chalcogenides in the 2019 dump (Sb2Te3 R-3m carries 26 ICSD refs at hull 1.02). A primary resting on fewer than 5 ICSD references is flagged weak; the ambient phase may simply be absent from the snapshot, as it is for Bi2Se3.

While you have the host in view, also record what each minor element DOES, in `dopant_roles` -- the role follows from the prototype and cannot be judged without it. A median host has 2 such elements. Not everything listed is a dopant: O, C, N and H are usually milling or pressing residue, and an element just under 5 at.% may be an alloying end member rather than dilute doping. The doping LEVEL is computed later from the parsed fractions -- do not work it out by hand here.

A polymorph list is NOT a thermal sequence. SnSe has three known structures but only Pnma -> Cmcm happens on heating; rocksalt SnSe is metastable (2 icsd refs against 32). Put thermally reached phases in `phases` with their transition temperatures, and everything else in `other_polymorphs` with an occurrence reason. hull and icsd counts are shown to help you tell them apart.

A host may need MORE THAN ONE prototype. Transport is measured across a wide window and many thermoelectrics transform inside it, so where a "MEASUREMENT CROSSES A TRANSITION" line appears, record each phase with its own temperature range in the `phases` field. Transition temperatures shown are approximate and composition-dependent.

Both references describe which phases EXIST in a chemistry, not which phase this paper made. Al-O-Zn is best attested as ZnAl2O4 spinel (227) while almost every sample in it is Al-doped wurtzite ZnO (186). Weigh them against the compositions; do not follow them blindly.

## Dy-Er-Gd-Ho-Nb-O-Sm
- rank 3151 | 1 samples | 1 papers | 1 compositions
- compositions: (Sm0.2Gd0.2Dy0.2Ho0.2Er0.2)3NbO7 (1)
- measured range: 298-1174 K (5th-95th pct of 1 curves)
- papers: Achieved limit thermal conductivity and enhancements of mechanical properties in fluorite RE3NbO7 via entropy engineering

## Dy-Er-Gd-O-Si-Y-Yb
- rank 3152 | 1 samples | 1 papers | 1 compositions
- compositions: (Yb0.2Er0.2Y0.2Dy0.2Gd0.2)2SiO5 (1)
- measured range: 300-1273 K (5th-95th pct of 1 curves)
- papers: Improved thermophysical properties of rare-earth monosilicates applied as environmental barrier coatings by adjusting structural distortion with RE-doping

## Dy-Er-Ho-Nb-O
- rank 3153 | 1 samples | 1 papers | 1 compositions
- compositions: (Dy0.33Ho0.33Er0.33)3NbO7 (1)
- measured range: 297-1174 K (5th-95th pct of 1 curves)
- papers: Achieved limit thermal conductivity and enhancements of mechanical properties in fluorite RE3NbO7 via entropy engineering

## Dy-Er-Ho-O-Si-Y-Yb
- rank 3154 | 1 samples | 1 papers | 1 compositions
- compositions: (Yb0.2Er0.2Ho0.2Y0.2Dy0.2)2SiO5 (1)
- measured range: 301-1273 K (5th-95th pct of 1 curves)
- papers: Improved thermophysical properties of rare-earth monosilicates applied as environmental barrier coatings by adjusting structural distortion with RE-doping

## Dy-Er-O-Si
- rank 3155 | 1 samples | 1 papers | 1 compositions
- compositions: DyErSiO5 (1)
- measured range: 293-293 K (5th-95th pct of 1 curves)
- papers: Tailoring thermal properties of multi-component rare earth monosilicates

## Dy-Eu-Gd-Ho-Nb-O
- rank 3156 | 1 samples | 1 papers | 1 compositions
- compositions: (Eu0.25Gd0.25Dy0.25Ho0.25)3NbO7 (1)
- measured range: 297-1173 K (5th-95th pct of 1 curves)
- papers: Achieved limit thermal conductivity and enhancements of mechanical properties in fluorite RE3NbO7 via entropy engineering

## Dy-Eu-O-Sm-Zr
- rank 3157 | 1 samples | 1 papers | 1 compositions
- compositions: (Sm0.33Eu0.33Dy0.33)2Zr2O7 (1)
- measured range: 297-1272 K (5th-95th pct of 1 curves)
- papers: Multicomponent high-entropy zirconates with comprehensive properties for advanced thermal barrier coating

## Dy-Ga
- rank 3158 | 1 samples | 1 papers | 1 compositions
- compositions: DyGa2 (1)
- measured range: 16-289 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): DyGa2 P6/mmm (191) mp-20064 [hull=0.000, icsd=8, PRIMARY]; DyGa Cmcm (63) mp-30604 [hull=0.000, icsd=7, PRIMARY]; DyGa3 P6_3/mmc (194) mp-865103 [hull=0.000, icsd=1, PRIMARY, AMBIGUOUS]; DyGa6 P4/nbm (125) mp-1104534 [hull=0.012, icsd=1, PRIMARY]; Dy3Ga Pm-3m (221) mp-984713 [hull=0.079, PRIMARY]
- papers: Thermoelectric power and resistivity studies in the Kondo-lattice system CeGa2with Sn or Al substitutions and RGa2(R identical to Ho,Dy,Tb) alloys

## Dy-Gd
- rank 3159 | 1 samples | 1 papers | 1 compositions
- compositions: Gd0.18Dy0.82 (1)
- measured range: 166-220 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Gd3Dy Pm-3m (221) mp-1184431 [hull=0.064, PRIMARY]; GdDy P-6m2 (187) mp-1224750 [hull=0.019, PRIMARY]
- papers: Thermal Property of Magnetic Materials for Hydrogen Magnetic Refrigeration and Effect of Magnetic Field on Them

## Dy-Ge-Ni
- rank 3160 | 1 samples | 1 papers | 1 compositions
- compositions: Dy2NiGe6 (1)
- measured range: 12-283 K (5th-95th pct of 2 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): DyNiGe2 Cmcm (63) mp-1078577 [hull=0.000, icsd=2, PRIMARY]; Dy(NiGe)2 I4/mmm (139) mp-21415 [hull=0.000, icsd=2, PRIMARY]; DyNiGe Pnma (62) mp-1102455 [hull=0.000, icsd=2, PRIMARY]; DyNiGe3 Cmmm (65) mp-1087478 [hull=0.000, icsd=1, PRIMARY]; Dy3Ni11Ge4 P6_3/mmc (194) mp-1213533 [hull=0.060, PRIMARY]
- papers: Electric transport in R2MGe6 ternary compounds (R=La, Ce, Gd, Tb, Dy, Ho; M=Mn, Ni, Cu)

## Dy-Ge-Pd
- rank 3161 | 1 samples | 1 papers | 1 compositions
- compositions: Dy2PdGe6 (1)
- measured range: 17-328 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): DyGePd Pmmn (59) mp-1190638 [hull=0.000, icsd=1, PRIMARY, AMBIGUOUS]; Dy(GePd)2 I4/mmm (139) mp-22180 [hull=0.000, icsd=1, PRIMARY]; Dy2Ge6Pd Cmce (64) mp-1202284 [hull=0.000, icsd=1, PRIMARY]; DyGePd2 Pnma (62) mp-1106158 [hull=0.000, icsd=1, PRIMARY]; DyGe2Pd Immm (71) mp-1212976 [hull=0.000, PRIMARY]
- papers: Physical properties of polycrystalline Dy2PdGe6 and La2PdGe6

## Dy-Ge-Ru
- rank 3162 | 1 samples | 1 papers | 1 compositions
- compositions: Dy3Ru4Ge13 (1)
- measured range: 17-804 K (5th-95th pct of 5 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Dy(GeRu)2 I4/mmm (139) mp-21082 [hull=0.000, icsd=2, PRIMARY]; DyGeRu Pnma (62) mp-19986 [hull=0.000, icsd=2, PRIMARY]; Dy3Ge13Ru4 Pm-3n (223) mp-1197267 [hull=0.025, icsd=1, PRIMARY]; Dy2Ge5Ru3 Ibam (72) mp-1105812 [hull=0.000, icsd=1, PRIMARY]; Dy3Ge3Ru2 Cmcm (63) mp-1189819 [hull=0.002, icsd=1, PRIMARY]
- papers: Thermoelectric properties of rare earth–ruthenium–germanium compounds

## Dy-Ge-Si
- rank 3163 | 1 samples | 1 papers | 1 compositions
- compositions: Dy5Si2Ge2 (1)
- measured range: 19-301 K (5th-95th pct of 1 curves)
- papers: Magnetic and electrical transport properties of DyxGd5−xSi2Ge2 (x=0.0, 1.5, 2.5, 3.0, 3.5, 4.5 and 5.0) compounds

## Dy-Ge-Sn
- rank 3164 | 1 samples | 1 papers | 1 compositions
- compositions: DySnGe (1)
- measured range: 11-197 K (5th-95th pct of 2 curves; full span incl. outliers 11-300 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): DySnGe Cmcm (63) mp-1080405 [hull=0.000, icsd=1, PRIMARY]
- papers: A comparative study of HoSn1.1Ge0.9 and DySn1.1Ge0.9 compounds using magnetic, magneto-thermal and magneto-transport measurements

## Dy-Ho-Pd-Sb
- rank 3165 | 1 samples | 1 papers | 1 compositions
- compositions: Ho0.75Dy0.25PdSb1.05 (1)
- measured range: 200-349 K (5th-95th pct of 2 curves)
- papers: Antimonides with the half-Heusler structure: New thermoelectric materials

## Dy-In
- rank 3166 | 1 samples | 1 papers | 1 compositions
- compositions: DyIn3 (1)
- measured range: 12-274 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): DyIn3 Pm-3m (221) mp-20236 [hull=0.000, icsd=6, PRIMARY]; Dy2In P6_3/mmc (194) mp-21351 [hull=0.000, icsd=3, PRIMARY]; DyIn Pm-3m (221) mp-257 [hull=0.000, icsd=2, PRIMARY]; Dy3In Pm-3m (221) mp-20786 [hull=0.000, icsd=1, PRIMARY]
- papers: Resistivity and thermopower of monocrystalline TbIn3 and DyIn3

## Dy-K-Mn-O
- rank 3167 | 1 samples | 1 papers | 1 compositions
- compositions: Dy0.7K0.3MnO3 (1)
- measured range: 138-300 K (5th-95th pct of 1 curves)
- papers: Effects of Dy sub lattice dilution on transport and magnetic properties in Dy1-xKxMnO3

## Dy-La-O-Sb
- rank 3168 | 1 samples | 1 papers | 1 compositions
- compositions: La1.5Dy1.5SbO3 (1)
- measured range: 15-396 K (5th-95th pct of 1 curves)
- papers: Synthesis, Crystal Structure, and Electronic Properties of the Tetragonal (REIREII)3SbO3Phases (REI= La, Ce; REII= Dy, Ho)

## Dy-Mg-Zn
- rank 3169 | 1 samples | 1 papers | 1 compositions
- compositions: Dy8.7Mg34.6Zn56.8_IQC (1)
- measured range: 12-297 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): DyMgZn2 Fm-3m (225) mp-865142 [hull=0.000, PRIMARY]
- papers: Growth of large-grain R-Mg-Zn quasicrystals from the ternary melt (R = Y, Er, Ho, Dy and Tb)

## Dy-Mn-Si
- rank 3170 | 1 samples | 1 papers | 1 compositions
- compositions: Dy2Mn3Si5 (1)
- measured range: 24-280 K (5th-95th pct of 2 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Dy(MnSi)2 I4/mmm (139) mp-4985 [hull=0.000, icsd=4, PRIMARY]; DyMnSi Pnma (62) mp-22101 [hull=0.048, icsd=1, PRIMARY]
- papers: Magnetism and electronic transport in R2Mn3Si5 (R=Dy, Ho and Er) compounds

## Dy-Mo-O-Y
- rank 3171 | 1 samples | 1 papers | 1 compositions
- compositions: (Dy0.6Y0.4)2Mo2O7 (1)
- measured range: 27-254 K (5th-95th pct of 1 curves)
- papers: Electrical conductivity and thermoelectric power of the compounds (DyxY1-x)2Mo2O7

## Dy-N
- rank 3172 | 1 samples | 1 papers | 1 compositions
- compositions: DyN (1)
- measured range: 300-1473 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): DyN Fm-3m (225) mp-1410 [hull=0.000, icsd=7, PRIMARY]; Dy2N3 Ia-3 (206) mp-1205065 [hull=0.798, icsd=1, PRIMARY]
- papers: Thermophysical properties of several nitrides prepared by spark plasma sintering

## Dy-N-Ti
- rank 3173 | 1 samples | 1 papers | 1 compositions
- compositions: Ti0.6Dy0.4N (1)
- measured range: 302-1474 K (5th-95th pct of 1 curves)
- papers: Thermophysical properties of several nitrides prepared by spark plasma sintering

## Dy-N-Zr
- rank 3174 | 1 samples | 1 papers | 1 compositions
- compositions: Zr0.6Dy0.4N (1)
- measured range: 300-1474 K (5th-95th pct of 1 curves)
- papers: Thermophysical properties of several nitrides prepared by spark plasma sintering

## Dy-Nb-O
- rank 3175 | 1 samples | 1 papers | 1 compositions
- compositions: Dy3NbO7 (1)
- measured range: 292-1271 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): DyNbO4 I4_1/a (88) mp-1095234 [hull=0.002, icsd=21, PRIMARY]; Dy2Nb2O7 Fd-3m (227) mp-754120 [hull=0.092, PRIMARY]; Dy3NbO7 P1 (1) mp-676951 [hull=0.068, PRIMARY]; DyNbO4 P2/c (13) mp-1178380 [hull=0.006]; DyNbO4 C2/m (12) mp-768227 [hull=0.072]
- papers: Diffused Lattice Vibration and Ultralow Thermal Conductivity in the Binary Ln–Nb–O Oxide System

## Dy-O-Sc
- rank 3176 | 1 samples | 1 papers | 1 compositions
- compositions: DyScO3 (1)
- measured range: 17-295 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): DyScO3 Pnma (62) mp-31120 [hull=0.026, icsd=1, PRIMARY]
- papers: Enhanced Thermoelectric Power Factor of NaxCoO2Thin Films by Structural Engineering

## Dy-O-Sc-Si
- rank 3177 | 1 samples | 1 papers | 1 compositions
- compositions: DyScSiO5 (1)
- measured range: 293-293 K (5th-95th pct of 1 curves)
- papers: Tailoring thermal properties of multi-component rare earth monosilicates

## Dy-O-Si
- rank 3178 | 1 samples | 1 papers | 1 compositions
- compositions: Dy2SiO5 (1)
- measured range: 293-293 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Dy2Si2O7 P-1 (2) mp-17062 [hull=0.003, icsd=2, PRIMARY]; Dy2SiO5 C2/c (15) mp-768317 [hull=0.000, PRIMARY]; Dy5Si2BO13 Pm (6) mp-1225574 [hull=0.025, PRIMARY]; Dy2Si2O7 P1 (1) mp-1225780 [hull=0.004]; Dy2SiO5 P2_1/c (14) mp-752405 [hull=0.022]
- papers: Tailoring thermal properties of multi-component rare earth monosilicates

## Dy-O-Sr-Ti
- rank 3179 | 1 samples | 1 papers | 1 compositions
- compositions: Sr0.90Dy1.00TiO3 (1)
- measured range: 373-968 K (5th-95th pct of 3 curves)
- papers: Thermoelectric Properties of Dy-Doped SrTiO3 Ceramics

## Dy-O-U
- rank 3180 | 1 samples | 1 papers | 1 compositions
- compositions: (U0.8Dy0.2)O2 (1)
- measured range: 376-1471 K (5th-95th pct of 1 curves)
- papers: Variation of the thermal conductivity of (U,Dy)O2 solid solutions as a function of the Dy content

## Dy-Se-Sn
- rank 3181 | 1 samples | 1 papers | 1 compositions
- compositions: DySnSe2 (1)
- measured range: 346-674 K (5th-95th pct of 1 curves)
- papers: Phase relations and properties of alloys in the SnSe-DySe system

## Er
- rank 3182 | 1 samples | 1 papers | 1 compositions
- compositions: Er (1)
- measured range: 323-673 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Er P6_3/mmc (194) mp-99 [hull=0.000, icsd=7, PRIMARY]; Er Fm-3m (225) mp-10752 [hull=0.028, icsd=1]; Er Im-3m (229) mp-10753 [hull=0.141, icsd=1]; Er R-3m (166) mp-1184115 [hull=0.005]
- papers: Phase State and Thermal and Mechanical Properties of Zr-Er Alloys

## Er-Gd-Lu-O-Si-Y
- rank 3183 | 1 samples | 1 papers | 1 compositions
- compositions: (Lu0.2Y0.2Er0.2Y0.2Gd0.2)2SiO5 (1)
- measured range: 300-1273 K (5th-95th pct of 1 curves)
- papers: Improved thermophysical properties of rare-earth monosilicates applied as environmental barrier coatings by adjusting structural distortion with RE-doping

## Er-H-Pd-Sb-Y
- rank 3184 | 1 samples | 1 papers | 1 compositions
- compositions: Er0.25DY0.75Pd1.02Sb (1)
- measured range: 20-350 K (5th-95th pct of 3 curves)
- papers: Antimonides with the half-Heusler structure: New thermoelectric materials

## Er-Ho-Lu-O-Si-Y
- rank 3185 | 1 samples | 1 papers | 1 compositions
- compositions: (Lu0.2Y0.2Er0.2Ho0.2Y0.2)2SiO5 (1)
- measured range: 300-1273 K (5th-95th pct of 1 curves)
- papers: Improved thermophysical properties of rare-earth monosilicates applied as environmental barrier coatings by adjusting structural distortion with RE-doping

## Er-Ho-Pd-Sb
- rank 3186 | 1 samples | 1 papers | 1 compositions
- compositions: Ho0.50Er0.50PdSb1.05 (1)
- measured range: 19-349 K (5th-95th pct of 3 curves)
- papers: Antimonides with the half-Heusler structure: New thermoelectric materials

## Er-In
- rank 3187 | 1 samples | 1 papers | 1 compositions
- compositions: ErIn3 (1)
- measured range: 11-48 K (5th-95th pct of 2 curves; full span incl. outliers 11-293 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): ErIn3 Pm-3m (221) mp-1291 [hull=0.000, icsd=5, PRIMARY]; Er2In P6_3/mmc (194) mp-877 [hull=0.000, icsd=3, PRIMARY]; Er5In3 P6_3/mcm (193) mp-1189039 [hull=0.021, icsd=1, PRIMARY]; Er3In5 Cmcm (63) mp-1106153 [hull=0.000, icsd=1, PRIMARY]; ErIn Pm-3m (221) mp-11370 [hull=0.000, icsd=1, PRIMARY]
- papers: Thermoelectric power of the REIn3 single crystals where RE = La, Ce, Pr, Nd, Sm, Gd, Ho, ErIn3, TmandLu

## Er-La-O-Ru-Sr
- rank 3188 | 1 samples | 1 papers | 1 compositions
- compositions: (Sr0.7La0.3)2ErRuO6 (1)
- measured range: 193-782 K (5th-95th pct of 2 curves)
- papers: High-temperature thermoelectric properties of the double-perovskite ruthenium oxide (Sr1−xLax)2ErRuO6

## Er-Mg-Zn
- rank 3189 | 1 samples | 1 papers | 1 compositions
- compositions: Er8.7Mg34.6Zn56.8_IQC (1)
- measured range: 11-298 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): ErMgZn2 Fm-3m (225) mp-977433 [hull=0.000, PRIMARY]
- papers: Growth of large-grain R-Mg-Zn quasicrystals from the ternary melt (R = Y, Er, Ho, Dy and Tb)

## Er-Mn-Si
- rank 3190 | 1 samples | 1 papers | 1 compositions
- compositions: Er2Mn3Si5 (1)
- measured range: 25-290 K (5th-95th pct of 2 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Er(MnSi)2 I4/mmm (139) mp-4729 [hull=0.000, icsd=7, PRIMARY]; Er2Mn3Si5 P4/mnc (128) mp-622190 [hull=0.000, icsd=3, PRIMARY]; ErMnSi Pnma (62) mp-19738 [hull=0.036, icsd=1, PRIMARY]; ErMnSi2 Cmcm (63) mp-1206071 [hull=0.185, PRIMARY]
- papers: Magnetism and electronic transport in R2Mn3Si5 (R=Dy, Ho and Er) compounds

## Er-Mo-Nd-O
- rank 3191 | 1 samples | 1 papers | 1 compositions
- compositions: (Nd0.6Er0.4)2MoO7 (1)
- measured range: 87-267 K (5th-95th pct of 1 curves)
- papers: Thermoelectric power of RE2Mo2O7 pyrochlores

## Er-Nb-O
- rank 3192 | 1 samples | 1 papers | 1 compositions
- compositions: Er3NbO7 (1)
- measured range: 294-1271 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): ErNbO4 C2/c (15) mp-5370 [hull=0.000, icsd=2, PRIMARY]; Er2Nb2O7 Fd-3m (227) mp-756393 [hull=0.094, PRIMARY]; ErNbO2 I4_1/amd (141) mp-1213215 [hull=0.650, PRIMARY]; ErNbO4 P2/c (13) mp-756457 [hull=0.024]
- papers: Diffused Lattice Vibration and Ultralow Thermal Conductivity in the Binary Ln–Nb–O Oxide System

## Er-Nb-S
- rank 3193 | 1 samples | 1 papers | 1 compositions
- compositions: (Er2S2)2NbS2 (1)
- measured range: 12-299 K (5th-95th pct of 1 curves)
- papers: Crystal Structure and Thermoelectric Properties of Misfit-Layered Sulfides [Ln2S2] p NbS2 (Ln = Lanthanides)

## Er-O
- rank 3194 | 1 samples | 1 papers | 1 compositions
- compositions: Er2O3 (1)
- measured range: 293-573 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Er2O3 Ia-3 (206) mp-679 [hull=0.000, icsd=19, PRIMARY]; ErO P6_3/mmc (194) mp-1184211 [hull=0.251, PRIMARY]; ErO2 P2_1/m (11) mp-1206338 [hull=0.178, PRIMARY]; ErO3 P6_3/m (176) mp-1025483 [hull=0.451, PRIMARY]; Er2O3 C2/m (12) mp-2460 [hull=0.048, icsd=2]
- papers: Phase State and Thermal and Mechanical Properties of Zr-Er Alloys

## Er-O-Si
- rank 3195 | 1 samples | 1 papers | 1 compositions
- compositions: Er2SiO5 (1)
- measured range: 293-293 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Er2Si2O7 C2/m (12) mp-7064 [hull=0.000, icsd=3, PRIMARY]; BaEr4Si5O17 P2_1/m (11) mp-1195598 [hull=0.000, icsd=1, PRIMARY]; Er2SiO5 P2_1/c (14) mp-16993 [hull=0.025, icsd=1, PRIMARY]; Er2Si2O7 P2_1/c (14) mp-7624 [hull=0.003, icsd=1]
- papers: Tailoring thermal properties of multi-component rare earth monosilicates

## Er-O-Si-Yb
- rank 3196 | 1 samples | 1 papers | 1 compositions
- compositions: YbErSiO5 (1)
- measured range: 293-293 K (5th-95th pct of 1 curves)
- papers: Tailoring thermal properties of multi-component rare earth monosilicates

## Er-Sb-Zn
- rank 3197 | 1 samples | 1 papers | 1 compositions
- compositions: (Zn0.7Er0.3)4Sb3 (1)
- measured range: 301-674 K (5th-95th pct of 2 curves)
- papers: Dislocation-induced ultra-low lattice thermal conductivity in rare earth doped β-Zn4Sb3

## Er-Te
- rank 3198 | 1 samples | 1 papers | 1 compositions
- compositions: Er2Te3 (1)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): ErTe Fm-3m (225) mp-1280 [hull=0.000, icsd=3, PRIMARY]; Er2Te3 Fddd (70) mp-14643 [hull=0.000, icsd=2, PRIMARY]; ErTe3 Cmcm (63) mp-1078991 [hull=0.000, icsd=2, PRIMARY]; ErTe2 P4/nmm (129) mp-1018692 [hull=0.064, icsd=1, PRIMARY]; ErTe P4/mmm (123) mp-1225436 [hull=1.203]
- papers: Thermoelectric and Electrical Measurements in the Erbium‐Tellurium System

## Eu-F-O-Sb-Ti
- rank 3199 | 1 samples | 1 papers | 1 compositions
- compositions: (EuF)2Ti2Sb2O (1)
- measured range: 11-298 K (5th-95th pct of 1 curves)
- papers: Structure and Physical Properties of the Layered Titanium-Based Pnictide Oxides (EuF)<sub>2</sub>Ti<sub>2</sub>Pn<sub>2</sub>O (Pn = Sb, Bi)

## Eu-Fe-Sb
- rank 3200 | 1 samples | 1 papers | 1 compositions
- compositions: EuFe4Sb12 (1)
- measured range: 299-803 K (5th-95th pct of 5 curves)
- papers: High-temperature electrical and thermal transport properties of fully filled skutterudites RFe4Sb12 (R = Ca, Sr, Ba, La, Ce, Pr, Nd, Eu, and Yb)
