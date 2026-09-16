# Host systems -- chunk 020 of 73

Ranks 951-1000 by sample count. These 50 host systems cover 300 samples (0.58% of the TE set); cumulative through this chunk: 89.08%.

Assign each host system a structural prototype from `data/annotated/taxonomy/prototypes_seed_v3.json`, or propose a new one in `taxonomy/prototypes_proposed.jsonl` first. Append results to `data/annotated/annotations/family_assignments.jsonl`.

The hand-entered MaterialFamily labels are deliberately NOT shown here -- they are held out in `df_host_systems.parquet` to validate this classification later. Decide from the compositions.

A "seed hypothesis" line means the taxonomy already names this host under that prototype. Confirm it against the compositions rather than accepting it; two or more listed means the host is mixed and needs splitting per composition.

Evidence follows the project precedence. Your judgement about the thermoelectric chemistry decides the prototype. [ref 1] is TEDesignLab, ICSD-backed and thermoelectric-specific -- prefer it. [ref 2] is Materials Project. Within a formula, polymorphs are ranked by ICSD reference count and the top one is marked PRIMARY -- not by e_above_hull, which is unusable for layered chalcogenides in the 2019 dump (Sb2Te3 R-3m carries 26 ICSD refs at hull 1.02). A primary resting on fewer than 5 ICSD references is flagged weak; the ambient phase may simply be absent from the snapshot, as it is for Bi2Se3.

While you have the host in view, also record what each minor element DOES, in `dopant_roles` -- the role follows from the prototype and cannot be judged without it. A median host has 2 such elements. Not everything listed is a dopant: O, C, N and H are usually milling or pressing residue, and an element just under 5 at.% may be an alloying end member rather than dilute doping. The doping LEVEL is computed later from the parsed fractions -- do not work it out by hand here.

A polymorph list is NOT a thermal sequence. SnSe has three known structures but only Pnma -> Cmcm happens on heating; rocksalt SnSe is metastable (2 icsd refs against 32). Put thermally reached phases in `phases` with their transition temperatures, and everything else in `other_polymorphs` with an occurrence reason. hull and icsd counts are shown to help you tell them apart.

A host may need MORE THAN ONE prototype. Transport is measured across a wide window and many thermoelectrics transform inside it, so where a "MEASUREMENT CROSSES A TRANSITION" line appears, record each phase with its own temperature range in the `phases` field. Transition temperatures shown are approximate and composition-dependent.

Both references describe which phases EXIST in a chemistry, not which phase this paper made. Al-O-Zn is best attested as ZnAl2O4 spinel (227) while almost every sample in it is Al-doped wurtzite ZnO (186). Weigh them against the compositions; do not follow them blindly.

## Ag-S
- rank 951 | 6 samples | 3 papers | 3 compositions
- compositions: Ag2S (4); Ag2S1.05 (1); Ag2S1.1 (1)
- measured range: 303-543 K (5th-95th pct of 18 curves)
- [ref 1] TEDesignLab / ICSD: Ag2S P2_12_12_1 (19) mp-1095694 [hull=0.046, icsd=2]; Ag2S P2_1 (4) mp-31053 [hull=0.000, icsd=1]
- [ref 2] MP, ranked by ICSD evidence: Ag2S P2_1/c (14) mp-610517 [hull=0.024, icsd=7, PRIMARY]; Ag8S F-43m (216) mp-28963 [hull=0.265, icsd=1, PRIMARY]; Ag3S P6_3/mmc (194) mp-1183254 [hull=0.151, PRIMARY]; Ag2S Cmc2_1 (36) mp-32669 [hull=0.005]; Ag2S C2/m (12) mp-32884 [hull=0.006]
- papers: Superionic Phase Transition in Silver Chalcogenide Nanocrystals Realizing Optimized Thermoelectric Performance | General surfactant-free synthesis of binary silver chalcogenides with tuneable thermoelectric properties | Mixed-phase effect of a high Seebeck coefficient and low electrical resistivity in Ag2S

## Ag-Sb-Se-Sn-Te
- rank 952 | 6 samples | 2 papers | 6 compositions
- compositions: Sn0.88Cd0.05Te0.64Ag0.12Sb0.12Se0.24 (1); Sn0.85Cd0.05Te0.55Ag0.15Sb0.15Se0.3 (1); Sn0.4Ag0.3Sb0.3Se0.4Te0.6 (1); Sn0.7Ag0.15Sb0.15Se0.7Te0.3 (1); Sn0.6Ag0.2Sb0.2Se0.6Te0.4 (1); Sn0.5Ag0.25Sb0.25Se0.5Te0.5 (1)
- dopant candidates (<5% at.): Cd (2)
- solid-solution axis: Se/(Se+Te) spans 0.27-0.70 (median 0.50) over 6 compositions
     ISOELECTRONIC SERIES: the parent compound depends on the composition, not on this host. Near either end the minor element is a dilute substituent; in the middle it is a genuine alloy. Record the axis, not one parent -- and note the 5% split used the whole formula, not the sublattice, so its cut lands at a different level on each site.
- measured range: 298-829 K (5th-95th pct of 30 curves)
- papers: Synthesis of SnTe/AgSbSe 2  nanocomposite as a promising lead-free thermoelectric material | Band flattening and phonon-defect scattering in cubic SnSe–AgSbTe2 alloy for thermoelectric enhancement

## Al-Ba-Ga-Si
- rank 953 | 6 samples | 2 papers | 6 compositions
- compositions: Ba7.8Al5.3Ga7.4Si33.3 (1); Ba7.6Al6.1Ga6.4Si33.5 (1); Ba8Ga16Al3Si27 (1); Ba8Ga16Al6Si24 (1); Ba8Ga11Al6Si29 (1); Ba8Ga10Al6Si30 (1)
- solid-solution axis: Al/(Al+Ga) spans 0.16-0.49 (median 0.37) over 6 compositions
     ISOELECTRONIC SERIES: the parent compound depends on the composition, not on this host. Near either end the minor element is a dilute substituent; in the middle it is a genuine alloy. Record the axis, not one parent -- and note the 5% split used the whole formula, not the sublattice, so its cut lands at a different level on each site.
