# Host systems -- chunk 043 of 73

Ranks 2101-2150 by sample count. These 50 host systems cover 100 samples (0.19% of the TE set); cumulative through this chunk: 96.68%.

Assign each host system a structural prototype from `data/annotated/taxonomy/prototypes_seed_v3.json`, or propose a new one in `taxonomy/prototypes_proposed.jsonl` first. Append results to `data/annotated/annotations/family_assignments.jsonl`.

The hand-entered MaterialFamily labels are deliberately NOT shown here -- they are held out in `df_host_systems.parquet` to validate this classification later. Decide from the compositions.

A "seed hypothesis" line means the taxonomy already names this host under that prototype. Confirm it against the compositions rather than accepting it; two or more listed means the host is mixed and needs splitting per composition.

Evidence follows the project precedence. Your judgement about the thermoelectric chemistry decides the prototype. [ref 1] is TEDesignLab, ICSD-backed and thermoelectric-specific -- prefer it. [ref 2] is Materials Project. Within a formula, polymorphs are ranked by ICSD reference count and the top one is marked PRIMARY -- not by e_above_hull, which is unusable for layered chalcogenides in the 2019 dump (Sb2Te3 R-3m carries 26 ICSD refs at hull 1.02). A primary resting on fewer than 5 ICSD references is flagged weak; the ambient phase may simply be absent from the snapshot, as it is for Bi2Se3.

While you have the host in view, also record what each minor element DOES, in `dopant_roles` -- the role follows from the prototype and cannot be judged without it. A median host has 2 such elements. Not everything listed is a dopant: O, C, N and H are usually milling or pressing residue, and an element just under 5 at.% may be an alloying end member rather than dilute doping. The doping LEVEL is computed later from the parsed fractions -- do not work it out by hand here.

A polymorph list is NOT a thermal sequence. SnSe has three known structures but only Pnma -> Cmcm happens on heating; rocksalt SnSe is metastable (2 icsd refs against 32). Put thermally reached phases in `phases` with their transition temperatures, and everything else in `other_polymorphs` with an occurrence reason. hull and icsd counts are shown to help you tell them apart.

A host may need MORE THAN ONE prototype. Transport is measured across a wide window and many thermoelectrics transform inside it, so where a "MEASUREMENT CROSSES A TRANSITION" line appears, record each phase with its own temperature range in the `phases` field. Transition temperatures shown are approximate and composition-dependent.

Both references describe which phases EXIST in a chemistry, not which phase this paper made. Al-O-Zn is best attested as ZnAl2O4 spinel (227) while almost every sample in it is Al-doped wurtzite ZnO (186). Weigh them against the compositions; do not follow them blindly.

## Co-Fe-O-Y
- rank 2101 | 2 samples | 1 papers | 2 compositions
- compositions: YFe0.5Co0.5O3 (1); Ca0.1Y0.9Fe0.5Co0.5O3 (1)
- dopant candidates (<5% at.): Ca (1)
- sample form: pellets (2)
- measured range: 823-1023 K (5th-95th pct of 2 curves)
- papers: https://doi.org/10.1016/j.jpowsour.2018.12.030 (Enhanced oxygen reduction reaction through Ca and Co Co-doped YFeO3 as...)

## Co-Fe-Pb-Sb-Te
- rank 2102 | 2 samples | 1 papers | 2 compositions
- compositions: La0.3Ce0.37Fe3CoSb12PbTe (1); La0.3Ce0.37Fe3CoSb12(PbTe)1.5 (1)
- dopant candidates (<5% at.): Ce (2), La (2)
- sample form: Bulk (2)
- measured range: 472-773 K (5th-95th pct of 8 curves)
- papers: https://doi.org/10.1016/j.jallcom.2013.01.038 (Enhancement of thermoelectric figure of merit in binary-phased La0.3Ce...)

## Co-Fe-S-Sn
- rank 2103 | 2 samples | 1 papers | 2 compositions
- compositions: Co2.5Fe0.5Sn2S2 (1); Co2.5Fe0.5Sn1.8In0.2S2 (1)
- dopant candidates (<5% at.): In (1)
- sample form: Bulk (2)
- measured range: 297-621 K (5th-95th pct of 10 curves)
- papers: https://doi.org/10.1021/acsaem.9b02272 (Improved Thermoelectric Performance through Double Substitution in Sha...)

## Co-Fe-Sb-Zr
- rank 2104 | 2 samples | 1 papers | 1 compositions
- compositions: ZrFe0.2Co0.8Sb (2)
- sample form: Bulk (2)
- measured range: 300-897 K (5th-95th pct of 8 curves)
- papers: https://doi.org/10.1016/j.mseb.2015.03.015 (Microstructure and thermoelectric properties in Fe-doped ZrCoSb half-H...)

