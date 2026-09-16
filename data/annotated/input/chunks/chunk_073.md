# Host systems -- chunk 073 of 73

Ranks 3601-3648 by sample count. These 48 host systems cover 48 samples (0.09% of the TE set); cumulative through this chunk: 100.00%.

Assign each host system a structural prototype from `data/annotated/taxonomy/prototypes_seed_v3.json`, or propose a new one in `taxonomy/prototypes_proposed.jsonl` first. Append results to `data/annotated/annotations/family_assignments.jsonl`.

The hand-entered MaterialFamily labels are deliberately NOT shown here -- they are held out in `df_host_systems.parquet` to validate this classification later. Decide from the compositions.

A "seed hypothesis" line means the taxonomy already names this host under that prototype. Confirm it against the compositions rather than accepting it; two or more listed means the host is mixed and needs splitting per composition.

Evidence follows the project precedence. Your judgement about the thermoelectric chemistry decides the prototype. [ref 1] is TEDesignLab, ICSD-backed and thermoelectric-specific -- prefer it. [ref 2] is Materials Project. Within a formula, polymorphs are ranked by ICSD reference count and the top one is marked PRIMARY -- not by e_above_hull, which is unusable for layered chalcogenides in the 2019 dump (Sb2Te3 R-3m carries 26 ICSD refs at hull 1.02). A primary resting on fewer than 5 ICSD references is flagged weak; the ambient phase may simply be absent from the snapshot, as it is for Bi2Se3.

While you have the host in view, also record what each minor element DOES, in `dopant_roles` -- the role follows from the prototype and cannot be judged without it. A median host has 2 such elements. Not everything listed is a dopant: O, C, N and H are usually milling or pressing residue, and an element just under 5 at.% may be an alloying end member rather than dilute doping. The doping LEVEL is computed later from the parsed fractions -- do not work it out by hand here.

A polymorph list is NOT a thermal sequence. SnSe has three known structures but only Pnma -> Cmcm happens on heating; rocksalt SnSe is metastable (2 icsd refs against 32). Put thermally reached phases in `phases` with their transition temperatures, and everything else in `other_polymorphs` with an occurrence reason. hull and icsd counts are shown to help you tell them apart.

A host may need MORE THAN ONE prototype. Transport is measured across a wide window and many thermoelectrics transform inside it, so where a "MEASUREMENT CROSSES A TRANSITION" line appears, record each phase with its own temperature range in the `phases` field. Transition temperatures shown are approximate and composition-dependent.

Both references describe which phases EXIST in a chemistry, not which phase this paper made. Al-O-Zn is best attested as ZnAl2O4 spinel (227) while almost every sample in it is Al-doped wurtzite ZnO (186). Weigh them against the compositions; do not follow them blindly.

## Pr-Rh
- rank 3601 | 1 samples | 1 papers | 1 compositions
- compositions: Pr7Rh3 (1)
- measured range: 10-288 K (5th-95th pct of 2 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): PrRh2 Fd-3m (227) mp-2529 [hull=0.000, icsd=2, PRIMARY]; Pr3Rh2 R-3 (148) mp-1104158 [hull=0.000, icsd=1, PRIMARY]; Pr7Rh3 P6_3mc (186) mp-1106086 [hull=0.000, icsd=1, PRIMARY]; PrRh Cmcm (63) mp-999305 [hull=0.000, icsd=1, PRIMARY]; Pr4Rh Fd-3m (227) mp-1209468 [hull=0.417, PRIMARY]
- papers: Magnetic and electrical properties of the intermetallic compounds R7Rh3 (R=La, Ce, Pr and Nd)

## Pr-Ru-Sb
- rank 3602 | 1 samples | 1 papers | 1 compositions
- compositions: PrRu4Sb12 (1)
- measured range: 20-262 K (5th-95th pct of 1 curves)
- papers: Transport properties in the filled-skutterudite compounds RERu4Sb12 (RE La, Ce, Pr and Nd); an exotic heavy fermion semimetal CeRu4Sb12

