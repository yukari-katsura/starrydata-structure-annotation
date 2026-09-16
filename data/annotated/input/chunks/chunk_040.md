# Host systems -- chunk 040 of 73

Ranks 1951-2000 by sample count. These 50 host systems cover 100 samples (0.19% of the TE set); cumulative through this chunk: 96.11%.

Assign each host system a structural prototype from `data/annotated/taxonomy/prototypes_seed_v3.json`, or propose a new one in `taxonomy/prototypes_proposed.jsonl` first. Append results to `data/annotated/annotations/family_assignments.jsonl`.

The hand-entered MaterialFamily labels are deliberately NOT shown here -- they are held out in `df_host_systems.parquet` to validate this classification later. Decide from the compositions.

A "seed hypothesis" line means the taxonomy already names this host under that prototype. Confirm it against the compositions rather than accepting it; two or more listed means the host is mixed and needs splitting per composition.

Evidence follows the project precedence. Your judgement about the thermoelectric chemistry decides the prototype. [ref 1] is TEDesignLab, ICSD-backed and thermoelectric-specific -- prefer it. [ref 2] is Materials Project. Within a formula, polymorphs are ranked by ICSD reference count and the top one is marked PRIMARY -- not by e_above_hull, which is unusable for layered chalcogenides in the 2019 dump (Sb2Te3 R-3m carries 26 ICSD refs at hull 1.02). A primary resting on fewer than 5 ICSD references is flagged weak; the ambient phase may simply be absent from the snapshot, as it is for Bi2Se3.

While you have the host in view, also record what each minor element DOES, in `dopant_roles` -- the role follows from the prototype and cannot be judged without it. A median host has 2 such elements. Not everything listed is a dopant: O, C, N and H are usually milling or pressing residue, and an element just under 5 at.% may be an alloying end member rather than dilute doping. The doping LEVEL is computed later from the parsed fractions -- do not work it out by hand here.

A polymorph list is NOT a thermal sequence. SnSe has three known structures but only Pnma -> Cmcm happens on heating; rocksalt SnSe is metastable (2 icsd refs against 32). Put thermally reached phases in `phases` with their transition temperatures, and everything else in `other_polymorphs` with an occurrence reason. hull and icsd counts are shown to help you tell them apart.

A host may need MORE THAN ONE prototype. Transport is measured across a wide window and many thermoelectrics transform inside it, so where a "MEASUREMENT CROSSES A TRANSITION" line appears, record each phase with its own temperature range in the `phases` field. Transition temperatures shown are approximate and composition-dependent.

Both references describe which phases EXIST in a chemistry, not which phase this paper made. Al-O-Zn is best attested as ZnAl2O4 spinel (227) while almost every sample in it is Al-doped wurtzite ZnO (186). Weigh them against the compositions; do not follow them blindly.

