# Host systems -- chunk 066 of 73

Ranks 3251-3300 by sample count. These 50 host systems cover 50 samples (0.10% of the TE set); cumulative through this chunk: 99.33%.

Assign each host system a structural prototype from `data/annotated/taxonomy/prototypes_seed_v3.json`, or propose a new one in `taxonomy/prototypes_proposed.jsonl` first. Append results to `data/annotated/annotations/family_assignments.jsonl`.

The hand-entered MaterialFamily labels are deliberately NOT shown here -- they are held out in `df_host_systems.parquet` to validate this classification later. Decide from the compositions.

A "seed hypothesis" line means the taxonomy already names this host under that prototype. Confirm it against the compositions rather than accepting it; two or more listed means the host is mixed and needs splitting per composition.

Evidence follows the project precedence. Your judgement about the thermoelectric chemistry decides the prototype. [ref 1] is TEDesignLab, ICSD-backed and thermoelectric-specific -- prefer it. [ref 2] is Materials Project. Within a formula, polymorphs are ranked by ICSD reference count and the top one is marked PRIMARY -- not by e_above_hull, which is unusable for layered chalcogenides in the 2019 dump (Sb2Te3 R-3m carries 26 ICSD refs at hull 1.02). A primary resting on fewer than 5 ICSD references is flagged weak; the ambient phase may simply be absent from the snapshot, as it is for Bi2Se3.

While you have the host in view, also record what each minor element DOES, in `dopant_roles` -- the role follows from the prototype and cannot be judged without it. A median host has 2 such elements. Not everything listed is a dopant: O, C, N and H are usually milling or pressing residue, and an element just under 5 at.% may be an alloying end member rather than dilute doping. The doping LEVEL is computed later from the parsed fractions -- do not work it out by hand here.

A polymorph list is NOT a thermal sequence. SnSe has three known structures but only Pnma -> Cmcm happens on heating; rocksalt SnSe is metastable (2 icsd refs against 32). Put thermally reached phases in `phases` with their transition temperatures, and everything else in `other_polymorphs` with an occurrence reason. hull and icsd counts are shown to help you tell them apart.

A host may need MORE THAN ONE prototype. Transport is measured across a wide window and many thermoelectrics transform inside it, so where a "MEASUREMENT CROSSES A TRANSITION" line appears, record each phase with its own temperature range in the `phases` field. Transition temperatures shown are approximate and composition-dependent.

Both references describe which phases EXIST in a chemistry, not which phase this paper made. Al-O-Zn is best attested as ZnAl2O4 spinel (227) while almost every sample in it is Al-doped wurtzite ZnO (186). Weigh them against the compositions; do not follow them blindly.

## Fe-Sn
- rank 3251 | 1 samples | 1 papers | 1 compositions
- compositions: Fe3Sn (1)
- measured range: 300-596 K (5th-95th pct of 3 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): FeSn P6/mmm (191) mp-21260 [hull=0.000, icsd=11, PRIMARY]; FeSn2 I4/mcm (140) mp-22752 [hull=0.018, icsd=10, PRIMARY]; Fe3Sn P6_3/mmc (194) mp-1080038 [hull=0.034, icsd=4, PRIMARY]; Fe3Sn2 R-3m (166) mp-27505 [hull=0.002, icsd=1, PRIMARY]; FeSn3 P6_3/mmc (194) mp-1184775 [hull=0.577, PRIMARY]
- papers: Magnetic and Thermoelectric Properties of Fe–Ti–Sn Alloys

## Fe-Sn-Ti-V
- rank 3252 | 1 samples | 1 papers | 1 compositions
- compositions: Fe2Ti0.8V0.2Sn (1)
- measured range: 297-975 K (5th-95th pct of 3 curves)
- papers: Influence of V Doping on the Thermoelectric Properties of Fe2Ti1 –xVxSn Heusler Alloys

## Fe-Sn-V
- rank 3253 | 1 samples | 1 papers | 1 compositions
- compositions: Fe2VSn (1)
- measured range: 11-300 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): VFe2Sn Fm-3m (225) mp-636359 [hull=0.130, icsd=1, PRIMARY]; V2FeSn Amm2 (38) mp-1216897 [hull=0.120, PRIMARY]
- papers: Enhancement in power factor values of Sn substituted Fe2 VAl Heusler alloys