## Pr-Ru-Sn
- rank 3603 | 1 samples | 1 papers | 1 compositions
- compositions: PrRuSn3 (1)
- measured range: 10-297 K (5th-95th pct of 3 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): PrSn3Ru Pm-3n (223) mp-1198507 [hull=0.000, icsd=2, PRIMARY]; PrSnRu Pnma (62) mp-21010 [hull=0.000, icsd=1, PRIMARY]; Pr3Sn13Ru4 Pm-3n (223) mp-1210053 [hull=0.000, PRIMARY]; Pr(Sn3Ru2)2 I-42m (121) mp-1206351 [hull=0.000, PRIMARY]
- papers: Transport and magnetic properties of RERuSn3(RE=La, Ce, Pr, Nd, Sm): a heavy fermion compound CeRuSn3and a new valence fluctuating compound SmRuSn3

## Pr-Se-Tl
- rank 3604 | 1 samples | 1 papers | 1 compositions
- compositions: TlPrSe2 (1)
- measured range: 308-831 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): PrTlSe2 R-3m (166) mp-999289 [hull=0.000, icsd=1, PRIMARY]
- papers: []

## Pr-Te-Tl
- rank 3605 | 1 samples | 1 papers | 1 compositions
- compositions: Tl9PrTe6 (1)
- measured range: 315-550 K (5th-95th pct of 5 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): PrTlTe2 R-3m (166) mp-999288 [hull=0.000, icsd=1, PRIMARY]
- papers: Thermoelectric properties of hot-pressed Tl9LnTe6 (Ln=La, Ce, Pr, Nd, Sm, Gd, Tb) and Tl10−xLaxTe6 (0.90⩽x⩽1.05)

## Pt-Sb-Sc
- rank 3606 | 1 samples | 1 papers | 1 compositions
- compositions: ScPtSb (1)
- measured range: 92-400 K (5th-95th pct of 2 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): ScSbPt F-43m (216) mp-7173 [hull=0.000, icsd=1, PRIMARY]
- papers: Thermoelectrical properties of the compounds ScMVIIISb and YMVIIISb (MVIII   Ni, Pd, Pt)

## Pt-Sc
- rank 3607 | 1 samples | 1 papers | 1 compositions
- compositions: Sc57Pt13_1_1 (1)
- measured range: 15-299 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): ScPt3 Pm-3m (221) mp-481 [hull=0.000, icsd=4, PRIMARY]; ScPt Pm-3m (221) mp-892 [hull=0.000, icsd=2, PRIMARY]; Sc57Pt13 Pm-3 (200) mp-1196981 [hull=0.000, icsd=1, PRIMARY]; Sc2Pt Pnma (62) mp-11550 [hull=0.000, icsd=1, PRIMARY]
- papers: Electrical resistivity of crystal approximants in Sc-based alloys

## Pt-Sn-U
- rank 3608 | 1 samples | 1 papers | 1 compositions
- compositions: U3Pt3Sn4 (1)
- measured range: 13-349 K (5th-95th pct of 3 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): USnPt P-62m (189) mp-1080562 [hull=0.000, icsd=1, PRIMARY]; U2SnPt2 P4/mbm (127) mp-1080130 [hull=0.038, icsd=1, PRIMARY]; U3Sn4Pt3 I-43d (220) mp-1189480 [hull=0.005, icsd=1, PRIMARY]; USnPt2 P6_3/mmc (194) mp-1078970 [hull=0.075, icsd=1, PRIMARY]; USnPt F-43m (216) mp-30848 [hull=0.084, icsd=1]
- papers: Uranium-based materials for thermoelectric applications

## Pt-Sn-Yb
- rank 3609 | 1 samples | 1 papers | 1 compositions
- compositions: Yb2Pt3Sn5 (1)
- measured range: 10-497 K (5th-95th pct of 3 curves; full span incl. outliers 10-545 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): YbSnPt P-62m (189) mp-22779 [hull=0.000, icsd=2, PRIMARY]; Yb2Sn5Pt3 Pnma (62) mp-21820 [hull=0.000, icsd=1, PRIMARY]
- papers: Magnetic and Thermoelectric Properties of a Heterogeneous Mixed-Valence System, Yb2Pt3Sn5