## Co-Fe-Te
- rank 2105 | 2 samples | 1 papers | 2 compositions
- compositions: Fe0.8Co0.2Te2 (1); Fe0.6Co0.4Te2 (1)
- sample form: Bulk (2)
- measured range: 291-829 K (5th-95th pct of 5 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): FeCoTe2 P-3m1 (164) mp-1224955 [hull=0.193, PRIMARY]
- papers: https://doi.org/10.1063/1.2361088 (Preparation and thermoelectric properties of sintered Fe1−xCoxTe2 (0≤x...)

## Co-Ga-Mn
- rank 2106 | 2 samples | 2 papers | 1 compositions
- compositions: Co2MnGa (2)
- measured range: 10-380 K (5th-95th pct of 4 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): MnGaCo2 Fm-3m (225) mp-21171 [hull=0.000, icsd=5, PRIMARY]; Mn2GaCo F-43m (216) mp-20160 [hull=0.139, icsd=1, PRIMARY]; MnGa2Co Fm-3m (225) mp-623453 [hull=0.158, icsd=1, PRIMARY]
- papers: https://doi.org/10.1038/s41427-019-0116-z (Anomalous Nernst effect beyond the magnetization scaling relation in t...) | https://doi.org/10.1103/physrevb.101.180404 (Anomalous transverse response of \n<mml:math xmlns:mml=\"http://www.w3...)

## Co-Ga-O-Sr
- rank 2107 | 2 samples | 1 papers | 1 compositions
- compositions: (Ga0.33Co0.67)2Sr2CoO6 (2)
- measured range: 10-300 K (5th-95th pct of 2 curves; full span incl. outliers 10-386 K)
- papers: https://doi.org/10.1016/j.jssc.2004.12.035 (A new layered cobaltite (Ga1/3Co2/3)2Sr2CoO6+δ with high spin Co3+: mo...)

## Co-Gd
- rank 2108 | 2 samples | 1 papers | 2 compositions
- compositions: Gd4Co3 (1); Gd(Co0.95Cu0.05)3 (1)
- dopant candidates (<5% at.): Cu (1)
- sample form: Bulk (2)
- measured range: 12-292 K (5th-95th pct of 2 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): GdCo2 Fd-3m (227) mp-1080387 [hull=0.000, icsd=25, PRIMARY]; GdCo5 P6/mmm (191) mp-1077071 [hull=0.018, icsd=15, PRIMARY]; Gd2Co17 P6_3/mmc (194) mp-1201816 [hull=0.000, icsd=3, PRIMARY]; Gd6Co5 P6_3/m (176) mp-1192075 [hull=0.000, icsd=1, PRIMARY]; Gd4Co3 P-3 (147) mp-1225806 [hull=0.005, PRIMARY]
- papers: https://doi.org/10.1063/1.3549597 (Thermoelectric power of Gd4(Co1-xCux)3 compounds)