## Fe-U
- rank 3254 | 1 samples | 1 papers | 1 compositions
- compositions: U6Fe (1)
- measured range: 12-301 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): UFe2 Fd-3m (227) mp-21050 [hull=0.000, icsd=14, PRIMARY]; U6Fe I4/mcm (140) mp-21108 [hull=0.028, icsd=7, PRIMARY]; U4Fe Fd-3m (227) mp-1208119 [hull=0.756, PRIMARY]; U24CrFe3 C222 (21) mp-1217610 [hull=0.065, PRIMARY]
- papers: Some Characteristics of the Thermoelectric Power in Uranium Intermetallic Compounds

## Fe-Zr
- rank 3255 | 1 samples | 1 papers | 1 compositions
- compositions: Fe2Zr (1)
- measured range: 331-1111 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): ZrFe2 Fd-3m (227) mp-1718 [hull=0.000, icsd=29, PRIMARY]; Zr2Fe I4/mcm (140) mp-1159 [hull=0.017, icsd=7, PRIMARY]; Zr3Fe Cmcm (63) mp-31205 [hull=0.000, icsd=6, PRIMARY]; Zr4Fe Fd-3m (227) mp-1207484 [hull=0.673, PRIMARY]; ZrFe2 P6_3/mmc (194) mp-1190681 [hull=0.008, icsd=2]
- papers: Thermal and Mechanical Properties of Fe<sub>2</sub>Zr

## Ga-Ge-K-Sr
- rank 3256 | 1 samples | 1 papers | 1 compositions
- compositions: K8Sr16Ga39Ge97 (1)
- measured range: 88-1004 K (5th-95th pct of 4 curves)
- papers: Synthesis and thermoelectric properties of semiconducting germanium-based type-II clathrate (K,Sr) 24 (Ga,Ge) 136

## Ga-Ge-Re
- rank 3257 | 1 samples | 1 papers | 1 compositions
- compositions: ReGa2Ge (1)
- measured range: 11-395 K (5th-95th pct of 3 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): GaReGe2 Immm (71) mp-1097303 [hull=2.346, PRIMARY]
- papers: Electron-Precise Semiconducting ReGa2Ge: Extending the IrIn3 Structure Type to Group 7 of the Periodic Table

## Ga-Ho
- rank 3258 | 1 samples | 1 papers | 1 compositions
- compositions: HoGa2 (1)
- measured range: 11-280 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): HoGa3 Pm-3m (221) mp-2688 [hull=0.005, icsd=4, PRIMARY]; HoGa2 P6/mmm (191) mp-1256 [hull=0.000, icsd=4, PRIMARY]; HoGa Cmcm (63) mp-1018073 [hull=0.000, icsd=3, PRIMARY]; HoGa6 P4/nbm (125) mp-1103872 [hull=0.010, icsd=3, PRIMARY]; Ho5Ga3 P4/ncc (130) mp-1196886 [hull=0.000, icsd=1, PRIMARY]
- papers: Thermoelectric power and resistivity studies in the Kondo-lattice system CeGa2with Sn or Al substitutions and RGa2(R identical to Ho,Dy,Tb) alloys

## Ga-In-Nb-Ru
- rank 3259 | 1 samples | 1 papers | 1 compositions
- compositions: Ru2NbGa0.80In0.20 (1)
- measured range: 11-298 K (5th-95th pct of 5 curves)
- papers: Thermoelectric properties of chemically substituted Heusler-type Ru2-Nb1+Ga and Ru2NbGa1-M  (M = In, Ge, and Sn) alloys

## Ga-In-Sn
- rank 3260 | 1 samples | 1 papers | 1 compositions
- compositions: Ga77.2In14.4Sn8.4 (1)
- measured range: 291-686 K (5th-95th pct of 3 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): In2GaSn Immm (71) mp-1093652 [hull=1.178, PRIMARY]; InGa2Sn Immm (71) mp-1096249 [hull=1.205, PRIMARY]
- papers: Thermophysical Properties of the Liquid Ga–In–Sn Eutectic Alloy

