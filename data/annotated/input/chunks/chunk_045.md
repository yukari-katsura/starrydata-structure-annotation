# Host systems -- chunk 045 of 73

Ranks 2201-2250 by sample count. These 50 host systems cover 100 samples (0.19% of the TE set); cumulative through this chunk: 97.07%.

Assign each host system a structural prototype from `data/annotated/taxonomy/prototypes_seed_v3.json`, or propose a new one in `taxonomy/prototypes_proposed.jsonl` first. Append results to `data/annotated/annotations/family_assignments.jsonl`.

The hand-entered MaterialFamily labels are deliberately NOT shown here -- they are held out in `df_host_systems.parquet` to validate this classification later. Decide from the compositions.

A "seed hypothesis" line means the taxonomy already names this host under that prototype. Confirm it against the compositions rather than accepting it; two or more listed means the host is mixed and needs splitting per composition.

Evidence follows the project precedence. Your judgement about the thermoelectric chemistry decides the prototype. [ref 1] is TEDesignLab, ICSD-backed and thermoelectric-specific -- prefer it. [ref 2] is Materials Project. Within a formula, polymorphs are ranked by ICSD reference count and the top one is marked PRIMARY -- not by e_above_hull, which is unusable for layered chalcogenides in the 2019 dump (Sb2Te3 R-3m carries 26 ICSD refs at hull 1.02). A primary resting on fewer than 5 ICSD references is flagged weak; the ambient phase may simply be absent from the snapshot, as it is for Bi2Se3.

While you have the host in view, also record what each minor element DOES, in `dopant_roles` -- the role follows from the prototype and cannot be judged without it. A median host has 2 such elements. Not everything listed is a dopant: O, C, N and H are usually milling or pressing residue, and an element just under 5 at.% may be an alloying end member rather than dilute doping. The doping LEVEL is computed later from the parsed fractions -- do not work it out by hand here.

A polymorph list is NOT a thermal sequence. SnSe has three known structures but only Pnma -> Cmcm happens on heating; rocksalt SnSe is metastable (2 icsd refs against 32). Put thermally reached phases in `phases` with their transition temperatures, and everything else in `other_polymorphs` with an occurrence reason. hull and icsd counts are shown to help you tell them apart.

A host may need MORE THAN ONE prototype. Transport is measured across a wide window and many thermoelectrics transform inside it, so where a "MEASUREMENT CROSSES A TRANSITION" line appears, record each phase with its own temperature range in the `phases` field. Transition temperatures shown are approximate and composition-dependent.

Both references describe which phases EXIST in a chemistry, not which phase this paper made. Al-O-Zn is best attested as ZnAl2O4 spinel (227) while almost every sample in it is Al-doped wurtzite ZnO (186). Weigh them against the compositions; do not follow them blindly.

## Fe-Hf-Nb-Sb
- rank 2201 | 2 samples | 2 papers | 2 compositions
- compositions: Fe0.89Nb1.10Hf0.16Sb1.00 (1); FeNb0.8Hf0.2Sb (1)
- measured range: 300-1061 K (5th-95th pct of 6 curves)
- papers: https://doi.org/10.2320/matertrans.e-m2018806 (Thermoelectric Properties of <i>p</i>-Type Half-Heusler Compounds FeNb...) | https://doi.org/10.1016/j.ensm.2017.07.014 (Enhancing thermoelectric performance of FeNbSb half-Heusler compound b...)