- measured range: 199-1037 K (5th-95th pct of 15 curves)
- papers: Thermoelectric Properties of Ga-Doped Ba8Al x Si46−x Clathrate | The High-Temperature Thermoelectric Properties of Polycrystalline Ba8Ga x Al y Si46−x−y Type-I Clathrates

## Al-Co-Mn
- rank 954 | 6 samples | 3 papers | 1 compositions
- compositions: Co2MnAl (6)
- measured range: 15-1013 K (5th-95th pct of 9 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): MnAlCo2 Fm-3m (225) mp-3623 [hull=0.000, icsd=3, PRIMARY]; Mn2AlCo F-43m (216) mp-13079 [hull=0.032, icsd=1, PRIMARY]; MnAl2Co P4/mmm (123) mp-1221642 [hull=0.002, PRIMARY]
- papers: Specific features of the properties of half-metallic ferromagnetic Heusler alloys Fe2MnAl, Fe2MnSi, and Co2MnAl | Structural and Thermoelectric Properties of Ternary Full-Heusler Alloys | Anomalous resistivity upturn in epitaxial L21-Co2MnAl films

## Al-Li
- rank 955 | 6 samples | 1 papers | 1 compositions
- compositions: LiAl02 (6)
- measured range: 378-972 K (5th-95th pct of 6 curves; full span incl. outliers 378-1167 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): LiAl Fd-3m (227) mp-1067 [hull=0.000, icsd=26, PRIMARY]; LiAl3 Pm-3m (221) mp-10890 [hull=0.006, icsd=1, PRIMARY]; Li3Al2 R-3m (166) mp-16506 [hull=0.000, icsd=1, PRIMARY]; Li3Al I4/mmm (139) mp-975868 [hull=0.052, PRIMARY]; Li2Al Cmcm (63) mp-1210753 [hull=0.000, PRIMARY]
- papers: Effects of Fast Neutron Irradiation on Thermal Conductivity of Li2O and LiAlO2

## Al-Mg-O
- rank 956 | 6 samples | 2 papers | 4 compositions
- compositions: MgAl2O4 (3); Mg0.73Fe0.33Al1.93O4 (1); (MgO)0.92(Al2O3)0.08 (1); (MgO)0.88(Al2O3)0.12 (1)
- dopant candidates (<5% at.): Fe (1)
- measured range: 15-1000 K (5th-95th pct of 6 curves; full span incl. outliers 15-1468 K)
- [ref 1] TEDesignLab / ICSD: MgAl2O4 Fd-3m (227) mp-3536 [hull=0.000, icsd=28, PRIMARY]; MgAl2O4 Pnma (62) mp-5857 [hull=0.099, icsd=3]; MgAl2O4 (63)
- [ref 2] MP, ranked by ICSD evidence: Mg16Al12O I-43m (217) mp-1185684 [hull=0.123, PRIMARY, AMBIGUOUS]; CaMg2Al6O12 P-6 (174) mp-1227128 [hull=0.081, PRIMARY]; Mg2Al2O5 P4/mmm (123) mp-1185757 [hull=0.396, PRIMARY]; Mg2AlO6 P-1 (2) mp-1222192 [hull=0.488, PRIMARY]; Mg3AlO4 Pm-3m (221) mp-1024039 [hull=0.334, PRIMARY]
- papers: Thermal Conductivity of MgO,Al2O3, MgAl2O4, andFe3O4Crystals from 3° to 300°K | Achieving ultrahigh dielectric breakdown strength in MgO-based ceramics by composite structure design

## Al-Rh-Si
- rank 957 | 6 samples | 1 papers | 6 compositions
- compositions: Al63Rh28Si9 (1); Al65Rh28Si7 (1); Al64Rh27Si9 (1); Al64Rh28Si8 (1); Al65Rh27Si8 (1); Al66Rh27Si7 (1)
- measured range: 13-296 K (5th-95th pct of 6 curves)
- papers: Electrical resistivity of the Al65Rh27Si8 2/1 cubic approximant

## Al-Sb
- rank 958 | 6 samples | 3 papers | 5 compositions
- compositions: AlSb (2); Al0.985Mg0.015Sb (1); Al0.980Mg0.020Sb (1); Al0.995Mg0.005Sb (1); Al0.990Mg0.010Sb (1)
- dopant candidates (<5% at.): Mg (4)
- measured range: 306-858 K (5th-95th pct of 26 curves)
- [ref 1] TEDesignLab / ICSD: AlSb F-43m (216) mp-2624 [hull=0.000, icsd=10, PRIMARY]
- [ref 2] MP, ranked by ICSD evidence: AlSb P6_3mc (186) mp-1018100 [hull=0.008, icsd=1]; AlSb Pa-3 (205) mp-15621 [hull=0.113, icsd=1]; AlSb Cmcm (63) mp-1023918 [hull=0.191]; AlSb I-4m2 (119) mp-1228806 [hull=0.242]
- papers: Mechanical and Thermoelectric Properties of Bulk AlSb Synthesized by Controlled Melting, Pulverizing and Subsequent Vacuum Hot Pressing | Composite fabrication for improvement of thermoelectric properties in AlSb | Improvement of Thermoelectric Properties of AlSb by Incorporation of Mg as p-type Dopant

## Al-Sc-Yb
- rank 959 | 6 samples | 2 papers | 6 compositions
- compositions: Yb0.75Sc0.25Al3 (1); Yb0.5Sc0.5Al3 (1); Yb0.25Sc0.75Al3 (1); Yb0.4Sc0.6Al2 (1); Yb0.2Sc0.8Al2 (1); Yb0.3Sc0.7Al2 (1)
- solid-solution axis: Sc/(Sc+Yb) spans 0.25-0.80 (median 0.70) over 6 compositions
     ISOELECTRONIC SERIES: the parent compound depends on the composition, not on this host. Near either end the minor element is a dilute substituent; in the middle it is a genuine alloy. Record the axis, not one parent -- and note the 5% split used the whole formula, not the sublattice, so its cut lands at a different level on each site.
- measured range: 14-350 K (5th-95th pct of 21 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): YbScAl4 F-43m (216) mp-1215458 [hull=0.036, PRIMARY]
- papers: Synthesis, crystal structure, and thermoelectric properties of the YbAl3-ScAl3 solid solution | Enhanced thermoelectric power factor in Yb1−xScxAl2 alloys using chemical pressure tuning of the Yb valence

