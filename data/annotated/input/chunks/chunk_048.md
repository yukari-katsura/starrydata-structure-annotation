# Host systems -- chunk 048 of 73

Ranks 2351-2400 by sample count. These 50 host systems cover 78 samples (0.15% of the TE set); cumulative through this chunk: 97.60%.

Assign each host system a structural prototype from `data/annotated/taxonomy/prototypes_seed_v3.json`, or propose a new one in `taxonomy/prototypes_proposed.jsonl` first. Append results to `data/annotated/annotations/family_assignments.jsonl`.

The hand-entered MaterialFamily labels are deliberately NOT shown here -- they are held out in `df_host_systems.parquet` to validate this classification later. Decide from the compositions.

A "seed hypothesis" line means the taxonomy already names this host under that prototype. Confirm it against the compositions rather than accepting it; two or more listed means the host is mixed and needs splitting per composition.

Evidence follows the project precedence. Your judgement about the thermoelectric chemistry decides the prototype. [ref 1] is TEDesignLab, ICSD-backed and thermoelectric-specific -- prefer it. [ref 2] is Materials Project. Within a formula, polymorphs are ranked by ICSD reference count and the top one is marked PRIMARY -- not by e_above_hull, which is unusable for layered chalcogenides in the 2019 dump (Sb2Te3 R-3m carries 26 ICSD refs at hull 1.02). A primary resting on fewer than 5 ICSD references is flagged weak; the ambient phase may simply be absent from the snapshot, as it is for Bi2Se3.

While you have the host in view, also record what each minor element DOES, in `dopant_roles` -- the role follows from the prototype and cannot be judged without it. A median host has 2 such elements. Not everything listed is a dopant: O, C, N and H are usually milling or pressing residue, and an element just under 5 at.% may be an alloying end member rather than dilute doping. The doping LEVEL is computed later from the parsed fractions -- do not work it out by hand here.

A polymorph list is NOT a thermal sequence. SnSe has three known structures but only Pnma -> Cmcm happens on heating; rocksalt SnSe is metastable (2 icsd refs against 32). Put thermally reached phases in `phases` with their transition temperatures, and everything else in `other_polymorphs` with an occurrence reason. hull and icsd counts are shown to help you tell them apart.

A host may need MORE THAN ONE prototype. Transport is measured across a wide window and many thermoelectrics transform inside it, so where a "MEASUREMENT CROSSES A TRANSITION" line appears, record each phase with its own temperature range in the `phases` field. Transition temperatures shown are approximate and composition-dependent.

Both references describe which phases EXIST in a chemistry, not which phase this paper made. Al-O-Zn is best attested as ZnAl2O4 spinel (227) while almost every sample in it is Al-doped wurtzite ZnO (186). Weigh them against the compositions; do not follow them blindly.

## P-U
- rank 2351 | 2 samples | 1 papers | 1 compositions
- compositions: U3P4 (2)
- measured range: 11-148 K (5th-95th pct of 2 curves; full span incl. outliers 11-195 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): UP Fm-3m (225) mp-2011 [hull=0.000, icsd=16, PRIMARY]; UP2 P4/nmm (129) mp-413 [hull=0.002, icsd=4, PRIMARY]; U3P4 I-43d (220) mp-787 [hull=0.000, icsd=3, PRIMARY]; U2P3 P4/mmm (123) mp-1207317 [hull=4.103, PRIMARY]; UP3 P6_3/mmc (194) mp-865428 [hull=0.000, PRIMARY]
- papers: Giant anisotropic magnetoresistance and magnetothermopower in cubic 3:4 uranium pnictides

## Pb-Pt-Te
- rank 2352 | 2 samples | 1 papers | 2 compositions
- compositions: (PbTe)0.5(PtTe2)0.5 (1); (PbTe)0.67(PtTe2)0.33 (1)
- measured range: 303-664 K (5th-95th pct of 6 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): TePtPb P2_13 (198) mp-1217437 [hull=0.000, PRIMARY]
- papers: Binary-Phased Nanoparticles for Enhanced Thermoelectric Properties