## Re-Ti
- rank 3610 | 1 samples | 1 papers | 1 compositions
- compositions: Re24Ti5 (1)
- measured range: 10-297 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ti5Re24 I-43m (217) mp-518 [hull=0.000, icsd=3, PRIMARY]; TiRe Pm-3m (221) mp-2179 [hull=0.000, icsd=2, PRIMARY]; Ti2Re P-3m1 (164) mp-1018125 [hull=0.000, icsd=1, PRIMARY]; Ti21Re25 R-3c (167) mp-1196561 [hull=0.083, icsd=1, PRIMARY]
- papers: Investigation of normal and superconducting states in noncentrosymmetric Re24Ti5

## Re-W
- rank 3611 | 1 samples | 1 papers | 1 compositions
- compositions: W74.25Re25.75 (1)
- measured range: 270-1306 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Re2W P6_3/mmc (194) mp-1102921 [hull=0.202, icsd=1, PRIMARY]; Re3W I4/mmm (139) mp-974416 [hull=0.127, PRIMARY, AMBIGUOUS]; ReW2 Fmmm (69) mp-1219490 [hull=0.105, PRIMARY]; ReW3 Pm-3n (223) mp-1206445 [hull=0.060, PRIMARY]; ReW4 Fmmm (69) mp-1219494 [hull=0.068, PRIMARY]
- papers: Electronic transport properties of liquid Ga–Zn alloys

## Rh
- rank 3612 | 1 samples | 1 papers | 1 compositions
- compositions: Rh (1)
- measured range: 90-1400 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Rh Fm-3m (225) mp-74 [hull=0.000, icsd=12, PRIMARY]; Rh P6_3/mmc (194) mp-1186916 [hull=0.024]
- papers: Measurement and Calculation of the Absolute Thermoelectric Power of Rhodium and Iridium

## Rh-Sb-U
- rank 3613 | 1 samples | 1 papers | 1 compositions
- compositions: U3Rh3Sb4 (1)
- measured range: 13-274 K (5th-95th pct of 2 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): U3Sb4Rh3 I-43d (220) mp-971830 [hull=0.000, icsd=1, PRIMARY]; USbRh F-43m (216) mp-10624 [hull=0.098, icsd=1, PRIMARY]
- papers: Coexistence of antiferromagnetic and spin-glass behaviour in U3Rh3Sb4

## Rh-Sc
- rank 3614 | 1 samples | 1 papers | 1 compositions
- compositions: Sc57Rh13_1_1 (1)
- measured range: 16-299 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): ScRh3 Pm-3m (221) mp-635 [hull=0.000, icsd=3, PRIMARY]; ScRh Pm-3m (221) mp-1780 [hull=0.000, icsd=2, PRIMARY]; Sc57Rh13 Pm-3 (200) mp-30863 [hull=0.000, icsd=1, PRIMARY]; Sc50In3Rh13 Fm-3 (202) mp-1210379 [hull=0.000, PRIMARY]; Sc5BRh15 P4/mmm (123) mp-1219416 [hull=0.007, PRIMARY]
- papers: Electrical resistivity of crystal approximants in Sc-based alloys

## Rh-Si-U
- rank 3615 | 1 samples | 1 papers | 1 compositions
- compositions: U2Rh3Si5 (1)
- measured range: 11-294 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): U(SiRh)2 I4/mmm (139) mp-5556 [hull=0.000, icsd=6, PRIMARY]; USiRh Pnma (62) mp-20184 [hull=0.000, icsd=3, PRIMARY]; U2Si5Rh3 C2/c (15) mp-1189009 [hull=0.008, icsd=1, PRIMARY]; U2Si3Rh Pmm2 (25) mp-1216620 [hull=0.034, PRIMARY]; U2Si5Rh3 Ibam (72) mp-1187808 [hull=0.000]
- papers: Transport and magnetic properties of U2M3Si5 silicides (M = Co, Rh, Ru)

## Rh-Sn-Te
- rank 3616 | 1 samples | 1 papers | 1 compositions
- compositions: RhSn1.5Te1.5 (1)
- measured range: 71-874 K (5th-95th pct of 4 curves; full span incl. outliers 71-979 K)
- papers: Electronic structure and thermoelectric properties of pnictogen-substituted ASn1.5Te1.5 (A = Co, Rh, Ir) skutterudites