## Ga-K-Sb
- rank 3261 | 1 samples | 1 papers | 1 compositions
- compositions: (Ba0.025K0.975)1.05GaSb4. (1)
- dopant candidates (<5% at.): Ba (1)
- measured range: 327-624 K (5th-95th pct of 1 curves)
- [ref 1] TEDesignLab / ICSD: KGaSb4 Pnma (62) mp-29374 [hull=0.000, icsd=1, PRIMARY]
- [ref 2] MP, ranked by ICSD evidence: K2Ga2Sb3 P2_1/c (14) mp-15433 [hull=0.000, icsd=1, PRIMARY]; K2GaSb2 Pnma (62) mp-30077 [hull=0.000, icsd=1, PRIMARY]; KGaSb2 Cmce (64) mp-29383 [hull=0.000, icsd=1, PRIMARY]; K30Ga9Sb19 R-3 (148) mp-1225850 [hull=0.000, PRIMARY]
- papers: Discovery of n-Type Zintl Phases RbAlSb4, RbGaSb4, CsAlSb4, and CsGaSb4

## Ga-La-Mn-O
- rank 3262 | 1 samples | 1 papers | 1 compositions
- compositions: La0.5Ga0.5MnO3 (1)
- measured range: 270-410 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): La2MnGaO6 P2_1/c (14) mp-1223352 [hull=0.029, PRIMARY]
- papers: Conductivity and switching phenomena in Mn-doped perovskite single crystals and manganite thin films

## Ga-La-O-Sr
- rank 3263 | 1 samples | 1 papers | 1 compositions
- compositions: SrLaGaO4 (1)
- measured range: 34-400 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Sr2LaGa11O20 Cm (8) mp-1218805 [hull=0.015, PRIMARY]; Sr2LaGaO5 Fmmm (69) mp-1218758 [hull=0.030, PRIMARY]; SrLaGa3O7 Cmm2 (35) mp-1218197 [hull=0.000, PRIMARY]; SrLaGaO4 I4mm (107) mp-1218152 [hull=0.050, PRIMARY]
- papers: High-temperature ferromagnetic insulating phase in strained La<sub>0.8</sub>Sr<sub>0.2</sub>MnO<sub>3</sub> thin films

## Ga-La-Ru
- rank 3264 | 1 samples | 1 papers | 1 compositions
- compositions: La2Ru3Ga9 (1)
- measured range: 17-389 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): La3(GaRu)2 P2_1/m (11) mp-1199411 [hull=0.000, icsd=1, PRIMARY]; La2(Ga3Ru)3 Cmcm (63) mp-1211948 [hull=0.000, PRIMARY]
- papers: Revisiting the physical properties of Ce2Ru3Ga9: Intermediate valence, or Kondo lattice system?

## Ga-Li-Te
- rank 3265 | 1 samples | 1 papers | 1 compositions
- compositions: LiGa3Te5 (1)
- measured range: 300-482 K (5th-95th pct of 1 curves)
- [ref 1] TEDesignLab / ICSD: LiGaTe2 I-42d (122) mp-5048 [hull=0.000, icsd=2, PRIMARY]
- [ref 2] MP, ranked by ICSD evidence: Li7(Ga3Te5)8 P1 (1) mp-685906 [hull=0.019, PRIMARY]; LiGa3Te5 R3 (146) mp-33338 [hull=0.004, PRIMARY]
- papers: Modified Bridgman growth and characterization of a novel mid-infrared transparent optical crystal: LiGa3Te5

## Ga-Mn
- rank 3266 | 1 samples | 1 papers | 1 compositions
- compositions: MnGa (1)
- measured range: 15-301 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Mn2Ga5 P4/mbm (127) mp-607225 [hull=0.033, icsd=3, PRIMARY]; Mn3Ga P6_3/mmc (194) mp-1078584 [hull=0.102, icsd=2, PRIMARY]; Mn6Ga29 P-1 (2) mp-1196402 [hull=0.009, icsd=2, PRIMARY]; Mn8Ga5 I-43m (217) mp-1194466 [hull=0.197, icsd=2, PRIMARY]; MnGa4 Im-3m (229) mp-1069288 [hull=0.000, icsd=2, PRIMARY]
- papers: Observation of orbital two-channel Kondo effect in a ferromagnetic L10-MnGa film