## Pb-S-Sn-Te
- rank 2353 | 2 samples | 1 papers | 1 compositions
- compositions: (PbTe)75(PbSnS2)25(PbI2)0.055 (2)
- dopant candidates (<5% at.): I (2)
- measured range: 302-718 K (5th-95th pct of 8 curves; full span incl. outliers 302-759 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): SnTe(PbS)4 R3m (160) mp-1218922 [hull=0.038, PRIMARY]
- papers: PbTe–PbSnS2 thermoelectric composites: low lattice thermal conductivity from large microstructures

## Pb-S-Ti
- rank 2354 | 2 samples | 2 papers | 1 compositions
- compositions: (PbS)1.18(TiS2)2 (2)
- measured range: 321-774 K (5th-95th pct of 6 curves)
- papers: Energy-filtering-induced high power factor in PbS-nanoparticles-embedded TiS2 | Low-Thermal-Conductivity (MS)1+x(TiS2)2 (M = Pb, Bi, Sn) Misfit Layer Compounds for Bulk Thermoelectric Materials

## Pd-Sb-Sn-Sr
- rank 2355 | 2 samples | 1 papers | 2 compositions
- compositions: SrPd4Sn5Sb7 (1); SrPd4Sn6Sb6 (1)
- measured range: 10-323 K (5th-95th pct of 6 curves)
- papers: Crystal Structure and Physical Properties of Skutterudites SrPd4Sn x Sb12−x