## Rh-Sn-U
- rank 3617 | 1 samples | 1 papers | 1 compositions
- compositions: U2Rh2Sn (1)
- measured range: 11-50 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): U2SnRh2 P4/mbm (127) mp-639876 [hull=0.000, icsd=3, PRIMARY]; USnRh P-62m (189) mp-1079696 [hull=0.000, icsd=3, PRIMARY]; U3Sn13Rh4 Pm-3n (223) mp-12717 [hull=0.040, icsd=1, PRIMARY]; USnRh2 Pnma (62) mp-1207880 [hull=0.000, PRIMARY]
- papers: Low-temperature transport properties of U2Rh2Sn and U2Fe2Sn

## Ru
- rank 3618 | 1 samples | 1 papers | 1 compositions
- compositions: Sr2Ru09975Ti0.0025O4 (1)
- dopant candidates (<5% at.): O (1), Sr (1), Ti (1)
- measured range: 11-20 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ru P6_3/mmc (194) mp-1061133 [hull=0.000, icsd=17, PRIMARY]; Ru Fm-3m (225) mp-8639 [hull=0.116, icsd=1]
- papers: Effect of Ti substitution on the residual resistivity in the spin-triplet superconductor Sr2RuO4

## Ru-Sb-Zn
- rank 3619 | 1 samples | 1 papers | 1 compositions
- compositions: Ru9Zn7Sb8 (1)
- measured range: 16-300 K (5th-95th pct of 2 curves; full span incl. outliers 16-675 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Zn7Sb8Ru9 Fm-3m (225) mp-981247 [hull=0.000, icsd=1, PRIMARY]; Zn11SbRu3 Ama2 (40) mp-1215721 [hull=0.008, PRIMARY]; ZnSbRu2 Immm (71) mp-1093589 [hull=2.794, PRIMARY]
- papers: Ru9Zn7Sb8: A Structure with a 2 × 2 × 2 Supercell of the Half-Heusler Phase

## Ru-Sc
- rank 3620 | 1 samples | 1 papers | 1 compositions
- compositions: Sc57Ru13_1_1 (1)
- measured range: 16-298 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): ScRu Pm-3m (221) mp-30867 [hull=0.000, icsd=1, PRIMARY]; Sc44Ru7 F-43m (216) mp-1209947 [hull=0.000, PRIMARY]; Sc57Ru13 Pm-3 (200) mp-1210377 [hull=0.000, PRIMARY]; Sc5Ru3 P6_3/mcm (193) mp-1209003 [hull=0.000, PRIMARY]; ScRu3 I4/mmm (139) mp-973022 [hull=0.247, PRIMARY, AMBIGUOUS]
- papers: Electrical resistivity of crystal approximants in Sc-based alloys

## Ru-Sn-Th
- rank 3621 | 1 samples | 1 papers | 1 compositions
- compositions: Th2Ru2Sn (1)
- measured range: 10-301 K (5th-95th pct of 2 curves; full span incl. outliers 10-377 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Th3Sn13Ru4 Pm-3n (223) mp-1211693 [hull=0.015, PRIMARY]; ThSnRu2 Fm-3m (225) mp-865944 [hull=0.000, PRIMARY]
- papers: Magnetic, thermodynamic, NMR, and transport properties of the heavy-fermion semiconductor<mml:math xmlns:mml=\"http://www.w3.org/1998/Math/MathML\" display=\"inline\"><mml:mrow><mml:msub><mml:mrow><mml:mi mathvariant=\"normal\">U</mml:mi></mml:mrow><mml:mrow><mml:mn>2</mml:mn></mml:mrow></mml:msub></mml:mrow><mml:mrow><mml:msub><mml:mrow><mml:mi mathvariant=\"normal\">Ru</mml:mi></mml:mrow><mml:mrow><mml:mn>2</mml:mn></mml:mrow></mml:msub></mml:mrow><mml:mi mathvariant=\"normal\">Sn</mml:mi></mml:math>

## Ru-Zn
- rank 3622 | 1 samples | 1 papers | 1 compositions
- compositions: YbRu2Zn20 (1)
- dopant candidates (<5% at.): Yb (1)
- measured range: 12-299 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Zn3Ru I4/mmm (139) mp-1380 [hull=0.000, icsd=3, PRIMARY]; U(Zn10Ru)2 Fd-3m (227) mp-1199869 [hull=0.000, icsd=1, PRIMARY]; Y(Zn10Ru)2 Fd-3m (227) mp-640315 [hull=0.000, icsd=1, PRIMARY]; Zn6Ru P4_132 (213) mp-1205290 [hull=0.000, icsd=1, PRIMARY]
- papers: Thermoelectric power of the YbT2Zn20(T=Fe, Ru, Os, Ir, Rh, and Co) heavy fermions

## S-Sb-Te
- rank 3623 | 1 samples | 1 papers | 1 compositions
- compositions: Sb2Te2S (1)
- measured range: 11-293 K (5th-95th pct of 4 curves)
- papers: Thermoelectric properties of the tetradymite-type Bi2Te2S–Sb2Te2S solid solution

## S-Sm-Tl
- rank 3624 | 1 samples | 1 papers | 1 compositions
- compositions: TlSmS2 (1)
- measured range: 350-782 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): SmTlS2 R-3m (166) mp-999138 [hull=0.000, icsd=1, PRIMARY]
- papers: Phase diagram of the TlSe-SmSe system and transport properties of TlSmX2 (X = S, Se, Te) crystals