## Co-Ge-Yb
- rank 2109 | 2 samples | 1 papers | 2 compositions
- compositions: Yb3Co4Ge13 (1); Yb2.3La0.7Co4Ge13 (1)
- dopant candidates (<5% at.): La (1)
- sample form: Bulk (2)
- measured range: 239-380 K (5th-95th pct of 8 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Yb5(Co2Ge5)2 P4/mbm (127) mp-1202795 [hull=0.023, icsd=2, PRIMARY]; Yb3Co4Ge13 Pm-3n (223) mp-1203071 [hull=0.000, icsd=1, PRIMARY]; Yb(CoGe)6 P6/mmm (191) mp-1103535 [hull=0.007, icsd=1, PRIMARY]; YbCoGe2 Cmcm (63) mp-1086674 [hull=0.000, icsd=1, PRIMARY]; Yb7In(CoGe3)4 P4/m (83) mp-641845 [hull=0.000, icsd=1, PRIMARY]
- papers: https://doi.org/10.1016/j.jallcom.2012.09.024 (Thermoelectric properties of Pr3Rh4Sn13-type Yb3Co4Ge13 and Yb3Co4Sn13...)

## Co-H-Sb
- rank 2110 | 2 samples | 1 papers | 2 compositions
- compositions: TI0.1In0.2Co4Sb12 (1); TI0.1In0.3Co4Sb12 (1)
- dopant candidates (<5% at.): In (2), I (2)
- sample form: Bulk (2)
- measured range: 325-761 K (5th-95th pct of 8 curves)
- papers: https://doi.org/10.1063/1.4748340 (Enhancement of thermoelectric properties of CoSb3-based skutterudites ...)

## Co-Hf-Nb-Sb-Ta-Ti-V-Zr
- rank 2111 | 2 samples | 1 papers | 1 compositions
- compositions: Ti0.167Zr0.167Hf0.167V0.167Nb0.167Ta0.167CoSb (2)
- sample form: Polycrystal (2)
- measured range: 322-925 K (5th-95th pct of 8 curves)
- papers: https://doi.org/10.1016/j.jallcom.2021.162045 (Synthesis and thermoelectric properties of high-entropy half-Heusler M...)

## Co-Hf-Pt-Sb-Sn-Zr
- rank 2112 | 2 samples | 2 papers | 1 compositions
- compositions: (Zr0.65Hf0.35)(Co0.65Pt0.35)(Sb0.65Sn0.35) (2)
- measured range: 11-301 K (5th-95th pct of 4 curves)
- papers: https://doi.org/10.1109/ict.2005.1519965 (Half-Heusler phases as prospective p-type thermoelectric materials) | https://doi.org/10.1063/1.1305829 (Thermoelectric properties of semimetallic (Zr, Hf)CoSb half-Heusler ph...)

## Co-In-S
- rank 2113 | 2 samples | 1 papers | 2 compositions
- compositions: Co3Sn0.2In1.8S2 (1); Co3In2S2 (1)
- dopant candidates (<5% at.): Sn (1)
- sample form: Bulk (2)
- measured range: 313-676 K (5th-95th pct of 6 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): In2Co3S2 R-3m (166) mp-19804 [hull=0.000, icsd=3, PRIMARY]; In2CoS4 Fd-3m (227) mp-21173 [hull=0.135, icsd=2, PRIMARY]
- papers: https://doi.org/10.1021/acs.chemmater.5b00801 (Interplay of Metal-Atom Ordering, Fermi Level Tuning, and Thermoelectr...)

## Co-La-Nb-O
- rank 2114 | 2 samples | 1 papers | 2 compositions
- compositions: LaCo0.75Nb0.25O3 (1); LaCo0.67Nb0.33O3 (1)
- measured range: 973-1273 K (5th-95th pct of 2 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): La4Nb(CoO4)3 P-1 (2) mp-1223118 [hull=0.032, PRIMARY]
- papers: https://doi.org/10.1016/j.jssc.2012.04.026 (Structure, thermal expansion and electrical conductivity of Nb-substit...)

## Co-Li-Mg-O
- rank 2115 | 2 samples | 1 papers | 2 compositions
- compositions: LiCo0.8Mg0.2O2 (1); LiCo0.7Mg0.3O2 (1)
- sample form: Bulk (2)
- measured range: 13-1180 K (5th-95th pct of 11 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Li14MgCo13O28 P-1 (2) mp-769537 [hull=0.012, PRIMARY]; Li2MgCo13O28 P1 (1) mp-764439 [hull=0.029, PRIMARY]; Li2MgCo3O8 C2/m (12) mp-1177928 [hull=0.048, PRIMARY]; Li4MgCo3O8 R-3m (166) mp-773461 [hull=0.026, PRIMARY]; Li8MgCo13O28 P1 (1) mp-778042 [hull=0.103, PRIMARY]
- papers: https://doi.org/10.7567/jjap.56.021101 (Thermoelectric properties of LiCo1−xMxO2(M = Cu, Mg, Ni, Zn): Comparis...)

## Co-Lu
- rank 2116 | 2 samples | 2 papers | 1 compositions
- compositions: LuCo2 (2)
- measured range: 12-627 K (5th-95th pct of 4 curves; full span incl. outliers 12-1000 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): LuCo2 Fd-3m (227) mp-1071554 [hull=0.000, icsd=11, PRIMARY]; Lu2Co17 P6_3/mmc (194) mp-1204082 [hull=0.000, icsd=2, PRIMARY]; LuCo3 R-3m (166) mp-1101900 [hull=0.000, icsd=2, PRIMARY]; Lu2Co7 R-3m (166) mp-1189949 [hull=0.012, icsd=1, PRIMARY]; Lu4Co3 P-3 (147) mp-1222465 [hull=0.000, PRIMARY]
- papers: https://doi.org/10.1016/s0921-4526(97)00157-9 (Transport phenomena in spin fluctuations systems) | https://doi.org/10.1088/0953-8984/7/33/008 (The transport properties of RCo2compounds)

## Co-Mn-O
- rank 2117 | 2 samples | 2 papers | 2 compositions
- compositions: (Mn0.5Co0.5)3O4 (1); Cu0.23Mn1.44Co1.32O4 (1)
- dopant candidates (<5% at.): Cu (1)
- curator composition details (from the paper): bulk (sintered pellet) (1)
- sample form: Unknown (1)
- measured range: 309-1067 K (5th-95th pct of 3 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Mn(CoO2)2 P1 (1) mp-767807 [hull=0.041, PRIMARY]; Mn(CoO2)4 C2/m (12) mp-773238 [hull=0.070, PRIMARY]; Mn(CoO3)2 C2/m (12) mp-763057 [hull=0.025, PRIMARY, AMBIGUOUS]; Mn2Co2O5 P4/mmm (123) mp-974861 [hull=0.522, PRIMARY]; Mn2Co5O12 C2 (5) mp-771625 [hull=0.106, PRIMARY]
- papers: https://doi.org/10.2109/jcersj2.15316 (Development and electrical properties of wurtzite (Al,Ti)N materials f...) | https://doi.org/10.1016/j.ceramint.2017.03.060 (Formation of sol–gel derived (Cu,Mn,Co)3O4 spinel and its electrical p...)

## Co-Mn-Si
- rank 2118 | 2 samples | 2 papers | 1 compositions
- compositions: Co2MnSi (2)
- curator composition details (from the paper): Co2MnSi + x mol %SiC; x=0 (1)
- sample form: Polycrystal (1)
- measured range: 308-1026 K (5th-95th pct of 8 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): MnCoSi Pnma (62) mp-19809 [hull=0.005, icsd=7, PRIMARY]; MnCo2Si Fm-3m (225) mp-4492 [hull=0.000, icsd=6, PRIMARY]; Mn2CoSi F-43m (216) mp-13082 [hull=0.020, icsd=1, PRIMARY]; MnCoSi2 P2_1 (4) mp-1221669 [hull=0.035, PRIMARY]; MnCoSi P6_3/mmc (194) mp-10365 [hull=0.413, icsd=1]
- papers: https://doi.org/10.1007/s11664-016-4944-0 (Structural and Thermoelectric Properties of Ternary Full-Heusler Alloys) | https://doi.org/10.1021/acsaem.5c00578 (Impact of SiC Nanodispersions on the Thermoelectric and Mechanical Pro...)

## Co-Mn-Sn
- rank 2119 | 2 samples | 2 papers | 1 compositions
- compositions: Co2MnSn (2)
- sample form: Bulk (1)
- measured range: 11-392 K (5th-95th pct of 5 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): MnCo2Sn Fm-3m (225) mp-20840 [hull=0.000, icsd=9, PRIMARY]; Mn2CoSn F-43m (216) mp-22465 [hull=0.177, icsd=2, PRIMARY]; MnCoSn P6_3/mmc (194) mp-1206556 [hull=0.087, PRIMARY]; MnCoSn4 I422 (97) mp-1221689 [hull=0.023, PRIMARY]
- papers: https://doi.org/10.1002/adfm.201102792 (Thermomagnetic Properties Improved by Self-Organized Flower-Like Phase...) | https://doi.org/10.1103/physrevb.82.104420 (Phase-separation-induced changes in the magnetic and transport propert...)

## Co-Mo-Nb-Sn
- rank 2120 | 2 samples | 1 papers | 2 compositions
- compositions: CoNb0.7Mo0.3Sn (1); CoNb0.5Mo0.5Sn (1)
- measured range: 332-843 K (5th-95th pct of 8 curves)
- papers: https://doi.org/10.1016/j.jallcom.2004.04.095 (High temperature thermoelectric properties of CoNb1−xMxSn half-Heusler...)

## Co-Na-Ni-O
- rank 2121 | 2 samples | 1 papers | 2 compositions
- compositions: Na(Co0.8Ni0.2)2O4 (1); Na(Co0.75Ni0.25)2O4 (1)
- sample form: Bulk (2)
- measured range: 721-1073 K (5th-95th pct of 6 curves)
- papers: https://doi.org/10.1016/j.matlet.2005.10.086 (Improvement in high-temperature thermoelectric properties of NaCo2O4 t...)

## Co-Nb-Sb-Ta-V
- rank 2122 | 2 samples | 1 papers | 2 compositions
- compositions: Ta0.333Nb0.333V0.333CoSb (1); Ta0.25Nb0.375V0.375CoSb (1)
- measured range: 20-702 K (5th-95th pct of 10 curves)
- papers: https://doi.org/10.1039/c5ra21404a (Thermal conductivity reduction by isoelectronic elements V and Ta for ...)

## Co-Nd-Sn
- rank 2123 | 2 samples | 1 papers | 2 compositions
- compositions: Nd6Co2Sn (1); Nd12Co6Sn (1)
- sample form: Bulk (2)
- measured range: 79-379 K (5th-95th pct of 4 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Nd3Co4Sn13 Pm-3n (223) mp-1198940 [hull=0.000, icsd=1, PRIMARY]; Nd2CoSn4 Amm2 (38) mp-1220521 [hull=0.000, PRIMARY]; Nd3(Co2Sn)4 P6_3mc (186) mp-1210125 [hull=0.057, PRIMARY]; Nd3Co6Sn5 Immm (71) mp-1209874 [hull=0.068, PRIMARY]; Nd6Co2Sn Immm (71) mp-1210166 [hull=0.028, PRIMARY]
- papers: https://doi.org/10.1016/s0925-8388(03)00644-3 (Crystal structure, magnetic and electric properties of ternary neodymi...)

## Co-Ni-O-Pr
- rank 2124 | 2 samples | 2 papers | 2 compositions
- compositions: PrNi0.4Co0.6O3 (1); PrNi0.6Co0.4O3 (1)
- measured range: 322-1172 K (5th-95th pct of 2 curves; full span incl. outliers 322-1272 K)
- papers: https://doi.org/10.3390/ma15062166 (Nickel-Containing Perovskites, PrNi0.4Fe0.6O3–δ and PrNi0.4Co0.6O3–δ, ...) | https://doi.org/10.1016/j.jpowsour.2011.10.025 (PrNi0.6Co0.4O3–Ce0.8Sm0.2O1.9 composite cathodes for intermediate temp...)

## Co-Ni-O-Sr
- rank 2125 | 2 samples | 1 papers | 2 compositions
- compositions: SrCo0.6Ni0.4O3 (1); SrCo0.7Ni0.3O3 (1)
- measured range: 298-773 K (5th-95th pct of 2 curves)
- papers: https://doi.org/10.1007/s10904-015-0295-1 (Structural, Electrical and Electrochemical Characterizations of Perovs...)

## Co-Ni-Sb-Sn-Ti-Zr
- rank 2126 | 2 samples | 1 papers | 2 compositions
- compositions: Ti1.1Al0.2Ta0.2Zr0.5NiCoSn0.5Sb1.5 (1); Ti0.6Al0.2Ta0.2ZrNiCoSn0.5Sb1.5 (1)
- dopant candidates (<5% at.): Al (2), Ta (2)
- curator composition details (from the paper): Ti2‑x−y−qAlxTayZrqNiCoSn0.5Sb1.5 (2)
- sample form: pellets (2)
- measured range: 294-875 K (5th-95th pct of 10 curves)
- papers: https://doi.org/10.1021/acsaem.4c03382 (Entropy Engineering in the Off-Stoichiometric Ti<sub>2</sub>NiCoSn<sub...)

## Co-O-Pb-Sr
- rank 2127 | 2 samples | 1 papers | 2 compositions
- compositions: Pb0.7Sr1.5Ca0.5Co0.3O3(CoO2)1.75 (1); Pb0.7Sr2Co0.3O3(CoO2)1.79 (1)
- dopant candidates (<5% at.): Ca (1)
- measured range: 11-699 K (5th-95th pct of 6 curves)
- papers: https://doi.org/10.1063/1.1494114 (Thermopower enhancement in misfit cobaltites)

## Co-O-Pr-W
- rank 2128 | 2 samples | 1 papers | 1 compositions
- compositions: CoPr2W2O10 (2)
- measured range: 297-494 K (5th-95th pct of 2 curves)
- papers: https://doi.org/10.1080/14786435.2012.704427 (Dielectric and magnetic permittivities of three new ceramic tungstates...)

## Co-Pb-Sb-Te
- rank 2129 | 2 samples | 1 papers | 2 compositions
- compositions: (PbTe)0.24Co0.88Ni0.12Sb2.91Sn0.09 (1); (PbTe)0.48Co0.88Ni0.12Sb2.91Sn0.09 (1)
- dopant candidates (<5% at.): Ni (2), Sn (2)
- curator composition details (from the paper): X content of PbTe(mass percentage) (2)
- measured range: 297-803 K (5th-95th pct of 4 curves)
- papers: https://doi.org/10.1007/s10904-011-9514-6 (Effect of PbTe on Thermoelectric Properties of Co0.88Ni0.12Sb2.91Sn0.09)

## Co-S-Ti
- rank 2130 | 2 samples | 1 papers | 2 compositions
- compositions: Co0.2Ti0.8S2 (1); Co0.3Ti0.7S2 (1)
- measured range: 10-310 K (5th-95th pct of 10 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ti2CoS4 C2/m (12) mp-1025269 [hull=0.004, icsd=1, PRIMARY]; Ti4CoS8 C2/m (12) mp-1105097 [hull=0.001, icsd=1, PRIMARY]; Ti3CoS6 R-3 (148) mp-1217185 [hull=0.002, PRIMARY]; Ti3CoS6 P6_322 (182) mp-1208259 [hull=0.057]
- papers: https://doi.org/10.1007/s11664-010-1474-z (Thermoelectric Properties of Co-Doped TiS2)

## Co-Sb-Zn
- rank 2131 | 2 samples | 1 papers | 2 compositions
- compositions: Zn3.5Co0.5Sb3 (1); Zn3.6Co0.4Sb3 (1)
- measured range: 299-600 K (5th-95th pct of 8 curves)
- papers: https://doi.org/10.1109/ict.2007.4569461 (Thermoelectric properties of vacuum melted Zn<inf>4&#x2212;x</inf>Co<i...)

## Co-Sc
- rank 2132 | 2 samples | 2 papers | 1 compositions
- compositions: ScCo2 (2)
- measured range: 12-983 K (5th-95th pct of 4 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): ScCo2 Fd-3m (227) mp-253 [hull=0.000, icsd=10, PRIMARY]; Sc2Co I4/mcm (140) mp-30562 [hull=0.011, icsd=3, PRIMARY]; ScCo Pm-3m (221) mp-2212 [hull=0.000, icsd=2, PRIMARY]; Sc3Co Pnma (62) mp-27162 [hull=0.000, icsd=1, PRIMARY]; Sc4Co Fd-3m (227) mp-1209073 [hull=0.467, PRIMARY]
- papers: https://doi.org/10.1016/s0921-4526(97)00157-9 (Transport phenomena in spin fluctuations systems) | https://doi.org/10.1088/0953-8984/7/33/008 (The transport properties of RCo2compounds)

## Co-Si-Ti
- rank 2133 | 2 samples | 2 papers | 1 compositions
- compositions: Co2TiSi (2)
- measured range: 11-894 K (5th-95th pct of 6 curves; full span incl. outliers 11-949 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): TiCo2Si Fm-3m (225) mp-1064854 [hull=0.000, icsd=5, PRIMARY]; TiCoSi Pnma (62) mp-21306 [hull=0.000, icsd=4, PRIMARY]; Ti6Co16Si7 Fm-3m (225) mp-672677 [hull=0.000, icsd=2, PRIMARY]; Ti4Co4Si7 I4/mmm (139) mp-1193657 [hull=0.000, icsd=2, PRIMARY]; Ti2CoSi F-43m (216) mp-999060 [hull=0.308, icsd=1, PRIMARY]
- papers: https://doi.org/10.1098/rsta.2011.0183 (Anomalous transport properties of the half-metallic ferromagnets Co2Ti...) | https://doi.org/10.1103/physrevb.81.064404 (Itinerant half-metallic ferromagnetsCo2TiZ(Z=Si, Ge, Sn):Ab initiocalc...)

## Co-Sm-Zn
- rank 2134 | 2 samples | 2 papers | 1 compositions
- compositions: Sm3Zn2Co3 (2)
- sample form: Rod (1)
- measured range: 214-376 K (5th-95th pct of 4 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): SmZnCo2 P6_3/mmc (194) mp-1208993 [hull=0.036, PRIMARY]
- papers: https://doi.org/10.1103/physrev.95.1134 (Thermoelectric Power and Electron Scattering in Metal Alloys) | https://doi.org/10.1134/s0031918x13080085 (Thermoelectric properties of rare-earth alloys)

## Cr-Cs-S
- rank 2135 | 2 samples | 1 papers | 1 compositions
- compositions: Cs0.97In0.03Cr2S4 (2)
- dopant candidates (<5% at.): In (2)
- measured range: 10-296 K (5th-95th pct of 4 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): CsCr5S8 C2/m (12) mp-1021518 [hull=0.041, PRIMARY]
- papers: https://doi.org/10.1209/0295-5075/104/17005 (Magnetic-polaron–induced colossal magnetocapacitance in CdCr2S4)

## Cr-Cu-Fe-S
- rank 2136 | 2 samples | 1 papers | 2 compositions
- compositions: Fe0.41Cu0.59Cr2S4 (1); Fe0.55Cu0.45Cr2S4 (1)
- measured range: 19-554 K (5th-95th pct of 2 curves)
- [ref 1] TEDesignLab / ICSD: Cr4FeCuS8 F-43m (216) mp-6685 [hull=0.045, icsd=2, PRIMARY]
- [ref 2] MP, ranked by ICSD evidence: Cr8Fe3CuS16 P-4m2 (115) mp-1226582 [hull=0.085, PRIMARY]; Cr8Fe3CuS16 R3m (160) mp-1226186 [hull=0.112]
- papers: https://doi.org/10.1063/1.2163563 (Electrical Transport in FeCr2S4‐CuCr2S4 Spinels)

## Cr-Cu-S-Ti
- rank 2137 | 2 samples | 2 papers | 1 compositions
- compositions: CuCrTiS4 (2)
- sample form: Bulk (1)
- measured range: 11-322 K (5th-95th pct of 6 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): TiCrCuS4 Imma (74) mp-1216972 [hull=0.000, PRIMARY]
- papers: https://doi.org/10.1016/j.jallcom.2014.01.222 (Thermodynamic and electrical properties of) | https://doi.org/10.1080/14686996.2021.1951593 (Thermoelectric materials taking advantage of spin entropy: lessons fro...)

## Cr-Fe-O-Zr
- rank 2138 | 2 samples | 1 papers | 2 compositions
- compositions: (Y0.06Zr0.97O2.03)37.8(Ni0.08Cr0.18Fe0.76)56.7 (1); (Y0.06Zr0.97O2.03)19.7(Ni0.08Cr0.18Fe0.76)78.6 (1)
- dopant candidates (<5% at.): Ni (2), Y (2)
- measured range: 64-1368 K (5th-95th pct of 4 curves)
- papers: https://doi.org/10.2355/tetsutohagane1955.82.9_789 (Thermal Conductivities of SUS304/PSZ Composite Materials)

## Cr-Fe-Sb
- rank 2139 | 2 samples | 1 papers | 2 compositions
- compositions: (Fe0.8Cr0.2)Sb2 (1); (Fe0.5Cr0.5)Sb2 (1)
- measured range: 11-303 K (5th-95th pct of 6 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): CrFe2Sb Fm-3m (225) mp-1008225 [hull=0.207, icsd=1, PRIMARY]; Cr(Fe2Sb5)2 P2/m (10) mp-1226377 [hull=0.024, PRIMARY]; CrFe3Sb4 P-3m1 (164) mp-1226271 [hull=0.070, PRIMARY]; CrFeSb4 P2/m (10) mp-1226216 [hull=0.055, PRIMARY]
- papers: https://doi.org/10.1063/1.4731251 (Enhancement of the thermoelectric properties in doped FeSb2 bulk crystals)

## Cr-Ga-Mn-N
- rank 2140 | 2 samples | 1 papers | 2 compositions
- compositions: GaNCr2Mn (1); GaNCr1.5Mn1.5 (1)
- sample form: Polycrystal (2)
- measured range: 10-325 K (5th-95th pct of 2 curves)
- papers: https://doi.org/10.1016/j.jssc.2013.10.034 (Synthesis and characterization of antiperovskite nitrides GaNCr3−xMnx)

## Cr-H-Ni
- rank 2141 | 2 samples | 1 papers | 2 compositions
- compositions: Ni0.90Cr0.10H0.5 (1); Ni0.90Cr0.10H0.7 (1)
- measured range: 91-227 K (5th-95th pct of 2 curves)
- papers: https://doi.org/10.1016/j.jallcom.2004.11.126 (Transport properties of some hydrogenated nickel-based alloys)

## Cr-La-O-Sr
- rank 2142 | 2 samples | 2 papers | 2 compositions
- compositions: La0.75Sr0.25CrO3 (1); La0.6Sr0.4CrO3 (1)
- curator composition details (from the paper): The logarithmic values in Fig 5a were converted by making them exponents of e
original va... (1)
- measured range: 151-348 K (5th-95th pct of 2 curves; full span incl. outliers 151-1123 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Sr2LaCrO6 Fm-3m (225) mp-1079391 [hull=0.234, icsd=1, PRIMARY]; SrLa3Cr4O12 P2 (3) mp-1218265 [hull=0.027, PRIMARY]; SrLa4Cr5O15 C2/m (12) mp-1218283 [hull=0.070, PRIMARY]; SrLaCrO4 I4mm (107) mp-1218189 [hull=0.000, PRIMARY]
- papers: https://doi.org/10.1021/acs.chemmater.2c03831 (Chemical Synthesis of La<sub>0.75</sub>Sr<sub>0.25</sub>CrO<sub>3</sub...) | https://doi.org/10.1039/d2nj04357b (Enhanced CO<sub>2</sub> electrolysis through modulation of oxygen vaca...)

## Cr-Mg
- rank 2143 | 2 samples | 1 papers | 2 compositions
- compositions: Mg2.46Cr0.22Cu0.1Ga0.1Fe0.1Mn0.1Si0.1Zn0.1Ti0.01V0.01Ca0.01Zr0.001 (1); Mg3.32Cr0.21Cu0.1Fe0.1Mn0.1Si0.1Ti0.01V0.01Zn0.01Zr0.01Ca0.001Pb0.001 (1)
- dopant candidates (<5% at.): Cu (2), Fe (2), Mn (2), Si (2), Zn (2), Ti (2), V (2), Ca (2), Zr (2), Ga (1), Pb (1)
- measured range: 10-278 K (5th-95th pct of 6 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Mg3Cr Pnma (62) mp-1180365 [hull=0.340, icsd=1, PRIMARY]; Mg149Cr P-6m2 (187) mp-1185585 [hull=0.000, PRIMARY]; Mg15Cr P-6m2 (187) mp-1023490 [hull=0.075, PRIMARY]; Mg7Cr P-6m2 (187) mp-1016326 [hull=0.140, PRIMARY]; MgCr Pm-3m (221) mp-973060 [hull=0.572, PRIMARY]
- papers: https://doi.org/10.1063/1.1735617 (Low‐Temperature Transport Properties of Commercial Metals and Alloys. ...)

## Cr-N-V
- rank 2144 | 2 samples | 1 papers | 2 compositions
- compositions: Cr0.90V0.10N (1); Cr0.9V0.1N (1)
- curator composition details (from the paper): ammonolysis and sintering (1)
- sample form: Bulk (1)
- measured range: 19-408 K (5th-95th pct of 4 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): VCrN2 R-3m (166) mp-1216389 [hull=0.153, PRIMARY]
- papers: https://doi.org/10.1063/1.3120280 (Thermoelectric properties of stoichiometric and hole-doped CrN)

## Cr-Na-O
- rank 2145 | 2 samples | 1 papers | 2 compositions
- compositions: NaCr2O4 (1); Na0.75Ca0.25Cr2O4 (1)
- dopant candidates (<5% at.): Ca (1)
- sample form: Bulk (2)
- measured range: 11-371 K (5th-95th pct of 4 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Na2CrO4 Cmcm (63) mp-18779 [hull=0.000, icsd=3, PRIMARY]; NaCr3O8 C2/m (12) mp-19280 [hull=0.000, icsd=2, PRIMARY]; Na2Cr2O7 P-1 (2) mp-704459 [hull=0.000, icsd=1, PRIMARY]; Na2Cr3O9 P2_1/m (11) mp-1194274 [hull=0.043, icsd=1, PRIMARY]; Na4UCr3O14 P-1 (2) mp-697861 [hull=0.000, icsd=1, PRIMARY]
- papers: https://doi.org/10.1063/1.4810855 (Electronic, thermoelectric, and magneto-dielectric properties of Ca1−x...)

## Cr-Si-Te
- rank 2146 | 2 samples | 1 papers | 1 compositions
- compositions: Cr2Si2Te6 (2)
- measured range: 10-139 K (5th-95th pct of 2 curves)
- [ref 1] TEDesignLab / ICSD: CrSiTe3 R-3 (148) mp-3779 [hull=0.000, icsd=4, PRIMARY]; CrSiTe3 (146)
- papers: https://doi.org/10.48550/ARXIV.2305.13268 (Spin-phonon scattering-induced low thermal conductivity in a van der W...)

## Cs-Hf-I
- rank 2147 | 2 samples | 1 papers | 1 compositions
- compositions: Cs2HfI6 (2)
- measured range: 200-800 K (5th-95th pct of 6 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Cs2HfI6 Fm-3m (225) mp-29398 [hull=0.000, icsd=1, PRIMARY]
- papers: https://doi.org/10.1016/j.materresbull.2020.111112 (Influence of the spin-orbit coupling effect on the electronic and ther...)

## Cs-I-Zr
- rank 2148 | 2 samples | 1 papers | 1 compositions
- compositions: Cs2ZrI6 (2)
- measured range: 200-800 K (5th-95th pct of 6 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Cs2ZrI6 Fm-3m (225) mp-1206511 [hull=0.000, PRIMARY]
- papers: https://doi.org/10.1016/j.materresbull.2020.111112 (Influence of the spin-orbit coupling effect on the electronic and ther...)

## Cs-K-O-V
- rank 2149 | 2 samples | 1 papers | 2 compositions
- compositions: (K0.40Cs0.60)VO3 (1); (K0.60Cs0.40)VO3 (1)
- measured range: 611-691 K (5th-95th pct of 2 curves)
- papers: https://doi.org/10.1007/bf02746039 (Thermoelectric power of ferroelectric potassium vanadate, cesium vanad...)

## Cs-N-Pb-Te
- rank 2150 | 2 samples | 1 papers | 1 compositions
- compositions: PbTe NCs (2)
- measured range: 299-476 K (5th-95th pct of 8 curves)
- papers: https://doi.org/10.1039/c5nj02113h (Low temperature formation of rectangular PbTe nanocrystals and their t...)