## Ga-Mn-N
- rank 3267 | 1 samples | 1 papers | 1 compositions
- compositions: GaN2.5Mn0.5 (1)
- measured range: 11-331 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Mn3GaN Pm-3m (221) mp-627439 [hull=0.000, icsd=1, PRIMARY]
- papers: Synthesis and characterization of antiperovskite nitrides GaNCr3−xMnx

## Ga-Na-Sn
- rank 3268 | 1 samples | 1 papers | 1 compositions
- compositions: Na2.19Ga2.19Sn3.81 (1)
- measured range: 295-386 K (5th-95th pct of 3 curves)
- papers: A Thermoelectric Zintl Phase Na2+xGa2+xSn4-xwith Disordered Na Atoms in Helical Tunnels

## Ga-Ni-Sb
- rank 3269 | 1 samples | 1 papers | 1 compositions
- compositions: Ni3GaSb (1)
- measured range: 331-1054 K (5th-95th pct of 5 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): GaNi3Sb P-6m2 (187) mp-1224811 [hull=0.159, PRIMARY]
- papers: Synthesis and high-temperature thermoelectric properties of Ni3GaSb and Ni3InSb

## Ga-Ni-U
- rank 3270 | 1 samples | 1 papers | 1 compositions
- compositions: UNiGa (1)
- measured range: 10-290 K (5th-95th pct of 3 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): UGaNi P-62m (189) mp-21320 [hull=0.000, icsd=5, PRIMARY]; UGa5Ni P4/mmm (123) mp-21251 [hull=0.000, icsd=3, PRIMARY]; UGa3Ni I4mm (107) mp-1070301 [hull=0.049, icsd=1, PRIMARY]; U4Ga20Ni11 C2/m (12) mp-680664 [hull=0.005, icsd=1, PRIMARY]; U4Ga12Ni Im-3m (229) mp-1207934 [hull=0.001, PRIMARY]
- papers: Hall effect and thermoelectric power in UNiGa

## Ga-Ni-Yb
- rank 3271 | 1 samples | 1 papers | 1 compositions
- compositions: YbNiGa (1)
- measured range: 12-286 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): YbGa2Ni Cmcm (63) mp-1078497 [hull=0.000, icsd=5, PRIMARY]; YbGa4Ni Cmcm (63) mp-12895 [hull=0.000, icsd=3, PRIMARY]; YbGaNi Pnma (62) mp-1095431 [hull=0.000, icsd=2, PRIMARY]; Yb4Ga21Ni10 C2/m (12) mp-1203792 [hull=0.016, icsd=1, PRIMARY]; YbGa2Ni3 P6/mmm (191) mp-1189384 [hull=0.000, icsd=1, PRIMARY]
- papers: Low-temperature properties of the Yb-based heavy-fermion antiferromagnets YbPtIn, YbRhSn, and YbNiGa

## Ga-O-Ru
- rank 3272 | 1 samples | 1 papers | 1 compositions
- compositions: Ga2RuO4 (1)
- measured range: 71-561 K (5th-95th pct of 1 curves)
- papers: Destruction of the Mott insulating ground state of<mml:math xmlns:mml=\"http://www.w3.org/1998/Math/MathML\" display=\"inline\"><mml:mrow><mml:msub><mml:mrow><mml:mi mathvariant=\"normal\">Ca</mml:mi></mml:mrow><mml:mrow><mml:mn>2</mml:mn></mml:mrow></mml:msub></mml:mrow><mml:mrow><mml:msub><mml:mrow><mml:mi mathvariant=\"normal\">RuO</mml:mi></mml:mrow><mml:mrow><mml:mn>4</mml:mn></mml:mrow></mml:msub></mml:mrow></mml:math>by a structural transition

## Ga-O-Ti
- rank 3273 | 1 samples | 1 papers | 1 compositions
- compositions: Ti3GaO (1)
- measured range: 11-298 K (5th-95th pct of 1 curves)
- [ref 1] TEDesignLab / ICSD: Ti(GaO2)4 (12) [PRIMARY]
- [ref 2] MP, ranked by ICSD evidence: TiGa2O5 Cmcm (63) mp-760501 [hull=0.039, PRIMARY]; TiGa2O5 C2/c (15) mp-752733 [hull=0.077]
- papers: Ternary Suboxides Ti<sub>7</sub>Ga<sub>2</sub>O<sub>6</sub>, Ti<sub>3</sub>GaO, and Ti<sub>5</sub>Ga<sub>3</sub>O