## S-Ta-Ti
- rank 3625 | 1 samples | 1 papers | 1 compositions
- compositions: Ti0.6Ta0.4S2 (1)
- measured range: 299-699 K (5th-95th pct of 5 curves)
- papers: Thermoelectric properties in the series Ti1-xTaxS2

## S-Th
- rank 3626 | 1 samples | 1 papers | 1 compositions
- compositions: ThS (1)
- measured range: 291-1250 K (5th-95th pct of 2 curves; full span incl. outliers 291-1337 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): ThS2 Pnma (62) mp-1146 [hull=0.000, icsd=5, PRIMARY]; ThS Fm-3m (225) mp-503 [hull=0.000, icsd=5, PRIMARY]; Th2S5 Pbcn (60) mp-1666 [hull=0.000, icsd=3, PRIMARY]; Th2S3 Pnma (62) mp-20163 [hull=0.000, icsd=2, PRIMARY]; Th3S I4/mmm (139) mp-978993 [hull=0.751, PRIMARY, AMBIGUOUS]
- papers: Thermoelectric Properties of Uranium Monosulfide, Thorium Monosulfide, and US‐ThS Solid Solutions

## Sb-Sc
- rank 3627 | 1 samples | 1 papers | 1 compositions
- compositions: ScSb (1)
- measured range: 11-299 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): ScSb Fm-3m (225) mp-549 [hull=0.000, icsd=5, PRIMARY]; Sc2Sb P4/nmm (129) mp-7192 [hull=0.000, icsd=2, PRIMARY]; Sc5Sb3 Pnma (62) mp-1209044 [hull=0.000, icsd=1, PRIMARY]; Sc3Sb I4/mmm (139) mp-978546 [hull=0.091, PRIMARY]; Sc3Sb2 P4/mmm (123) mp-1212550 [hull=3.388, PRIMARY]
- papers: Specific heat and NMR evidence for the low Fermi-level density of states in semimetallic ScSb

## Sb-Se-Sn-Te
- rank 3628 | 1 samples | 1 papers | 1 compositions
- compositions: Sn0.839Sb0.107Te0.839Se0.161 (1)
- measured range: 297-812 K (5th-95th pct of 5 curves)
- papers: Achieving Enhanced Thermoelectric Performance in (SnTe)1-x(Sb2Te3)x and (SnTe)1-y(Sb2Se3)y Synthesized via Solvothermal Reaction and Sintering

## Sb-Se-U
- rank 3629 | 1 samples | 1 papers | 1 compositions
- compositions: USbSe (1)
- measured range: 13-287 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): USbSe P4/nmm (129) mp-9937 [hull=0.000, icsd=2, PRIMARY]; U2SbSe2 P4/mmm (123) mp-1207046 [hull=1.301, PRIMARY]
- papers: Electrical transport properties of USbSe and USbTe