## Fe-Hf-Sb
- rank 2202 | 2 samples | 2 papers | 2 compositions
- compositions: HfFe4Sb12 (1); Hf6FeSb2 (1)
- measured range: 10-300 K (5th-95th pct of 5 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Hf20(FeSb3)3 C222 (21) mp-1224612 [hull=0.024, PRIMARY]; Hf5FeSb2 I4/mcm (140) mp-1212486 [hull=0.024, PRIMARY]; Hf6FeSb2 P-62m (189) mp-1206135 [hull=0.000, PRIMARY]; HfFeSb Pnma (62) mp-1212435 [hull=0.056, PRIMARY]
- papers: https://doi.org/10.1063/1.1854747 (Synthesis and transport properties of HfFe4Sb12) | https://doi.org/10.1016/s0925-8388(99)00537-x (Thermoelectric properties of ternary transition metal antimonides)

## Fe-Mn-Mo-O-Sr
- rank 2203 | 2 samples | 1 papers | 1 compositions
- compositions: SrFe0.5Mn0.25Mo0.25O3 (2)
- measured range: 311-887 K (5th-95th pct of 2 curves; full span incl. outliers 311-1085 K)
- papers: https://doi.org/10.1149/2.0981509jes (Carbon Deposition and Sulfur Poisoning in SrFe<sub>0.75</sub>Mo<sub>0....)

## Fe-Nb-O-Ti
- rank 2204 | 2 samples | 1 papers | 1 compositions
- compositions: FeTiNbO6 (2)
- measured range: 346-857 K (5th-95th pct of 2 curves; full span incl. outliers 346-899 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): TiNbFeO6 P4_2nm (102) mp-1216798 [hull=0.040, PRIMARY]
- papers: https://doi.org/10.1007/s10832-012-9765-9 (Electrical properties of rutile-type FeTiMO6 (M = Ta,Nb))

## Fe-Nd-O-Se
- rank 2205 | 2 samples | 1 papers | 2 compositions
- compositions: Nd2Fe2Se2O3 (1); Nd2(Fe0.875Mn0.125)2Se2O3 (1)
- dopant candidates (<5% at.): Mn (1)
- measured range: 70-323 K (5th-95th pct of 6 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Nd2Fe2Se2O3 I4/mmm (139) mp-1078182 [hull=0.000, icsd=4, PRIMARY]
- papers: https://doi.org/10.1016/j.jallcom.2014.08.145 (Synthesis, structure and properties of new layered oxyselenides Nd2(Fe...)

## Fe-Ni-O-Zn
- rank 2206 | 2 samples | 1 papers | 2 compositions
- compositions: Ni0.6Zn0.4Fe2O4 (1); Ni0.4Zn0.6Fe2O4 (1)
- measured range: 306-745 K (5th-95th pct of 2 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Zn3Fe16Ni5O32 P1 (1) mp-1199236 [hull=0.270, icsd=1, PRIMARY]; ZnFe16Ni7O32 P1 (1) mp-1198303 [hull=0.233, icsd=1, PRIMARY]; ZnFe4NiO8 Cm (8) mp-1201822 [hull=0.231, icsd=1, PRIMARY]; ZnFe8Ni3O16 Cm (8) mp-1203466 [hull=0.317, icsd=1, PRIMARY]; ZnFe4NiO8 R3m (160) mp-1215703 [hull=0.013]
- papers: https://doi.org/10.1016/s0167-577x(00)00016-1 (Thermoelectric power studies of zinc-substituted nickel ferrites)

## Fe-Ni-Sb-Sn-Ti
- rank 2207 | 2 samples | 1 papers | 2 compositions
- compositions: Ti2FeNiSb1.6Sn0.4 (1); Ti2FeNiSb1.5Sn0.5 (1)
- measured range: 299-975 K (5th-95th pct of 10 curves)
- papers: https://doi.org/10.1002/pssa.202000096 (Enhanced Thermoelectric Properties in p‐Type Double Half‐Heusler Ti<su...)

## Fe-O-Ta-Ti
- rank 2208 | 2 samples | 1 papers | 1 compositions
- compositions: FeTiTaO6 (2)
- measured range: 538-881 K (5th-95th pct of 2 curves; full span incl. outliers 538-930 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): TaTiFeO6 P4_2nm (102) mp-1217927 [hull=0.024, PRIMARY]
- papers: https://doi.org/10.1007/s10832-012-9765-9 (Electrical properties of rutile-type FeTiMO6 (M = Ta,Nb))

## Fe-O-Zr
- rank 2209 | 2 samples | 1 papers | 2 compositions
- compositions: (Y0.06Zr0.97O2.03)79.6(Ni0.08Cr0.18Fe0.76)19.9 (1); (Y0.06Zr0.97O2.03)59.1(Ni0.08Cr0.18Fe0.76)39.4 (1)
- dopant candidates (<5% at.): Y (2), Cr (2), Ni (2)
- measured range: 65-1366 K (5th-95th pct of 4 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Zr6Fe2O C2/m (12) mp-1215351 [hull=0.366, PRIMARY]
- papers: https://doi.org/10.2355/tetsutohagane1955.82.9_789 (Thermal Conductivities of SUS304/PSZ Composite Materials)

## Fe-Pb-S-Sb
- rank 2210 | 2 samples | 1 papers | 2 compositions
- compositions: Co0.08Fe0.92FePb4Sb6S14 (1); Co0.12Fe0.88FePb4Sb6S14 (1)
- dopant candidates (<5% at.): Co (2)
- measured range: 166-290 K (5th-95th pct of 2 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): FeSb6(Pb2S7)2 P2_1/c (14) mp-22369 [hull=0.042, icsd=4, PRIMARY]
- papers: https://doi.org/10.1016/j.jallcom.2004.08.041 (Electronic structure and thermoelectric properties of the thioantimona...)

## Fe-Sn-U
- rank 2211 | 2 samples | 1 papers | 1 compositions
- compositions: U2Fe2Sn (2)
- measured range: 15-237 K (5th-95th pct of 2 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): U2Fe2Sn P4/mbm (127) mp-21357 [hull=0.000, icsd=2, PRIMARY]; UFe5Sn Pnma (62) mp-21701 [hull=0.063, icsd=1, PRIMARY]
- papers: https://doi.org/10.1016/0921-4526(96)00234-7 (Low-temperature transport properties of U2Rh2Sn and U2Fe2Sn)

## Fe-Zn
- rank 2212 | 2 samples | 1 papers | 2 compositions
- compositions: YFe2Zn20 (1); YbFe2Zn20 (1)
- dopant candidates (<5% at.): Y (1), Yb (1)
- measured range: 11-300 K (5th-95th pct of 2 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Zn13Fe C2/m (12) mp-1722 [hull=0.000, icsd=3, PRIMARY]; Tb(Zn10Fe)2 Fd-3m (227) mp-12817 [hull=0.000, icsd=1, PRIMARY]; U(Zn10Fe)2 Fd-3m (227) mp-1197936 [hull=0.000, icsd=1, PRIMARY]; Zr(Zn10Fe)2 Fd-3m (227) mp-1195553 [hull=0.000, icsd=1, PRIMARY]; Zn10Fe3 Fmm2 (42) mp-1215735 [hull=0.000, PRIMARY]
- papers: https://doi.org/10.1103/physrevb.86.115110 (Thermoelectric power of the YbT2Zn20(T=Fe, Ru, Os, Ir, Rh, and Co) hea...)

## Ga-Gd-Ni
- rank 2213 | 2 samples | 1 papers | 2 compositions
- compositions: GdNi0.6Ga3.4 (1); GdNiGa3 (1)
- measured range: 13-298 K (5th-95th pct of 2 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Gd3(GaNi3)2 Im-3m (229) mp-1191116 [hull=0.000, icsd=1, PRIMARY]
- papers: https://doi.org/10.12693/aphyspola.127.382 (Magnetic and Electronic Properties in Series of GdTxGa4-xSolid Solutio...)

## Ga-Gd-O-Sr
- rank 2214 | 2 samples | 1 papers | 1 compositions
- compositions: ((Nd)0.01(SrGd)0.99)Ga3O7 (2)
- dopant candidates (<5% at.): Nd (2)
- measured range: 303-561 K (5th-95th pct of 2 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Sr2GdGaO5 Fmmm (69) mp-1218806 [hull=0.059, PRIMARY]
- papers: https://doi.org/10.1063/1.3483955 (Synthesis, growth, and characterization of Nd-doped SrGdGa3O7 crystal)

## Ga-Ge-Si-Sr
- rank 2215 | 2 samples | 2 papers | 1 compositions
- compositions: Sr7.57Ga15.65Si3.72Ge27.06 (2)
- measured range: 19-301 K (5th-95th pct of 4 curves)
- papers: https://doi.org/10.1109/ict.2005.1519928 (Thermoelectric properties of Ba-filled Si-Ge alloy type I semiconducti...) | https://doi.org/10.1063/1.2171775 (Structural and transport properties of Ba8Ga16SixGe30−x clathrates)

## Ga-La
- rank 2216 | 2 samples | 1 papers | 1 compositions
- compositions: LaGa2 (2)
- measured range: 15-249 K (5th-95th pct of 2 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): LaGa2 P6/mmm (191) mp-19839 [hull=0.000, icsd=6, PRIMARY]; LaGa6 P4/nbm (125) mp-644739 [hull=0.000, icsd=4, PRIMARY]; LaGa Cmcm (63) mp-1002133 [hull=0.000, icsd=3, PRIMARY]; La3Ga Pm-3m (221) mp-20487 [hull=0.053, icsd=2, PRIMARY]; La5Ga3 P4/ncc (130) mp-672217 [hull=0.000, icsd=1, PRIMARY]
- papers: https://doi.org/10.1016/0921-4526(93)90665-s (Transport properties of RGa2 (R=La, Ce and Sm))

## Ga-La-Ni
- rank 2217 | 2 samples | 1 papers | 2 compositions
- compositions: La(Ni0.9Ga0.1)5 (1); La(Ni0.865Ga0.135)5 (1)
- measured range: 16-883 K (5th-95th pct of 4 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): LaGa2Ni Cmmm (65) mp-1079217 [hull=0.000, icsd=2, PRIMARY]; LaGaNi P2_1/c (14) mp-1102982 [hull=0.000, icsd=1, PRIMARY]; La2Ga10Ni I4/mmm (139) mp-1104497 [hull=0.004, icsd=1, PRIMARY]; La2Ga12Ni P4/nbm (125) mp-604613 [hull=0.000, icsd=1, PRIMARY]; La3(GaNi)2 Pbcm (57) mp-21529 [hull=0.000, icsd=1, PRIMARY]
- papers: https://doi.org/10.1016/s0925-8388(01)01007-6 (Dependence of the CeNi5 thermoelectric power on strong 4f-electron ins...)

## Ga-Re-Te
- rank 2218 | 2 samples | 1 papers | 2 compositions
- compositions: Re6Ga2Te15 (1); Re6Ga1.5Te15 (1)
- measured range: 92-317 K (5th-95th pct of 2 curves)
- papers: https://doi.org/10.1016/j.matchemphys.2009.08.061 (Thermoelectric properties of Re6GaxSeyTe15−y (0≤x≤2; 0≤y≤7.5))

## Ga-Se
- rank 2219 | 2 samples | 1 papers | 1 compositions
- compositions: Ga2Se3 (2)
- measured range: 320-672 K (5th-95th pct of 2 curves)
- [ref 1] TEDesignLab / ICSD: Ga2Se3 Cc (9) mp-1340 [hull=0.000, icsd=6, PRIMARY]; GaSe R3m (160) mp-11342 [hull=0.000, icsd=1]; GaSe (186)
- [ref 2] MP, ranked by ICSD evidence: GaSe P6_3/mmc (194) mp-1943 [hull=0.000, icsd=5, PRIMARY, AMBIGUOUS]; GaSe2 I-43m (217) mp-680721 [hull=0.304, icsd=2, PRIMARY]; Ga3Se Pm-3m (221) mp-1184214 [hull=0.250, PRIMARY]; GaSe P-6m2 (187) mp-1572 [hull=0.000, icsd=6]; Ga2Se3 Imm2 (44) mp-1224809 [hull=0.009]
- papers: https://doi.org/10.1007/s11664-010-1479-7 (Effect of Vacancy Distribution on the Thermal Conductivity of Ga2Te3 a...)

## Ga-Si-Sr
- rank 2220 | 2 samples | 2 papers | 2 compositions
- compositions: Sr8Al0Ga16Si30 (1); Sr8Ga16Si30 (1)
- measured range: 10-130 K (5th-95th pct of 2 curves; full span incl. outliers 10-767 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Sr2GaSi Amm2 (38) mp-1218812 [hull=0.000, PRIMARY]; Sr4GaSi3 Pmm2 (25) mp-1218379 [hull=0.000, PRIMARY]; SrGaSi P-6m2 (187) mp-1218262 [hull=0.000, PRIMARY]
- papers: https://doi.org/10.1143/apex.1.031201 (Synthesis and Thermoelectric Properties of Silicon Clathrates Sr8AlxGa...) | https://doi.org/10.1063/1.4983817 (High-temperature thermal conductivity of thermoelectric clathrates)

## Ga-Te-Tl
- rank 2221 | 2 samples | 2 papers | 2 compositions
- compositions: TlGaTe2 (1); TlIn0.1Ga0.9Te2 (1)
- dopant candidates (<5% at.): In (1)
- measured range: 293-869 K (5th-95th pct of 6 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): TlGaTe2 I4/mcm (140) mp-3785 [hull=0.000, icsd=6, PRIMARY]
- papers: https://doi.org/10.1063/1.2987471 (Systematic investigation of the thermoelectric properties of TlMTe[sub...) | https://doi.org/10.1134/s002016851007006x (X-ray diffraction characterization and electrical properties of TlIn1 ...)

## Gd-Ir-O
- rank 2222 | 2 samples | 1 papers | 2 compositions
- compositions: Bi0.5Gd1.5Ir2O7 (1); Gd2Ir2O7 (1)
- dopant candidates (<5% at.): Bi (1)
- measured range: 11-297 K (5th-95th pct of 2 curves)
- papers: https://doi.org/10.1007/s10948-019-05418-9 (Magnetic and Electrical Behavior of Gd Doping Pyrochlore Bi2Ir2O7)

## Gd-Mo-O
- rank 2223 | 2 samples | 2 papers | 1 compositions
- compositions: Gd2Mo2O7 (2)
- measured range: 13-287 K (5th-95th pct of 2 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Gd2Mo2O7 Fd-3m (227) mp-642754 [hull=0.000, icsd=5, PRIMARY]; Gd2(MoO4)3 Pba2 (32) mp-650449 [hull=0.000, icsd=1, PRIMARY, AMBIGUOUS]; Gd6Mo10O39 C2/c (15) mp-1195215 [hull=0.024, icsd=1, PRIMARY]; Gd2Mo5O18 Pbcn (60) mp-704238 [hull=0.008, icsd=1, PRIMARY]; Gd4Mo4O11 Pbam (55) mp-1200768 [hull=0.164, icsd=1, PRIMARY]
- papers: https://doi.org/10.1016/0022-3697(86)90030-2 (Thermoelectric power of RE2Mo2O7 pyrochlores) | https://doi.org/10.1016/0025-5408(80)90094-x (Electrical properties of Ln2Mo2O7 pyrochlores (Ln=SmYb,Y))

## Gd-N
- rank 2224 | 2 samples | 1 papers | 1 compositions
- compositions: GdN (2)
- measured range: 299-1273 K (5th-95th pct of 2 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): GdN Fm-3m (225) mp-940 [hull=0.000, icsd=11, PRIMARY]
- papers: https://doi.org/10.1016/j.jnucmat.2021.152785 (Thermal conductivity of gadolinium added uranium mononitride fuel pell...)

## Gd-N-O-U
- rank 2225 | 2 samples | 1 papers | 2 compositions
- compositions: (Gd2O3)7.17(UN)92.83 (1); (Gd2O3)10.93(UN)89.07 (1)
- measured range: 300-1275 K (5th-95th pct of 2 curves)
- papers: https://doi.org/10.1016/j.jnucmat.2021.152785 (Thermal conductivity of gadolinium added uranium mononitride fuel pell...)

## Gd-O-Sr-Ti
- rank 2226 | 2 samples | 1 papers | 2 compositions
- compositions: Gd0.285Sr0.715TiO3 (1); Gd0.560Sr0.440TiO3 (1)
- measured range: 10-300 K (5th-95th pct of 2 curves)
- papers: https://doi.org/10.1016/j.tsf.2015.03.065 (Metal–insulator transitions in epitaxial Gd1−Sr TiO3 thin films grown ...)

## Gd-O-Ta
- rank 2227 | 2 samples | 2 papers | 2 compositions
- compositions: GdTa3O9 (1); GdTaO4 (1)
- measured range: 373-1073 K (5th-95th pct of 2 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): GdTaO4 P2/c (13) mp-4875 [hull=0.000, icsd=3, PRIMARY]; Gd3TaO7 P-1 (2) mp-779424 [hull=0.000, PRIMARY, AMBIGUOUS]; GdTa3O9 P2_1/m (11) mp-770998 [hull=0.000, PRIMARY]; GdTa4O12 Amm2 (38) mp-1224653 [hull=0.054, PRIMARY]; GdTa7O19 P-6c2 (188) mp-770124 [hull=0.001, PRIMARY]
- papers: https://doi.org/10.1016/j.actamat.2021.117152 (Spontaneously formed nanostructures in double perovskite rare-earth ta...) | https://doi.org/10.1002/adma.201808222 (Diffused Lattice Vibration and Ultralow Thermal Conductivity in the Bi...)

## Gd-O-V
- rank 2228 | 2 samples | 1 papers | 1 compositions
- compositions: (Nd)0.05(Lu0.14Gd0.86)0.95VO4 (2)
- dopant candidates (<5% at.): Lu (2), Nd (2)
- measured range: 302-553 K (5th-95th pct of 2 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): GdVO4 I4_1/amd (141) mp-25140 [hull=0.000, icsd=7, PRIMARY]; GdVO3 Pnma (62) mp-615979 [hull=0.015, icsd=1, PRIMARY]; Gd3YV4O16 C222 (21) mp-1224710 [hull=0.000, PRIMARY]; Gd2V2O7 Fd-3m (227) mp-773164 [hull=0.025, PRIMARY]; Gd2V2O7 P-1 (2) mp-769861 [hull=0.071]
- papers: https://doi.org/10.1063/1.2743876 (Characterization of mixed Nd:LuxGd1−xVO4 laser crystals)

## Gd-Pd-Sb
- rank 2229 | 2 samples | 2 papers | 1 compositions
- compositions: GdPdSb (2)
- measured range: 296-922 K (5th-95th pct of 3 curves; full span incl. outliers 296-967 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): GdSbPd P6_3mc (186) mp-21061 [hull=0.000, icsd=1, PRIMARY]
- papers: https://doi.org/10.1063/1.2339886 (LnPdSb (Ln=La,Gd): Promising intermetallics with large carrier mobilit...) | https://doi.org/10.1063/1.2756045 (High-temperature Hall measurements of lanthanide based ternary interme...)

## Ge-I-Sb
- rank 2230 | 2 samples | 2 papers | 1 compositions
- compositions: Ge38Sb8I8 (2)
- measured range: 294-528 K (5th-95th pct of 2 curves; full span incl. outliers 294-756 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ge19(SbI)4 P-43n (218) mp-1212622 [hull=0.028, PRIMARY]
- papers: https://doi.org/10.1063/1.2209207 (Preparation and thermoelectric properties of sintered iodine-containin...) | https://doi.org/10.1063/1.2364473 (Synthesis and thermoelectric properties of type-I clathrate Ge30P16Te8)

## Ge-Ir-Lu-Yb
- rank 2231 | 2 samples | 1 papers | 2 compositions
- compositions: (Yb0.4Lu0.6)3Ir4Ge13 (1); (Yb0.6Lu0.4)3Ir4Ge13 (1)
- measured range: 13-124 K (5th-95th pct of 2 curves)
- papers: https://doi.org/10.1103/physrevb.99.085120 (Low-carrier density and fragile magnetism in a Kondo lattice system)

## Ge-Ir-Sb
- rank 2232 | 2 samples | 1 papers | 1 compositions
- compositions: La0.3Ir4Ge0.9Sb11.1 (2)
- dopant candidates (<5% at.): La (2)
- measured range: 298-954 K (5th-95th pct of 1 curves)
- papers: https://doi.org/10.1007/s11664-004-0117-7 (Effect of partial la filling on high-temperature thermoelectric proper...)

## Ge-Ir-Yb
- rank 2233 | 2 samples | 1 papers | 1 compositions
- compositions: Yb3Ir4Ge13 (2)
- measured range: 10-77 K (5th-95th pct of 2 curves; full span incl. outliers 10-298 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Yb4Ge6Ir7 Im-3m (229) mp-17578 [hull=0.000, icsd=2, PRIMARY]; Yb2Ge2Ir C2/m (12) mp-10998 [hull=0.000, icsd=1, PRIMARY]; Yb3Ge13Ir4 Pm-3n (223) mp-1195984 [hull=0.000, icsd=1, PRIMARY]; Yb5(Ge5Ir2)2 P4/mbm (127) mp-1199005 [hull=0.000, icsd=1, PRIMARY]
- papers: https://doi.org/10.1103/physrevb.99.085120 (Low-carrier density and fragile magnetism in a Kondo lattice system)

## Ge-K-Zn
- rank 2234 | 2 samples | 1 papers | 2 compositions
- compositions: K8Zn4Ge42 (1); K6Ba2Zn5Ge41 (1)
- dopant candidates (<5% at.): Ba (1)
- measured range: 93-1014 K (5th-95th pct of 10 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): K14ZnGe16 Pmn2_1 (31) mp-1195294 [hull=0.000, icsd=1, PRIMARY]
- papers: https://doi.org/10.1063/1.4711100 (Crystal structure and thermoelectric properties of KxBa8−xZnyGe46−y cl...)

## Ge-Mg-Si-Sn
- rank 2235 | 2 samples | 2 papers | 2 compositions
- compositions: Mg2Si0.4Sn0.4Ge0.2 (1); Mg2Si0.38Sn0.4Ge0.20Bi0.02 (1)
- dopant candidates (<5% at.): Bi (1)
- measured range: 19-820 K (5th-95th pct of 9 curves; full span incl. outliers 19-986 K)
- papers: https://doi.org/10.1063/1.4918311 (Suppressing the bipolar contribution to the thermoelectric properties ...) | https://doi.org/10.1007/s11664-014-3235-x (Τhe Effect of Ge on Mg2Si0.6−x Sn0.4Ge x Materials)

## Ge-P-Te
- rank 2236 | 2 samples | 2 papers | 2 compositions
- compositions: Ge30P16Te8 (1); Ge129.3P42.7Te21.53 (1)
- measured range: 293-667 K (5th-95th pct of 6 curves; full span incl. outliers 293-723 K)
- papers: https://doi.org/10.1063/1.2364473 (Synthesis and thermoelectric properties of type-I clathrate Ge30P16Te8) | https://doi.org/10.1021/ic401203r (Cationic Clathrate of Type-III Ge172–xPxTey(y≈ 21.5,x≈ 2y): Synthesis,...)

## Ge-Pd-U
- rank 2237 | 2 samples | 1 papers | 2 compositions
- compositions: URu0.1Pd0.9Ge (1); UPdGe (1)
- dopant candidates (<5% at.): Ru (1)
- measured range: 13-299 K (5th-95th pct of 2 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): U(GePd)2 I4/mmm (139) mp-4297 [hull=0.000, icsd=2, PRIMARY]; UGePd Pnma (62) mp-1102677 [hull=0.000, icsd=2, PRIMARY]
- papers: https://doi.org/10.12693/aphyspola.127.287 (Thermoelectric Power of the URu1-xPdxGe System)

## Ge-Pt-Yb
- rank 2238 | 2 samples | 1 papers | 2 compositions
- compositions: YbPtGe (1); (Yb0.9La0.1)PtGe (1)
- dopant candidates (<5% at.): La (1)
- measured range: 10-278 K (5th-95th pct of 3 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): YbGePt Pnma (62) mp-22453 [hull=0.000, icsd=2, PRIMARY]; Yb3Ge13Pt4 P4_2cm (101) mp-1200714 [hull=0.000, icsd=1, PRIMARY]; Yb2Ge6Pt Amm2 (38) mp-1092256 [hull=0.082, icsd=1, PRIMARY]; YbGe2Pt Immm (71) mp-1188677 [hull=0.000, icsd=1, PRIMARY]; Yb2(GePt3)3 C2/c (15) mp-1207679 [hull=0.000, PRIMARY]
- papers: https://doi.org/10.1016/s0925-8388(98)00744-0 (Electrical and magnetic properties of YbPdGe and YbPtGe)

## Ge-Ru-U
- rank 2239 | 2 samples | 1 papers | 2 compositions
- compositions: URuGe (1); URu0.9Pd0.1Ge (1)
- dopant candidates (<5% at.): Pd (1)
- measured range: 10-297 K (5th-95th pct of 2 curves)
- papers: https://doi.org/10.12693/aphyspola.127.287 (Thermoelectric Power of the URu1-xPdxGe System)

## Ge-Sb-Se
- rank 2240 | 2 samples | 1 papers | 2 compositions
- compositions: Ge25Se65Sb10 (1); Ge25Se65Sb7.5Cu2.5 (1)
- dopant candidates (<5% at.): Cu (1)
- measured range: 300-450 K (5th-95th pct of 4 curves)
- papers: https://doi.org/10.1016/j.rinp.2019.102492 (Semiconducting chalcogenide Ge-Se-Sb-Cu as new prospective thermoelect...)

## Ge-Sn
- rank 2241 | 2 samples | 1 papers | 1 compositions
- compositions: GeSn (2)
- measured range: 302-746 K (5th-95th pct of 2 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Sn3Ge I4/mmm (139) mp-1187030 [hull=0.147, PRIMARY]; SnGe P3m1 (156) mp-995181 [hull=0.489, PRIMARY]; SnGe3 I4/mmm (139) mp-979254 [hull=0.294, PRIMARY]; Sn3Ge Pm-3m (221) mp-1187023 [hull=0.178]; Sn3Ge Fm-3m (225) mp-1187027 [hull=0.227]
- papers: https://doi.org/10.1063/1.4937386 (Carrier and heat transport properties of polycrystalline GeSn films on...)

## Ge-Te-Tl
- rank 2242 | 2 samples | 2 papers | 2 compositions
- compositions: Tl2GeTe3 (1); Tl8GeTe5 (1)
- measured range: 299-704 K (5th-95th pct of 10 curves; full span incl. outliers 299-752 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Tl2GeTe5 P4/mbm (127) mp-28639 [hull=0.005, icsd=2, PRIMARY]; Tl2GeTe3 Pnma (62) mp-29034 [hull=0.000, icsd=1, PRIMARY]; Tl3GeTe3 P-1 (2) mp-17217 [hull=0.000, icsd=1, PRIMARY]
- papers: https://doi.org/10.1063/1.2181427 (Thermoelectric properties of Tl–X–Te (X=Ge, Sn, and Pb) compounds with...) | https://doi.org/10.2320/matertrans.e-mra2008815 (Thermoelectric Properties of Tl<SUB>8</SUB>GeTe<SUB>5</SUB> with Low T...)

## H-Sb-Te
- rank 2243 | 2 samples | 1 papers | 2 compositions
- compositions: (Sb2Te3)19.3(CH3NH3I)3.5 (1); (Sb2Te3)19.5(CH3NH3I)2.5 (1)
- dopant candidates (<5% at.): C (2), N (2), I (2)
- measured range: 300-450 K (5th-95th pct of 8 curves)
- papers: https://doi.org/10.1039/c8nr02065e (High-performance p-type inorganic–organic hybrid thermoelectric thin f...)

## H-Yb
- rank 2244 | 2 samples | 1 papers | 2 compositions
- compositions: YbH1.85 (1); YbH1.88 (1)
- measured range: 298-419 K (5th-95th pct of 10 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): YbH2 Fm-3m (225) mp-634751 [hull=0.059, icsd=3, PRIMARY]; YbH3 Fm-3m (225) mp-634930 [hull=0.290, icsd=1, PRIMARY]; Yb3H8 C2/m (12) mp-697915 [hull=0.095, PRIMARY]; Yb3H P6_3/mmc (194) mp-1187975 [hull=0.638, PRIMARY]; YbH2 Pnma (62) mp-864603 [hull=0.000, icsd=2]
- papers: https://doi.org/10.1016/j.jallcom.2019.153496 (Experimental study of the thermoelectric properties of YbH2)

## Hf-Rh
- rank 2245 | 2 samples | 2 papers | 1 compositions
- compositions: Rh3Hf (2)
- measured range: 299-1096 K (5th-95th pct of 2 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Hf2Rh Fd-3m (227) mp-1190626 [hull=0.000, icsd=3, PRIMARY]; HfRh3 Pm-3m (221) mp-1027 [hull=0.000, icsd=3, PRIMARY]; Hf3Rh5 Pbam (55) mp-17045 [hull=0.000, icsd=1, PRIMARY]; HfRh Pm-3m (221) mp-11457 [hull=0.000, icsd=1, PRIMARY]
- papers: https://doi.org/10.1595/147106706x106182 (Thermophysical Properties of Rh<SUB>3</SUB>X for Ultra-High Temperatur...) | https://doi.org/10.1016/s0925-8388(03)00006-9 (Thermal conductivity and thermal expansion of L12 intermetallic compou...)

## Hf-Rh-Sb-Zr
- rank 2246 | 2 samples | 1 papers | 2 compositions
- compositions: Zr0.5Hf0.5Co0.1Rh0.9Sb0.99Sn0.01 (1); 	Zr0.5Hf0.5RhSb0.99Sn0.01 (1)
- dopant candidates (<5% at.): Sn (2), Co (1)
- measured range: 294-753 K (5th-95th pct of 10 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): HfZr(SbRh)2 R3m (160) mp-1224215 [hull=0.638, PRIMARY]
- papers: https://doi.org/10.1016/j.jssc.2010.03.023 (Effects of Rh on the thermoelectric performance of the p-type Zr0.5Hf0...)

## Ho-N
- rank 2247 | 2 samples | 1 papers | 1 compositions
- compositions: HoN (2)
- measured range: 10-91 K (5th-95th pct of 2 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): HoN Fm-3m (225) mp-883 [hull=0.000, icsd=9, PRIMARY]; Ho2N3 Ia-3 (206) mp-1201150 [hull=0.810, icsd=1, PRIMARY]; HoN Pm-3m (221) mp-1001844 [hull=0.937, icsd=1]
- papers: https://doi.org/10.1063/1.2158689 (Specific heat and thermal conductivity of HoN and ErN at cryogenic tem...)

## I-P-Sn
- rank 2248 | 2 samples | 1 papers | 2 compositions
- compositions: Sn24P19.3I8 (1); Sn24P19.3Br2I6 (1)
- dopant candidates (<5% at.): Br (1)
- measured range: 24-286 K (5th-95th pct of 2 curves)
- papers: https://doi.org/10.1016/j.solidstatesciences.2007.05.008 (Crystal structure, thermoelectric and magnetic properties of the type-...)

## I-V
- rank 2249 | 2 samples | 1 papers | 1 compositions
- compositions: VI3 (2)
- measured range: 10-91 K (5th-95th pct of 2 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): VI2 P-3m1 (164) mp-1018138 [hull=0.000, icsd=1, PRIMARY]; VI P6_3mc (186) mp-1187728 [hull=0.903, PRIMARY]; VI3 P6_3/mmc (194) mp-865493 [hull=0.000, PRIMARY]
- papers: https://doi.org/10.48550/ARXIV.2305.13268 (Spin-phonon scattering-induced low thermal conductivity in a van der W...)

## In-La-Pd
- rank 2250 | 2 samples | 2 papers | 2 compositions
- compositions: LaPdIn (1); La6Pd12In5 (1)
- measured range: 11-299 K (5th-95th pct of 4 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): La2InPd2 P4/mbm (127) mp-1087240 [hull=0.000, icsd=3, PRIMARY]; La4In21Pd10 C2/m (12) mp-1197789 [hull=0.000, icsd=1, PRIMARY]; LaIn2Pd Cmcm (63) mp-21367 [hull=0.000, icsd=1, PRIMARY]; LaInPd2 P6_3/mmc (194) mp-20743 [hull=0.000, icsd=1, PRIMARY]; LaInPd P-62m (189) mp-20138 [hull=0.227, PRIMARY]
- papers: https://doi.org/10.7567/jjaps.26s3.549 (Magnetic and Transport Properties of New Kondo Compounds CeTIn (T=Ni, ...) | https://doi.org/10.1063/1.4967990 (Detailed investigation of thermal and electron transport properties in...)