## Ga-Os
- rank 3274 | 1 samples | 1 papers | 1 compositions
- compositions: OsGa3 (1)
- measured range: 298-942 K (5th-95th pct of 3 curves)
- papers: Thermoelectric properties of semiconductorlike intermetallic compounds TMGa3 (TM=Fe, Ru, and Os)

## Ga-P
- rank 3275 | 1 samples | 1 papers | 1 compositions
- compositions: GaP (1)
- measured range: 156-1165 K (5th-95th pct of 2 curves)
- [ref 1] TEDesignLab / ICSD: GaP F-43m (216) mp-2490 [hull=0.000, icsd=18, PRIMARY]; GaP P6_3mc (186) mp-8882 [hull=0.010, icsd=2]
- [ref 2] MP, ranked by ICSD evidence: Ga3P I4/mmm (139) mp-1184292 [hull=0.353, PRIMARY]; GaP R-3m (166) mp-1018275 [hull=0.135, icsd=1]; GaP Pa-3 (205) mp-971632 [hull=0.170]; GaP Imm2 (44) mp-971648 [hull=0.481]; GaP P4/mmm (123) mp-971631 [hull=0.579]
- papers: Nanograined Half-Heusler Semiconductors as Advanced Thermoelectrics: An Ab Initio High-Throughput Statistical Study

## Ga-Pt
- rank 3276 | 1 samples | 1 papers | 1 compositions
- compositions: PtGa2 (1)
- measured range: 11-297 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): GaPt3 I4/mcm (140) mp-862621 [hull=0.000, icsd=2, PRIMARY]; Ga7Pt3 Im-3m (229) mp-1188512 [hull=0.000, icsd=2, PRIMARY]; GaPt2 Pmma (51) mp-2223 [hull=0.000, icsd=2, PRIMARY]; Ga2Pt Fm-3m (225) mp-22095 [hull=0.000, icsd=1, PRIMARY]; Ga3Pt2 P-3m1 (164) mp-21400 [hull=0.009, icsd=1, PRIMARY]
- papers: Electrical resistivity, magnetic susceptibility and thermoelectric power of PtGa2

## Ga-Rb-Sb
- rank 3277 | 1 samples | 1 papers | 1 compositions
- compositions: (Ba0.025Rb0.975)1.05GaSb4 (1)
- dopant candidates (<5% at.): Ba (1)
- measured range: 326-623 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Rb2GaSb2 Pnma (62) mp-29371 [hull=0.000, icsd=1, PRIMARY]
- papers: Discovery of n-Type Zintl Phases RbAlSb4, RbGaSb4, CsAlSb4, and CsGaSb4

## Ga-Rb-Si
- rank 3278 | 1 samples | 1 papers | 1 compositions
- compositions: Rb8Ga8Si38 (1)
- measured range: 11-300 K (5th-95th pct of 3 curves)
- papers: Synthesis, Structure, Thermoelectric Properties, and Band Gaps of Alkali Metal Containing Type I Clathrates: A8Ga8Si38(A = K, Rb, Cs) and K8Al8Si38

## Ga-Ru-V
- rank 3279 | 1 samples | 1 papers | 1 compositions
- compositions: Ru2VGa (1)
- measured range: 10-298 K (5th-95th pct of 4 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): VGaRu2 Fm-3m (225) mp-865586 [hull=0.000, PRIMARY]
- papers: Thermoelectric properties of Heusler-type Ru2VAl1−Ga  alloys

## Ga-S-Se-Tl
- rank 3280 | 1 samples | 1 papers | 1 compositions
- compositions: TlGaSSe (1)
- measured range: 245-493 K (5th-95th pct of 1 curves)
- papers: Influence of temperature on the thermal transport properties of a TlGaSSe compound

## Ga-Sb-Yb
- rank 3281 | 1 samples | 1 papers | 1 compositions
- compositions: Yb5Ga2Sb6 (1)
- measured range: 300-875 K (5th-95th pct of 4 curves)
- papers: Thermoelectric properties of the Zintl phases Yb5M2Sb6 (M = Al, Ga, In)