## Sb-Se-Zn
- rank 3630 | 1 samples | 1 papers | 1 compositions
- compositions: (Cu3SbSe4)0.11Zn4Sb3 (1)
- dopant candidates (<5% at.): Cu (1)
- measured range: 299-650 K (5th-95th pct of 5 curves)
- papers: Enhanced thermoelectric performance of β-Zn4Sb3 based composites incorporated with large proportion of nanophase Cu3SbSe4

## Sb-Ti
- rank 3631 | 1 samples | 1 papers | 1 compositions
- compositions: TiSb2 (1)
- measured range: 61-298 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ti3Sb Pm-3n (223) mp-1412 [hull=0.000, icsd=7, PRIMARY]; TiSb2 I4/mcm (140) mp-568 [hull=0.000, icsd=5, PRIMARY]; Ti5Sb3 Pnma (62) mp-22033 [hull=0.000, icsd=3, PRIMARY]; TiSb P6_3/mmc (194) mp-2187 [hull=0.000, icsd=3, PRIMARY]; Ti13Sb3 Pmm2 (25) mp-1217255 [hull=0.039, PRIMARY]
- papers: Constitution of the binary M-Sb systems (M = Ti, Zr, Hf) and physical properties of MSb 2

## Sb-Zr
- rank 3632 | 1 samples | 1 papers | 1 compositions
- compositions: ZrSb2 (1)
- measured range: 71-297 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Zr5Sb3 P6_3/mcm (193) mp-2649 [hull=0.008, icsd=5, PRIMARY]; ZrSb2 Pnnm (58) mp-979 [hull=0.000, icsd=3, PRIMARY]; Zr2Sb I4/mmm (139) mp-31379 [hull=0.003, icsd=2, PRIMARY]; Zr3Sb I-4 (82) mp-1105139 [hull=0.000, icsd=2, PRIMARY]; ZrSb Cmcm (63) mp-10638 [hull=0.008, icsd=1, PRIMARY]
- papers: Constitution of the binary M-Sb systems (M = Ti, Zr, Hf) and physical properties of MSb 2

## Sc-Sr-Te
- rank 3633 | 1 samples | 1 papers | 1 compositions
- compositions: SrSc2Te4 (1)
- measured range: 161-294 K (5th-95th pct of 2 curves; full span incl. outliers 161-425 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Sr(ScTe2)2 Pnma (62) mp-18660 [hull=0.019, icsd=1, PRIMARY]
- papers: Thermoelectric properties of the new tellurides SrSc2Te4 and BaSc2Te4 in comparison to BaY2Te4

## Sc-Te
- rank 3634 | 1 samples | 1 papers | 1 compositions
- compositions: Sc2Te3 (1)
- measured range: 301-1099 K (5th-95th pct of 6 curves)
- [ref 1] TEDesignLab / ICSD: Sc2Te3 Fddd (70) mp-12383 [hull=0.022, icsd=1, PRIMARY]
- [ref 2] MP, ranked by ICSD evidence: ScTe P6_3/mmc (194) mp-10026 [hull=0.000, icsd=1, PRIMARY]; Sc2Te Pnma (62) mp-21576 [hull=0.000, icsd=1, PRIMARY]; Sc9Te2 Cmc2_1 (36) mp-1197413 [hull=0.000, icsd=1, PRIMARY]; Sc3Te P6_3/mmc (194) mp-1186975 [hull=0.195, PRIMARY]; Sc3Te4 R3m (160) mp-1219373 [hull=0.052, PRIMARY]
- papers: Thermoelectric Properties of Scandium Sesquitelluride

## Se-Sm-Tl
- rank 3635 | 1 samples | 1 papers | 1 compositions
- compositions: TlSmSe2 (1)
- measured range: 315-714 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): SmTlSe2 R-3m (166) mp-999137 [hull=0.000, icsd=1, PRIMARY]
- papers: Phase diagram of the TlSe-SmSe system and transport properties of TlSmX2 (X = S, Se, Te) crystals

## Se-Sr-Ti
- rank 3636 | 1 samples | 1 papers | 1 compositions
- compositions: Sr0.2TiSe2 (1)
- measured range: 320-650 K (5th-95th pct of 1 curves)
- papers: Thermoelectric performance of layered SrxTiSe2above 300 K

