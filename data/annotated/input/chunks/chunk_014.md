# Host systems -- chunk 014 of 73

Ranks 651-700 by sample count. These 50 host systems cover 484 samples (0.93% of the TE set); cumulative through this chunk: 84.81%.

Assign each host system a structural prototype from `data/annotated/taxonomy/prototypes_seed_v3.json`, or propose a new one in `taxonomy/prototypes_proposed.jsonl` first. Append results to `data/annotated/annotations/family_assignments.jsonl`.

The hand-entered MaterialFamily labels are deliberately NOT shown here -- they are held out in `df_host_systems.parquet` to validate this classification later. Decide from the compositions.

A "seed hypothesis" line means the taxonomy already names this host under that prototype. Confirm it against the compositions rather than accepting it; two or more listed means the host is mixed and needs splitting per composition.

Evidence follows the project precedence. Your judgement about the thermoelectric chemistry decides the prototype. [ref 1] is TEDesignLab, ICSD-backed and thermoelectric-specific -- prefer it. [ref 2] is Materials Project. Within a formula, polymorphs are ranked by ICSD reference count and the top one is marked PRIMARY -- not by e_above_hull, which is unusable for layered chalcogenides in the 2019 dump (Sb2Te3 R-3m carries 26 ICSD refs at hull 1.02). A primary resting on fewer than 5 ICSD references is flagged weak; the ambient phase may simply be absent from the snapshot, as it is for Bi2Se3.

While you have the host in view, also record what each minor element DOES, in `dopant_roles` -- the role follows from the prototype and cannot be judged without it. A median host has 2 such elements. Not everything listed is a dopant: O, C, N and H are usually milling or pressing residue, and an element just under 5 at.% may be an alloying end member rather than dilute doping. The doping LEVEL is computed later from the parsed fractions -- do not work it out by hand here.

A polymorph list is NOT a thermal sequence. SnSe has three known structures but only Pnma -> Cmcm happens on heating; rocksalt SnSe is metastable (2 icsd refs against 32). Put thermally reached phases in `phases` with their transition temperatures, and everything else in `other_polymorphs` with an occurrence reason. hull and icsd counts are shown to help you tell them apart.

A host may need MORE THAN ONE prototype. Transport is measured across a wide window and many thermoelectrics transform inside it, so where a "MEASUREMENT CROSSES A TRANSITION" line appears, record each phase with its own temperature range in the `phases` field. Transition temperatures shown are approximate and composition-dependent.

Both references describe which phases EXIST in a chemistry, not which phase this paper made. Al-O-Zn is best attested as ZnAl2O4 spinel (227) while almost every sample in it is Al-doped wurtzite ZnO (186). Weigh them against the compositions; do not follow them blindly.