## Ga-Sr
- rank 3282 | 1 samples | 1 papers | 1 compositions
- compositions: SrGa4 (1)
- measured range: 16-292 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): SrGa2 P6/mmm (191) mp-182 [hull=0.000, icsd=7, PRIMARY]; SrGa4 I4/mmm (139) mp-1827 [hull=0.000, icsd=4, PRIMARY]; SrGa P2_13 (198) mp-1199262 [hull=0.013, icsd=1, PRIMARY]; Sr8Ga7 P2_13 (198) mp-30667 [hull=0.000, icsd=1, PRIMARY]
- papers: Characteristic Fermi surfaces and charge density wave in SrAl4 and related compounds with the BaAl4-type tetragonal structure

## Ga-Tb
- rank 3283 | 1 samples | 1 papers | 1 compositions
- compositions: TbGa2 (1)
- measured range: 12-279 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): TbGa Cmcm (63) mp-11417 [hull=0.000, icsd=2, PRIMARY]; TbGa2 P6/mmm (191) mp-2684 [hull=0.000, icsd=2, PRIMARY]; TbGa3 P6_3/mmc (194) mp-867246 [hull=0.000, icsd=1, PRIMARY]; Tb5Ga3 I4/mcm (140) mp-1188342 [hull=0.000, icsd=1, PRIMARY]; TbGa6 P4/nbm (125) mp-1104458 [hull=0.008, icsd=1, PRIMARY]
- papers: Thermoelectric power and resistivity studies in the Kondo-lattice system CeGa2with Sn or Al substitutions and RGa2(R identical to Ho,Dy,Tb) alloys

## Ga-Te-Yb
- rank 3284 | 1 samples | 1 papers | 1 compositions
- compositions: YbGa6Te10 (1)
- measured range: 10-194 K (5th-95th pct of 2 curves; full span incl. outliers 10-361 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Yb(Ga3Te5)2 C2 (5) mp-676644 [hull=0.000, PRIMARY]
- papers: Structure and transport properties of new rare-earth gallium telluride YbGa6Te10

## Ga-V
- rank 3285 | 1 samples | 1 papers | 1 compositions
- compositions: V3Ga (1)
- measured range: 13-21 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): V3Ga Pm-3n (223) mp-22568 [hull=0.000, icsd=19, PRIMARY]; V2Ga5 P4/mbm (127) mp-20405 [hull=0.000, icsd=6, PRIMARY]; V5Ga3 P6_3/mcm (193) mp-1190304 [hull=0.084, icsd=2, PRIMARY]; V3Ga2 P4_132 (213) mp-1189774 [hull=0.092, icsd=1, PRIMARY]; V8Ga41 R-3 (148) mp-21965 [hull=0.000, icsd=1, PRIMARY]
- papers: A study of the heat conduction of superconductors. (1st report Measurement of thermal conductivities of Nb3Sn and V3Ga)