## Al-Ti
- rank 960 | 6 samples | 3 papers | 5 compositions
- compositions: LaTi2Al20 (2); PrTi2Al20 (1); Ti94Al6 (1); Ti89Al11 (1); Ti0.67Al0.33 (1)
- dopant candidates (<5% at.): La (2), Pr (1)
- measured range: 11-1037 K (5th-95th pct of 6 curves; full span incl. outliers 11-1103 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): TiAl P4/mmm (123) mp-1953 [hull=0.000, icsd=17, PRIMARY]; Ti3Al P6_3/mmc (194) mp-1823 [hull=0.000, icsd=5, PRIMARY]; La(TiAl10)2 Fd-3m (227) mp-1200087 [hull=0.000, icsd=1, PRIMARY]; Ti2Al F-43m (216) mp-1008753 [hull=0.894, icsd=1, PRIMARY]; Pr(TiAl10)2 Fd-3m (227) mp-1204502 [hull=0.000, icsd=1, PRIMARY]
- papers: Thermoelectric Power Anomaly of PrTi2Al20and PrV2Al20with Non-Kramers Γ3Ground State | Thermoelectric Property of SmT<sub>2</sub>Al<sub>20</sub> (T = Ti, V, and Cr) at Low Temperatures | Electrical conduction in concentrated disordered transition metal alloys