## Ca-Fe-Mo-O
- rank 651 | 10 samples | 3 papers | 8 compositions
- compositions: Ca2FeMoO6 (3); Ca1.7Sr0.3FeMoO6 (1); Ca1.9Sr0.1FeMoO6 (1); Ca1.8Sr0.2FeMoO6 (1); Ca1.9La0.1FeMoO6 (1); Ca1.8La0.2FeMoO6 (1)
- dopant candidates (<5% at.): La (4), Sr (3)
- seed hypothesis (confirm): double_perovskite
- measured range: 28-1247 K (5th-95th pct of 27 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ca2FeMoO6 P2_1/c (14) mp-18783 [hull=0.001, icsd=1, PRIMARY]; CaFe(MoO3)2 P2_1/c (14) mp-1214052 [hull=0.173, PRIMARY]
- papers: Structure and thermoelectric properties of Ca2−xSrxFeMoO6 (0≤x≤0.3) double-perovskite oxides | Effect of alkaline-earth and transition metals on the electrical transport of double perovskites | Disorder induced magnetism and electrical conduction in La doped Ca2FeMoO6 double perovskite

## Cd-Yb
- rank 652 | 10 samples | 5 papers | 7 compositions
- compositions: Cd6Yb (3); Cd84Yb16 (2); Cd86Yb14 (1); Cd83Yb17 (1); Cd85Yb15 (1); Cd5.7Yb (1)
- measured range: 11-300 K (5th-95th pct of 31 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): YbCd Pm-3m (221) mp-1857 [hull=0.000, icsd=3, PRIMARY]; YbCd2 P6_3/mmc (194) mp-1102731 [hull=0.012, icsd=1, PRIMARY]; Yb3Cd Pm-3m (221) mp-1187925 [hull=0.073, PRIMARY]; YbCd3 Fm-3m (225) mp-865366 [hull=0.000, PRIMARY, AMBIGUOUS]; YbCd6 I23 (197) mp-680604 [hull=0.000, PRIMARY, AMBIGUOUS]
- papers: Thermoelectric properties of binary Cd-Yb quasicrystals and Cd6Yb | Electronic transport in Cd–Yb and Y–Mg–Zn quasicrystals | Thermoelectric Properties of Binary Cd–Yb Quasicrystal and Its Approximant

## Ce-Cu-La-Si
- rank 653 | 10 samples | 4 papers | 7 compositions
- compositions: Ce0.7La0.3Cu2.05Si2 (2); Ce0.5La0.5Cu2.05Si2 (2); Ce0.3La0.7Cu2.05Si2 (2); CeLaCu2Si2 (1); Ce0.7La0.3Cu2Si2 (1); Ce0.3La0.7Cu2Si2 (1)
- seed hypothesis (confirm): thcr2si2_122
- solid-solution axis: Ce/(Ce+La) spans 0.30-0.70 (median 0.50) over 7 compositions
     ISOELECTRONIC SERIES: the parent compound depends on the composition, not on this host. Near either end the minor element is a dilute substituent; in the middle it is a genuine alloy. Record the axis, not one parent -- and note the 5% split used the whole formula, not the sublattice, so its cut lands at a different level on each site.
- measured range: 10-330 K (5th-95th pct of 12 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): LaCe(CuSi)4 P4/mmm (123) mp-1225580 [hull=0.002, PRIMARY]
- papers: Electric and magnetic properties of the Kondo-lattice compound CeCu2Si2 | Nernst Effect: Evidence of Local Kondo Scattering in Heavy Fermions | Transport properties of the<mml:math xmlns:mml=\"http://www.w3.org/1998/Math/MathML\" display=\"inline\"><mml:mrow><mml:msub><mml:mrow><mml:mi mathvariant=\"normal\">Ce</mml:mi></mml:mrow><mml:mrow><mml:mi>x</mml:mi></mml:mrow></mml:msub></mml:mrow><mml:mrow><mml:msub><mml:mrow><mml:mi mathvariant=\"normal\">La</mml:mi></mml:mrow><mml:mrow><mml:mn>1</mml:mn><mml:mi>−</mml:mi><mml:mi>x</mml:mi></mml:mrow></mml:msub></mml:mrow><mml:mrow><mml:msub><mml:mrow><mml:mi mathvariant=\"normal\">Cu</mml:mi></mml:mrow><mml:mrow><mml:mn>2.05</mml:mn></mml:mrow></mml:msub></mml:mrow><mml:mrow><mml:msub><mml:mrow><mml:mi mathvariant=\"normal\">Si</mml:mi></mml:mrow><mml:mrow><mml:mn>2</mml:mn></mml:mrow></mml:msub></mml:mrow></mml:math>heavy-fermion alloy system

## Ce-Ga-Pd
- rank 654 | 10 samples | 4 papers | 6 compositions
- compositions: CePd2Ga (4); CePdGa (2); CePd0.4Ga3.6 (1); CePd0.8Ga3.2 (1); CePd0.5Ga3.5 (1); CePd0.6Ga3.4 (1)
- measured range: 10-296 K (5th-95th pct of 10 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): CeGaPd2 Pnma (62) mp-639863 [hull=0.000, icsd=3, PRIMARY]; CeGa3Pd2 P6/mmm (191) mp-3494 [hull=0.000, icsd=2, PRIMARY]; Ce(GaPd)2 P4/nmm (129) mp-1095071 [hull=0.000, icsd=1, PRIMARY]; Ce2Ga10Pd I4/mmm (139) mp-12746 [hull=0.007, icsd=1, PRIMARY]; Ce8GaPd24 Pm-3m (221) mp-1195670 [hull=0.029, icsd=1, PRIMARY]
- papers: Suppression of ferromagnetism in solid solution CePdxGa4−x | Magnetic, thermal and transport properties of a CePd2Ga single crystal | Magnetic transport and neutron scattering studies on ternary equiatomic compound: CePdGa

## Ce-Ge-Pt
- rank 655 | 10 samples | 7 papers | 5 compositions
- compositions: CePt4Ge12 (4); CePtGe (3); Ce3Pt4Ge6 (1); Pr0.125Ce0.875Pt4Ge12 (1); CePt4Ge11.5Sb0.5 (1)
- dopant candidates (<5% at.): Pr (1), Sb (1)
- measured range: 10-308 K (5th-95th pct of 19 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ce(GePt)2 P4/nmm (129) mp-20400 [hull=0.000, icsd=1, PRIMARY]; Ce(Ge3Pt)4 Im-3 (204) mp-1190040 [hull=0.000, icsd=1, PRIMARY]; CeGe2Pt Immm (71) mp-1189580 [hull=0.000, icsd=1, PRIMARY]; CeGePt Pmmn (59) mp-627355 [hull=0.000, icsd=1, PRIMARY]; Ce2Ge6Pt Amm2 (38) mp-1206251 [hull=0.047, PRIMARY]
- papers: Thermoelectric Properties of Correlated Electron Systems Ln 3Pt4Ge6and LnPt4Ge12(Ln = Ce, Pr) and Non-centrosymmetric X 2 T 12P7(X = Yb, Hf and T = Fe, Co) | Thermoelectric power of CeTGe (T: Ni, Pd and Pt) | Probing the superconductivity ofPrPt4Ge12through Ce substitution

## Ce-O
- rank 656 | 10 samples | 5 papers | 4 compositions
- compositions: CeO2 (6); Gd0.1Ce0.9O2 (2); (Ce3Si2)3.86(CeO2)96.14 (1); Ce0.9Sm0.1O1.95 (1)
- dopant candidates (<5% at.): Gd (2), Si (1), Sm (1)
- measured range: 75-1273 K (5th-95th pct of 10 curves; full span incl. outliers 75-1868 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): CeO2 Fm-3m (225) mp-20194 [hull=0.000, icsd=49, PRIMARY]; Ce2O3 P-3m1 (164) mp-2721 [hull=0.039, icsd=6, PRIMARY]; Ce7O12 R-3 (148) mp-2629 [hull=0.000, icsd=3, PRIMARY]; CeO3 P6_3/m (176) mp-1205900 [hull=0.503, icsd=1, PRIMARY]; CeO Fm-3m (225) mp-10688 [hull=0.000, icsd=1, PRIMARY]
- papers: Thermoelectric power of Gd-doped CeO2 (Gd0.1Ce0.9O(2−δ) (GDC10)): Measurements on porous samples | Fabrication and thermal conductivity of CeO2–Ce3Si2 composite | Applicability of CeO2 as a surrogate for PuO2 in a MOX fuel development

## Ce-Pd-Rh
- rank 657 | 10 samples | 2 papers | 5 compositions
- compositions: CePd0.6Rh0.4 (6); Ce(Pd0.85Rh0.09Ag0.06)3 (1); Ce(Pd0.85Rh0.15)3B0.05 (1); Ce(Pd0.91Rh0.09)3B0.05 (1); 	CePd0.6Rh0.4 (1)
- dopant candidates (<5% at.): B (2), Ag (1)
- measured range: 10-300 K (5th-95th pct of 24 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ce2(PdRh)3 Pmmm (47) mp-1226828 [hull=0.031, PRIMARY]; CePdRh2 P4/mmm (123) mp-1226507 [hull=0.039, PRIMARY]
- papers: The influence of substitution and doping on the thermoelectric properties of CePd<inf>3</inf> | Multiprobe high-pressure experiments in<mml:math xmlns:mml=\"http://www.w3.org/1998/Math/MathML\" altimg=\"si0002.gif\" overflow=\"scroll\"><mml:msub><mml:mrow><mml:mi>CePd</mml:mi></mml:mrow><mml:mrow><mml:mn>0.6</mml:mn></mml:mrow></mml:msub><mml:msub><mml:mrow><mml:mi>Rh</mml:mi></mml:mrow><mml:mrow><mml:mn>0.4</mml:mn></mml:mrow></mml:msub></mml:math>and<mml:math xmlns:mml=\"http://www.w3.org/1998/Math/MathML\" altimg=\"si0001.gif\" overflow=\"scroll\"><mml:msub><mml:mrow><mml:mi>CePd</mml:mi></mml:mrow><mml:mrow><mml:mn>3</mml:mn></mml:mrow></mml:msub></mml:math>

## Co-Cu-O
- rank 658 | 10 samples | 3 papers | 5 compositions
- compositions: CuCoO2 (3); CuCo0.9998Mg0.0002O2 (2); CuCo0.9991Mg0.0009O2 (2); CuCo0.9984Mg0.0016O2 (2); Co1.6Cu0.4O4 (1)
- dopant candidates (<5% at.): Mg (6)
- measured range: 11-423 K (5th-95th pct of 11 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Co(CuO2)4 P-1 (2) mp-773271 [hull=0.039, PRIMARY]; Co(CuO3)2 Fmmm (69) mp-1226484 [hull=0.323, PRIMARY]; Co11CuO16 P2/m (10) mp-761492 [hull=0.101, PRIMARY]; Co21Cu3O32 R3m (160) mp-761377 [hull=0.006, PRIMARY]; Co25Cu11O48 Cm (8) mp-762204 [hull=0.004, PRIMARY]
- papers: Characterization of delafossite-type CuCoO2 prepared by ion exchange | Electrical resistivity and thermopower of hole-doped delafossite CuCoO2 polycrystals | Impurity-induced transition and impurity-enhanced thermopower in the thermoelectric oxide<mml:math xmlns:mml=\"http://www.w3.org/1998/Math/MathML\" display=\"inline\"><mml:mrow><mml:msub><mml:mrow><mml:mi mathvariant=\"normal\">NaCo</mml:mi></mml:mrow><mml:mrow><mml:mn>2</mml:mn><mml:mi>−</mml:mi><mml:mi>x</mml:mi></mml:mrow></mml:msub></mml:mrow><mml:mrow><mml:msub><mml:mrow><mml:mi mathvariant=\"normal\">Cu</mml:mi></mml:mrow><mml:mrow><mml:mi>x</mml:mi></mml:mrow></mml:msub></mml:mrow><mml:mrow><mml:msub><mml:mrow><mml:mi mathvariant=\"normal\">O</mml:mi></mml:mrow><mml:mrow><mml:mn>4</mml:mn></mml:mrow></mml:msub></mml:mrow></mml:math>

## Co-Ge-S
- rank 659 | 10 samples | 1 papers | 10 compositions
- compositions: Co2Ge3S3 (1); Co2Ge2.99Cd0.01S3 (1); Co2Ge2.99Zn0.01S3 (1); Co2Ge2.95Zn0.05S3 (1); Co2Ge2.97Cd0.03S3 (1); Co2Ge2.95Cd0.05S3 (1)
- dopant candidates (<5% at.): Cd (3), Zn (3), Bi (3)
- measured range: 300-766 K (5th-95th pct of 50 curves)
- [ref 1] TEDesignLab / ICSD: Co2(GeS)3 (146)
- [ref 2] MP, ranked by ICSD evidence: Co2(GeS)3 R-3 (148) mp-2956 [hull=0.000, icsd=3, PRIMARY]; Co2(GeS)3 C2/m (12) mp-1226567 [hull=0.257]
- papers: Enhancement of thermoelectric properties by partial substitution of Ge sites in anion ring [Ge2S2]4- found in Co2Ge3S3 skutterudite-based material

## Co-Hf-Ir-Sb-Zr
- rank 660 | 10 samples | 2 papers | 8 compositions
- compositions: Zr0.5Hf0.5Co0.5Ir0.5Sb0.99Sn0.01 (3); Zr0.5Hf0.5Co0.7Ir0.3Sb0.99Sn0.01 (1); Zr0.5Hf0.5Co0.3Ir0.7Sb0.99Sn0.01 (1); (Zr0.5Hf0.5Co0.5Ir0.5Sb0.99Sn0.01)98.95(CoSb)1.05 (1); (Zr0.5Hf0.5Co0.5Ir0.5Sb0.99Sn0.01)97.93(CoSb)2.07 (1); (Zr0.5Hf0.5Co0.5Ir0.5Sb0.99Sn0.01)95.94(CoSb)4.06 (1)
- dopant candidates (<5% at.): Sn (10)
- solid-solution axis: Co/(Co+Ir) spans 0.30-0.70 (median 0.52) over 8 compositions
     ISOELECTRONIC SERIES: the parent compound depends on the composition, not on this host. Near either end the minor element is a dilute substituent; in the middle it is a genuine alloy. Record the axis, not one parent -- and note the 5% split used the whole formula, not the sublattice, so its cut lands at a different level on each site.
- measured range: 299-774 K (5th-95th pct of 50 curves)
- papers: Effects of Ir Substitution and Processing Conditions on Thermoelectric Performance of p-Type Zr0.5Hf0.5Co1−x Ir x Sb0.99Sn0.01 Half-Heusler Alloys | Spinodal Decomposition in Off-stoichiometric Zr<sub>0.5</sub>Hf<sub>0.5</sub>Co<sub>1-y</sub>Ir<sub>y</sub>Sb<sub>1-z</sub>Sn<sub>z</sub> half-Heusler Phases

## Co-Hf-Sb
- rank 661 | 10 samples | 8 papers | 4 compositions
- compositions: HfCoSb (7); HfCoSb0.85Sn0.15 (1); Hf6CoSb2 (1); Hf0.88Nb0.12CoSb (1)
- dopant candidates (<5% at.): Sn (1), Nb (1)
- seed hypothesis (confirm): half_heusler
- measured range: 12-1164 K (5th-95th pct of 28 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Hf6CoSb2 P-62m (189) mp-1206239 [hull=0.000, PRIMARY]; HfCo2Sb Immm (71) mp-1097490 [hull=2.825, PRIMARY]
- papers: Thermoelectric and Thermophysical Properties of TiCoSb-ZrCoSb-HfCoSb Pseudo Ternary System Prepared by Spark Plasma Sintering | Short and long range order of Half-Heusler phases in (Ti,Zr,Hf)CoSb thermoelectric compounds | Thermoelectric and thermophysical properties of TiCoSb, ZrCoSb, HfCoSb prepared by SPS

## Co-Mn-Sb-V
- rank 662 | 10 samples | 1 papers | 8 compositions
- compositions: CoV0.6Mn0.4Sb (3); CoV0.4Mn0.6Sb (1); CoV0.2Mn0.8Sb (1); CoV0.75Mn0.25Sb (1); CoV0.7Mn0.3Sb (1); CoV0.55Mn0.45Sb (1)
- measured range: 10-300 K (5th-95th pct of 17 curves)
- papers: Galvanomagnetic properties of disordered Mn semi-Heusler phases with Anderson localisation

## Co-Zr
- rank 663 | 10 samples | 1 papers | 1 compositions
- compositions: CoZr2 (10)
- seed hypothesis (confirm): cual2_c16
- measured range: 10-391 K (5th-95th pct of 11 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): ZrCo2 Fd-3m (227) mp-929 [hull=0.000, icsd=21, PRIMARY]; ZrCo Pm-3m (221) mp-2283 [hull=0.000, icsd=6, PRIMARY]; Zr2Co I4/mcm (140) mp-628 [hull=0.000, icsd=5, PRIMARY]; Zr6Co23 Fm-3m (225) mp-30569 [hull=0.000, icsd=4, PRIMARY]; Zr3Co Cmcm (63) mp-30619 [hull=0.000, icsd=3, PRIMARY]
- papers: Anisotropy of the normal state properties of the superconducting Co1?x Ni x Zr2 system

## Cr-Fe-Zr
- rank 664 | 10 samples | 1 papers | 8 compositions
- compositions: ZrFe1.4Cr0.6 (2); ZrFe0.5Cr1.5 (2); ZrFe1.75Cr0.25 (1); ZrFe1.8Cr0.2 (1); ZrFe1.65Cr0.35 (1); ZrFe1.6Cr0.4 (1)
- measured range: 15-302 K (5th-95th pct of 14 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Zr2Cr3Fe Amm2 (38) mp-1215757 [hull=0.029, PRIMARY]; Zr2CrFe3 Amm2 (38) mp-1215712 [hull=0.027, PRIMARY]; ZrCrFe Amm2 (38) mp-1215295 [hull=0.031, PRIMARY]; Zr2CrFe3 P6_3/mmc (194) mp-1215662 [hull=0.038]; ZrCrFe F-43m (216) mp-631429 [hull=0.891]
- papers: Electrical transport properties of ZrFe2−xCrxHy

## Cr-La-Mn-O-Sr
- rank 665 | 10 samples | 2 papers | 4 compositions
- compositions: La0.75Sr0.25Cr0.5Mn0.5O3 (5); La0.75Sr0.25Cr0.4Mn0.6O3 (2); La0.75Sr0.25Cr0.6Mn0.4O3 (2); La0.75Sr0.25Cr0.3Mn0.7O3 (1)
- measured range: 574-1172 K (5th-95th pct of 10 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Sr3LaMnCrO8 Amm2 (38) mp-1218443 [hull=0.000, PRIMARY]; SrLa3Mn2Cr2O12 P2 (3) mp-1218286 [hull=0.015, PRIMARY, AMBIGUOUS]; SrLa3Mn3CrO12 R3 (146) mp-1218266 [hull=0.011, PRIMARY]; SrLa3Mn2Cr2O12 C2 (5) mp-1218313 [hull=0.020]; SrLa3Mn2Cr2O12 P1 (1) mp-1218314 [hull=0.033]
- papers: Cr doping effect in B-site of La0.75Sr0.25MnO3 on its phase stability and performance as an SOFC anode | La0.75Sr0.25Cr0.5Mn0.5O3−δ+Cu composite anode running on H2 and CH4 fuels

## Eu-Ga-Ge
- rank 666 | 10 samples | 4 papers | 1 compositions
- compositions: Eu8Ga16Ge30 (10)
- measured range: 10-760 K (5th-95th pct of 16 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Eu3(Ga2Ge3)2 C2/m (12) mp-1193402 [hull=0.000, icsd=1, PRIMARY]; EuGaGe P6_3/mmc (194) mp-1101845 [hull=0.000, icsd=1, PRIMARY]; Eu(GaGe2)2 Cmcm (63) mp-1225812 [hull=0.063, PRIMARY]
- papers: High-temperature thermoelectric properties of α- and β-Eu/sub 8/Ga/sub 16/Ge/sub 30/ | Towards strongly correlated semimetals: U2Ru2Sn and Eu8Ga16Ge30 | Nanostructured clathrates and clathrate-based nanocomposites

## Eu-In-Sb
- rank 667 | 10 samples | 2 papers | 9 compositions
- compositions: Eu5In2Sb6 (2); Eu5In1.975Zn0.025Sb6 (1); Eu5In1.95Zn0.05Sb6 (1); Eu5In1.9Zn0.1Sb6 (1); Eu5In1.8Zn0.2Sb6 (1); Eu5In1.98Cd0.02Sb6 (1)
- dopant candidates (<5% at.): Zn (4), Cd (4)
- seed hypothesis (confirm): zintl_5_2_6
- measured range: 303-777 K (5th-95th pct of 45 curves)
- papers: High temperature thermoelectric properties of Zn-doped Eu5In2Sb6 | Cd substitution in Zintl phase Eu5In2Sb6 enhancing the thermoelectric performance

## Fe-La-O-P
- rank 668 | 10 samples | 3 papers | 9 compositions
- compositions: LaFePO (2); LaFePO0.92F0.08 (1); LaFePO0.97F0.03 (1); LaFePO0.9F0.1 (1); LaFePO0.95F0.05 (1); La0.9Sr0.1FePO (1)
- dopant candidates (<5% at.): F (4), Ce (3), Sr (1)
- measured range: 13-298 K (5th-95th pct of 30 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): La2FeP2O P4/mmm (123) mp-1211330 [hull=1.819, PRIMARY]
- papers: Thermoelectric Properties of LaFePO1-xFxand LaFeAsO1-xFx–Possibility of the Hidden Mass Enhancement of LaFeAsO1-xFx– | Three superconducting phases with different categories of pairing in hole- and electron-doped \nLaFeAs1−xPxO | Spin glass, single-ion and dense Kondo effects in La\n                    <sub>1−x</sub>\n                    Ce\n                    <sub>x</sub>\n                    FePO

## Fe-Si-V
- rank 669 | 10 samples | 2 papers | 10 compositions
- compositions: Fe2.6V0.4Si (1); Fe2.2V0.8Si (1); Fe2.8V0.2Si (1); Fe2.08V0.92Si (1); Fe0.7V0.05Si0.25 (1); Fe0.65V0.1Si0.25 (1)
- seed hypothesis (confirm): full_heusler
- measured range: 294-1061 K (5th-95th pct of 34 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): VFe2Si Fm-3m (225) mp-4595 [hull=0.000, icsd=3, PRIMARY]; V2FeSi Ama2 (40) mp-1216581 [hull=0.000, PRIMARY]; V5Fe5Si6 Amm2 (38) mp-1216470 [hull=0.056, PRIMARY]; VFe3Si4 R3 (146) mp-1216327 [hull=0.067, PRIMARY]
- papers: Thermoelectric properties of Fe–V–Si Heusler type compounds | Thermoelectric Properties of Fe-Mn-Si Alloys and Compound Fe3Si doped with Mn and V

## Ga-Rh-U
- rank 670 | 10 samples | 1 papers | 2 compositions
- compositions: URh0.97Pd0.03Ga5 (8); URhGa5 (2)
- dopant candidates (<5% at.): Pd (8)
- measured range: 10-313 K (5th-95th pct of 13 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): UGa5Rh P4/mmm (123) mp-1078033 [hull=0.000, icsd=1, PRIMARY]; UGaRh P-62m (189) mp-1078870 [hull=0.000, icsd=1, PRIMARY]; U2(Ga3Rh)3 Cmcm (63) mp-1208091 [hull=0.024, PRIMARY]
- papers: Effect of Pd for Rh substitution on thermoelectric power in the semimetallic compound URhGa5

## Gd-Nd-S
- rank 671 | 10 samples | 3 papers | 7 compositions
- compositions: NdGdS3 (4); NdGd1.02S3 (1); NdGd1.05S3 (1); NdGd1.08S3 (1); NdGd1.01S3 (1); NdGd1.04S3 (1)
- measured range: 303-976 K (5th-95th pct of 46 curves)
- papers: Synthesis of multinary rare-earth sulfides PrGdS3, NdGdS3, and SmEuGdS4, and investigation of their thermoelectric properties | Thermoelectric properties of NdGdS3 prepared by reaction of oxides with CS2 | Thermoelectric Properties of NdGd1+x S3 Prepared by CS2 Sulfurization

## Hf-O-Sn-Sr-Ti-Zr
- rank 672 | 10 samples | 1 papers | 1 compositions
- compositions: Sr0.9La0.1(Zr0.25Sn0.25Ti0.25Hf0.25)O3 (10)
- dopant candidates (<5% at.): La (10)
- measured range: 292-1073 K (5th-95th pct of 10 curves)
- papers: A novel high-entropy perovskite ceramics Sr0.9La0.1(Zr0.25Sn0.25Ti0.25Hf0.25)O3 with low thermal conductivity and high Seebeck coefficient

## La-O-Zr
- rank 673 | 10 samples | 5 papers | 6 compositions
- compositions: La2Zr2O7 (5); (La0.95Y0.05)2Zr2O7 (1); (La0.85Y0.15)2Zr2O7 (1); (La0.82Y0.18)2(Zr0.98Y0.02)2O6.98 (1); (La0.90Y0.10)2Zr2O7 (1); (La0.78Y0.22)2(Zr0.97Y0.03)2O6.97 (1)
- dopant candidates (<5% at.): Y (5)
- seed hypothesis (confirm): pyrochlore
- measured range: 293-1372 K (5th-95th pct of 10 curves; full span incl. outliers 293-1772 K)
- [ref 1] TEDesignLab / ICSD: La2Zr2O7 Fd-3m (227) mp-4974 [hull=0.000, icsd=8, PRIMARY]
- [ref 2] MP, ranked by ICSD evidence: La3NdZr4O14 R-3m (166) mp-1223092 [hull=0.003, PRIMARY]; La4CeZr3O14 R-3m (166) mp-1223232 [hull=0.338, PRIMARY]; LaZr9O20 P1 (1) mp-675329 [hull=0.078, PRIMARY]; LaZrO3 Pm-3m (221) mp-1185065 [hull=0.290, PRIMARY]; La2Zr2O7 Pmma (51) mp-674999 [hull=0.272]
- papers: Thermophysical properties of rare earth barium aluminates | Zirconates as New Materials for Thermal Barrier Coatings | Investigation of the thermal conductivity of selected compounds of gadolinium and lanthanum

## Li-O-Ti
- rank 674 | 10 samples | 3 papers | 9 compositions
- compositions: Li1.1Ti2O4 (2); LiTi2O4 (1); Li1.1Ti1.9O4 (1); Li0.8Ti2.2O4 (1); Li1.2Ti1.8O4 (1); Li0.9Ti2.1O4 (1)
- dopant candidates (<5% at.): V (2)
- measured range: 10-298 K (5th-95th pct of 10 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): LiTi2O4 Fd-3m (227) mp-5670 [hull=0.000, icsd=6, PRIMARY]; Li2TiO3 C2/c (15) mp-2931 [hull=0.000, icsd=5, PRIMARY]; Li2Ti3O7 P2_1/m (11) mp-1190132 [hull=0.013, icsd=2, PRIMARY]; Li2Ti6O13 C2/m (12) mp-1190625 [hull=0.015, icsd=2, PRIMARY]; LiTiO2 I4_1/amd (141) mp-38280 [hull=0.000, icsd=1, PRIMARY]
- papers: Superconducting and normal state properties of Li1+x Ti2?x O4 spinel compounds. I. Preparation, crystallography, superconducting properties, electrical resistivity, dielectric behavior, and magnetic susceptibility | The V and Mn doping effects on Spinel superconductor LiTi2O4 | []

## Mn-Nd-O
- rank 675 | 10 samples | 5 papers | 7 compositions
- compositions: NdMnO3 (4); Nd0.88Na0.18MnO2.98 (1); Nd0.95Na0.03MnO3.09 (1); Nd0.73Na0.21MnO2.97 (1); Nd0.89Na0.10MnO3.03 (1); Nd0.84Na0.17MnO3.08 (1)
- dopant candidates (<5% at.): Na (6)
- seed hypothesis (confirm): perovskite
- measured range: 11-1073 K (5th-95th pct of 15 curves; full span incl. outliers 11-1239 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): NdMn2O5 Pbam (55) mp-19393 [hull=0.000, icsd=5, PRIMARY]; NdMnO3 Pnma (62) mp-25051 [hull=0.000, icsd=4, PRIMARY]; Nd20Mn20O59 P1 (1) mp-1173621 [hull=0.013, PRIMARY]; Nd20Mn19O60 P-1 (2) mp-1173614 [hull=0.006, PRIMARY]; Nd9Mn10O30 P1 (1) mp-1173531 [hull=0.028, PRIMARY]
- papers: Thermopower and resistivity studies of Nd-Na-Mn-O manganites | Giant magnetothermal conductivity and magnetostriction effect in the charge ordered Nd\n                    0.8\n                    Na\n                    0.2\n                    MnO\n                    3\n                    compound | Anomalous thermal expansion and strong damping of the thermal conductivity ofNdMnO3andTbMnO3due to4fcrystal-field excitations

## Mn-Nd-O-Pb
- rank 676 | 10 samples | 2 papers | 3 compositions
- compositions: Nd0.7Pb0.3MnO3 (5); (La0.35Nd0.65)0.7Pb0.3MnO3 (4); La0.2Nd0.5Pb0.3MnO3 (1)
- dopant candidates (<5% at.): La (5)
- measured range: 10-399 K (5th-95th pct of 14 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Nd5Mn8(PbO8)3 Pm-3m (221) mp-1210163 [hull=0.103, PRIMARY]
- papers: Thermal conductivity of colossal magnetoresistive manganites (La1−xNdx)0.7Pb0.3MnO3 | Variation of magnetic and transport properties in magnetoresistive oxides La-ln-Pb-Mn-O (Ln=Pr, Nd, Dy, and Y)

## Mn-O-Tl
- rank 677 | 10 samples | 4 papers | 7 compositions
- compositions: Tl2Mn2O7 (4); Tl1.95Sc0.05Mn2O7 (1); Tl1.8Sc0.2Mn2O7 (1); Tl1.7Sc0.3Mn2O7 (1); Tl1.6Sc0.4Mn2O7 (1); Tl2Mn1.95Ru0.05O7 (1)
- dopant candidates (<5% at.): Sc (4), Ru (2)
- seed hypothesis (confirm): pyrochlore
- measured range: 10-347 K (5th-95th pct of 10 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Mn2Tl2O7 Fd-3m (227) mp-25554 [hull=0.000, icsd=3, PRIMARY]; MnTlO3 P6_3cm (185) mp-771257 [hull=0.031, PRIMARY]; MnTlO3 Pnma (62) mp-770870 [hull=0.052]; MnTlO3 P2_1/c (14) mp-769883 [hull=0.063]; MnTlO3 R-3 (148) mp-771272 [hull=0.127]
- papers: Carrier density change in the colossal-magnetoresistance pyrochlore<mml:math xmlns:mml=\"http://www.w3.org/1998/Math/MathML\" display=\"inline\"><mml:mrow><mml:msub><mml:mrow><mml:mi mathvariant=\"normal\">Tl</mml:mi></mml:mrow><mml:mrow><mml:mn>2</mml:mn></mml:mrow></mml:msub></mml:mrow><mml:mrow><mml:msub><mml:mrow><mml:mi mathvariant=\"normal\">Mn</mml:mi></mml:mrow><mml:mrow><mml:mn>2</mml:mn></mml:mrow></mml:msub></mml:mrow><mml:mrow><mml:msub><mml:mrow><mml:mi mathvariant=\"normal\">O</mml:mi></mml:mrow><mml:mrow><mml:mn>7</mml:mn></mml:mrow></mml:msub></mml:mrow></mml:math> | Powder magnetoresistance of Tl<sub>2</sub>Mn<sub>2</sub>O<sub>7</sub>and related compounds | Large Enhancement of Magnetoresistance in Tl\n            <sub>2</sub>\n            Mn\n            <sub>2</sub>\n            O\n            <sub>7</sub>\n            : Pyrochlore Versus Perovskite

## N-Nd
- rank 678 | 10 samples | 1 papers | 1 compositions
- compositions: NdN (10)
- measured range: 297-1473 K (5th-95th pct of 10 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): NdN Fm-3m (225) mp-2599 [hull=0.000, icsd=21, PRIMARY]; NdN2 Cm (8) mp-1220310 [hull=0.216, PRIMARY]; NdN Pm-3m (221) mp-1009237 [hull=0.781, icsd=1]
- papers: Thermal properties of polycrystalline NdN bulk samples with various porosities

## Nb-Sb
- rank 679 | 10 samples | 2 papers | 3 compositions
- compositions: NbSb2 (8); (Zn0.005Nb0.995)4Sb3 (1); (Zn0.01Nb0.99)4Sb3 (1)
- dopant candidates (<5% at.): Zn (2)
- seed hypothesis (confirm): marcasite
- measured range: 10-812 K (5th-95th pct of 20 curves; full span incl. outliers 10-856 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Nb3Sb Pm-3n (223) mp-2053 [hull=0.000, icsd=6, PRIMARY]; NbSb2 C2/m (12) mp-1969 [hull=0.000, icsd=5, PRIMARY]; Nb5Sb4 I4/m (87) mp-274 [hull=0.000, icsd=3, PRIMARY]; Nb2Sb P1 (1) mp-673700 [hull=0.301, PRIMARY]; NbSb P6_3/mmc (194) mp-1207123 [hull=0.152, PRIMARY]
- papers: Effects of Nb doping on thermoelectric properties of Zn4Sb3 at high temperatures | Constitution of the systems {V,Nb,Ta}-Sb and physical properties of di-antimonides {V,Nb,Ta}Sb2

## Ni-Sb-Tm
- rank 680 | 10 samples | 5 papers | 1 compositions
- compositions: TmNiSb (10)
- measured range: 10-993 K (5th-95th pct of 19 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): TmNiSb F-43m (216) mp-4025 [hull=0.000, icsd=2, PRIMARY]; Tm5Ni2Sb I4/mcm (140) mp-1207984 [hull=0.000, PRIMARY]
- papers: High-temperature power factor of half-Heusler phases RENiSb (RE = Sc, Dy, Ho, Er, Tm, Lu) | Enhanced thermoelectric power factor of half-Heusler solid solution Sc1-xTmxNiSb prepared by high-pressure high-temperature sintering method | Power factor enhancement in a composite based on the half-Heusler antimonide TmNiSb

## O-Rh-Sr
- rank 681 | 10 samples | 5 papers | 8 compositions
- compositions: Sr2RhO4 (3); Sr5CoRh3O12 (1); SrRhO3 (1); Sr1.9Ce0.1RhO4 (1); Sr1.85Ce0.15RhO4 (1); Sr1.8Ce0.2RhO4 (1)
- dopant candidates (<5% at.): Ce (4), Co (1)
- seed hypothesis (confirm): ruddlesden_popper
- measured range: 11-391 K (5th-95th pct of 10 curves; full span incl. outliers 11-1111 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Sr2RhO4 I4_1/acd (142) mp-757102 [hull=0.000, icsd=1, PRIMARY]; SrRhO3 Pm-3m (221) mp-1017441 [hull=0.102, icsd=1, PRIMARY]; Sr6(RhO3)5 R32 (155) mp-4048 [hull=0.001, icsd=1, PRIMARY]; Sr(RhO2)2 Pmmn (59) mp-766173 [hull=0.000, PRIMARY]; Sr(RhO2)4 C2 (5) mp-1218903 [hull=0.038, PRIMARY]
- papers: Magnetic and thermoelectric properties of quasi-one-dimensional oxides An+2CoBnO3n+3 (A=Ca,Sr, B=Co,Rh,Ir; n=1–3) | Enhanced paramagnetism of the<mml:math xmlns:mml=\"http://www.w3.org/1998/Math/MathML\" display=\"inline\"><mml:mn>4</mml:mn><mml:mi>d</mml:mi></mml:math>itinerant electrons in the rhodium oxide perovskite<mml:math xmlns:mml=\"http://www.w3.org/1998/Math/MathML\" display=\"inline\"><mml:mrow><mml:msub><mml:mrow><mml:mi mathvariant=\"normal\">SrRhO</mml:mi></mml:mrow><mml:mrow><mml:mn>3</mml:mn></mml:mrow></mml:msub></mml:mrow></mml:math> | Universality of charge doping driven metal-insulator transition in \n<mml:math xmlns:mml=\"http://www.w3.org/1998/Math/MathML\"><mml:msub><mml:mrow><mml:mi>Sr</mml:mi></mml:mrow><mml:mn>2</mml:mn></mml:msub><mml:msub><mml:mrow><mml:mi>RhO</mml:mi></mml:mrow><mml:mn>4</mml:mn></mml:msub></mml:math>\n and role of spin-orbit coupling

## Ru-Sb-Ti
- rank 682 | 10 samples | 1 papers | 10 compositions
- compositions: TiRu1.5Sb (1); TiRu1.8Sb (1); TiRu2Sb (1); TiRu1.1Sb (1); TiRu1.3Sb (1); TiRu1.4Sb (1)
- measured range: 340-961 K (5th-95th pct of 26 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): TiSbRu F-43m (216) mp-31458 [hull=0.093, icsd=1, PRIMARY]
- papers: Half-Heusler-like compounds with wide continuous compositions and tunable p- to n-type semiconducting thermoelectrics

## Sb-Se-Te
- rank 683 | 10 samples | 4 papers | 8 compositions
- compositions: Sb2Te2Se (3); Sb2Te2.4Se0.6 (1); Sb2Te1.4Se1.6 (1); Sb2Te1.2Se1.8 (1); Te0.97(Sb2Se3)0.03 (1); Te0.90(Sb2Se3)0.10 (1)
- seed hypothesis (confirm): tetradymite
- solid-solution axis: Se/(Se+Te) spans 0.08-0.60 (median 0.33) over 8 compositions
     ISOELECTRONIC SERIES: the parent compound depends on the composition, not on this host. Near either end the minor element is a dilute substituent; in the middle it is a genuine alloy. Record the axis, not one parent -- and note the 5% split used the whole formula, not the sublattice, so its cut lands at a different level on each site.
- measured range: 13-601 K (5th-95th pct of 33 curves; full span incl. outliers 12-999 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Sb2Te2Se R-3m (166) mp-3525 [hull=0.660, icsd=2, PRIMARY]; Sb2TeSe2 R3m (160) mp-8612 [hull=0.331, icsd=1, PRIMARY]; Sb4(TeSe)3 Cm (8) mp-1219473 [hull=0.500, PRIMARY]; Sb2Te2Se R3m (160) mp-1219475 [hull=0.695]
- papers: Tuning of thermoelectric properties with changing Se content in Sb2Te3 | Valence-band changes inSb2−xInxTe3andSb2Te3−ySeyby transport and Shubnikov–de Haas effect measurements | Low Thermal Conductivity and Optimized Thermoelectric Properties of p-Type Te–Sb2Se3: Synergistic Effect of Doping and Defect Engineering

## Sb-Si-Te
- rank 684 | 10 samples | 1 papers | 4 compositions
- compositions: Sb2Si2Te6 (3); Sb2Si2Te6.93 (3); Sb2Si2Te6.43 (2); Sb2Si2Te7.5 (2)
- measured range: 307-828 K (5th-95th pct of 38 curves)
- papers: High-Performance Thermoelectrics from Cellular Nanostructured Sb2Si2Te6

## Ag-Ba-Sb
- rank 685 | 9 samples | 2 papers | 8 compositions
- compositions: BaAgSb (2); Ba0.99AgSb (1); Ba0.97AgSb (1); Ba0.97Eu0.1AgSb (1); Ba0.98AgSb (1); Ba1.01AgSb (1)
- dopant candidates (<5% at.): Eu (1)
- measured range: 299-1013 K (5th-95th pct of 48 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): BaAgSb P6_3/mmc (194) mp-1205316 [hull=0.000, icsd=1, PRIMARY]; Ba2AgSb Fm-3m (225) mp-984720 [hull=0.023, PRIMARY]
- papers: Point defect approach to enhance the thermoelectric performance of Zintl-phase BaAgSb | Symmetry‐Guaranteed High Carrier Mobility in Quasi‐2D Thermoelectric Semiconductors

## Ag-Bi-Te
- rank 686 | 9 samples | 3 papers | 3 compositions
- compositions: AgBiTe (7); Ag0.4Bi2Te3 (1); Ag1.6969Te0.848Bi0.304Te0.456 (1)
- measured range: 298-580 K (5th-95th pct of 18 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): AgBiTe2 R-3m (166) mp-29656 [hull=0.018, icsd=2, PRIMARY]; Ag(BiTe2)3 Cmmm (65) mp-1206226 [hull=1.500, PRIMARY]; AgBiTe2 P-3m1 (164) mp-1182952 [hull=0.163]; AgBiTe2 P4/mmm (123) mp-1229085 [hull=0.266]
- papers: Improved Thermoelectric Performance of Silver Nanoparticles-Dispersed Bi2Te3Composites Deriving from Hierarchical Two-Phased Heterostructure | Thermoelectric Properties of Silver Telluride–Bismuth Telluride Nanowire Heterostructure Synthesized by Site-Selective Conversion | Thermoelectric Generators from AgBiTe and AgSbTe Thin Films Modified by High-Energy Beam

## Al-B
- rank 687 | 9 samples | 4 papers | 5 compositions
- compositions: AlB12 (5); Y0.62Al1.24B14 (1); Y0.62Al1.55B14 (1); Y0.62Al1.86B14 (1); AlB2 (1)
- dopant candidates (<5% at.): Y (3)
- seed hypothesis (confirm): boron_carbide
- solid-solution axis: Al/(Al+B) spans 0.08-0.33 (median 0.10) over 5 compositions
     ISOELECTRONIC SERIES: the parent compound depends on the composition, not on this host. Near either end the minor element is a dilute substituent; in the middle it is a genuine alloy. Record the axis, not one parent -- and note the 5% split used the whole formula, not the sublattice, so its cut lands at a different level on each site.
- measured range: 80-1138 K (5th-95th pct of 21 curves; full span incl. outliers 79-1231 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): AlB2 P6/mmm (191) mp-944 [hull=0.012, icsd=7, PRIMARY]
- papers: New Synthesis Route for Complex Borides; Rapid Synthesis of Thermoelectric Yttrium Aluminoboride via Liquid-Phase Assisted Reactive Spark Plasma Sintering | Thermal conductivity of PrRh4.8B2, a layered boride compound | The effect of structural defects on thermal conductivity polycrystalline AlB12 and EuB6

## Al-Ce-Nd
- rank 688 | 9 samples | 1 papers | 9 compositions
- compositions: (Ce0.9Nd0.1)3Al (1); (Ce0.4Nd0.6)3Al (1); (Ce0.3Nd0.7)3Al (1); (Ce0.2Nd0.8)3Al (1); (Ce0.7Nd3)3Al (1); (Ce0.8Nd0.2)3Al (1)
- solid-solution axis: Ce/(Ce+Nd) spans 0.19-0.90 (median 0.50) over 9 compositions
     ISOELECTRONIC SERIES: the parent compound depends on the composition, not on this host. Near either end the minor element is a dilute substituent; in the middle it is a genuine alloy. Record the axis, not one parent -- and note the 5% split used the whole formula, not the sublattice, so its cut lands at a different level on each site.
- measured range: 10-295 K (5th-95th pct of 10 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): CeNdAl4 F-43m (216) mp-1226518 [hull=0.019, PRIMARY]
- papers: Physical and magnetic properties of (Ce1−xNdx)3Al (x = 0.3): Coexisting ferromagnetism and Kondo effect

## Al-Ce-Ru
- rank 689 | 9 samples | 3 papers | 5 compositions
- compositions: CeRu2Al10 (5); Ce0.95Y0.05Ru2Al10 (1); Ce0.9Y0.1Ru2Al10 (1); Ce0.95La0.05Ru2Al10 (1); Ce0.9La0.1Ru2Al10 (1)
- dopant candidates (<5% at.): Y (2), La (2)
- measured range: 10-350 K (5th-95th pct of 17 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ce(Al5Ru)2 Cmcm (63) mp-31364 [hull=0.000, icsd=2, PRIMARY]; Ce2AlRu2 Cmce (64) mp-1078316 [hull=0.000, icsd=1, PRIMARY]; Ce5Al2Ru3 R3 (146) mp-1182608 [hull=0.001, icsd=1, PRIMARY]; Ce3(Al3Ru)4 P6_3/mmc (194) mp-31079 [hull=0.000, icsd=1, PRIMARY]; CeAlRu Pnma (62) mp-604008 [hull=0.000, icsd=1, PRIMARY]
- papers: Anisotropic Transport Properties of CeRu2Al10 | Transport, thermal, and NMR characteristics ofCeRu2Al10 | Effects of Y- and La-doping on the magnetic ordering, Kondo effect, and spin dynamics in Ce\n                    <sub>\n                      1−\n                      <i>x</i>\n                    </sub>\n                    <i>M</i>\n                    <sub>\n                      <i>x</i>\n                    </sub>\n                    Ru\n                    <sub>2</sub>\n                    Al\n                    <sub>10</sub>

## Al-Co-Fe-V
- rank 690 | 9 samples | 2 papers | 7 compositions
- compositions: (Fe0.8Co0.2)2VAl (2); (Fe0.6Co0.4)2VAl (2); (Fe0.85Co0.15)2VAl (1); (Fe0.88Co0.12)2VAl (1); (Fe0.7Co0.3)2VAl (1); (Fe0.5Co0.5)2VAl (1)
- measured range: 81-851 K (5th-95th pct of 43 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): AlVFeCo F-43m (216) mp-1008530 [hull=0.027, icsd=1, PRIMARY]
- papers: Thermoelectric properties of (Fe1−xCox)2VAl Heusler-type compounds | Low-Temperature Thermoelectric Properties of Fe2VAl with Partial Cobalt Doping

## Al-Ga-Si-Sr
- rank 691 | 9 samples | 1 papers | 8 compositions
- compositions: Sr8Al10Ga6Si30 (2); Sr8Al11Ga5Si30 (1); Sr8Al8Ga8Si30 (1); Sr8Al7Ga9Si30 (1); Sr8Al12Ga4Si30 (1); Sr8Al9Ga7Si30 (1)
- seed hypothesis (confirm): clathrate_i
- solid-solution axis: Al/(Al+Ga) spans 0.31-0.75 (median 0.56) over 8 compositions
     ISOELECTRONIC SERIES: the parent compound depends on the composition, not on this host. Near either end the minor element is a dilute substituent; in the middle it is a genuine alloy. Record the axis, not one parent -- and note the 5% split used the whole formula, not the sublattice, so its cut lands at a different level on each site.
- measured range: 293-983 K (5th-95th pct of 8 curves)
- papers: Synthesis and Thermoelectric Properties of Silicon Clathrates Sr8AlxGa16-xSi30with the Type-I and Type-VIII Structures

## Al-K-Si
- rank 692 | 9 samples | 4 papers | 6 compositions
- compositions: K8Al8Si38 (3); K6.5Ba1.5Al9.5Si36.5 (2); K6Ba2Al10Si36 (1); K7Ba1Al9Si37 (1); K7.7Al7.5Si38.8 (1); K8Al7Si39 (1)
- dopant candidates (<5% at.): Ba (4)
- measured range: 10-887 K (5th-95th pct of 53 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): KAlSi2 I4_1/acd (142) mp-1180795 [hull=0.054, icsd=1, PRIMARY]
- papers: A Combined Metal-Halide/Metal Flux Synthetic Route towards Type-I Clathrates: Crystal Structures and Thermoelectric Properties of A8Al8Si38(A=K, Rb, and Cs) | Synthesis, Structure, Thermoelectric Properties, and Band Gaps of Alkali Metal Containing Type I Clathrates: A8Ga8Si38(A = K, Rb, Cs) and K8Al8Si38 | Tuning Thermoelectric Properties of Type I Clathrate K8–xBaxAl8+xSi38–xthrough Barium Substitution

## Al-Pd-Ru
- rank 693 | 9 samples | 4 papers | 8 compositions
- compositions: Al71Pd20Re2.7Ru6.3_IQC (2); Al71Pd20Re2.7Ru6.3 (1); Al71Pd20Ru9 (1); Al71Pd20Re1.35Ru7.65 (1); Al71Pd20(Re0.3Ru0.7)9 (1); Al71Pd20(Re0.15Ru0.85)9 (1)
- dopant candidates (<5% at.): Re (7)
- seed hypothesis (confirm): quasicrystal_approximant
- measured range: 13-943 K (5th-95th pct of 20 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Al2PdRu Fm-3m (225) mp-862715 [hull=0.000, PRIMARY]
- papers: Effect of Ru substitution for Re on the thermoelectric properties of AlPdRe icosahedral quasicrystals | Thermoelectric properties of Al-Pd-Re(-Ru) icosahedral quasicrystals | Metallic–covalent bonding conversion and thermoelectric properties of Al-based icosahedral quasicrystals and approximants

## As-B
- rank 694 | 9 samples | 4 papers | 3 compositions
- compositions: B21As20I (6); BAs (2); B12As2 (1)
- dopant candidates (<5% at.): I (6)
- measured range: 12-500 K (5th-95th pct of 11 curves; full span incl. outliers 12-600 K)
- [ref 1] TEDesignLab / ICSD: BAs F-43m (216) mp-10044 [hull=0.080, icsd=3, PRIMARY]
- [ref 2] MP, ranked by ICSD evidence: B6As R-3m (166) mp-624 [hull=0.000, icsd=3, PRIMARY]; BAs P6_3mc (186) mp-984718 [hull=0.090]
- papers: Thermal and thermoelectric transport measurements of an individual boron arsenide microstructure | Unusual high thermal conductivity in boron arsenide bulk crystals | Experimental observation of high thermal conductivity in boron arsenide

## As-Ce-F-Fe-O-Y
- rank 695 | 9 samples | 1 papers | 1 compositions
- compositions: Ce0.6Y0.4FeAsO0.8F0.2 (9)
- seed hypothesis (confirm): zrcusias_1111
- measured range: 10-149 K (5th-95th pct of 9 curves)
- papers: Correlation between superconductivity and structural properties under high pressure of iron pnictide superconductor Ce<sub>0.6</sub>Y<sub>0.4</sub>FeAsO<sub>0.8</sub>F<sub>0.2</sub>

## As-Fe-Nd-O-Ru
- rank 696 | 9 samples | 1 papers | 4 compositions
- compositions: NdFe0.2Ru0.8AsO0.89F0.11 (3); NdFe0.5Ru0.5AsO0.89F0.11 (3); NdFe0.7Ru0.3AsO0.89F0.11 (2); NdFe0.4Ru0.6AsO0.89F0.11 (1)
- dopant candidates (<5% at.): F (9)
- solid-solution axis: Fe/(Fe+Ru) spans 0.20-0.70 (median 0.50) over 4 compositions
     ISOELECTRONIC SERIES: the parent compound depends on the composition, not on this host. Near either end the minor element is a dilute substituent; in the middle it is a genuine alloy. Record the axis, not one parent -- and note the 5% split used the whole formula, not the sublattice, so its cut lands at a different level on each site.
- measured range: 10-300 K (5th-95th pct of 9 curves)
- papers: Effects of Ru Doping on the Transport Behavior and Superconducting Transition Temperature of NdFeAsO0.89F0.11

## B-Ca
- rank 697 | 9 samples | 5 papers | 5 compositions
- compositions: CaB6 (5); Ca0.75Sr0.25B6 (1); Ca0.75Ba0.25B6 (1); Ca0.95Yb0.05B6 (1); Ca0.75B4.5Sr0.25B1.5 (1)
- dopant candidates (<5% at.): Sr (2), Ba (1), Yb (1)
- seed hypothesis (confirm): cab6_hexaboride
- measured range: 288-1120 K (5th-95th pct of 18 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): CaB6 Pm-3m (221) mp-865 [hull=0.000, icsd=10, PRIMARY]; CaB2 P6/mmm (191) mp-1009695 [hull=0.183, icsd=2, PRIMARY]; CaB4 P4/mbm (127) mp-1213975 [hull=0.000, PRIMARY]
- papers: Improvement of thermoelectric properties of alkaline-earth hexaborides | High-pressure densified solid solutions of alkaline earth hexaborides (Ca/Sr, Ca/Ba, Sr/Ba) and their high-temperature thermoelectric properties | Thermoelectric properties of metal-hexaborides

## B-Hf
- rank 698 | 9 samples | 4 papers | 3 compositions
- compositions: HfB2 (7); HfB1.9 (1); HfB2.1 (1)
- measured range: 290-1273 K (5th-95th pct of 9 curves; full span incl. outliers 290-2173 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): HfB2 P6/mmm (191) mp-1994 [hull=0.000, icsd=14, PRIMARY]; HfB Fm-3m (225) mp-345 [hull=0.348, icsd=2, PRIMARY]; HfB12 Fm-3m (225) mp-1001600 [hull=0.043, icsd=1, PRIMARY]; HfB6 Pm-3m (221) mp-1004377 [hull=0.541, PRIMARY]
- papers: Mechanical, Thermal, and Oxidation Properties of Refractory Hafnium and zirconium Compounds | Thermal Conductivity Characterization of Hafnium Diboride-Based Ultra-High-Temperature Ceramics | Thermal properties of La2O3-doped ZrB2- and HfB2-based ultra-high temperature ceramics

## Ba-Bi-Co-O-Rh
- rank 699 | 9 samples | 2 papers | 7 compositions
- compositions: Bi1.7Ba2(Co0.5Rh0.5)2O8 (3); Bi1.7Ba2(Co0.4Rh0.6)2O8 (1); Bi1.7Ba2(Co0.6Rh0.4)2O8 (1); Bi1.8Ba2(Co0.5Rh0.5)2O8 (1); Bi1.6Ba2(Co0.5Rh0.5)2O8 (1); Bi1.7Ba2(Co0.5Rh0.5)1.8O8 (1)
- seed hypothesis (confirm): misfit_cobaltite
- solid-solution axis: Co/(Co+Rh) spans 0.40-0.60 (median 0.50) over 7 compositions
     ISOELECTRONIC SERIES: the parent compound depends on the composition, not on this host. Near either end the minor element is a dilute substituent; in the middle it is a genuine alloy. Record the axis, not one parent -- and note the 5% split used the whole formula, not the sublattice, so its cut lands at a different level on each site.
- measured range: 10-301 K (5th-95th pct of 22 curves)
- papers: Thermoelectric properties of bismuth based cobalt-rhodium oxides with hexagonal (Co,Rh)O2 layers | Thermoelectric properties of cobalt rhodium oxides: [Bi2Ba2O4]p(Co,Rh)O2

## Ba-Cu-Se
- rank 700 | 9 samples | 1 papers | 9 compositions
- compositions: Ba1Cu2Se3 (1); Ba0.99Na0.01Cu2Se2 (1); Ba0.985Na0.015Cu2Se2 (1); Ba0.975Na0.025Cu2Se2 (1); Ba0.9Na0.1Cu2Se2 (1); Ba0.995Na0.005Cu2Se2 (1)
- dopant candidates (<5% at.): Na (8)
- measured range: 21-771 K (5th-95th pct of 42 curves)
- [ref 1] TEDesignLab / ICSD: Ba(CuSe)2 Pnma (62) mp-4473 [hull=0.004, icsd=2, PRIMARY]; Ba(CuSe)2 I4/mmm (139) mp-10437 [hull=0.036, icsd=1]
- papers: BaCu2Se2 based compounds as promising thermoelectric materials