## Se-Ti-Tl
- rank 3637 | 1 samples | 1 papers | 1 compositions
- compositions: Tl5AgTi6Se27 (1)
- dopant candidates (<5% at.): Ag (1)
- measured range: 85-300 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ti5TlSe8 C2/m (12) mp-8244 [hull=0.002, icsd=2, PRIMARY]
- papers: Exploring Thallium Compounds as Thermoelectric Materials:  Seventeen New Thallium Chalcogenides

## Se-Tl
- rank 3638 | 1 samples | 1 papers | 1 compositions
- compositions: Tl66Se34 (1)
- measured range: 742-975 K (5th-95th pct of 2 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): TlSe I4/mcm (140) mp-1078808 [hull=0.000, icsd=6, PRIMARY]; Tl2Se3 C2/c (15) mp-1080677 [hull=0.013, icsd=1, PRIMARY]; Tl5Se3 P4/ncc (130) mp-21657 [hull=0.007, icsd=1, PRIMARY]; TlSe Pm-3m (221) mp-10647 [hull=0.203, icsd=1]
- papers: The thermoelectric figure of merit of poor thermal conductors

## Se-Tl-V
- rank 3639 | 1 samples | 1 papers | 1 compositions
- compositions: TlV5Se8 (1)
- measured range: 12-672 K (5th-95th pct of 3 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Tl3VSe4 I-43m (217) mp-1025549 [hull=0.000, icsd=2, PRIMARY]
- papers: The solid solution series Tl(V1−xCrx)5Se8: crystal structure, magnetic and thermoelectric properties

## Se-Zr
- rank 3640 | 1 samples | 1 papers | 1 compositions
- compositions: ZrSe2 (1)
- measured range: 12-292 K (5th-95th pct of 3 curves)
- [ref 1] TEDesignLab / ICSD: ZrSe3 P2_1/m (11) mp-1683 [hull=0.000, icsd=5, PRIMARY]
- [ref 2] MP, ranked by ICSD evidence: ZrSe2 P-3m1 (164) mp-2076 [hull=0.000, icsd=9, PRIMARY]; Zr2Se Pnnm (58) mp-22642 [hull=0.000, icsd=3, PRIMARY]; Zr2Se3 C2/m (12) mp-1215598 [hull=0.000, PRIMARY]; Zr3Se P6_3/mmc (194) mp-1188055 [hull=0.432, PRIMARY]; Zr3Se4 Cmmm (65) mp-1215400 [hull=0.075, PRIMARY]
- papers: Thermoelectric Properties of Li-Intercalated ZrSe2 Single Crystals

## Si-W
- rank 3641 | 1 samples | 1 papers | 1 compositions
- compositions: W0.05P0.02Si0.93 (1)
- dopant candidates (<5% at.): P (1)
- measured range: 294-1209 K (5th-95th pct of 4 curves; full span incl. outliers 294-1255 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Si2W I4/mmm (139) mp-1620 [hull=0.000, icsd=9, PRIMARY]; Si3W5 I4/mcm (140) mp-31219 [hull=0.020, icsd=2, PRIMARY]; Si2W3 P4/mbm (127) mp-1079377 [hull=0.207, icsd=1, PRIMARY]; Si3W P6_3/mmc (194) mp-972748 [hull=0.658, PRIMARY]; Si2W P6_222 (180) mp-8939 [hull=0.066, icsd=2]
- papers: Microwave plasma synthesis of Si/Ge and Si/WSi2nanoparticles for thermoelectric applications

## Sm
- rank 3642 | 1 samples | 1 papers | 1 compositions
- compositions: Sm (1)
- measured range: 19-299 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Sm R-3m (166) mp-86 [hull=0.008, icsd=4, PRIMARY]; Sm P6_3/mmc (194) mp-69 [hull=0.000, icsd=3]; Sm Fm-3m (225) mp-21377 [hull=0.011, icsd=1]
- papers: Electric Evolution in Sputter-Deposited Sn&lt;sub&gt;&lt;i&gt;c&lt;/i&gt;&lt;sub&gt;Sn&lt;/sub&gt;&lt;/sub&gt;Si&lt;sub&gt;1−&lt;i&gt;c&lt;/i&gt;&lt;sub&gt;Sn&lt;/sub&gt;&lt;/sub&gt; Alloy Films

## Sn-Ti
- rank 3643 | 1 samples | 1 papers | 1 compositions
- compositions: Ti3Sn (1)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ti3Sn P6_3/mmc (194) mp-21030 [hull=0.004, icsd=5, PRIMARY]; Ti6Sn5 P6_3/mmc (194) mp-20382 [hull=0.000, icsd=4, PRIMARY]; Ti5Sn3 P6_3/mcm (193) mp-20847 [hull=0.000, icsd=4, PRIMARY]; Ti2Sn P6_3/mmc (194) mp-30875 [hull=0.000, icsd=3, PRIMARY]; Ti2Sn3 Cmce (64) mp-637255 [hull=0.000, icsd=3, PRIMARY]
- papers: The anomalous low temperature lattice thermal conductivity of VP3Sn and related compounds

## Sn-Ti-V
- rank 3644 | 1 samples | 1 papers | 1 compositions
- compositions: V2.4Ti0.6Sn (1)
- measured range: 11-16 K (5th-95th pct of 1 curves)
- papers: The anomalous low temperature lattice thermal conductivity of VP3Sn and related compounds

## Sn-V
- rank 3645 | 1 samples | 1 papers | 1 compositions
- compositions: V3Sn (1)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): V3Sn Pm-3n (223) mp-21342 [hull=0.000, icsd=7, PRIMARY]; VSn2 Fddd (70) mp-20887 [hull=0.000, icsd=2, PRIMARY]; VSn3 P6_3/mmc (194) mp-1187826 [hull=0.490, PRIMARY]; V3Sn P6_3/mmc (194) mp-22211 [hull=0.041, icsd=2]
- papers: The anomalous low temperature lattice thermal conductivity of VP3Sn and related compounds

## Tb-Te-Tl
- rank 3646 | 1 samples | 1 papers | 1 compositions
- compositions: Tl9TbTe6 (1)
- measured range: 312-552 K (5th-95th pct of 5 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): TbTlTe2 R-3m (166) mp-999121 [hull=0.000, icsd=1, PRIMARY]
- papers: Thermoelectric properties of hot-pressed Tl9LnTe6 (Ln=La, Ce, Pr, Nd, Sm, Gd, Tb) and Tl10−xLaxTe6 (0.90⩽x⩽1.05)

## Tb-Zn
- rank 3647 | 1 samples | 1 papers | 1 compositions
- compositions: TbZn (1)
- measured range: 13-258 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): TbZn Pm-3m (221) mp-836 [hull=0.000, icsd=11, PRIMARY]; TbZn2 Imma (74) mp-2338 [hull=0.000, icsd=3, PRIMARY]; Tb2Zn17 P6_3/mmc (194) mp-30880 [hull=0.002, icsd=2, PRIMARY]; TbZn12 I4/mmm (139) mp-1104493 [hull=0.007, icsd=2, PRIMARY]; Tb3Zn11 Immm (71) mp-1104325 [hull=0.000, icsd=1, PRIMARY]
- papers: Electrical and thermoelectric transport properties of RZn and RCd compounds (R = Tb, Gd, Nd, Pr)

## Te-U
- rank 3648 | 1 samples | 1 papers | 1 compositions
- compositions: UTe2 (1)
- measured range: 12-68 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): UTe2 Immm (71) mp-666 [hull=0.000, icsd=18, PRIMARY]; UTe Fm-3m (225) mp-912986 [hull=0.098, icsd=10, PRIMARY]; U2Te3 Pnma (62) mp-619501 [hull=0.014, icsd=4, PRIMARY]; U3Te4 I-43d (220) mp-20520 [hull=0.026, icsd=4, PRIMARY]; UTe5 Pnma (62) mp-28500 [hull=0.002, icsd=2, PRIMARY]
- papers: Fermi-Surface Instability in the Heavy-Fermion Superconductor \n<mml:math xmlns:mml=\"http://www.w3.org/1998/Math/MathML\" display=\"inline\"><mml:mrow><mml:msub><mml:mrow><mml:mi>UTe</mml:mi></mml:mrow><mml:mrow><mml:mn>2</mml:mn></mml:mrow></mml:msub></mml:mrow></mml:math>