## Pd-Si-Yb
- rank 2356 | 2 samples | 2 papers | 2 compositions
- compositions: Yb3Pd20Si6 (1); YbPd2Si2 (1)
- measured range: 10-276 K (5th-95th pct of 2 curves; full span incl. outliers 10-378 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Yb(SiPd)2 I4/mmm (139) mp-4633 [hull=0.000, icsd=3, PRIMARY]; YbSiPd2 Pnma (62) mp-1189833 [hull=0.000, icsd=1, PRIMARY]; Yb3(Si3Pd10)2 Fm-3m (225) mp-1207621 [hull=0.000, PRIMARY]; YbSi3Pd5 Pnma (62) mp-1207527 [hull=0.000, PRIMARY]; YbSiPd Pnma (62) mp-1207493 [hull=0.000, PRIMARY]
- papers: Physical phenomena of the cage compounds RE3Pd20Si6 (RE=Yb, Lu) | Thermoelectric power of YbMCu4 (M = Ag, Au and Pd) and YbPd2Si2

## Pt-Sb-U
- rank 2357 | 2 samples | 1 papers | 1 compositions
- compositions: U3Pt3Sb4 (2)
- measured range: 12-346 K (5th-95th pct of 8 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): U3Sb4Pt3 I-43d (220) mp-1188604 [hull=0.000, icsd=1, PRIMARY]
- papers: Uranium-based materials for thermoelectric applications

## Pt-Sn-Ti
- rank 2358 | 2 samples | 2 papers | 1 compositions
- compositions: TiPtSn (2)
- measured range: 219-1073 K (5th-95th pct of 6 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): TiSnPt F-43m (216) mp-30847 [hull=0.000, icsd=1, PRIMARY]
- papers: Ordered Structures and Thermoelectric Properties of MNiSn (M = Ti, Zr, Hf)-Based Half-Heusler Compounds Affected by Close Relationship with Heusler Compounds | Thermoelectric Properties of P-type Half-Heusler Compounds HfPtSn and ZrPtSn

## Pt-Sn-Zr
- rank 2359 | 2 samples | 2 papers | 1 compositions
- compositions: ZrPtSn (2)
- measured range: 214-1071 K (5th-95th pct of 6 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): ZrSnPt F-43m (216) mp-961713 [hull=0.000, PRIMARY]
- papers: Ordered Structures and Thermoelectric Properties of MNiSn (M = Ti, Zr, Hf)-Based Half-Heusler Compounds Affected by Close Relationship with Heusler Compounds | Thermoelectric Properties of P-type Half-Heusler Compounds HfPtSn and ZrPtSn

## Rh-Ta
- rank 2360 | 2 samples | 2 papers | 1 compositions
- compositions: Rh3Ta (2)
- measured range: 301-1099 K (5th-95th pct of 2 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): TaRh3 Pm-3m (221) mp-1020 [hull=0.000, icsd=2, PRIMARY]; TaRh2 Pnma (62) mp-1103212 [hull=0.000, icsd=1, PRIMARY]
- papers: Thermophysical Properties of Rh<SUB>3</SUB>X for Ultra-High Temperature Applications | Thermal conductivity and thermal expansion of L12 intermetallic compounds based on rhodium

## Rh-Ti
- rank 2361 | 2 samples | 2 papers | 1 compositions
- compositions: Rh3Ti (2)
- measured range: 300-1095 K (5th-95th pct of 2 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): TiRh P4/mmm (123) mp-2583 [hull=0.000, icsd=5, PRIMARY]; TiRh3 Pm-3m (221) mp-1152 [hull=0.000, icsd=5, PRIMARY]; Ti3Rh5 Pbam (55) mp-17413 [hull=0.000, icsd=1, PRIMARY]; Ti2Rh I4/mmm (139) mp-1018124 [hull=0.000, icsd=1, PRIMARY]; TiRh Pm-3m (221) mp-11563 [hull=0.026, icsd=1]
- papers: Thermophysical Properties of Rh<SUB>3</SUB>X for Ultra-High Temperature Applications | Thermal conductivity and thermal expansion of L12 intermetallic compounds based on rhodium

## Rh-V
- rank 2362 | 2 samples | 2 papers | 1 compositions
- compositions: Rh3V (2)
- measured range: 299-1095 K (5th-95th pct of 2 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): V3Rh Pm-3n (223) mp-1578 [hull=0.000, icsd=4, PRIMARY]; VRh P4/mmm (123) mp-1251 [hull=0.022, icsd=3, PRIMARY]; VRh3 Pm-3m (221) mp-1185 [hull=0.008, icsd=3, PRIMARY]; V3Rh5 Amm2 (38) mp-1216486 [hull=0.022, PRIMARY]; VRh Cmmm (65) mp-971751 [hull=0.000, icsd=2]
- papers: Thermophysical Properties of Rh<SUB>3</SUB>X for Ultra-High Temperature Applications | Thermal conductivity and thermal expansion of L12 intermetallic compounds based on rhodium

## Rh-Zn
- rank 2363 | 2 samples | 2 papers | 1 compositions
- compositions: YbRh2Zn20 (2)
- dopant candidates (<5% at.): Yb (2)
- measured range: 13-300 K (5th-95th pct of 6 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): U(Zn10Rh)2 Fd-3m (227) mp-1198503 [hull=0.002, icsd=1, PRIMARY]; Zn11Rh2 I-43m (217) mp-13448 [hull=0.000, icsd=1, PRIMARY]; Zn13Rh C2/m (12) mp-13447 [hull=0.000, icsd=1, PRIMARY]; ZnRh Pm-3m (221) mp-6938 [hull=0.000, icsd=1, PRIMARY]; Zn3Rh I4/mmm (139) mp-865342 [hull=0.000, PRIMARY]
- papers: Thermoelectric power of the YbT2Zn20(T=Fe, Ru, Os, Ir, Rh, and Co) heavy fermions | Enhanced thermoelectric performance of heavy-fermion compounds YbTM2Zn20 (TM = Co, Rh, Ir) at low temperatures

## Rh-Zr
- rank 2364 | 2 samples | 2 papers | 1 compositions
- compositions: Rh3Zr (2)
- measured range: 299-1095 K (5th-95th pct of 2 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): ZrRh3 Pm-3m (221) mp-229 [hull=0.000, icsd=8, PRIMARY]; Zr3Rh5 Cmcm (63) mp-2626 [hull=0.000, icsd=3, PRIMARY]; ZrRh Pm-3m (221) mp-2808 [hull=0.071, icsd=2, PRIMARY]; Zr3Rh I-42m (121) mp-1188413 [hull=0.000, icsd=1, PRIMARY]; ZrRh Pnma (62) mp-669917 [hull=0.000, icsd=1]
- papers: Thermophysical Properties of Rh<SUB>3</SUB>X for Ultra-High Temperature Applications | Thermal conductivity and thermal expansion of L12 intermetallic compounds based on rhodium

## Ru-Sb-Sr
- rank 2365 | 2 samples | 1 papers | 1 compositions
- compositions: SrRu4Sb12 (2)
- measured range: 11-284 K (5th-95th pct of 3 curves; full span incl. outliers 11-499 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Sr(Sb3Ru)4 Im-3 (204) mp-22775 [hull=0.000, icsd=1, PRIMARY]; Sr(SbRu)2 I4/mmm (139) mp-1070613 [hull=0.022, icsd=1, PRIMARY]
- papers: Roles of spin fluctuations and rattling in magnetic and thermoelectric properties of AT4Sb12 (A=Ca, Sr, Ba, La; T=Fe, Ru, Os)

## Ru-Sm-Sn
- rank 2366 | 2 samples | 2 papers | 1 compositions
- compositions: SmRuSn3 (2)
- measured range: 10-298 K (5th-95th pct of 3 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Sm(Sn3Ru2)2 I-42m (121) mp-20208 [hull=0.000, icsd=1, PRIMARY]; SmSn3Ru Pm-3n (223) mp-1201411 [hull=0.006, icsd=1, PRIMARY]; Sm3Sn13Ru4 Pm-3n (223) mp-1209813 [hull=0.000, PRIMARY]
- papers: Transport and magnetic properties of a new valence fluctuating compound SmRuSn3 | Transport and magnetic properties of RERuSn3(RE=La, Ce, Pr, Nd, Sm): a heavy fermion compound CeRuSn3and a new valence fluctuating compound SmRuSn3

## Ru-Sn
- rank 2367 | 2 samples | 1 papers | 2 compositions
- compositions: Ru2Sn3 (1); Ru2Sn2.85 (1)
- measured range: 11-772 K (5th-95th pct of 8 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Sn7Ru3 Im-3m (229) mp-22344 [hull=0.000, icsd=3, PRIMARY]; Sn3Ru2 P-4c2 (116) mp-680677 [hull=0.000, icsd=2, PRIMARY]; Sn3Ru P6_3/mmc (194) mp-1187108 [hull=0.521, PRIMARY]
- papers: Thermoelectric properties of semi-metallic Ru2Sn3−δwith low thermal conductivity

## S-Sb
- rank 2368 | 2 samples | 2 papers | 1 compositions
- compositions: Sb2S3 (2)
- measured range: 10-295 K (5th-95th pct of 2 curves)
- [ref 1] TEDesignLab / ICSD: Sb2S3 Pnma (62) mp-2809 [hull=0.000, icsd=31, PRIMARY]
- [ref 2] MP, ranked by ICSD evidence: SbS P-1 (2) mp-1065860 [hull=0.180, icsd=1, PRIMARY]; Sb17S27 P1 (1) mp-767208 [hull=0.047, PRIMARY]; Sb11S18 P1 (1) mp-753921 [hull=0.053, PRIMARY]; Sb2S3 Pmn2_1 (31) mp-1189633 [hull=0.001, icsd=1]
- papers: Thermoelectric Properties of (Bi1−x Sb x )2S3 with Orthorhombic Structure | Bournonite PbCuSbS3: Stereochemically Active Lone-Pair Electrons that Induce Low Thermal Conductivity

## S-U
- rank 2369 | 2 samples | 1 papers | 1 compositions
- compositions: US (2)
- measured range: 273-1277 K (5th-95th pct of 4 curves; full span incl. outliers 273-1349 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): US Fm-3m (225) mp-2423 [hull=0.000, icsd=22, PRIMARY]; US2 Pnma (62) mp-639 [hull=0.003, icsd=5, PRIMARY]; U3S5 Pnma (62) mp-22536 [hull=0.000, icsd=5, PRIMARY]; U2S3 Pnma (62) mp-22126 [hull=0.000, icsd=5, PRIMARY]; US3 P2_1/m (11) mp-12406 [hull=0.000, icsd=3, PRIMARY]
- papers: Thermoelectric Properties of Uranium Monosulfide, Thorium Monosulfide, and US‐ThS Solid Solutions

## Sb-Sm-Yb
- rank 2370 | 2 samples | 2 papers | 1 compositions
- compositions: Yb3.6Sm0.4Sb3 (2)
- measured range: 289-1278 K (5th-95th pct of 8 curves)
- papers: High-temperature transport properties of complex antimonides with anti-Th3P4structure | High-Temperature Transport Properties of Yb4−x Sm x Sb3

## Sb-Sn
- rank 2371 | 2 samples | 1 papers | 2 compositions
- compositions: Sn0.95Sb0.05 (1); Sn0.9Sb0.1 (1)
- measured range: 10-330 K (5th-95th pct of 4 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): SnSb Fm-3m (225) mp-10635 [hull=0.014, icsd=2, PRIMARY]; Sn3Sb C222 (21) mp-1218972 [hull=0.039, PRIMARY]; SnSb Pm-3m (221) mp-1625 [hull=0.119, icsd=2]; SnSb F-43m (216) mp-16365 [hull=0.187, icsd=1]; SnSb P4/mmm (123) mp-1218920 [hull=0.033]
- papers: Role of chemical doping on the enhancement of thermoelectric performance in metal-based thermoelectric system SnCCo 3

## Sb-U
- rank 2372 | 2 samples | 1 papers | 1 compositions
- compositions: USb (2)
- measured range: 10-21 K (5th-95th pct of 4 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): USb Fm-3m (225) mp-519 [hull=0.076, icsd=9, PRIMARY]; U3Sb4 I-43d (220) mp-392 [hull=0.000, icsd=4, PRIMARY]; USb2 P4/nmm (129) mp-2707 [hull=0.000, icsd=3, PRIMARY]; U5Sb4 P6_3/mcm (193) mp-1207950 [hull=0.008, PRIMARY]; USb3 P6_3/mmc (194) mp-1187807 [hull=0.058, PRIMARY]
- papers: Single-ion-type Kondo resistivity and thermoelectric power in USb antiferromagnet

## Sm-Te-Tl
- rank 2373 | 2 samples | 2 papers | 2 compositions
- compositions: Tl9SmTe6 (1); TlSmTe2 (1)
- measured range: 306-551 K (5th-95th pct of 6 curves; full span incl. outliers 306-682 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Sm(Tl3Te2)3 I4/m (87) mp-1188848 [hull=0.007, icsd=1, PRIMARY]; SmTlTe2 R-3m (166) mp-999132 [hull=0.000, icsd=1, PRIMARY]; Sm3TlTe6 Cmmm (65) mp-1207249 [hull=2.269, PRIMARY]
- papers: Thermoelectric properties of hot-pressed Tl9LnTe6 (Ln=La, Ce, Pr, Nd, Sm, Gd, Tb) and Tl10−xLaxTe6 (0.90⩽x⩽1.05) | Phase diagram of the TlSe-SmSe system and transport properties of TlSmX2 (X = S, Se, Te) crystals

## Sm-Te-Zn
- rank 2374 | 2 samples | 2 papers | 1 compositions
- compositions: Sm2ZnTe (2)
- measured range: 220-374 K (5th-95th pct of 4 curves)
- papers: Thermoelectric Power and Electron Scattering in Metal Alloys | Thermoelectric properties of rare-earth alloys

## Sm-Zn
- rank 2375 | 2 samples | 2 papers | 1 compositions
- compositions: SmZn (2)
- measured range: 214-374 K (5th-95th pct of 4 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Sm2Zn17 R-3m (166) mp-30712 [hull=0.000, icsd=2, PRIMARY]; SmZn12 I4/mmm (139) mp-30870 [hull=0.000, icsd=2, PRIMARY]; SmZn Pm-3m (221) mp-2165 [hull=0.000, icsd=2, PRIMARY]; SmZn2 Imma (74) mp-962 [hull=0.000, icsd=2, PRIMARY]; Sm3Zn11 Immm (71) mp-1103573 [hull=0.000, icsd=1, PRIMARY]
- papers: Thermoelectric Power and Electron Scattering in Metal Alloys | Thermoelectric properties of rare-earth alloys

## Te-Tl-Zr
- rank 2376 | 2 samples | 2 papers | 2 compositions
- compositions: Tl4ZrTe4 (1); Tl2ZrTe3 (1)
- measured range: 296-568 K (5th-95th pct of 8 curves)
- papers: Syntheses, crystal structures and thermoelectric properties of two new thallium tellurides: Tl4ZrTe4 and Tl4HfTe4 | Structural, Thermal, and Physical Properties of the Thallium Zirconium Telluride Tl2ZrTe3

## Te-Yb
- rank 2377 | 2 samples | 1 papers | 2 compositions
- compositions: (YbTe)0.95(YbSb)0.05 (1); (YbTe) (1)
- dopant candidates (<5% at.): Sb (1)
- measured range: 300-769 K (5th-95th pct of 2 curves; full span incl. outliers 300-820 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): YbTe Fm-3m (225) mp-1779 [hull=0.000, icsd=7, PRIMARY]; Yb2Te3 Fddd (70) mp-1189945 [hull=0.391, icsd=1, PRIMARY]; YbTe2 P4/nmm (129) mp-1077459 [hull=0.122, icsd=1, PRIMARY]; Yb2Te3 P4/mmm (123) mp-1206896 [hull=2.331]
- papers: Synthesis and Thermoelectric Properties of the YbTe-YbSb System

## V
- rank 2378 | 2 samples | 2 papers | 1 compositions
- compositions: V (2)
- measured range: 18-299 K (5th-95th pct of 2 curves; full span incl. outliers 18-1534 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): V Im-3m (229) mp-1056037 [hull=0.000, icsd=22, PRIMARY]; V Fm-3m (225) mp-8632 [hull=0.252, icsd=1]
- papers: Intrinsic thermoelectric power of group VB metals | Thermoelectric properties of vanadium

## Ag-Au-Se
- rank 2379 | 1 samples | 1 papers | 1 compositions
- compositions: Ag3AuSe2 (1)
- measured range: 321-498 K (5th-95th pct of 1 curves)
- [ref 1] TEDesignLab / ICSD: Ag3AuSe2 I4_132 (214) mp-3172 [hull=0.000, icsd=2, PRIMARY]
- papers: Synthesis and Thermoelectric Properties of Noble Metal Ternary Chalcogenide Systems of Ag–Au–Se in the Forms of Alloyed Nanoparticles and Colloidal Nanoheterostructures

## Ag-B-I-O
- rank 2380 | 1 samples | 1 papers | 1 compositions
- compositions: (AgI)0.79(Ag2O)0.21(B2O3)0.21 (1)
- measured range: 337-490 K (5th-95th pct of 1 curves)
- papers: Thermoelectric power of the vitreous electrolyte (AgI)0.79(Ag2O.B2O3)0.21

## Ag-Bi-Cd-Se
- rank 2381 | 1 samples | 1 papers | 1 compositions
- compositions: CdAg2Bi6Se11 (1)
- measured range: 319-853 K (5th-95th pct of 5 curves)
- papers: Six Quaternary Chalcogenides of the Pavonite Homologous Series with Ultralow Lattice Thermal Conductivity

## Ag-Bi-Co-O-Sr
- rank 2382 | 1 samples | 1 papers | 1 compositions
- compositions: Ag1.2Bi2Sr2Co2O8.6 (1)
- measured range: 332-973 K (5th-95th pct of 3 curves)
- papers: High temperature thermoelectric properties of Bi2Sr2Co2Oy/Ag composites

## Ag-Bi-O-S
- rank 2383 | 1 samples | 1 papers | 1 compositions
- compositions: BiAgOS (1)
- measured range: 303-313 K (5th-95th pct of 1 curves)
- papers: Substituting Copper with Silver in the BiMOCh Layered Compounds (M = Cu or Ag; Ch = S, Se, or Te): Crystal, Electronic Structure, and Optoelectronic Properties

## Ag-Cd-Eu-Sb
- rank 2384 | 1 samples | 1 papers | 1 compositions
- compositions: Eu9Cd3.8Ag1.4Sb9 (1)
- measured range: 298-770 K (5th-95th pct of 4 curves)
- papers: Coinage-Metal-Stuffed Eu9Cd4Sb9: Metallic Compounds with Anomalous Low Thermal Conductivities

## Ag-Cd-In-Te
- rank 2385 | 1 samples | 1 papers | 1 compositions
- compositions: Ag0.4Cd0.5In2.2Te4 (1)
- measured range: 325-674 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Cd2In3Ag3Te8 P-4 (81) mp-1226985 [hull=0.007, PRIMARY]; Cd2InAgTe4 I-42m (121) mp-1226959 [hull=0.006, PRIMARY]; CdInAgTe3 Cm (8) mp-1226727 [hull=0.014, PRIMARY]
- papers: Silver Indium Telluride Semiconductors and Their Solid Solutions with Cadmium Indium Telluride: Structure and Physical Properties

## Ag-Ce-Ge
- rank 2386 | 1 samples | 1 papers | 1 compositions
- compositions: Ce3Ag4Ge4 (1)
- measured range: 10-295 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ce3(AgGe)4 Immm (71) mp-640597 [hull=0.000, icsd=3, PRIMARY]; Ce(AgGe)2 I4/mmm (139) mp-12063 [hull=0.000, icsd=2, PRIMARY]; CeAgGe P6_3mc (186) mp-11215 [hull=0.000, icsd=1, PRIMARY]; Ce2AgGe6 Amm2 (38) mp-1206886 [hull=0.091, PRIMARY]; Ce8Ag6Ge8O Pmc2_1 (26) mp-1229274 [hull=0.000, PRIMARY]
- papers: Magnetic, electronic and transport properties of the Ce3Ag4X4 (X=Ge, Sn) compounds

## Ag-Ce-Sn
- rank 2387 | 1 samples | 1 papers | 1 compositions
- compositions: Ce3Ag4Sn4 (1)
- measured range: 11-297 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ce5AgSn3 P6_3/mcm (193) mp-1213880 [hull=0.000, icsd=1, PRIMARY]; CeAgSn P6_3mc (186) mp-31420 [hull=0.000, icsd=1, PRIMARY]; Ce2AgSn Fm-3m (225) mp-1183725 [hull=0.085, PRIMARY]; CeAgSn P-3m1 (164) mp-1226708 [hull=0.163]
- papers: Magnetic, electronic and transport properties of the Ce3Ag4X4 (X=Ge, Sn) compounds

## Ag-Cr-Mg-O
- rank 2388 | 1 samples | 1 papers | 1 compositions
- compositions: AgCr0.8Mg0.2O2 (1)
- measured range: 168-300 K (5th-95th pct of 1 curves)
- papers: Facile chemical solution synthesis of p-type delafossite Ag-based transparent conducting AgCrO<sub>2</sub> films in an open condition

## Ag-Cu-In
- rank 2389 | 1 samples | 1 papers | 1 compositions
- compositions: Ag0.32Cu0.43In0.25 (1)
- measured range: 328-559 K (5th-95th pct of 4 curves)
- papers: Compatibility between Co-Metallized PbTe Thermoelectric Legs and an Ag–Cu–In Brazing Alloy

## Ag-Eu-Sb
- rank 2390 | 1 samples | 1 papers | 1 compositions
- compositions: EuAgSb (1)
- measured range: 303-782 K (5th-95th pct of 6 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): EuAgSb P6_3/mmc (194) mp-22707 [hull=0.000, icsd=2, PRIMARY]; Eu(Ag2Sb)2 R-3m (166) mp-1078223 [hull=0.011, icsd=1, PRIMARY]; Eu2AgSb Fm-3m (225) mp-1183942 [hull=0.037, PRIMARY]
- papers: Promising Zintl-Phase Thermoelectric Compound SrAgSb

## Ag-Eu-Si
- rank 2391 | 1 samples | 1 papers | 1 compositions
- compositions: EuAg2Si2 (1)
- measured range: 11-269 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Eu(SiAg)2 I4/mmm (139) mp-22653 [hull=0.000, icsd=2, PRIMARY]; Eu2Si3Ag Fddd (70) mp-1191372 [hull=0.000, icsd=1, PRIMARY]; EuSiAg P-6m2 (187) mp-1225142 [hull=0.081, PRIMARY]
- papers: Interaction of the components in the systems Ce–Ag–Si at 500°C and Eu–Ag–Si at 400°C

## Ag-Ga-S-Se
- rank 2392 | 1 samples | 1 papers | 1 compositions
- compositions: Ag9Ga(S0.85Se0.15)6 (1)
- measured range: 298-804 K (5th-95th pct of 6 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ga2Ag2Se3S C2 (5) mp-1224864 [hull=0.006, PRIMARY]; Ga2Ag2SeS3 C2 (5) mp-1224856 [hull=0.005, PRIMARY]; GaAgSeS Cc (9) mp-1224820 [hull=0.006, PRIMARY]; GaAgSeS I2_12_12_1 (24) mp-1224845 [hull=0.008]
- papers: Thermoelectric properties of Ag9GaS6 with ultralow lattice thermal conductivity

## Ag-Ge-Nd
- rank 2393 | 1 samples | 1 papers | 1 compositions
- compositions: NdAg2Ge2 (1)
- measured range: 12-296 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Nd(AgGe)2 I4/mmm (139) mp-4229 [hull=0.000, icsd=4, PRIMARY]; Nd2AgGe6 Amm2 (38) mp-1206791 [hull=0.104, PRIMARY]; Nd3(AgGe)4 Immm (71) mp-1206903 [hull=0.000, PRIMARY]
- papers: Magnetic, electronic and transport properties of RAg2Ge2 (R=Pr, Nd) compounds

## Ag-Ge-Pb-Te
- rank 2394 | 1 samples | 1 papers | 1 compositions
- compositions: Ge0.77Ag0.11Pb0.12Te (1)
- measured range: 299-801 K (5th-95th pct of 5 curves)
- papers: High figure-of-merit and power generation in high-entropy GeTe-based thermoelectrics

## Ag-Ge-Pr
- rank 2395 | 1 samples | 1 papers | 1 compositions
- compositions: PrAg2Ge2 (1)
- measured range: 11-295 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Pr(AgGe)2 I4/mmm (139) mp-5564 [hull=0.000, icsd=2, PRIMARY]; Pr2AgGe6 Amm2 (38) mp-1205983 [hull=0.104, PRIMARY]; Pr3(AgGe)4 Immm (71) mp-1205486 [hull=0.000, PRIMARY]; PrAgGe P6_3mc (186) mp-1206286 [hull=0.000, PRIMARY]
- papers: Magnetic, electronic and transport properties of RAg2Ge2 (R=Pr, Nd) compounds

## Ag-H-I-Te
- rank 2396 | 1 samples | 1 papers | 1 compositions
- compositions: Ag9TITe5 (1)
- papers: Promoting SnTe as an Eco-Friendly Solution for p-PbTe Thermoelectric via Band Convergence and Interstitial Defects

## Ag-I
- rank 2397 | 1 samples | 1 papers | 1 compositions
- compositions: AgI (1)
- measured range: 820-1050 K (5th-95th pct of 3 curves)
- [ref 1] TEDesignLab / ICSD: AgI F-43m (216) mp-22925 [hull=0.000, icsd=11]
- [ref 2] MP, ranked by ICSD evidence: AgI P6_3mc (186) mp-22894 [hull=0.001, icsd=16, PRIMARY]; AgI2 P-4m2 (115) mp-33154 [hull=0.137, PRIMARY]; AgI Fm-3m (225) mp-22919 [hull=0.092, icsd=6]; AgI Pm-3m (221) mp-22915 [hull=0.388, icsd=2]; AgI I-4m2 (119) mp-684580 [hull=0.002]
- papers: Thermoelectric properties of molten Bi2Te3, CuI, and AgI

## Ag-In-Pr
- rank 2398 | 1 samples | 1 papers | 1 compositions
- compositions: PrInAg2 (1)
- measured range: 13-291 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Pr2InAg P4/mmm (123) mp-1219894 [hull=0.000, PRIMARY]; Pr2InAg Fm-3m (225) mp-978100 [hull=0.002]
- papers: Non-enhancement of thermoelectric-power coefficient of at low temperatures

## Ag-K-Mo-Se
- rank 2399 | 1 samples | 1 papers | 1 compositions
- compositions: Ag3K2Mo15Se19 (1)
- measured range: 299-793 K (5th-95th pct of 4 curves)
- papers: Unravelling the Beneficial Influence of Ag insertion on the Thermoelectric Properties of the Cluster Compound K2Mo15Se19

## Ag-Li-O-Ru
- rank 2400 | 1 samples | 1 papers | 1 compositions
- compositions: Ag3LiRu2O6 (1)
- measured range: 14-300 K (5th-95th pct of 1 curves)
- papers: Interlayer tuning of electronic and magnetic properties in honeycomb ordered Ag3LiRu2O6