## Gd-Ge-Ni
- rank 3286 | 1 samples | 1 papers | 1 compositions
- compositions: Gd2NiGe6 (1)
- measured range: 10-282 K (5th-95th pct of 2 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Gd(NiGe)2 I4/mmm (139) mp-646399 [hull=0.000, icsd=2, PRIMARY]; GdNiGe3 Cmmm (65) mp-1079303 [hull=0.000, icsd=1, PRIMARY]
- papers: Electric transport in R2MGe6 ternary compounds (R=La, Ce, Gd, Tb, Dy, Ho; M=Mn, Ni, Cu)

## Gd-In
- rank 3287 | 1 samples | 1 papers | 1 compositions
- compositions: GdIn3 (1)
- measured range: 11-49 K (5th-95th pct of 2 curves; full span incl. outliers 11-292 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): GdIn3 Pm-3m (221) mp-20258 [hull=0.000, icsd=7, PRIMARY]; Gd2In P6_3/mmc (194) mp-638079 [hull=0.000, icsd=3, PRIMARY]; GdIn Pm-3m (221) mp-21005 [hull=0.000, icsd=2, PRIMARY]; Gd3In Pm-3m (221) mp-1184479 [hull=0.000, PRIMARY]; GdIn P4/mmm (123) mp-19819 [hull=0.004, icsd=1]
- papers: Thermoelectric power of the REIn3 single crystals where RE = La, Ce, Pr, Nd, Sm, Gd, Ho, ErIn3, TmandLu

## Gd-In-O-Ta
- rank 3288 | 1 samples | 1 papers | 1 compositions
- compositions: Gd2InTaO7 (1)
- measured range: 294-1072 K (5th-95th pct of 1 curves)
- papers: Thermal and oxygen transport properties of complex pyrochlore RE2InTaO7 for thermal barrier coating applications

## Gd-Ni-O
- rank 3289 | 1 samples | 1 papers | 1 compositions
- compositions: GdNiO3 (1)
- measured range: 43-467 K (5th-95th pct of 3 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Gd2NiO4 I4/mmm (139) mp-1207225 [hull=0.190, PRIMARY]
- papers: Correlation transports at p-/n-types in electron metastable perovskite family of rare-earth nickelates

## Gd-O
- rank 3290 | 1 samples | 1 papers | 1 compositions
- compositions: Gd2O3 (1)
- measured range: 300-1274 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Gd2O3 C2/m (12) mp-643084 [hull=0.039, icsd=5, PRIMARY]; GdO2 P4/nmm (129) mp-21149 [hull=0.141, icsd=1, PRIMARY]; GdO F-43m (216) mp-7870 [hull=0.219, icsd=1, PRIMARY]; GdO3 P6_3/m (176) mp-1206505 [hull=0.667, PRIMARY]; Gd2O3 P-3m1 (164) mp-20470 [hull=0.054, icsd=2]
- papers: Thermal conductivity of gadolinium added uranium mononitride fuel pellets sintered by spark plasma sintering

## Gd-O-Ru
- rank 3291 | 1 samples | 1 papers | 1 compositions
- compositions: Gd2Ru2O7 (1)
- measured range: 275-771 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Gd3RuO7 Pna2_1 (33) mp-683963 [hull=0.000, icsd=1, PRIMARY]; Gd3Bi(Ru2O7)2 R-3m (166) mp-1224726 [hull=0.013, PRIMARY]; Gd5(RuO7)2 C2/m (12) mp-673761 [hull=0.093, PRIMARY]; Gd3RuO7 Cmcm (63) mp-17237 [hull=0.004, icsd=1]
- papers: Chemical synthesis and characterization of nano-sized rare-earth ruthenium pyrochlore compounds \n                $$\\hbox {Ln}_{2}\\hbox {Ru}_{2}\\hbox {O}_{7}$$\n                \n                    \n                                    \n                        \n                            \n                                Ln\n                                2\n                            \n                            \n                                Ru\n                                2\n                            \n                            \n                                O\n                                7\n                            \n                        \n                    \n                \n             (Ln = rare earth)

## Gd-Os-P
- rank 3292 | 1 samples | 1 papers | 1 compositions
- compositions: GdOs4P12 (1)
- measured range: 12-301 K (5th-95th pct of 1 curves)
- papers: Thermal Properties of Filled Skutterudite PrOs4P12

## Gd-Pb-Sb
- rank 3293 | 1 samples | 1 papers | 1 compositions
- compositions: GdPbSb (1)
- measured range: 10-300 K (5th-95th pct of 3 curves)
- papers: Magnetic and transport properties of half-Heuslers, RPdSb (R = Gd and Tb)

## Gd-Se-Tl
- rank 3294 | 1 samples | 1 papers | 1 compositions
- compositions: TlGdSe2 (1)
- measured range: 295-605 K (5th-95th pct of 4 curves)
- papers: Thermoelectric Properties of TlGdQ2 (Q = Se, Te) and Tl9GdTe6

## Gd-Si
- rank 3295 | 1 samples | 1 papers | 1 compositions
- compositions: Gd5Si3 (1)
- measured range: 403-881 K (5th-95th pct of 2 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Gd5Si4 Pnma (62) mp-1199486 [hull=0.000, icsd=9, PRIMARY]; GdSi2 I4_1/amd (141) mp-21192 [hull=0.000, icsd=5, PRIMARY]; GdSi Pnma (62) mp-601371 [hull=0.000, icsd=5, PRIMARY]; Gd2Si3 P-6m2 (187) mp-1224874 [hull=0.215, PRIMARY]; Gd3Si P6_3/mmc (194) mp-1184530 [hull=0.139, PRIMARY]
- papers: Thermoelectric Properties of RE5X3(RE=Gd, La, X=Si, Ge)

## Gd-Te
- rank 3296 | 1 samples | 1 papers | 1 compositions
- compositions: GdTe3 (1)
- measured range: 10-15 K (5th-95th pct of 2 curves; full span incl. outliers 10-394 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Gd2Te3 Pnma (62) mp-1105966 [hull=0.000, icsd=3, PRIMARY]; GdTe2 P4/nmm (129) mp-1076964 [hull=0.000, icsd=1, PRIMARY]; GdTe P-6m2 (187) mp-1184509 [hull=0.022, PRIMARY]
- papers: High mobility in a van der Waals layered antiferromagnetic metal

## Gd-Y
- rank 3297 | 1 samples | 1 papers | 1 compositions
- compositions: Gd65.4Y34.6 (1)
- measured range: 94-218 K (5th-95th pct of 2 curves; full span incl. outliers 94-298 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Gd3Y Pm-3m (221) mp-1184469 [hull=0.050, PRIMARY]; GdY3 I4/mmm (139) mp-1184538 [hull=0.029, PRIMARY]; GdY3 Pm-3m (221) mp-1184639 [hull=0.034]
- papers: Transport properties and ultrasonic propagation in single crystal Gd65.4-Y34.6

## Gd-Zn
- rank 3298 | 1 samples | 1 papers | 1 compositions
- compositions: GdZn (1)
- measured range: 64-296 K (5th-95th pct of 2 curves; full span incl. outliers 64-392 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): GdZn Pm-3m (221) mp-2497 [hull=0.000, icsd=8, PRIMARY]; Gd2Zn17 P6_3/mmc (194) mp-1198632 [hull=0.003, icsd=1, PRIMARY]; Gd6Zn23 Fm-3m (225) mp-1193017 [hull=0.001, icsd=1, PRIMARY]; GdZn2 Imma (74) mp-1076988 [hull=0.000, icsd=1, PRIMARY]; Gd3Zn Pm-3m (221) mp-1184460 [hull=0.125, PRIMARY]
- papers: Electrical and thermoelectric transport properties of RZn and RCd compounds (R = Tb, Gd, Nd, Pr)

## Ge-Ho-Ni
- rank 3299 | 1 samples | 1 papers | 1 compositions
- compositions: Ho2NiGe6 (1)
- measured range: 10-277 K (5th-95th pct of 2 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ho(NiGe)2 I4/mmm (139) mp-4291 [hull=0.000, icsd=2, PRIMARY]; HoNiGe2 Cmcm (63) mp-974399 [hull=0.000, icsd=2, PRIMARY]; Ho3NiGe2 Pnma (62) mp-1190282 [hull=0.000, icsd=1, PRIMARY]; Ho2NiGe6 Amm2 (38) mp-12987 [hull=0.008, icsd=1, PRIMARY]; HoNiGe3 Cmmm (65) mp-1079921 [hull=0.000, icsd=1, PRIMARY]
- papers: Electric transport in R2MGe6 ternary compounds (R=La, Ce, Gd, Tb, Dy, Ho; M=Mn, Ni, Cu)

## Ge-Ho-Ru
- rank 3300 | 1 samples | 1 papers | 1 compositions
- compositions: Ho3Ru4Ge13 (1)
- measured range: 18-799 K (5th-95th pct of 5 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): HoGeRu Pnma (62) mp-22041 [hull=0.000, icsd=4, PRIMARY]; Ho2Ge5Ru3 Ibam (72) mp-1105625 [hull=0.000, icsd=2, PRIMARY]; Ho(GeRu)2 I4/mmm (139) mp-5260 [hull=0.000, icsd=2, PRIMARY]; Ho3Ge3Ru2 Cmcm (63) mp-30172 [hull=0.000, icsd=2, PRIMARY]; Ho3Ge13Ru4 Pm-3n (223) mp-1202131 [hull=0.021, icsd=1, PRIMARY]
- papers: Thermoelectric properties of rare earth–ruthenium–germanium compounds