## Ba-Cu-O-Sr-Yb
- rank 1951 | 2 samples | 1 papers | 2 compositions
- compositions: YbBa1.2Sr0.8Cu3O7 (1); YbBaSrCu3O7 (1)
- measured range: 55-259 K (5th-95th pct of 2 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ba8Sr2Yb5(Cu3O7)5 Pm (6) mp-1228720 [hull=0.036, PRIMARY]
- papers: Structure and superconductivity studies on LnBa2−xSrxCu3O7 (Ln=Yb and Lu; 0.0≤x≤0.5)

## Ba-Cu-Se-Sn
- rank 1952 | 2 samples | 2 papers | 1 compositions
- compositions: BaCu2SnSe4 (2)
- measured range: 217-296 K (5th-95th pct of 2 curves; full span incl. outliers 217-674 K)
- [ref 1] TEDesignLab / ICSD: BaCu2SnSe4 Ama2 (40) mp-12364 [hull=0.000, icsd=1, PRIMARY]
- papers: Exploratory synthesis of new heavy main group chalcogenides | Origins of ultralow thermal conductivity in 1-2-1-4 quaternary selenides

## Ba-Cu-Se-Te
- rank 1953 | 2 samples | 1 papers | 1 compositions
- compositions: BaCu5.9SeTe6 (2)
- measured range: 303-618 K (5th-95th pct of 10 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): BaCu6Te6Se P2 (3) mp-1228039 [hull=0.053, PRIMARY]
- papers: Thermoelectric Properties of the Quaternary Chalcogenides BaCu5.9STe6and BaCu5.9SeTe6

## Ba-Fe-Mn-Mo-O-Sr
- rank 1954 | 2 samples | 1 papers | 2 compositions
- compositions: Sr2BaFeMnMo0.8V0.2O6 (1); Sr1.4Ba0.6Fe1MnMo0.8V0.2O6 (1)
- dopant candidates (<5% at.): V (2)
- measured range: 373-973 K (5th-95th pct of 4 curves)
- papers: Thermoelectric Properties of Double Perovskite (Sr, Ba)2(Fe, Mn)(Mo, V)O6

## Ba-Fe-Mo-O-Sr
- rank 1955 | 2 samples | 1 papers | 2 compositions
- compositions: Sr1.4Ba0.6Fe0.8Mn0.2Mo0.8V0.2O6 (1); Sr1.4Ba0.6Fe0.9Mn0.1Mo0.8V0.2O6 (1)
- dopant candidates (<5% at.): Mn (2), V (2)
- measured range: 374-972 K (5th-95th pct of 4 curves)
- papers: Thermoelectric Properties of Double Perovskite (Sr, Ba)2(Fe, Mn)(Mo, V)O6

## Ba-Fe-O-Pr-Sr
- rank 1956 | 2 samples | 1 papers | 2 compositions
- compositions: Sr0.6Ba0.6Pr0.4Cu0.2Ti0.2Fe0.8O3 (1); Sr0.4Ba0.4Pr0.6Cu0.2Ti0.2Fe0.8O3 (1)
- dopant candidates (<5% at.): Cu (2), Ti (2)
- measured range: 573-1073 K (5th-95th pct of 2 curves)
- papers: Physical properties of (SrBa)1-xPrx(CuTi)0.2Fe0.8O3-δ (x = 0–1.0) and its application in H-SOFCs

## Ba-Fe-O-Sm
- rank 1957 | 2 samples | 2 papers | 2 compositions
- compositions: Sm1.875Ba3.125Fe5O15 (1); Sm0.5Ba0.5FeO3 (1)
- measured range: 316-1124 K (5th-95th pct of 2 curves; full span incl. outliers 316-1164 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ba2Sm2Fe4O11 Cmmm (65) mp-704632 [hull=0.020, PRIMARY]
- papers: Cobalt-free quintuple perovskite Sm 1.875 Ba 3.125 Fe 5 O 15−δ as a novel cathode for intermediate temperature solid oxide fuel cells | Structure and properties of perovskites for SOFC cathodes as a function of the A-site cation size disorder

## Ba-La-Mn-O-Ti
- rank 1958 | 2 samples | 1 papers | 1 compositions
- compositions: La0.7Ba0.3Ti0.5Mn0.4Ni0.1O3 (2)
- dopant candidates (<5% at.): Ni (2)
- measured range: 723-1123 K (5th-95th pct of 2 curves)
- papers: A-site cation influences on performance, structure and conductivity of a lanthanide-based perovskite electrode for symmetrical solid oxide fuel cells

## Ba-Mn-O-Pd-Pr
- rank 1959 | 2 samples | 1 papers | 1 compositions
- compositions: (Pr0.67Ba0.33MnO3)0.7(PdO)0.3 (2)
- measured range: 12-285 K (5th-95th pct of 2 curves)
- papers: Magnetotransport, magnetization and thermoelectric power of Pr2/3Ba1/3MnO3 : PdO composite manganites

## Ba-Mo-O
- rank 1960 | 2 samples | 2 papers | 1 compositions
- compositions: BaMoO3 (2)
- measured range: 285-1275 K (5th-95th pct of 3 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): BaMoO4 I4_1/a (88) mp-19276 [hull=0.000, icsd=9, PRIMARY]; Ba(Mo3O5)2 P1 (1) mp-624196 [hull=0.172, icsd=1, PRIMARY]; BaMo3O10 P2_1 (4) mp-1182540 [hull=0.015, icsd=1, PRIMARY]; BaMoO3 Pm-3m (221) mp-19322 [hull=0.000, icsd=1, PRIMARY]; Ba3(Mo9O14)2 P2_1 (4) mp-745095 [hull=0.238, PRIMARY]
- papers: Thermoelectric properties of perovskite type barium molybdate | Thermoelectric properties of perovskite type strontium ruthenium oxide

## Ba-O-Os
- rank 1961 | 2 samples | 2 papers | 2 compositions
- compositions: Ba3Os2O9 (1); BaOsO3 (1)
- measured range: 19-351 K (5th-95th pct of 2 curves; full span incl. outliers 19-395 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): BaOsO9 Pnma (62) mp-1203815 [hull=0.541, icsd=1, PRIMARY]; BaOsO3 Pm-3m (221) mp-781625 [hull=0.086, icsd=1, PRIMARY]; BaOsO2 I4_1/amd (141) mp-1214372 [hull=0.785, PRIMARY]; Ba2OsO4 I4/mmm (139) mp-1147775 [hull=0.076, PRIMARY]
- papers: Synthesis, crystal structure, and magnetic properties of Ba 3 Os 2 O 9 : A new osmate with Cs 3 Tl 2 Cl 9 -type structure | High-Pressure Synthesis of 5d Cubic Perovskite BaOsO<sub>3</sub> at 17 GPa: Ferromagnetic Evolution over 3d to 5d Series

## Ba-O-Sn-Sr
- rank 1962 | 2 samples | 1 papers | 2 compositions
- compositions: (Ba0.6Sr0.4)0.95La0.05SnO3 (1); (Ba0.4Sr0.6)0.95La0.05SnO3 (1)
- dopant candidates (<5% at.): La (2)
- measured range: 368-1069 K (5th-95th pct of 2 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ba3Sr(SnO3)4 Pmmm (47) mp-1228079 [hull=0.014, PRIMARY]; Ba4Sr(SnO3)5 P4/mmm (123) mp-1228076 [hull=0.011, PRIMARY]; BaSr(SnO3)2 P4/mmm (123) mp-1227742 [hull=0.024, PRIMARY]; BaSr2(SnO3)3 C2 (5) mp-1227830 [hull=0.012, PRIMARY]; BaSr3(SnO3)4 Pm (6) mp-1227795 [hull=0.021, PRIMARY]
- papers: High-Temperature Thermoelectric Properties of La-Doped Ba1-xSrxSnO3 Ceramics

## Ba-O-Ti-Zr
- rank 1963 | 2 samples | 1 papers | 2 compositions
- compositions: (Ba0.9Sm0.1)(Zr0.52Ti0.48)O3 (1); (Ba0.8Sm0.2)(Zr0.52Ti0.48)O3 (1)
- dopant candidates (<5% at.): Sm (2)
- measured range: 312-672 K (5th-95th pct of 2 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ba2ZrTiO6 Fm-3m (225) mp-1078457 [hull=0.005, icsd=2, PRIMARY]; Ba4Zr3TiO12 P4/mmm (123) mp-1228038 [hull=0.015, PRIMARY]
- papers: NTCR behavior of Sm-substituted barium zirconium titanate nanocrystalline solid solution

## Ba-O-U
- rank 1964 | 2 samples | 2 papers | 1 compositions
- compositions: BaUO3 (2)
- measured range: 284-1255 K (5th-95th pct of 5 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): BaUO4 Pbcm (57) mp-5611 [hull=0.000, icsd=5, PRIMARY]; Ba2U2O7 Imma (74) mp-917358 [hull=0.000, icsd=1, PRIMARY]; BaU2O7 I4_1/amd (141) mp-27649 [hull=0.010, icsd=1, PRIMARY]; Ba17U11O42 P-1 (2) mp-759291 [hull=0.000, PRIMARY]; Ba2U2O3 Pm (6) mp-675410 [hull=0.356, PRIMARY]
- papers: Thermoelectric properties of BaUO3 | Thermophysical properties of BaUO3

## Ba-O-W
- rank 1965 | 2 samples | 1 papers | 1 compositions
- compositions: BaWO4 (2)
- measured range: 297-563 K (5th-95th pct of 2 curves)
- [ref 1] TEDesignLab / ICSD: Ba3W2O9 R-3c (167) mp-18867 [hull=0.005, icsd=3, PRIMARY]
- [ref 2] MP, ranked by ICSD evidence: BaWO4 I4_1/a (88) mp-19048 [hull=0.000, icsd=11, PRIMARY]; Ba3WO6 Fm-3m (225) mp-25172 [hull=0.055, icsd=1, PRIMARY]; Ba2WO6 P2_1/c (14) mp-1196168 [hull=0.148, icsd=1, PRIMARY]; Ba(WO3)6 C2/m (12) mp-868170 [hull=0.000, PRIMARY]; Ba10LiW7O30 P3m1 (156) mp-773964 [hull=0.063, PRIMARY]
- papers: Thermal and mechanical properties of BaWO4 crystal

## Ba-Os-Sb
- rank 1966 | 2 samples | 1 papers | 1 compositions
- compositions: BaOs4Sb12 (2)
- measured range: 10-286 K (5th-95th pct of 3 curves; full span incl. outliers 10-482 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ba(Sb3Os)4 Im-3 (204) mp-1106056 [hull=0.000, icsd=1, PRIMARY]
- papers: Roles of spin fluctuations and rattling in magnetic and thermoelectric properties of AT4Sb12 (A=Ca, Sr, Ba, La; T=Fe, Ru, Os)

## Ba-Ru-Sb
- rank 1967 | 2 samples | 1 papers | 1 compositions
- compositions: BaRu4Sb12 (2)
- measured range: 12-292 K (5th-95th pct of 3 curves; full span incl. outliers 12-498 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ba(Sb3Ru)4 Im-3 (204) mp-9976 [hull=0.000, icsd=2, PRIMARY]; Ba(SbRu)2 I4/mmm (139) mp-1069937 [hull=0.031, icsd=1, PRIMARY]
- papers: Roles of spin fluctuations and rattling in magnetic and thermoelectric properties of AT4Sb12 (A=Ca, Sr, Ba, La; T=Fe, Ru, Os)

## Bi-Br-Cu-O-Se
- rank 1968 | 2 samples | 1 papers | 1 compositions
- compositions: Bi6Cu2Se3BrO6 (2)
- measured range: 295-875 K (5th-95th pct of 10 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Cu3BiSe2BrO8 Pmmn (59) mp-628637 [hull=0.000, icsd=1, PRIMARY]
- papers: Electrical and Thermal Transport Properties of\n            n\n            ‐type Bi\n            6\n            Cu\n            2\n            Se\n            4\n            O\n            6\n            (2BiCuSeO + 2Bi\n            2\n            O\n            2\n            Se)

## Bi-Br-Te
- rank 1969 | 2 samples | 2 papers | 1 compositions
- compositions: BiTeBr (2)
- measured range: 10-296 K (5th-95th pct of 8 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Bi(TeBr2)2 P-1 (2) mp-29127 [hull=0.028, icsd=1, PRIMARY]; BiTeBr P3m1 (156) mp-33723 [hull=0.000, PRIMARY]
- papers: Galvanomagnetic and thermoelectric properties of BiTeBr and BiTeI single crystals and their electronic structure | On the electronic structure and thermoelectric properties of BiTeBr and BiTeI single crystals and of BiTeI with the addition of BiI3 and CuI

## Bi-C-H-N-Te
- rank 1970 | 2 samples | 1 papers | 1 compositions
- compositions: (Bi2Te3)67.58(C4H2NH)32.42 (2)
- measured range: 299-476 K (5th-95th pct of 10 curves)
- papers: Effects of the Interface between Inorganic and Organic Components in a Bi2Te3–Polypyrrole Bulk Composite on Its Thermoelectric Performance

## Bi-C-Se-Te
- rank 1971 | 2 samples | 2 papers | 2 compositions
- compositions: Bi2(Se0.15Te0.85)3C0.6 (1); Bi2Te2.4Se0.6C0.3 (1)
- measured range: 296-545 K (5th-95th pct of 9 curves)
- papers: Fabrication Process and Thermoelectric Properties of CNT/Bi2(Se,Te)3Composites | On the effect of carbon nanotubes on the thermoelectric properties of n-Bi2Te2.4Se0.6 made by mechanical alloying

## Bi-C-Si-Te
- rank 1972 | 2 samples | 1 papers | 1 compositions
- compositions: Bi2(Te0.91Se0.09)3SiC (2)
- dopant candidates (<5% at.): Se (2)
- measured range: 303-469 K (5th-95th pct of 4 curves)
- papers: From thermoelectric bulk to nanomaterials: Current progress for Bi2Te3and CoSb3

## Bi-Ca
- rank 1973 | 2 samples | 2 papers | 2 compositions
- compositions: Ca16Bi11 (1); Ca14AlBi11 (1)
- dopant candidates (<5% at.): Al (1)
- measured range: 12-941 K (5th-95th pct of 5 curves; full span incl. outliers 12-1272 K)
- [ref 1] TEDesignLab / ICSD: Ca2Bi (139) [PRIMARY]
- [ref 2] MP, ranked by ICSD evidence: Ca5Bi3 Pnma (62) mp-27145 [hull=0.000, icsd=2, PRIMARY]; Ca11Bi10 I4/mmm (139) mp-27298 [hull=0.000, icsd=1, PRIMARY]; CaBi2 Cmcm (63) mp-1077466 [hull=0.000, icsd=1, PRIMARY]; Ca2Bi7 C2/m (12) mp-1227392 [hull=0.176, PRIMARY]; Ca3Bi2 Pm-3m (221) mp-1013735 [hull=0.366, PRIMARY]
- papers: Thermoelectric properties and electronic structure calculations of low thermal conductivity Zintl phase series M16X11 (M=Ca and Yb; X=Sb and Bi) | Ca14AlBi11—a new Zintl phase from earth-abundant elements with a great potential for thermoelectric energy conversion

## Bi-Ca-Co-O-Pb
- rank 1974 | 2 samples | 1 papers | 1 compositions
- compositions: (Bi0.5Pb0.5)2(Ca0.8Pr0.2)2Co2O7 (2)
- dopant candidates (<5% at.): Pr (2)
- measured range: 107-954 K (5th-95th pct of 2 curves)
- papers: Development of Thermoelectric Bi-Based Cobaltites with an Easy Axis of Magnetization Parallel to theC-Axis for Magnetic Alignment

## Bi-Ca-Cu-La-O-Sr
- rank 1975 | 2 samples | 1 papers | 2 compositions
- compositions: Bi2Sr1.3La0.9Ca0.8Cu2O8 (1); Bi2Sr1.1La0.8CaCu2O8 (1)
- measured range: 12-210 K (5th-95th pct of 8 curves)
- papers: In-plane thermoelectric properties of heavily underdoped high-temperature superconductor Bi2Sr2CaCu2O8+δ

## Bi-Ca-Cu-O-Se
- rank 1976 | 2 samples | 1 papers | 2 compositions
- compositions: Bi0.8Ca0.2CuSeO (1); Bi0.7Ca0.3CuSeO (1)
- measured range: 120-929 K (5th-95th pct of 8 curves)
- papers: The oxidation states of elements in pure and Ca-doped BiCuSeO thermoelectric oxides

## Bi-Ca-Mn
- rank 1977 | 2 samples | 1 papers | 1 compositions
- compositions: CaMnBi2 (2)
- measured range: 11-346 K (5th-95th pct of 6 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ca9Mn4Bi9 Pbam (55) mp-31042 [hull=0.112, icsd=2, PRIMARY]; Ca(MnBi)2 P-3m1 (164) mp-29615 [hull=0.365, icsd=1, PRIMARY]; CaMnBi2 P4/nmm (129) mp-611153 [hull=0.179, icsd=1, PRIMARY]
- papers: Large magnetothermopower effect in Dirac materials (Sr/Ca)MnBi2

## Bi-Cd-Cu-O-Sr
- rank 1978 | 2 samples | 1 papers | 1 compositions
- compositions: Bi2Sr2Ca0.2Cd0.8Cu2O8 (2)
- dopant candidates (<5% at.): Ca (2)
- measured range: 10-200 K (5th-95th pct of 2 curves; full span incl. outliers 10-300 K)
- papers: Structural characterization and transport properties of the HTc Bi2Sr2(Ca,Cd)Cu2O8+δ glass-ceramic rods

## Bi-Ce-La-Pt
- rank 1979 | 2 samples | 1 papers | 2 compositions
- compositions: (Ce0.75La0.25)3Bi4Pt3 (1); (Ce0.5La0.5)3Bi4Pt3 (1)
- measured range: 15-299 K (5th-95th pct of 2 curves)
- papers: Substitutional effects on the electronic transport of the Kondo semiconductorCe3Bi4Pt3

## Bi-Co-Gd
- rank 1980 | 2 samples | 1 papers | 2 compositions
- compositions: Gd12Co5Bi (1); Gd12Co5.3Bi (1)
- measured range: 12-874 K (5th-95th pct of 4 curves)

## Bi-Co-La-Mn-O
- rank 1981 | 2 samples | 1 papers | 1 compositions
- compositions: LaBiMn1.33Co0.67O6.02 (2)
- measured range: 112-320 K (5th-95th pct of 2 curves; full span incl. outliers 112-400 K)
- papers: Enhancement of ferromagnetism by Co and Ni substitution in the perovskite LaBiMn2O6+δ

## Bi-Co-La-O-Sr-Ti
- rank 1982 | 2 samples | 1 papers | 1 compositions
- compositions: (La0.7Sr0.3CoO3)85(SrBi4Ti4O15)15 (2)
- measured range: 297-805 K (5th-95th pct of 8 curves)
- papers: Colossal seebeck coefficient in Aurivillius phase-perovskite oxide composite

## Bi-Co-O
- rank 1983 | 2 samples | 1 papers | 1 compositions
- compositions: BiCoO3 (2)
- measured range: 10-295 K (5th-95th pct of 8 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): CoBiO3 Pnma (62) mp-1188346 [hull=0.117, icsd=1, PRIMARY]; Co(Bi3O5)4 I23 (197) mp-694906 [hull=0.019, PRIMARY]; Co(Bi5O8)5 C2 (5) mp-706332 [hull=0.030, PRIMARY]; Co(BiO3)2 P321 (150) mp-766738 [hull=0.000, PRIMARY]; Co3BiO8 P4_332 (212) mp-774284 [hull=0.048, PRIMARY]
- papers: Synthesis, Characterization, and Thermoelectric Properties of Electrospun Boron-Doped Barium-Stabilized Bismuth-Cobalt Oxide Nanoceramics

## Bi-Cs-Pb-Te
- rank 1984 | 2 samples | 1 papers | 2 compositions
- compositions: CsPbBi3Te6 (1); CsPb2Bi3Te7 (1)
- measured range: 79-350 K (5th-95th pct of 4 curves)
- papers: CsMBi3Te6and CsM2Bi3Te7(M = Pb, Sn):  New Thermoelectric Compounds with Low-Dimensional Structures

## Bi-Cu-O-Pb-Se
- rank 1985 | 2 samples | 2 papers | 2 compositions
- compositions: Bi0.80Pb0.20OCuSe (1); Bi0.80Pb0.20CuSeO (1)
- measured range: 100-673 K (5th-95th pct of 8 curves; full span incl. outliers 100-873 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Cu4Bi3Pb(SeO)4 I4mm (107) mp-1225836 [hull=0.000, PRIMARY]
- papers: Synthesis, structural characterisation and thermoelectric properties of Bi1−xPbxOCuSe | Complex electronic structure and compositing effect in high performance thermoelectric BiCuSeO

## Bi-Cu-Pb-Te
- rank 1986 | 2 samples | 1 papers | 2 compositions
- compositions: (PbBi3.96Cd0.04Te7)0.999Cu1 (1); (PbBi3.98Cd0.02Te7)0.999Cu1 (1)
- dopant candidates (<5% at.): Cd (2)
- papers: Thermoelectric Properties of Cation-Substituted Solid Solutions Based on Layered Tetradymite-like Compounds

## Bi-Cu-Se-Te
- rank 1987 | 2 samples | 1 papers | 2 compositions
- compositions: Cu0.36Bi2Te2.7Se0.3 (1); Cu0.6Bi2Te2.7Se0.3 (1)
- measured range: 301-484 K (5th-95th pct of 4 curves)
- papers: Thermoelectric Transport Properties of Cu Nanoprecipitates EmbeddedBi2Te2.7Se0.3

## Bi-Er-Ni-Sb
- rank 1988 | 2 samples | 1 papers | 2 compositions
- compositions: ErNiSb0.8Bi0.2 (1); ErNiSb0.4Bi0.6 (1)
- measured range: 15-298 K (5th-95th pct of 4 curves)
- papers: Observed Properties and Electronic Structure of RNiSb Compounds (R = Ho, Er, Tm, Yb and Y). Potential Thermoelectric Materials

## Bi-Er-Se
- rank 1989 | 2 samples | 1 papers | 2 compositions
- compositions: Bi1.7Er0.3Se3 (1); Bi1.6Er0.4Se3 (1)
- measured range: 297-480 K (5th-95th pct of 10 curves)
- papers: Effective decoupling of seebeck coefficient and the electrical conductivity through isovalent substitution of erbium in bismuth selenide thermoelectric material

## Bi-Eu-Mg-Sm-Yb
- rank 1990 | 2 samples | 1 papers | 2 compositions
- compositions: Sm0.5Yb0.25Eu0.25Mg2Bi1.99 (1); Sm0.25Yb0.375Eu0.375Mg2Bi1.99 (1)
- measured range: 305-778 K (5th-95th pct of 10 curves)
- papers: Achieving high-performance p-type SmMg2Bi2 thermoelectric materials through band engineering and alloying effects

## Bi-F-La-O-S
- rank 1991 | 2 samples | 1 papers | 2 compositions
- compositions: LaO0.75F0.25BiS2 (1); LaO0.5F0.5BiS2 (1)
- measured range: 23-738 K (5th-95th pct of 6 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): La2Bi2S4OF P-4m2 (115) mp-1223274 [hull=0.052, PRIMARY]; La4Bi4S8O3F I-42m (121) mp-1223105 [hull=0.000, PRIMARY]
- papers: High-temperature thermoelectric properties of novel layered bismuth-sulfide LaO1−xFxBiS2

## Bi-F-La-O-S-Sm
- rank 1992 | 2 samples | 1 papers | 1 compositions
- compositions: La0.5Sm0.5O0.5F0.5BiS2 (2)
- papers: Enhancement of superconductivity inLa1−xSmxO0.5F0.5BiS2

## Bi-F-La-O-Se
- rank 1993 | 2 samples | 1 papers | 2 compositions
- compositions: LaO0.6F0.4BiSe2 (1); LaO0.5F0.5BiSe2 (1)
- measured range: 16-299 K (5th-95th pct of 2 curves)
- papers: Synthesis and physical property characterization of LaOBiSe2 and LaO0.5F0.5BiSe2 superconductor

## Bi-F-O-S-Sm
- rank 1994 | 2 samples | 1 papers | 1 compositions
- compositions: La0.2Sm0.8O0.5F0.5BiS2 (2)
- dopant candidates (<5% at.): La (2)
- papers: Enhancement of superconductivity inLa1−xSmxO0.5F0.5BiS2

## Bi-Fe-Mn
- rank 1995 | 2 samples | 1 papers | 2 compositions
- compositions: Mn50Fe5Bi45 (1); Mn47Fe8Bi45 (1)
- measured range: 13-290 K (5th-95th pct of 2 curves)
- papers: Structural, magnetic, and electron transport properties of MnBi:Fe thin films

## Bi-Fe-O-Sb
- rank 1996 | 2 samples | 1 papers | 2 compositions
- compositions: Bi0.88Sb0.12(BaFe12O19)0.04 (1); Bi0.88Sb0.12(BaFe12O19)0.025 (1)
- dopant candidates (<5% at.): Ba (2)
- measured range: 10-341 K (5th-95th pct of 8 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Fe2BiSbO7 Imma (74) mp-1224738 [hull=0.314, PRIMARY]
- papers: Percolation Conduction in Hybrid Thermoelectric Material Consisting of Bi0.88Sb0.12 and Barium Ferrite Particles

## Bi-Fe-Se
- rank 1997 | 2 samples | 1 papers | 2 compositions
- compositions: Bi35.34Se57.33Fe7.33 (1); Bi33.87Se56.49Fe9.63 (1)
- measured range: 12-300 K (5th-95th pct of 6 curves)
- papers: Enhancing the thermopower and tuning the resistivity in Bi2Se3 with Fe-doping

## Bi-Ga-O-Sb-Te
- rank 1998 | 2 samples | 1 papers | 2 compositions
- compositions: Bi0.5Sb1.5Te3(Ga2O3)0.15 (1); Bi0.5Sb1.5Te3(Ga2O3)0.23 (1)
- measured range: 299-501 K (5th-95th pct of 6 curves)
- papers: Effect of Ga2O3 Nanoparticles Dispersion on Microstructure and Thermoelectric Properties of p-Type BiSbTe Based Alloys

## Bi-Ga-Sb-Te
- rank 1999 | 2 samples | 2 papers | 2 compositions
- compositions: (Ga2Te3)0.2(Bi0.5Sb1.5Te3)0.8 (1); Ga0.4Bi0.5Sb1.1Te3 (1)
- measured range: 316-497 K (5th-95th pct of 6 curves; full span incl. outliers 316-556 K)
- papers: Preparation and thermoelectric properties of p-type (Ga2Te3)x–(Bi0.5Sb1.5Te3)1−x (x=0–0.2) alloys prepared by spark plasma sintering | Microstructures and thermoelectric properties of p-type pseudo-binary Bi–Sb–Te alloys with partial substitution of Ga for Sb prepared by spark plasma sintering

## Bi-Ho-O
- rank 2000 | 2 samples | 1 papers | 2 compositions
- compositions: Ho2Sn0.2Bi0.8O3 (1); Ho2BiO3 (1)
- dopant candidates (<5% at.): Sn (1)
- measured range: 10-398 K (5th-95th pct of 2 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ho2BiO2 I4/mmm (139) mp-1067937 [hull=0.000, icsd=3, PRIMARY]; Ho(Bi3O5)4 I23 (197) mp-769405 [hull=0.059, PRIMARY]; Ho2Bi2O7 Fd-3m (227) mp-769229 [hull=0.093, PRIMARY]; HoBiO3 R3c (161) mp-1178162 [hull=0.032, PRIMARY]; HoBiO3 Pnma (62) mp-770830 [hull=0.036]
- papers: Rare-Earth Pnictide Oxides (RE,Ca)mPnnOm (Pn = Sb, Bi): A Review of Crystal Structures, Chemistry, Compositions, and Physical Properties