## Al-Zn
- rank 961 | 6 samples | 3 papers | 5 compositions
- compositions: Zn0.91Al0.07Ni0.02 (2); (Al)84.98(Zn)15.02 (1); (Al)61.78(Zn)38.22 (1); (Al)31.59(Zn)68.41 (1); (Al)11.32(Zn)88.68 (1)
- dopant candidates (<5% at.): Ni (2)
- measured range: 12-733 K (5th-95th pct of 6 curves; full span incl. outliers 12-808 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Al2Zn P-3m1 (164) mp-1206713 [hull=0.024, PRIMARY]; Al3Zn Pm-3m (221) mp-983585 [hull=0.043, PRIMARY]
- papers: Solid-liquid interfacial energy of Al-Zn solid-solutions in equilibrium with Al-Zn liquid | Solid–liquid interfacial energy of the eutectoid β phase in the Al–Zn eutectic system | Al and Ni co-doped ZnO films with room temperature ferromagnetism, low resistivity and high transparence

## As-Ba-Co-Fe
- rank 962 | 6 samples | 1 papers | 4 compositions
- compositions: BaFe1.68Co0.32As2 (2); BaFe1.66Co0.34As2 (2); BaFe1.75Co0.25As2 (1); BaFe1.73Co0.27As2 (1)
- measured range: 10-299 K (5th-95th pct of 10 curves)
- papers: Thermoelectric properties of electron- and hole-dopedBaFe2As2

## As-Ba-Pd
- rank 963 | 6 samples | 1 papers | 1 compositions
- compositions: BaPd2As2 (6)
- measured range: 23-394 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ba(AsPd)2 P4/mmm (123) mp-8237 [hull=0.014, icsd=2, PRIMARY]; BaAs2Pd Cmcm (63) mp-9767 [hull=0.000, icsd=1, PRIMARY]; BaAsPd P-6m2 (187) mp-9744 [hull=0.000, icsd=1, PRIMARY]; Ba(AsPd)2 I4/mmm (139) mp-6962 [hull=0.020, icsd=1]
- papers: High-pressure effects on isotropic superconductivity in the iron-free layered pnictide superconductor \nBaPd2As2

## As-Cd-P
- rank 964 | 6 samples | 1 papers | 6 compositions
- compositions: Cd3(P0.4As0.6)2 (1); Cd3(P0.8As0.2)2 (1); Cd3(P0.2As0.8)2 (1); Cd3PAs (1); Cd3(P0.6As0.4)2 (1); Cd3(P0.7As0.3)2 (1)
- solid-solution axis: As/(As+P) spans 0.20-0.80 (median 0.50) over 6 compositions
     ISOELECTRONIC SERIES: the parent compound depends on the composition, not on this host. Near either end the minor element is a dilute substituent; in the middle it is a genuine alloy. Record the axis, not one parent -- and note the 5% split used the whole formula, not the sublattice, so its cut lands at a different level on each site.
- measured range: 84-373 K (5th-95th pct of 6 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): CdAsP I2_12_12_1 (24) mp-1226754 [hull=0.035, PRIMARY]
- papers: Physical and electronic properties of semiconducting solid solutions of the Cd3 As2Cd3 P2 system

## As-Lu
- rank 965 | 6 samples | 2 papers | 3 compositions
- compositions: LuAs (4); La0.05Lu0.95As (1); La0.09Lu0.91As (1)
- dopant candidates (<5% at.): La (2)
- measured range: 11-301 K (5th-95th pct of 6 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): LuAs Fm-3m (225) mp-2017 [hull=0.000, icsd=3, PRIMARY]; LuAs Pm-3m (221) mp-1009016 [hull=0.502, icsd=1]
- papers: Electron transport and magnetic properties of semimetallic LuAs | Temperature dependence of the electrical resistivity of La<sub>x</sub>Lu<sub>1-x</sub>As

## As-Th
- rank 966 | 6 samples | 2 papers | 3 compositions
- compositions: Th3As4 (4); Th3(As0.95Sb0.05)4 (1); (Th0.94U0.06)3As4 (1)
- dopant candidates (<5% at.): Sb (1), U (1)
- measured range: 11-1258 K (5th-95th pct of 9 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): ThAs Fm-3m (225) mp-1753 [hull=0.000, icsd=3, PRIMARY]; Th3As4 I-43d (220) mp-382 [hull=0.000, icsd=3, PRIMARY]; ThAs2 P4/nmm (129) mp-7097 [hull=0.000, icsd=1, PRIMARY]; Th2As3 P4/mmm (123) mp-1208450 [hull=3.836, PRIMARY]; ThAs Pm-3m (221) mp-19868 [hull=0.289, icsd=3]
- papers: Some X-Ray and Thermoelectric Studies on Cubic Th[sub 3]X[sub 4] Compounds | Electronic properties of Th3As4U3As4 solid solutions

## B-Ce-Ir
- rank 967 | 6 samples | 1 papers | 1 compositions
- compositions: CeIr2B2 (6)
- measured range: 10-301 K (5th-95th pct of 7 curves; full span incl. outliers 10-347 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ce(BIr)2 Fddd (70) mp-8680 [hull=0.000, icsd=2, PRIMARY]; CeB2Ir3 P6/mmm (191) mp-11593 [hull=0.000, icsd=2, PRIMARY]; Ce(BIr)4 P4_2/n (86) mp-1190481 [hull=0.000, icsd=1, PRIMARY]; Ce2B2Ir5 R-3m (166) mp-30898 [hull=0.000, icsd=1, PRIMARY]
- papers: Ferromagnetic ordering in CeIr2B2: Transport, magnetization, specific heat, and NMR studies

## B-Fe-Ni
- rank 968 | 6 samples | 3 papers | 4 compositions
- compositions: Fe40Ni40B20 (3); (Fe0.94Ni0.06)84B16 (1); (Fe0.92Ni0.08)84B16 (1); Fe20Ni60B20 (1)
- measured range: 61-526 K (5th-95th pct of 8 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Fe2NiB Pnma (62) mp-1105860 [hull=0.052, icsd=1, PRIMARY, AMBIGUOUS]; Fe3(Ni10B3)2 Fm-3m (225) mp-1193589 [hull=0.032, icsd=1, PRIMARY]; Fe3Ni3B2 P2_1 (4) mp-1224887 [hull=0.048, PRIMARY]; FeNiB Fmmm (69) mp-1224960 [hull=0.054, PRIMARY]; Fe2NiB I-4 (82) mp-1184343 [hull=0.058, icsd=1]
- papers: Thermoelectric power in some ferromagnetic Fe based amorphous alloys | Influence of small amounts of Co and Ni additives on thermoelectric power in amorphous Fe&lt;inf&gt;84&lt;/inf&gt;B&lt;inf&gt;16&lt;/inf&gt; | Transport properties of Fe-Ni Glasses

## B-Pr
- rank 969 | 6 samples | 2 papers | 1 compositions
- compositions: PrB6 (6)
- measured range: 10-25 K (5th-95th pct of 6 curves; full span incl. outliers 10-100 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): PrB6 Pm-3m (221) mp-12762 [hull=0.000, icsd=7, PRIMARY]; PrB4 P4/mbm (127) mp-12569 [hull=0.000, icsd=2, PRIMARY]; Pr2B5 C2/c (15) mp-16713 [hull=0.000, icsd=1, PRIMARY]; PrB3 P6_3/mmc (194) mp-16762 [hull=0.482, icsd=1, PRIMARY]; PrB12 Fm-3m (225) mp-1004753 [hull=0.070, PRIMARY]
- papers: Thermal conductivity ofRB6(R=Ce,Pr,Nd,Sm,Gd) single crystals | Magnetic Field Influence on the Thermal Conductivity of PrB6

## B-Tm
- rank 970 | 6 samples | 3 papers | 4 compositions
- compositions: TmB12 (3); Tm0.9Yb.1B12 (1); Tm0.7Yb0.3B12 (1); Tm0.95Yb0.05B12 (1)
- dopant candidates (<5% at.): Yb (3)
- measured range: 10-301 K (5th-95th pct of 9 curves; full span incl. outliers 10-1064 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): TmB2 P6/mmm (191) mp-800 [hull=0.000, icsd=3, PRIMARY]; TmB12 Fm-3m (225) mp-1104905 [hull=0.000, icsd=1, PRIMARY]
- papers: Antiferromagnetic instability and the metal-insulator transition in Tm1 − x Yb x B12 rare earth dodecaborides | Transition and rare earth element dodecaborides | Thermal conductivity of metal dodecaborides with a UB12 structure

## Ba-Bi-Te
- rank 971 | 6 samples | 2 papers | 3 compositions
- compositions: BaBiTe3 (4); BaBiTe2.95Se0.05 (1); BaBiTe2.9Se0.1 (1)
- dopant candidates (<5% at.): Se (2)
- measured range: 79-631 K (5th-95th pct of 16 curves)
- papers: Oligomerization Versus Polymerization of Texn-in the Polytelluride Compound BaBiTe3. Structural Characterization, Electronic Structure, and Thermoelectric Properties | Resonant Bonding, Multiband Thermoelectric Transport, and Native Defects in n-Type BaBiTe3–xSex (x = 0, 0.05, and 0.1)

## Ba-Co-Fe-La-O
- rank 972 | 6 samples | 1 papers | 4 compositions
- compositions: La0.33Ba0.67Co0.7Fe0.3O3 (2); La0.33Ba0.62Gd0.05Co0.7Fe0.3O3 (2); La0.33Ba0.47Gd0.2Co0.7Fe0.3O3 (1); La0.33Ba0.57Gd0.1Co0.7Fe0.3O3 (1)
- dopant candidates (<5% at.): Gd (4)
- measured range: 375-1078 K (5th-95th pct of 6 curves)
- papers: Impacts of A-site gadolinium doping on electrocatalytic performance of La0.33Ba0.62Gd0.05Co0.7Fe0.3O3- to realize promising cathode for intermediate-temperature solid oxide fuel cells

## Ba-Cu-Fe-O-Sm
- rank 973 | 6 samples | 3 papers | 5 compositions
- compositions: SmBaCuFeO5 (2); Sm0.6La0.4BaCuFeO5 (1); Sm0.8La0.2BaCuFeO5 (1); Sm0.7La0.3BaCuFeO5 (1); (SmBaCuFeO5)80(Ag)20 (1)
- dopant candidates (<5% at.): La (3), Ag (1)
- measured range: 36-1035 K (5th-95th pct of 20 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): BaSmFeCuO5 P4mm (99) mp-1214324 [hull=0.000, PRIMARY]
- papers: Thermoelectric properties of Sm1−xLaxBaCuFeO5 ceramics | Thermoelectric properties of layered ferrocuprates LnBaCuFeO5 + δ (Ln= La, Pr, Nd, Sm, Gd-Lu) | Enhanced Thermoelectric Performance of SmBaCuFeO5+δ/Ag Composite Ceramics

## Ba-Cu-Fe-O-Y
- rank 974 | 6 samples | 1 papers | 6 compositions
- compositions: YBaCuFeO5 (1); YBaCuFe0.975Ni0.025O5 (1); YBaCuFe0.95Ni0.05O5 (1); YBaCuFe0.9Ni0.1O5 (1); YBaCuFe0.8Ni0.2O5 (1); YBaCuFe0.7Ni0.3O5 (1)
- dopant candidates (<5% at.): Ni (5)
- measured range: 299-1086 K (5th-95th pct of 12 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ba4Y2FeCu5O14 C2/m (12) mp-1228213 [hull=0.066, PRIMARY]
- papers: Properties of YBaCuFe1 ? xNixO5 (0 < x ? 0.3) solid solutions

## Ba-Cu-S
- rank 975 | 6 samples | 3 papers | 5 compositions
- compositions: BaCu2S2 (2); K0.05Ba0.95Cu2S2 (1); K0.1Ba0.9Cu2S2 (1); BaCu4S3 (1); BaCu3.96S3 (1)
- dopant candidates (<5% at.): K (2)
- measured range: 292-871 K (5th-95th pct of 19 curves)
- [ref 1] TEDesignLab / ICSD: Ba(CuS)2 I4/mmm (139) mp-4255 [hull=0.017, icsd=5, PRIMARY]; BaCu4S3 Pnma (62) mp-654109 [hull=0.019, icsd=2, PRIMARY]; Ba(CuS)2 Pnma (62) mp-5970 [hull=0.002, icsd=2]; BaCu4S3 Cmcm (63) mp-27424 [hull=0.000, icsd=1]
- [ref 2] MP, ranked by ICSD evidence: BaCuS2 P4/nmm (129) mp-1147715 [hull=0.000, PRIMARY]; BaCuS2 Cmcm (63) mp-1147719 [hull=0.062]; BaCuS2 P4/mmm (123) mp-1096843 [hull=0.103]; BaCuS2 I-4m2 (119) mp-1147720 [hull=0.136]
- papers: Thermoelectric properties of β-BaCu2S2 | Thermoelectric properties of potassium-doped β-BaCu2S2 with natural superlattice structure | A p-type thermoelectric material BaCu4S3 with high electronic band degeneracy

## Ba-O-Ru
- rank 976 | 6 samples | 3 papers | 2 compositions
- compositions: Ba4Ru3O10 (4); BaRuO3 (2)
- measured range: 11-1007 K (5th-95th pct of 9 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): BaRuO3 R-3m (166) mp-5773 [hull=0.000, icsd=6, PRIMARY]; Ba4Ru3O10 P2_1/c (14) mp-1200068 [hull=0.001, icsd=1, PRIMARY]; Ba5(RuO5)2 P6_3/mmc (194) mp-28908 [hull=0.000, icsd=1, PRIMARY]; BaRuO5 R-3c (167) mp-1201605 [hull=0.000, icsd=1, PRIMARY]; Ba2RuO4 I4/mmm (139) mp-1025237 [hull=0.001, PRIMARY]
- papers: Thermoelectric properties of alkaline earth ruthenates prepared by SPS | Antiferromagnetic order and consequences on the transport properties of Ba4Ru3O10 | Synthesis and properties of epitaxial thin films of <i>c</i>-axis oriented metastable four-layered hexagonal BaRuO3

## Ba-Si-Zn
- rank 977 | 6 samples | 1 papers | 1 compositions
- compositions: Ba8Zn7Si39 (6)
- measured range: 10-708 K (5th-95th pct of 8 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ba(ZnSi)2 I4/mmm (139) mp-1070267 [hull=0.000, icsd=1, PRIMARY]; BaZnSi P6_3/mmc (194) mp-31147 [hull=0.000, icsd=1, PRIMARY]
- papers: Clathrates Ba8{Zn,Cd}xSi46−x,x∼7: synthesis, crystal structure and thermoelectric properties

## Bi-C-H-Te
- rank 978 | 6 samples | 4 papers | 3 compositions
- compositions: (Bi2Te3)92.95(C14H14O5S2)7.05 (4); (Bi2Te3)97.58(C14H14O5S2)2.42 (1); (Bi2Te2.7Se0.3)87.92(AgBi3S5)1.19(C4H2NH)10.89 (1)
- dopant candidates (<5% at.): S (6), O (5), Se (1), N (1), Ag (1)
- measured range: 296-554 K (5th-95th pct of 30 curves)
- papers: Selective Charge Carrier Transport and Bipolar Conduction in an Inorganic/Organic Bulk-Phase Composite: Optimization for Low-Temperature Thermoelectric Performance | High Thermoelectric Performance of n-type BiTeSe-Based Composites Incorporated with Both Inorganic and Organic Nanoinclusions | Energy filtering and phonon scattering effects in Bi2Te3–PEDOT:PSS composite resulting in enhanced n-type thermoelectric performance

## Bi-Cu-O-S-Se
- rank 979 | 6 samples | 1 papers | 6 compositions
- compositions: BiCuSe0.7S0.3O (1); BiCuSe0.6S0.4O (1); BiCuSe0.4S0.6O (1); BiCuSe0.3S0.7O (1); BiCuSe0.8S0.2O (1); BiCuSe0.5S0.5O (1)
- solid-solution axis: S/(S+Se) spans 0.20-0.70 (median 0.50) over 6 compositions
     ISOELECTRONIC SERIES: the parent compound depends on the composition, not on this host. Near either end the minor element is a dilute substituent; in the middle it is a genuine alloy. Record the axis, not one parent -- and note the 5% split used the whole formula, not the sublattice, so its cut lands at a different level on each site.
- measured range: 10-300 K (5th-95th pct of 6 curves)
- papers: Structure and Transport Properties of the BiCuSeO-BiCuSO Solid Solution

## Bi-Cu-Sr
- rank 980 | 6 samples | 1 papers | 6 compositions
- compositions: Bi2Sr2Cu6.04 (1); Bi2Sr2Cu6.08 (1); Bi2Sr2Cu6.12 (1); Bi2Sr2Cu6.19 (1); Bi2Sr2Cu6.23 (1); Bi2Sr2Cu6.48 (1)
- measured range: 11-300 K (5th-95th pct of 6 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): SrCuBi P6_3/mmc (194) mp-30451 [hull=0.028, icsd=1, PRIMARY]
- papers: Evidence for Antiferromagnetic Order in Bi2Sr2CuO6Phase with Stoichiometric Cation Composition

## Bi-Er-O
- rank 981 | 6 samples | 1 papers | 5 compositions
- compositions: Er2O1.3Bi1.7 (2); Er2O1.7Bi1.3 (1); Er2O1.5Bi1.5 (1); Er2O1.6Bi1.4 (1); Er2O1.8Bi1.2 (1)
- measured range: 10-99 K (5th-95th pct of 6 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Er2BiO2 I4/mmm (139) mp-1069613 [hull=0.000, icsd=1, PRIMARY]; Er(Bi3O5)4 I23 (197) mp-772790 [hull=0.060, PRIMARY]; Er(BiO2)3 R-3 (148) mp-754989 [hull=0.041, PRIMARY]; Er2Bi2O7 P4_1 (76) mp-772991 [hull=0.097, PRIMARY]; ErBiO3 R3c (161) mp-754943 [hull=0.031, PRIMARY]
- papers: Superconductivity in Anti-ThCr<sub>2</sub>Si<sub>2</sub>-type Er<sub>2</sub>O<sub>2</sub>Bi Induced by Incorporation of Excess Oxygen with CaO Oxidant

## Bi-Er-Pd
- rank 982 | 6 samples | 6 papers | 2 compositions
- compositions: ErPdBi (5); ErPd2Bi (1)
- measured range: 12-1000 K (5th-95th pct of 15 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Er5BiPd2 I4/mcm (140) mp-1213208 [hull=0.000, PRIMARY]; ErBiPd F-43m (216) mp-1206953 [hull=0.000, PRIMARY]
- papers: Thermoelectric and thermophysical properties of ErPdX (X=Sb and Bi) half-Heusler compounds | High-temperature Hall measurements of lanthanide based ternary intermetallics | Unusual features of erbium-based Heusler phases

## Bi-Gd-Pd
- rank 983 | 6 samples | 6 papers | 1 compositions
- compositions: GdPdBi (6)
- measured range: 12-955 K (5th-95th pct of 16 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): GdBiPd F-43m (216) mp-1076916 [hull=0.000, icsd=1, PRIMARY]
- papers: Thermoelectric Properties of Half-Heusler Type LaPdBi and GdPdBi | Physical properties of rare-earth-based Heusler phases REPdZ and REPd/sub 2/Z (Z = Sb,Bi) | High-temperature Hall measurements of lanthanide based ternary intermetallics

## Bi-Ge-Sb-Te
- rank 984 | 6 samples | 1 papers | 5 compositions
- compositions: GeBi3SbTe7 (2); GeBi3.2Sb0.8Te7 (1); GeBiSb3Te7 (1); GeBi3.12Sb0.88Te7 (1); GeBi2Sb2Te7 (1)
- solid-solution axis: Bi/(Bi+Sb) spans 0.25-0.80 (median 0.75) over 5 compositions
     ISOELECTRONIC SERIES: the parent compound depends on the composition, not on this host. Near either end the minor element is a dilute substituent; in the middle it is a genuine alloy. Record the axis, not one parent -- and note the 5% split used the whole formula, not the sublattice, so its cut lands at a different level on each site.
- measured range: 10-300 K (5th-95th pct of 16 curves)
- papers: Single-crystal growth and thermoelectric properties of Ge(Bi,Sb)4Te7

## Bi-Mn-Te
- rank 985 | 6 samples | 2 papers | 2 compositions
- compositions: Mn0.85Bi2.1Te4 (5); Bi2MnTe5 (1)
- measured range: 296-674 K (5th-95th pct of 13 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Mn(BiTe2)2 R-3m (166) mp-1077840 [hull=0.009, icsd=1, PRIMARY]
- papers: Crystal structure, properties and nanostructuring of a new layered chalcogenide semiconductor, Bi2MnTe4 | Chemical Aspects of the Candidate Antiferromagnetic Topological Insulator MnBi2Te4

## Bi-S-Te
- rank 986 | 6 samples | 2 papers | 6 compositions
- compositions: Bi2Te2S (1); Bi2Te1.9S1.1 (1); Bi2Te2S0.94Cl0.06 (1); Bi2Te1.8S1.2 (1); Bi2Te2S1 (1); Bi2Te1S2 (1)
- dopant candidates (<5% at.): Cl (1)
- solid-solution axis: S/(S+Te) spans 0.32-0.67 (median 0.37) over 6 compositions
     ISOELECTRONIC SERIES: the parent compound depends on the composition, not on this host. Near either end the minor element is a dilute substituent; in the middle it is a genuine alloy. Record the axis, not one parent -- and note the 5% split used the whole formula, not the sublattice, so its cut lands at a different level on each site.
- measured range: 10-676 K (5th-95th pct of 23 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Bi2Te2S R-3m (166) mp-27910 [hull=0.000, icsd=1, PRIMARY]; Bi3Te2S P-3m1 (164) mp-1103410 [hull=0.168, icsd=1, PRIMARY]; Bi4(TeS)3 R3m (160) mp-1227434 [hull=0.115, PRIMARY]; Bi2Te2S R3m (160) mp-1227335 [hull=0.192]; Bi2Te2S C2/m (12) mp-632485 [hull=0.221]
- papers: Thermoelectric properties of the tetradymite-type Bi2Te2S–Sb2Te2S solid solution | Studies on the Bi2Te3–Bi2Se3–Bi2S3system for mid-temperature thermoelectric energy conversion

## C-H-I-N-Pb
- rank 987 | 6 samples | 2 papers | 4 compositions
- compositions: CH3NH3PbI3 (3); (CH3NH3I)100(PbI2)99(BiI3)1 (1); (CH3NH3I)100(PbI2)97(BiI3)3 (1); (CH3NH3I)100(PbI2)95(BiI3)5 (1)
- dopant candidates (<5% at.): Bi (3)
- measured range: 30-401 K (5th-95th pct of 18 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): H36Pb3C10(I5N2)2 Aea2 (41) mp-1194995 [hull=0.047, icsd=1, PRIMARY]; H6PbCI3N Pnma (62) mp-995214 [hull=0.039, icsd=1, PRIMARY]; H12PbC2(I3N)2 P1 (1) mp-1120805 [hull=0.085, PRIMARY]; H3PbCI3N2 Pnma (62) mp-1232356 [hull=0.240, PRIMARY]; H5PbCI3N2 Pmm2 (25) mp-977014 [hull=0.037, PRIMARY]
- papers: Doping optimization of organic-inorganic hybrid perovskite CH 3 NH 3 PbI 3 for high thermoelectric efficiency | Bismuth Doping–Induced Stable Seebeck Effect Based on MAPbI\n            3\n            Polycrystalline Thin Films

## C-O-W
- rank 988 | 6 samples | 1 papers | 1 compositions
- compositions: W(CO)6 (6)
- measured range: 13-293 K (5th-95th pct of 6 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): HW2C9NO10 P-1 (2) mp-1224650 [hull=0.578, PRIMARY]; W2(CO)3 Cmmm (65) mp-1216282 [hull=1.279, PRIMARY]; W2CO Pmm2 (25) mp-1216273 [hull=1.612, PRIMARY, AMBIGUOUS]; W4C3O P-6m2 (187) mp-1216217 [hull=1.419, PRIMARY]; WCO2 P4/mmm (123) mp-1216158 [hull=1.333, PRIMARY]
- papers: Focused-Ion-Beam Direct-Writing of Ultra-Thin Superconducting Tungsten Composite Films

## C-O-Zn
- rank 989 | 6 samples | 2 papers | 3 compositions
- compositions: ZnOC0.14 (4); Zn0.98Al0.02OC0.17 (1); Zn0.98Al0.02OC0.24 (1)
- dopant candidates (<5% at.): Al (2)
- measured range: 42-1173 K (5th-95th pct of 32 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Zn(CO3)2 C2/c (15) mp-1188502 [hull=0.750, icsd=1, PRIMARY]; Zn5(CO6)2 C2/m (12) mp-1189100 [hull=0.242, icsd=1, PRIMARY]; ZnCO3 R-3c (167) mp-9812 [hull=0.000, icsd=1, PRIMARY]; ZnC5O8 Pbca (61) mp-1209101 [hull=1.158, PRIMARY]
- papers: One-Step Chemical Synthesis of ZnO/Graphene Oxide Molecular Hybrids for High-Temperature Thermoelectric Applications | Orientation dependent physical transport behavior and the micro-mechanical response of ZnO nanocomposites induced by SWCNTs and graphene: importance of intrinsic anisotropy and interfaces

## Ca-Co-Nd-O
- rank 990 | 6 samples | 1 papers | 3 compositions
- compositions: Nd0.75Ca0.25CoO3 (2); Nd0.625Ca0.375CoO3 (2); Nd0.5Ca0.5CoO3 (2)
- measured range: 10-347 K (5th-95th pct of 6 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): CaNdCoO4 I4mm (107) mp-1227058 [hull=0.044, PRIMARY, AMBIGUOUS]; CaNdCoO4 Cmcm (63) mp-1227089 [hull=0.050]
- papers: Transport and Magnetic Properties of R1-xAxCoO3(R = La, Pr and Nd; A = Ba, Sr and Ca)

## Ca-Cu-O-Ru
- rank 991 | 6 samples | 3 papers | 2 compositions
- compositions: CaCu3Ru4O12 (4); CaCu3Ti0.5Ru3.5O12 (2)
- dopant candidates (<5% at.): Ti (2)
- measured range: 11-298 K (5th-95th pct of 7 curves; full span incl. outliers 11-884 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): CaCu3(RuO3)4 Im-3 (204) mp-6036 [hull=0.025, icsd=3, PRIMARY]
- papers: Thermoelectric properties of the AA′3B4O12-type ordered perovskite oxides | Thermoelectric materials taking advantage of spin entropy: lessons from chalcogenides and oxides | Electronic phase transition between localized and itinerant states in the solid-solution system \n<mml:math xmlns:mml=\"http://www.w3.org/1998/Math/MathML\"><mml:mrow><mml:msub><mml:mi>CaCu</mml:mi><mml:mn>3</mml:mn></mml:msub><mml:msub><mml:mi>Ti</mml:mi><mml:mrow><mml:mn>4</mml:mn><mml:mo>−</mml:mo><mml:mi>x</mml:mi></mml:mrow></mml:msub><mml:msub><mml:mi>Ru</mml:mi><mml:mi>x</mml:mi></mml:msub><mml:msub><mml:mi mathvariant=\"normal\">O</mml:mi><mml:mn>12</mml:mn></mml:msub></mml:mrow></mml:math>

## Ca-Cu-O-Ti
- rank 992 | 6 samples | 3 papers | 2 compositions
- compositions: CaCu3Ti4O12 (3); CaCu3Ti3.5Ru0.5O12 (3)
- dopant candidates (<5% at.): Ru (3)
- measured range: 11-1072 K (5th-95th pct of 12 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): CaTi4(CuO4)3 Im-3 (204) mp-22592 [hull=0.054, icsd=15, PRIMARY]; CaTiCuO4 P4/nmm (129) mp-1147567 [hull=0.124, PRIMARY]; CaTi4(CuO4)3 Im-3m (229) mp-647452 [hull=0.430, icsd=1]
- papers: Thermoelectric Properties and Conduction Mechanism of CaCu3Ti4O12 Ceramics at High Temperatures | Thermoelectric properties of the AA′3B4O12-type ordered perovskite oxides | Electronic phase transition between localized and itinerant states in the solid-solution system \n<mml:math xmlns:mml=\"http://www.w3.org/1998/Math/MathML\"><mml:mrow><mml:msub><mml:mi>CaCu</mml:mi><mml:mn>3</mml:mn></mml:msub><mml:msub><mml:mi>Ti</mml:mi><mml:mrow><mml:mn>4</mml:mn><mml:mo>−</mml:mo><mml:mi>x</mml:mi></mml:mrow></mml:msub><mml:msub><mml:mi>Ru</mml:mi><mml:mi>x</mml:mi></mml:msub><mml:msub><mml:mi mathvariant=\"normal\">O</mml:mi><mml:mn>12</mml:mn></mml:msub></mml:mrow></mml:math>

## Ca-Eu-Sb-Zn
- rank 993 | 6 samples | 3 papers | 5 compositions
- compositions: Eu0.5Ca0.5Zn2Sb2 (2); Ca0.7Eu0.3Zn2Sb2 (1); Ca0.3Eu0.7Zn2Sb2 (1); Eu0.4Ca0.6Zn2Sb2 (1); Eu0.3Ca0.7Zn2Sb2 (1)
- measured range: 293-804 K (5th-95th pct of 32 curves)
- papers: Thermoelectric Properties of Zintl Phase Compounds of Ca1−x Eu x Zn2Sb2 (0 ≤ x ≤ 1) | Enhancement of thermoelectric performance of phase pure Zintl compounds Ca 1−x Yb x Zn 2 Sb 2 , Ca 1 −x Eu x Zn 2 Sb 2 , and Eu 1 −x Yb x Zn 2 Sb 2  by mechanical alloying and hot pressing | Single parabolic band transport in p-type EuZn2Sb2 thermoelectrics

## Ca-Ga-Sb
- rank 994 | 6 samples | 2 papers | 5 compositions
- compositions: Ca5Ga2Sb6 (2); Ca5Ga1.7Zn0.3Sb6 (1); Ca5Ga1.95Zn0.05Sb6 (1); Ca5Ga1.9Zn0.1Sb6 (1); Ca5Ga1.8Zn0.2Sb6 (1)
- dopant candidates (<5% at.): Zn (4)
- measured range: 298-874 K (5th-95th pct of 22 curves; full span incl. outliers 296-961 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ca5(GaSb3)2 Pbam (55) mp-17985 [hull=0.000, icsd=1, PRIMARY]; Ca11GaSb9 Iba2 (45) mp-1214384 [hull=0.000, PRIMARY]
- papers: Improved thermoelectric properties in Zn-doped Ca5Ga2Sb6 | Influence of the Triel Elements (M= Al, Ga, In) on the Transport Properties of Ca5M2Sb6Zintl Compounds

## Ca-K-Nb-O
- rank 995 | 6 samples | 1 papers | 1 compositions
- compositions: KCa2Nb3O10 (6)
- measured range: 11-293 K (5th-95th pct of 6 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): KCa2Nb3O10 Cmc2_1 (36) mp-1223594 [hull=0.012, PRIMARY]
- papers: Transport properties of Li intercalated KCa2Nb3O10

## Ca-O-Ti-V
- rank 996 | 6 samples | 1 papers | 2 compositions
- compositions: CaV0.6Ti0.4O3 (3); CaV0.7Ti0.3O3 (3)
- measured range: 11-320 K (5th-95th pct of 6 curves)
- papers: X-ray diffraction, magnetic, and transport study of lattice instabilities and metal-insulator transition inCaV1−xTixO3(0⩽x⩽0.4)

## Ca-Sb-Yb-Zn
- rank 997 | 6 samples | 2 papers | 3 compositions
- compositions: Ca0.75Yb0.25Zn2Sb2 (2); Ca0.5Yb0.5Zn2Sb2 (2); Ca0.25Yb0.75Zn2Sb2 (2)
- measured range: 297-774 K (5th-95th pct of 27 curves)
- papers: Zintl Phases as Thermoelectric Materials: Tuned Transport Properties of the Compounds CaxYb1-xZn2Sb2 | Enhancement of thermoelectric performance of phase pure Zintl compounds Ca 1−x Yb x Zn 2 Sb 2 , Ca 1 −x Eu x Zn 2 Sb 2 , and Eu 1 −x Yb x Zn 2 Sb 2  by mechanical alloying and hot pressing

## Cd-Cu-Fe-O
- rank 998 | 6 samples | 2 papers | 5 compositions
- compositions: Cd0.6Cu0.4Fe2O4 (2); Cd0.4Cu0.6Fe2O4 (1); Cd0.4Cu0.6Fe1.9Gd0.1O4 (1); Cu0.6Cd0.4Fe2O4 (1); Cu0.4Cd0.6Fe2O4 (1)
- dopant candidates (<5% at.): Gd (1)
- measured range: 305-687 K (5th-95th pct of 8 curves; full span incl. outliers 305-791 K)
- papers: Thermoelectric power in Gd3+-substituted Cu-Cd ferrites | Electrical transport properties of cadmium substituted copper ferrites

## Cd-Cu-Ge-Se
- rank 999 | 6 samples | 1 papers | 6 compositions
- compositions: Cu2.086Cd0.950Ge0.906Se4.058 (1); Cu2.123Cd0.935Ge0.901Se4.041 (1); Cu2.105Cd0.892Ge0.909Se4.094 (1); Cu2.103Cd0.915Ge0.911Se4.071 (1); Cu2.147Cd0.900Ge0.903Se4.050 (1); Cu2.125Cd0.875GeSe4 (1)
- measured range: 335-723 K (5th-95th pct of 24 curves)
- [ref 1] TEDesignLab / ICSD: CdCu2GeSe4 I-42m (121) mp-10967 [hull=0.000, icsd=4, PRIMARY]
- [ref 2] MP, ranked by ICSD evidence: CdCu2GeSe4 Pc (7) mp-1226932 [hull=0.020]
- papers: The effect of Cu addition on the thermoelectric properties of Cu2CdGeSe4

## Cd-Cu-Sb-Se
- rank 1000 | 6 samples | 1 papers | 6 compositions
- compositions: Cu3.0Cd1.0SbSe4 (1); Cu2.50Cd0.50Sb0.94Sn0.06Se4 (1); Cu2.0Cd1.0Sb0.94Sn0.06Se4 (1); Cu2.50Cd0.50SbSe4 (1); Cu2.25Cd0.75SbSe4 (1); Cu2.25Cd0.75Sb0.94Sn0.06Se4 (1)
- dopant candidates (<5% at.): Sn (3)
- measured range: 298-636 K (5th-95th pct of 29 curves)
- papers: The reduction of thermal conductivity in Cd and Sn co-doped Cu3SbSe4-based composites with a secondary-phase CdSe
