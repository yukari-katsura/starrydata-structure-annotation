# Host systems -- chunk 009 of 73

Ranks 401-450 by sample count. These 50 host systems cover 821 samples (1.58% of the TE set); cumulative through this chunk: 79.09%.

Assign each host system a structural prototype from `data/annotated/taxonomy/prototypes_seed_v3.json`, or propose a new one in `taxonomy/prototypes_proposed.jsonl` first. Append results to `data/annotated/annotations/family_assignments.jsonl`.

The hand-entered MaterialFamily labels are deliberately NOT shown here -- they are held out in `df_host_systems.parquet` to validate this classification later. Decide from the compositions.

A "seed hypothesis" line means the taxonomy already names this host under that prototype. Confirm it against the compositions rather than accepting it; two or more listed means the host is mixed and needs splitting per composition.

Evidence follows the project precedence. Your judgement about the thermoelectric chemistry decides the prototype. [ref 1] is TEDesignLab, ICSD-backed and thermoelectric-specific -- prefer it. [ref 2] is Materials Project. Within a formula, polymorphs are ranked by ICSD reference count and the top one is marked PRIMARY -- not by e_above_hull, which is unusable for layered chalcogenides in the 2019 dump (Sb2Te3 R-3m carries 26 ICSD refs at hull 1.02). A primary resting on fewer than 5 ICSD references is flagged weak; the ambient phase may simply be absent from the snapshot, as it is for Bi2Se3.

While you have the host in view, also record what each minor element DOES, in `dopant_roles` -- the role follows from the prototype and cannot be judged without it. A median host has 2 such elements. Not everything listed is a dopant: O, C, N and H are usually milling or pressing residue, and an element just under 5 at.% may be an alloying end member rather than dilute doping. The doping LEVEL is computed later from the parsed fractions -- do not work it out by hand here.

A polymorph list is NOT a thermal sequence. SnSe has three known structures but only Pnma -> Cmcm happens on heating; rocksalt SnSe is metastable (2 icsd refs against 32). Put thermally reached phases in `phases` with their transition temperatures, and everything else in `other_polymorphs` with an occurrence reason. hull and icsd counts are shown to help you tell them apart.

A host may need MORE THAN ONE prototype. Transport is measured across a wide window and many thermoelectrics transform inside it, so where a "MEASUREMENT CROSSES A TRANSITION" line appears, record each phase with its own temperature range in the `phases` field. Transition temperatures shown are approximate and composition-dependent.

Both references describe which phases EXIST in a chemistry, not which phase this paper made. Al-O-Zn is best attested as ZnAl2O4 spinel (227) while almost every sample in it is Al-doped wurtzite ZnO (186). Weigh them against the compositions; do not follow them blindly.

## Al-Ca-O
- rank 401 | 17 samples | 3 papers | 5 compositions
- compositions: Ca12Al14O33 (10); (CaO)12(Al2O3)7 (4); (Ca12Al14O33)34.73(CB)65.27 (1); (Ca12Al14O33)23.82(CB)76.18 (1); (Ca12Al14O33)61.97(CB)38.03 (1)
- dopant candidates (<5% at.): C (3), B (3)
- seed hypothesis (confirm): mayenite
- measured range: 11-1073 K (5th-95th pct of 23 curves)
- [ref 1] TEDesignLab / ICSD: CaAl4O7 C2/c (15) mp-4867 [hull=0.000, icsd=4, PRIMARY]; Ca4Al6O13 I-43m (217) mp-7531 [hull=0.013, icsd=1, PRIMARY]; CaAl2O4 Pnma (62) mp-12441 [hull=0.059, icsd=1]; CaAl2O4 (11)
- [ref 2] MP, ranked by ICSD evidence: Ca3Al2O12 Ia-3d (230) mp-1182533 [hull=0.407, icsd=10, PRIMARY]; CaAl2O4 P2_1/c (14) mp-2963 [hull=0.001, icsd=4, PRIMARY]; Ca6Al7O16 I-43d (220) mp-721592 [hull=0.000, icsd=3, PRIMARY]; Ca4Al6SO16 Pcc2 (27) mp-1019575 [hull=0.000, icsd=1, PRIMARY]; Ca3Al2O12 I-43d (220) mp-1200701 [hull=0.409, icsd=3]
- papers: https://doi.org/10.1103/physrevb.80.075201 (Thermal conductivity and Seebeck coefficient of12CaO⋅7Al2O3electride w...) | https://doi.org/10.1016/j.mtcomm.2019.100820 (Positive ionic conduction of mayenite cement Ca12Al14O33/nano-carbon b...) | https://doi.org/10.2320/matertrans.mbw200717 (Superconducting Transition in Electron-Doped 12CaO&amp;middot;7Al&lt;S...)

## Al-Ce
- rank 402 | 17 samples | 11 papers | 5 compositions
- compositions: CeAl3 (9); CeAl2 (5); Ce3Al (1); Ce0.9La0.1Al3 (1); Ce0.99La0.01Al3 (1)
- dopant candidates (<5% at.): La (2)
- measured range: 10-336 K (5th-95th pct of 38 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): CeAl2 Fd-3m (227) mp-2088 [hull=0.000, icsd=23, PRIMARY]; Ce3Al Pm-3m (221) mp-2413 [hull=0.018, icsd=4, PRIMARY]; CeAl4 I4/mmm (139) mp-2289 [hull=0.040, icsd=3, PRIMARY]; CeAl Cmcm (63) mp-20439 [hull=0.015, icsd=2, PRIMARY]; Ce3Al11 Immm (71) mp-1213865 [hull=0.003, PRIMARY]
- papers: https://doi.org/10.1016/j.enconman.2014.07.050 (Thermoelectric properties of CeAl3 prepared by hot-press method) | https://doi.org/10.1016/0304-8853(83)90564-4 (Thermoelectric power of RAl2) | https://doi.org/10.1134/s1063776107070138 (Anomalous thermopower in heavy-fermion compounds CeB6, CeAl3, and CeCu...)

## As-Ce-Fe-O
- rank 403 | 17 samples | 3 papers | 10 compositions
- compositions: CeO0.9F0.1Fe0.95Co0.05As (3); CeO0.9F0.1FeAs (3); CeO0.9F0.1Fe0.9Co0.1As (2); CeFeAsO (2); CeO0.9F0.1Fe0.85Co0.15As (2); CeFe0.95Co0.05AsO (1)
- dopant candidates (<5% at.): Co (11), F (10)
- seed hypothesis (confirm): zrcusias_1111
- measured range: 10-298 K (5th-95th pct of 17 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): CeFeAsO P4/nmm (129) mp-1079570 [hull=0.097, icsd=5, PRIMARY]; Ce2FeAs2O P4/mmm (123) mp-1213887 [hull=1.398, PRIMARY]; Ce8Fe8As8O7F I-4m2 (119) mp-705511 [hull=0.113, PRIMARY]; CeFeAsO P4mm (99) mp-605060 [hull=0.115]
- papers: https://doi.org/10.1016/j.physc.2009.04.013 (Thermoelectric power of RFeAsO (R=Ce, Pr, Nd, Sm and Gd)) | https://doi.org/10.1088/0953-8984/22/11/115701 (Effects of Co doping on the transport properties and superconductivity...) | https://doi.org/10.1016/j.physc.2010.07.008 (Effects of simultaneous carrier doping in the charge reservoir and con...)

## As-Eu-Fe
- rank 404 | 17 samples | 2 papers | 2 compositions
- compositions: Eu(Fe0.925Co0.075)2As2 (16); EuFe4As12 (1)
- dopant candidates (<5% at.): Co (16)
- measured range: 10-298 K (5th-95th pct of 19 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Eu(FeAs)2 I4/mmm (139) mp-20890 [hull=0.000, icsd=10, PRIMARY]
- papers: https://doi.org/10.1088/1742-6596/592/1/012032 (Investigation of ferromagnetic filled skutterudite compound EuFe4As12) | https://doi.org/10.1038/s41598-017-03762-1 (Hydrostatic pressure effects on the static magnetism in Eu(Fe0.925Co0....)

## Ba-Mn-O-Pr
- rank 405 | 17 samples | 5 papers | 11 compositions
- compositions: Pr0.67Ba0.33MnO3 (3); Pr0.5Ba0.5MnO3 (3); (Pr0.67Ba0.33MnO3)0.9(PdO)0.1 (2); (Pr0.67Ba0.33MnO3)0.8(PdO)0.2 (2); Pr2(Ba0.9Cs0.1)Mn3O9 (1); Pr2BaMn3O9 (1)
- dopant candidates (<5% at.): Pd (4), Cs (3)
- measured range: 10-1074 K (5th-95th pct of 25 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): BaPrMn2O6 P4/mmm (123) mp-19274 [hull=0.021, icsd=2, PRIMARY]; Ba4PrMn3O12 R-3m (166) mp-689498 [hull=0.023, icsd=1, PRIMARY]; BaPr2Mn3O9 C2/m (12) mp-1227914 [hull=0.024, PRIMARY]
- papers: https://doi.org/10.1140/epjb/e2008-00331-6 (Electrical and thermal properties of Pr2/3(Ba1−xCsx)1/3MnO3 manganites) | https://doi.org/10.1088/0022-3727/40/23/046 (Magnetotransport, magnetization and thermoelectric power of Pr2/3Ba1/3...) | https://doi.org/10.1088/0022-3727/40/3/005 (Thermopower studies of Pr0.67D0.33MnO3manganite system)

## Bi-Mg
- rank 406 | 17 samples | 4 papers | 6 compositions
- compositions: Mg3Bi0.33 (6); Mg3.2Bi2 (4); Mg3.2Bi1.998Te0.002 (2); Mg3Bi2 (2); Mg3.2Bi1.996Te0.004 (2); Mg3.2Bi1.898Sb0.1Te0.002 (1)
- dopant candidates (<5% at.): Te (5), Sb (1)
- measured range: 10-805 K (5th-95th pct of 52 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Mg3Bi2 Ia-3 (206) mp-1196079 [hull=0.014, icsd=1, PRIMARY]; Mg149Bi P-6m2 (187) mp-1185557 [hull=0.000, PRIMARY]; Mg2Bi C2/m (12) mp-978260 [hull=0.095, PRIMARY]; Mg15Bi P-6m2 (187) mp-1023495 [hull=0.028, PRIMARY]; Mg2Bi3 P-3m1 (164) mp-1207227 [hull=0.097, PRIMARY]
- papers: https://doi.org/10.1007/s11664-012-2417-7 (On the Thermoelectric Properties of Zintl Compounds Mg3Bi2−x Pn x (Pn ...) | https://doi.org/10.1088/0022-3727/39/24/035 (Electrical and thermoelectric properties of nanocrystal substitutional...) | https://doi.org/10.1126/science.aax7792 (High thermoelectric cooling performance of n-type Mg3Bi2-based materials)

## Cd-Sb
- rank 407 | 17 samples | 3 papers | 14 compositions
- compositions: CdSb (2); Ag0.0001CdSbTe0.0001 (2); Cd12.7Sb10 (2); Cd0.99Ag0.01Sb (1); Cd0.997Ag0.003Sb (1); Cd0.999Ag0.001Sb (1)
- dopant candidates (<5% at.): Te (9), Ag (8), Cu (1), Au (1)
- seed hypothesis (confirm): znsb_cdsb
- measured range: 15-602 K (5th-95th pct of 37 curves)
- [ref 1] TEDesignLab / ICSD: CdSb Pbca (61) mp-1321 [hull=0.000, icsd=4, PRIMARY]
- [ref 2] MP, ranked by ICSD evidence: Cd6Sb5 R-3c (167) mp-669510 [hull=0.508, icsd=1, PRIMARY]; CdSb3 P6_3/mmc (194) mp-1183739 [hull=0.229, PRIMARY]; CdSb Pmmm (47) mp-1226724 [hull=0.154]
- papers: https://doi.org/10.1021/cm504398d (Anisotropic Multicenter Bonding and High Thermoelectric Performance in...) | https://doi.org/10.1007/bf00836697 (Combined effects of donor and acceptor impurities on the thermoelectri...) | https://doi.org/10.1021/cm0629659 (Structure of Cd12.7(1)Sb10)

## Ce-Pd-Si
- rank 408 | 17 samples | 8 papers | 7 compositions
- compositions: CePd2Si2 (7); Ce3Pd5Si (3); Ce(Ni0.1Pd0.9)2Si2 (2); Ce2PdSi3 (2); Ce(Pd0.95Cu0.05)2Si2 (1); Ce0.8La0.2Pd2Si2 (1)
- dopant candidates (<5% at.): Ni (2), Cu (1), La (1)
- measured range: 10-298 K (5th-95th pct of 24 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ce(SiPd)2 I4/mmm (139) mp-3826 [hull=0.000, icsd=13, PRIMARY]; Ce3(Si3Pd10)2 Fm-3m (225) mp-1192814 [hull=0.000, icsd=1, PRIMARY]; Ce2(Si2Pd7)3 Fm-3m (225) mp-1193751 [hull=0.000, icsd=1, PRIMARY]; CeSiPd2 Pnma (62) mp-1181683 [hull=0.023, icsd=1, PRIMARY]; Ce2SiPd14 P4/nmm (129) mp-1203477 [hull=0.000, icsd=1, PRIMARY]
- papers: https://doi.org/10.1016/s0925-8388(02)01069-1 (Electronic and magnetic properties of Ce3Pd5Si) | https://doi.org/10.1063/1.1356049 (Heavy fermion behavior in Ce(NixPd1−x)2Si2) | https://doi.org/10.1007/s10909-014-1262-x (Low Temperature Thermoelectric Power of Ce(Pd $$_{1-x}$$ 1 - x Cu $$_x...)

## Ce-Rh-Si
- rank 409 | 17 samples | 4 papers | 6 compositions
- compositions: CeRhSi3 (8); Ce3RhSi3 (5); CeRh1.9Ni0.1Si2 (1); CeRh1.8Ni0.2Si2 (1); CeRh2Si2 (1); Ce(Rh0.90Ru0.10)2Si2 (1)
- dopant candidates (<5% at.): Ni (2), Ru (1)
- measured range: 10-298 K (5th-95th pct of 25 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ce(SiRh)2 I4/mmm (139) mp-4090 [hull=0.000, icsd=10, PRIMARY]; Ce2Si5Rh3 Ibam (72) mp-1188214 [hull=0.000, icsd=3, PRIMARY]; CeSi2Rh Cmcm (63) mp-1025411 [hull=0.000, icsd=2, PRIMARY]; Ce2Si3Rh P6/mmm (191) mp-31163 [hull=0.000, icsd=1, PRIMARY, AMBIGUOUS]; Ce3(SiRh)2 Pbcm (57) mp-978253 [hull=0.000, icsd=1, PRIMARY]
- papers: https://doi.org/10.1088/0953-8984/25/26/265601 (Anomalous Nernst effect in the ferromagnetic Kondo lattice Ce3RhSi3) | https://doi.org/10.3938/jkps.62.2016 (Thermoelectric power in single-crystalline CeRhSi3) | https://doi.org/10.1016/0038-1098(89)90175-0 (Thermoelectric power behaviour of CeRh2−xNixSi2 alloys)

## Co-Ni-Sb-Sn-Ti
- rank 410 | 17 samples | 6 papers | 15 compositions
- compositions: Ti2NiCoSnSb (3); TiCo0.8Ni0.2Sn0.2Sb0.8 (1); TiCo0.2Ni0.8Sn0.8Sb0.2 (1); TiCo0.5Ni0.5Sn0.5Sb0.5 (1); (TiCoSb)0.8(TiNi2Sn)0.2 (1); Ti2NiCoSn0.5Sb1.5 (1)
- dopant candidates (<5% at.): Al (5), Ta (5), Zr (1)
- measured range: 13-976 K (5th-95th pct of 84 curves)
- papers: https://doi.org/10.1002/zaac.200900349 (Investigation of the Thermoelectric Properties of the Series TiCo1-xNi...) | https://doi.org/10.1038/s41598-019-41818-6 (Ti2NiCoSnSb - a new half-Heusler type high-entropy alloy showing simul...) | https://doi.org/10.1016/j.jssc.2019.04.041 (Phase stability and thermoelectric properties of TiCoSb-TiM2Sn (M = Ni...)

## Co-O-Sr-Y
- rank 411 | 17 samples | 4 papers | 10 compositions
- compositions: Sr0.7Y0.3CoO3 (5); Sr3.0YCo4O10.5 (2); Sr2.2Ca0.8YCo4O10.5 (2); Sr2.6Ca0.4YCo4O10.5 (2); Sr3YCo3.8Ga0.2O10.5 (1); Sr3YCo3.7Ga0.3O10.5 (1)
- dopant candidates (<5% at.): Ca (4), Ga (3)
- measured range: 11-1203 K (5th-95th pct of 33 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Sr2YCoO6 Fm-3m (225) mp-1080434 [hull=0.068, icsd=1, PRIMARY]; Sr3Y(CoO4)2 Amm2 (38) mp-1218489 [hull=0.036, PRIMARY]; SrYCoO4 I4mm (107) mp-1217766 [hull=0.092, PRIMARY]
- papers: https://doi.org/10.1143/jjap.50.013002 (Effects of Structural Disorder and Charge Carriers on the Magnetic and...) | https://doi.org/10.1007/s11664-011-1524-1 (High-Temperature Thermoelectric and Microstructural Characteristics of...) | https://doi.org/10.1143/jpsj.78.094711 (Chemical and Physical Pressure Effects on the Magnetic and Transport P...)

## Cu-Fe-S-Sn
- rank 412 | 17 samples | 4 papers | 15 compositions
- compositions: Cu2FeSnS4 (2); Cu6Fe4Sn12S32 (2); Cu7.5Fe4Sn12S32 (1); Cu7Fe4Sn12S32 (1); Cu5Fe4Sn12S32 (1); Cu4Fe4Sn12S32 (1)
- measured range: 11-647 K (5th-95th pct of 69 curves; full span incl. outliers 10-702 K)
- [ref 1] TEDesignLab / ICSD: FeCu2SnS4 I-42m (121) mp-22648 [hull=0.043, icsd=3, PRIMARY]; FeCu2SnS4 (81)
- [ref 2] MP, ranked by ICSD evidence: FeCu6(SnS4)2 P-4m2 (115) mp-1105236 [hull=0.114, icsd=1, PRIMARY]; Fe2Cu6SnS8 P-4m2 (115) mp-651268 [hull=0.009, icsd=1, PRIMARY]; FeCu2Sn3S8 R-3m (166) mp-1225180 [hull=0.015, PRIMARY]; Fe3Cu(SnS4)2 Imm2 (44) mp-1225264 [hull=0.123, PRIMARY]; ZnFe2Cu6(SnS4)3 I-4 (82) mp-1216035 [hull=0.032, PRIMARY]
- papers: https://doi.org/10.1021/ic401310c (Enhanced Thermoelectric Figure of Merit in Stannite–Kuramite Solid Sol...) | https://doi.org/10.1039/c3mh00091e (Magnetic ions in wide band gap semiconductor nanocrystals for optimize...) | https://doi.org/10.1063/1.3569624 (Variable-range-hopping conduction and low thermal conductivity in chal...)

## Cu-Ge-S
- rank 413 | 17 samples | 6 papers | 15 compositions
- compositions: Cu26V2Ge6S32 (3); Cu24Zn2V2Ge6S32 (1); Cu7.36GeS6 (1); Cu7.76GeS6 (1); Cu7.6GeS6 (1); Cu7.2GeS6 (1)
- dopant candidates (<5% at.): V (4), Zn (4), Cr (4), Ta (2), Nb (2)
- seed hypothesis (confirm): cu2gese3, colusite  <-- MIXED, split per composition
- measured range: 10-819 K (5th-95th pct of 72 curves)
- [ref 1] TEDesignLab / ICSD: Cu8GeS6 Pmn2_1 (31) mp-5546 [hull=0.045, icsd=2, PRIMARY]; Cu2GeS3 Cc (9) mp-15252 [hull=0.000, icsd=1, PRIMARY]
- [ref 2] MP, ranked by ICSD evidence: Cu2GeS4 I-42m (121) mp-1147769 [hull=0.064, PRIMARY]; Cu2GeS3 Imm2 (44) mp-1072589 [hull=0.019, icsd=1]; Cu2GeS3 Fdd2 (43) mp-1225871 [hull=0.003]
- papers: https://doi.org/10.1063/1.4896998 (High-performance thermoelectric minerals: Colusites Cu26V2M6S32 (M = G...) | https://doi.org/10.1063/1.4955398 (Research Update: Cu–S based synthetic minerals as efficient thermoelec...) | https://doi.org/10.1063/1.4892593 (Tunable electronic properties and low thermal conductivity in syntheti...)

## Cu-Ge-Se-Zn
- rank 414 | 17 samples | 6 papers | 12 compositions
- compositions: Cu2ZnGeSe4 (6); Cu2.15Zn0.85GeSe3.9 (1); Cu2.05Zn0.95GeSe4 (1); Cu2.075Zn0.925GeSe4 (1); Cu2.1Zn0.9GeSe4 (1); Cu2.025Zn0.975GeSe4 (1)
- dopant candidates (<5% at.): In (4), Fe (2)
- measured range: 260-729 K (5th-95th pct of 69 curves)
- [ref 1] TEDesignLab / ICSD: ZnCu2GeSe4 I-42m (121) mp-10824 [hull=0.002, icsd=5, PRIMARY]
- papers: https://doi.org/10.1002/asia.201300425 (Synthesis of Wurtzite Cu2ZnGeSe4Nanocrystals and their Thermoelectric ...) | https://doi.org/10.1021/ja211952z (Cu2ZnGeSe4Nanocrystals: Synthesis and Thermoelectric Properties) | https://doi.org/10.1021/ja301452j (Influence of a Nano Phase Segregation on the Thermoelectric Properties...)

## Fe-Ga-V
- rank 415 | 17 samples | 4 papers | 14 compositions
- compositions: Fe2VGa (4); Fe2V0.9Ti0.1Ga (1); Fe2V0.85Ti0.15Ga (1); Fe2V0.95Ti0.05Ga (1); Fe2VGa0.9Ge0.1 (1); Fe2VGa0.98Ge0.02 (1)
- dopant candidates (<5% at.): Ti (3), Ge (3)
- seed hypothesis (confirm): full_heusler
- measured range: 10-701 K (5th-95th pct of 63 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): VGaFe2 Fm-3m (225) mp-21883 [hull=0.000, icsd=3, PRIMARY]; V2GaFe Cmm2 (35) mp-1216782 [hull=0.154, PRIMARY]; V9Ga4Fe3 Pm (6) mp-1216513 [hull=0.000, PRIMARY]
- papers: https://doi.org/10.1063/1.4934734 (Thermoelectric properties optimization of Fe2VGa by tuning electronic ...) | https://doi.org/10.1088/0953-8984/20/25/255233 (Effects of Ge substitution on the thermoelectric properties and pseudo...) | https://doi.org/10.1088/0953-8984/16/24/010 (Off-stoichiometric effect on the transport and pseudogap characteristi...)

## Fe-Nd-O-Sr
- rank 416 | 17 samples | 7 papers | 16 compositions
- compositions: Nd0.5Sr0.5Fe0.8Cu0.2O3 (2); Nd0.3Sr0.7Fe0.8Cu0.2O3 (1); Nd0.7Sr0.3Fe0.8Cu0.2O3 (1); Nd0.4Sr0.6Fe0.8Cu0.2O3 (1); Nd0.6Sr0.4Fe0.8Cu0.2O3 (1); La0.2Nd0.3Sr0.26Ca0.24FeO3 (1)
- dopant candidates (<5% at.): Cu (6), Zn (5), Co (2), Ca (1), La (1), Mo (1)
- measured range: 297-1173 K (5th-95th pct of 17 curves; full span incl. outliers 297-1221 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Sr2Nd(FeO3)3 C2/c (15) mp-1218798 [hull=0.000, PRIMARY]; Sr3Nd(FeO4)2 Amm2 (38) mp-1218438 [hull=0.006, PRIMARY]; SrNd2Fe2O7 I4mm (107) mp-1218180 [hull=0.076, PRIMARY]; SrNdFeO4 I4mm (107) mp-1218098 [hull=0.027, PRIMARY]
- papers: https://doi.org/10.1021/jp500371w (Structure and Properties of Novel Cobalt-Free Oxides Nd<sub><i>x</i></...) | https://doi.org/10.1149/1.3205797 (Performance of (Ln<sub>0.5</sub>M<sub>0.5</sub>)FeO<sub>3-δ</sub> Pero...) | https://doi.org/10.1016/j.jallcom.2006.04.005 (Structure, electrical conducting and thermal expansion properties of L...)

## Fe-O-Pr
- rank 417 | 17 samples | 5 papers | 10 compositions
- compositions: Pr0.9Sr0.1FeO3 (5); Pr0.8Sr0.2FeO3 (4); Pr0.9Ca0.1Fe0.8Ni0.2O3 (1); PrFe0.8Ni0.2O3 (1); Pr0.8Ca0.2Fe0.8Ni0.2O3 (1); Sr0.1Ba0.1Pr0.8Cu0.1Ti0.1Fe0.8O3 (1)
- dopant candidates (<5% at.): Sr (13), Ni (3), Ca (3), Ba (2), Cu (2), Ti (2), Mn (2), Co (1)
- measured range: 180-1122 K (5th-95th pct of 17 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): PrFeO3 Pnma (62) mp-24995 [hull=0.000, icsd=6, PRIMARY]; Pr3Fe5O12 Ia-3d (230) mp-1197438 [hull=0.008, icsd=2, PRIMARY]
- papers: https://doi.org/10.2320/matertrans.e-m2019812 (High-Temperature Thermoelectric Properties of Pr<sub>1−</sub><i><sub>x...) | https://doi.org/10.1039/c1jm10911a (A novel one step synthesized Co-free perovskite/brownmillerite nanocom...) | https://doi.org/10.1016/j.ssi.2020.115279 (Physical properties of (SrBa)1-xPrx(CuTi)0.2Fe0.8O3-δ (x = 0–1.0) and ...)

## Fe-S
- rank 418 | 17 samples | 4 papers | 11 compositions
- compositions: FeS2 (7); Fe0.98Co0.02S2 (1); Fe0.99Co0.01S2 (1); Fe0.97Co0.03S2 (1); Fe0.96Co0.04S2 (1); FeS1.99Se0.01 (1)
- dopant candidates (<5% at.): Co (5), Se (4)
- measured range: 54-604 K (5th-95th pct of 69 curves)
- [ref 1] TEDesignLab / ICSD: FeS P-62c (190) mp-2779 [hull=0.179, icsd=22, PRIMARY]; FeS2 Pa-3 (205) mp-226 [hull=0.007, icsd=18, PRIMARY]; FeS Pnma (62) mp-21410 [hull=0.235, icsd=9]; FeS P6_3/mmc (194) mp-2099 [hull=0.260, icsd=6]; FeS P6_3mc (186) mp-850122 [hull=0.202, icsd=3]
- [ref 2] MP, ranked by ICSD evidence: Fe3S4 Fd-3m (227) mp-21515 [hull=0.135, icsd=4, PRIMARY, AMBIGUOUS]; Fe7S8 C2/c (15) mp-850128 [hull=0.134, icsd=3, PRIMARY]; Fe3S Pnma (62) mp-1189032 [hull=0.161, icsd=1, PRIMARY]; Fe4S5 P2 (3) mp-850249 [hull=0.060, icsd=1, PRIMARY]; FeS2 Pnnm (58) mp-1522 [hull=0.000, icsd=8]
- papers: https://doi.org/10.1007/s11664-014-3065-x (Nanoscale FeS2 (Pyrite) as a Sustainable Thermoelectric Material) | https://doi.org/10.1109/ict.2003.1287526 (Thermoelectric figure of merit of M-sulphides (M=Fe, Co, Ni, Pd) thin ...) | https://doi.org/10.1016/j.jallcom.2019.152999 (Exploring the thermoelectric behavior of spark plasma sintered Fe7-xCo...)

## Ga-N
- rank 419 | 17 samples | 7 papers | 1 compositions
- compositions: GaN (17)
- seed hypothesis (confirm): wurtzite
- measured range: 103-976 K (5th-95th pct of 23 curves)
- [ref 1] TEDesignLab / ICSD: GaN P6_3mc (186) mp-804 [hull=0.000, icsd=22, PRIMARY]; GaN F-43m (216) mp-830 [hull=0.005, icsd=10]; GaN Fm-3m (225) mp-2853 [hull=0.478, icsd=4]
- [ref 2] MP, ranked by ICSD evidence: GaN P6_3/mmc (194) mp-1007824 [hull=0.355, icsd=1]
- papers: https://doi.org/10.1063/1.1951048 (Thermoelectric properties of and devices based on free-standing GaN) | https://doi.org/10.1016/j.tsf.2006.07.145 (Thermoelectric properties and thermoelectric devices of free-standing ...) | https://doi.org/10.1103/physrevlett.109.095901 (Thermal Conductivity and Large Isotope Effect in GaN from First Princi...)

## Ge-Se
- rank 420 | 17 samples | 6 papers | 12 compositions
- compositions: GeSe (5); GeAg0.05Sb0.05Se1.1 (2); Ge0.99Ag0.01Se (1); Ge0.97Ag0.03Se (1); Ge0.995Ag0.005Se (1); Ge0.998Ag0.002Se (1)
- dopant candidates (<5% at.): Ag (12), Sb (8), Te (1)
- measured range: 295-755 K (5th-95th pct of 72 curves; full span incl. outliers 293-997 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): GeSe Pnma (62) mp-700 [hull=0.000, icsd=9, PRIMARY]; GeSe2 I-42d (122) mp-10074 [hull=0.015, icsd=4, PRIMARY]; Ge4Se9 Pca2_1 (29) mp-680333 [hull=0.006, icsd=2, PRIMARY]; GeSe Fm-3m (225) mp-10759 [hull=0.010, icsd=1]; GeSe2 Fdd2 (43) mp-1190257 [hull=0.010, icsd=1]
- papers: https://doi.org/10.1038/srep09567 (High-efficient thermoelectric materials: The case of orthorhombic IV-V...) | https://doi.org/10.1016/j.jmat.2016.09.001 (Thermoelectric properties of GeSe) | https://doi.org/10.1016/j.jechem.2019.09.021 (Glass-like electronic and thermal transport in crystalline cubic germa...)

## Ir-Zn
- rank 421 | 17 samples | 5 papers | 14 compositions
- compositions: YbIr2Zn20 (4); PrIr2Zn20 (1); PrIr2Zn19.5Ga0.5 (1); PrIr2Zn19Ga (1); Yb0.6Ce0.4Ir2Zn20 (1); Yb0.87Ce0.08Sm0.05Ir2Zn20 (1)
- dopant candidates (<5% at.): Yb (10), Ce (8), Sm (7), Pr (3), Ga (2), Y (1)
- seed hypothesis (confirm): cecr2al20_cage
- measured range: 10-398 K (5th-95th pct of 63 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ce(Zn10Ir)2 Fd-3m (227) mp-1199912 [hull=0.000, icsd=1, PRIMARY]; U(Zn10Ir)2 Fd-3m (227) mp-1203280 [hull=0.000, icsd=1, PRIMARY]; Zn11Ir2 I-43m (217) mp-30747 [hull=0.000, icsd=1, PRIMARY]; Zn3Ir I4/mmm (139) mp-865362 [hull=0.000, PRIMARY]; ZnIr P-6m2 (187) mp-1206819 [hull=0.000, PRIMARY]
- papers: https://doi.org/10.1103/physrevb.86.115110 (Thermoelectric power of the YbT2Zn20(T=Fe, Ru, Os, Ir, Rh, and Co) hea...) | https://doi.org/10.1126/sciadv.aaw6183 (Enhanced thermoelectric performance of heavy-fermion compounds YbTM2Zn...) | https://doi.org/10.1088/1742-6596/683/1/012011 (Effect of Ga Substitution on the Γ3Doublet Ground State in PrIr2Zn20)

## Ag-In-Te
- rank 422 | 16 samples | 8 papers | 9 compositions
- compositions: AgInTe2 (6); Ag0.85InTe2 (2); AgIn5Te8 (2); Ag0.99InTe2 (1); Ag0.97InTe2 (1); Ag0.4Cd0.2In2.4Te4 (1)
- dopant candidates (<5% at.): Cd (1)
- measured range: 301-876 K (5th-95th pct of 48 curves)
- [ref 1] TEDesignLab / ICSD: InAgTe2 I-42d (122) mp-22386 [hull=0.000, icsd=9, PRIMARY]; In5AgTe8 (111)
- [ref 2] MP, ranked by ICSD evidence: In5AgTe8 C2 (5) mp-1224268 [hull=0.015, PRIMARY]; InAgTe2 P-4m2 (115) mp-1223798 [hull=0.013]; InAgTe2 R-3m (166) mp-1223792 [hull=0.121]; InAgTe2 P4/mmm (123) mp-1223782 [hull=0.127]; InAgTe2 P3m1 (156) mp-675371 [hull=0.269]
- papers: https://doi.org/10.1002/adma.201400058 (High-Performance Pseudocubic Thermoelectric Materials from Non-cubic C...) | https://doi.org/10.1016/j.mseb.2012.04.025 (High-temperature thermoelectric properties of non-stoichiometric Ag1−x...) | https://doi.org/10.1021/acs.inorgchem.5b00433 (Silver Indium Telluride Semiconductors and Their Solid Solutions with ...)

## Ag-Pd
- rank 423 | 16 samples | 1 papers | 3 compositions
- compositions: Pd0.86Ag0.14 (6); Pd0.77Ag0.23 (6); Pd0.61Ag0.39 (4)
- seed hypothesis (confirm): solid_solution_alloy
- measured range: 81-299 K (5th-95th pct of 16 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ag3Pd I4/mmm (139) mp-985296 [hull=0.000, PRIMARY, AMBIGUOUS]; AgPd R-3m (166) mp-1229012 [hull=0.000, PRIMARY, AMBIGUOUS]; Ag3Pd P6_3/mmc (194) mp-1183206 [hull=0.000]; AgPd P-6m2 (187) mp-1183222 [hull=0.008]
- papers: https://doi.org/10.1016/j.jallcom.2004.11.060 (Influence of hydrogen on electron transport of palladium alloyed with ...)

## Ag-Se-Te
- rank 424 | 16 samples | 2 papers | 4 compositions
- compositions: Ag2Se0.5Te0.5 (13); Ag2Se0.7Te0.3 (1); Ag2Se0.8Te0.2 (1); Ag2Se0.6Te0.4 (1)
- solid-solution axis: Se/(Se+Te) spans 0.50-0.80 (median 0.70) over 4 compositions
     ISOELECTRONIC SERIES: the parent compound depends on the composition, not on this host. Near either end the minor element is a dilute substituent; in the middle it is a genuine alloy. Record the axis, not one parent -- and note the 5% split used the whole formula, not the sublattice, so its cut lands at a different level on each site.
- measured range: 296-622 K (5th-95th pct of 44 curves)
- papers: https://doi.org/10.1063/1.4824353 (Enhanced thermoelectric performance in the very low thermal conductivi...) | https://doi.org/10.1021/acs.inorgchem.1c01563 (Ternary Ag2Se1–xTex: A Near-Room-Temperature Thermoelectric Material w...)

## Al-Co-Cr-Fe-Ni
- rank 425 | 16 samples | 2 papers | 15 compositions
- compositions: Al2CrCoFeNi (2); Al0.5CoCrFeNi (1); Al0.25CoCrFeNi (1); Al1.25CoCrFeNi (1); Al1.5CoCrFeNi (1); Al1.75CoCrFeNi (1)
- dopant candidates (<5% at.): Sc (2)
- seed hypothesis (confirm): high_entropy_alloy
- measured range: 343-1167 K (5th-95th pct of 63 curves; full span incl. outliers 320-1261 K)
- papers: https://doi.org/10.1063/1.4935489 (High-entropy alloys as high-temperature thermoelectric materials) | https://doi.org/10.3390/e20070488 (The Effect of Scandium Ternary Intergrain Precipitates in Al-Containin...)

## Al-Mn-V
- rank 426 | 16 samples | 2 papers | 4 compositions
- compositions: Mn2VAl (13); Mn2V(Al0.98Si0.02) (1); Mn2V(Al0.94Si0.06) (1); Mn2V(Al0.96Si0.04) (1)
- dopant candidates (<5% at.): Si (3)
- measured range: 301-1021 K (5th-95th pct of 58 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Mn2AlV Fm-3m (225) mp-10895 [hull=0.000, icsd=2, PRIMARY]; Mn11Al4V R-3m (166) mp-1222031 [hull=0.058, PRIMARY]; Mn3Al2V3 R3m (160) mp-1221807 [hull=0.056, PRIMARY]; Mn5Al2V R-3m (166) mp-1221708 [hull=0.038, PRIMARY]; Mn7Al4V5 R3m (160) mp-1221730 [hull=0.034, PRIMARY]
- papers: https://doi.org/10.1088/2053-1591/ab875b (Distinct impact of order degree on thermoelectric power factor of p-ty...) | https://doi.org/10.1016/j.jmat.2023.11.013 (Enhancement of the thermoelectric performance of half-metallic full-He...)

## Al-O-Zn
- rank 427 | 16 samples | 7 papers | 7 compositions
- compositions: Zn(Al)O (5); Al0.1Zn0.9O (5); ZnAlO (2); Al0.12Zn0.88O (1); (Zn0.876Al0.124)O (1); (Zn9Al1)O10 (1)
- seed hypothesis (confirm): wurtzite
- measured range: 25-746 K (5th-95th pct of 26 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Al2ZnO4 Fd-3m (227) mp-2908 [hull=0.000, icsd=44, PRIMARY]; Al10ZnO16 R3m (160) mp-760795 [hull=0.021, PRIMARY]; Al8Zn3CoO16 P-4m2 (115) mp-1228970 [hull=0.000, PRIMARY]; Al2ZnO4 Imma (74) mp-34210 [hull=0.127]
- papers: https://doi.org/10.1063/1.4790644 (Crystal orientation dependent thermoelectric properties of highly orie...) | https://doi.org/10.1016/j.elspec.2009.03.001 (X-ray photoelectron spectroscopy study and thermoelectric properties o...) | https://doi.org/10.1016/j.ceramint.2020.03.031 (Improved thermoelectric performance of Al and Sn doped ZnO nano partic...)

## Ba-Fe-Sb
- rank 428 | 16 samples | 7 papers | 6 compositions
- compositions: BaFe4Sb12 (5); BaIn0.5Fe3.7Co0.3Sb12 (5); Ba0.87Fe4Sb12 (3); Ba0.99Fe4Sb12 (1); BaFe3.9Pt0.1Sb12 (1); BaFe3.8Pt0.2Sb12 (1)
- dopant candidates (<5% at.): In (5), Co (5), Pt (2)
- measured range: 10-808 K (5th-95th pct of 54 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ba(FeSb3)4 Im-3 (204) mp-1189647 [hull=0.000, icsd=1, PRIMARY]
- papers: https://doi.org/10.1143/jjap.45.4025 (Effects of Co Substitution on Magnetic and Thermoelectric Properties o...) | https://doi.org/10.1016/j.physb.2006.03.067 (Roles of spin fluctuations and rattling in magnetic and thermoelectric...) | https://doi.org/10.1016/j.physb.2006.03.078 (Magnetic and thermoelectric properties of BayFe4−xCoxSb12)

## Ba-Ga-Ge-Si
- rank 429 | 16 samples | 4 papers | 12 compositions
- compositions: Ba8.05Ga15.55Si3.49Ge26.91 (2); Ba8.10Ga15.82Si5.11Ge24.98 (2); Ba8.08Ga15.83Si3.54Ge26.54 (2); Ba8.09Ga15.76Si4.96Ge25.19 (2); Ba8.05Ga15.78Si5.05Ge25.11 (1); Ba8.06Ga15.59Si4.54Ge25.71 (1)
- seed hypothesis (confirm): clathrate_i
- solid-solution axis: Ge/(Ge+Si) spans 0.55-0.89 (median 0.83) over 12 compositions
     ISOELECTRONIC SERIES: the parent compound depends on the composition, not on this host. Near either end the minor element is a dilute substituent; in the middle it is a genuine alloy. Record the axis, not one parent -- and note the 5% split used the whole formula, not the sublattice, so its cut lands at a different level on each site.
- measured range: 11-752 K (5th-95th pct of 48 curves)
- papers: https://doi.org/10.1021/cm802289n (Fast Preparation and Characterization of Quarternary Thermoelectric Cl...) | https://doi.org/10.1063/1.2817400 (Thermoelectric properties of silicon-germanium type I clathrates) | https://doi.org/10.1109/ict.2005.1519928 (Thermoelectric properties of Ba-filled Si-Ge alloy type I semiconducti...)

## Bi-Ir-O
- rank 430 | 16 samples | 4 papers | 8 compositions
- compositions: Bi2Ir2O7 (8); Y0.4Bi1.6Ir2O7 (2); Bi1.9Sr0.1Ir2O7 (1); Bi1.8Sr0.2Ir2O7 (1); Bi1.7Sr0.3Ir2O7 (1); Bi1.6Sr0.4Ir2O7 (1)
- dopant candidates (<5% at.): Sr (5), Y (2), Gd (1)
- measured range: 11-347 K (5th-95th pct of 16 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Bi3IrO2 Pnma (62) mp-1191283 [hull=0.163, icsd=1, PRIMARY]; Bi12Ir12O41 P3m1 (156) mp-685339 [hull=0.017, PRIMARY]; Bi12IrO20 I23 (197) mp-1214246 [hull=0.099, PRIMARY]; Bi3Ir3O11 Pn-3 (201) mp-772189 [hull=0.000, PRIMARY]
- papers: https://doi.org/10.1143/jpsj.72.1226 (Spin–Glass-like Transition and Hall Resistivity of Y2-xBixIr2O7) | https://doi.org/10.1016/j.jssc.2016.06.013 (On the electrical properties of the Bi2−Sr Ir2O7 pyrochlore solid solu...) | https://doi.org/10.1088/1367-2630/ab534c (Possible scale invariant linear magnetoresistance in pyrochlore iridat...)

## Ca-Fe-Sb
- rank 431 | 16 samples | 6 papers | 5 compositions
- compositions: CaFe4Sb12 (9); Ca0.93Fe4Sb12 (3); Ca0.91Fe4Sb12 (2); CaFe3.5Co0.5Sb12 (1); Ca0.92Fe4Sb12 (1)
- dopant candidates (<5% at.): Co (1)
- seed hypothesis (confirm): skutterudite, filled_skutterudite  <-- MIXED, split per composition
- measured range: 11-811 K (5th-95th pct of 45 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ca(FeSb3)4 Im-3 (204) mp-13464 [hull=0.000, icsd=2, PRIMARY]
- papers: https://doi.org/10.1016/j.jssc.2014.06.042 (Structures and thermoelectric properties of double-filled (CaxCe1−x)Fe...) | https://doi.org/10.1016/j.physb.2006.03.067 (Roles of spin fluctuations and rattling in magnetic and thermoelectric...) | https://doi.org/10.1016/j.actamat.2015.03.032 (Rare-earth free  p -type filled skutterudites: Mechanisms for low ther...)

## Ce-Cu-In
- rank 432 | 16 samples | 5 papers | 13 compositions
- compositions: CeInCu2 (3); CeCu4In (2); (Ce0.85La0.15)Cu5In (1); (Ce0.8La0.2)Cu5In (1); (Ce0.7La0.3)Cu5In (1); CeCu5In (1)
- dopant candidates (<5% at.): La (7), Ag (1)
- measured range: 10-299 K (5th-95th pct of 25 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): CeInCu2 Fm-3m (225) mp-19834 [hull=0.000, icsd=5, PRIMARY]; CeInCu P-62m (189) mp-20665 [hull=0.000, icsd=4, PRIMARY]; Ce2InCu2 P4/mbm (127) mp-1206783 [hull=0.000, icsd=1, PRIMARY]; Ce9In2Cu P4/mbm (127) mp-1214056 [hull=0.367, PRIMARY]; Ce2In3Cu Pmm2 (25) mp-1227288 [hull=0.039, PRIMARY]
- papers: https://doi.org/10.1088/0953-8984/16/12/007 (Specific heat, susceptibility, magnetotransport and thermoelectric pow...) | https://doi.org/10.1016/j.jallcom.2009.10.028 (Thermoelectric power in (, Ni; , Ga) compounds) | https://doi.org/10.1007/bf00683635 (Thermpower of Ce x Y1?x InCu2 and CeInCu y Ag2?y)

## Ce-Ru-Si
- rank 433 | 16 samples | 3 papers | 5 compositions
- compositions: CeRu2Si2 (11); Ce(Ru0.92Rh0.08)2Si2 (2); Ce0.87La0.13Ru2Si2 (1); Ce0.95La0.05Ru2Si2 (1); CeRuSi2 (1)
- dopant candidates (<5% at.): La (2), Rh (2)
- seed hypothesis (confirm): thcr2si2_122
- measured range: 10-292 K (5th-95th pct of 27 curves; full span incl. outliers 10-376 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ce(SiRu)2 I4/mmm (139) mp-3566 [hull=0.000, icsd=10, PRIMARY]; CeSi3Ru I4mm (107) mp-13120 [hull=0.000, icsd=2, PRIMARY]; CeSi2Ru P2_1/m (11) mp-1025521 [hull=0.000, icsd=1, PRIMARY]; CeSi2Ru3 P6/mmm (191) mp-30043 [hull=0.056, icsd=1, PRIMARY]; CeSiRu P4/nmm (129) mp-8653 [hull=0.000, icsd=1, PRIMARY]
- papers: https://doi.org/10.1007/bf00681532 (Transport properties under magnetic fields of the heavy fermion system...) | https://doi.org/10.7566/jpsj.82.054704 (Magnetic Field Driven Electronic Singularities through Metamagnetic Ph...) | https://doi.org/10.1140/epjb/e2013-31058-8 (Anomalous ferromagnetism and non-Fermi-liquid behavior in the Kondo la...)

## Co-Fe-La-O-Sr
- rank 434 | 16 samples | 8 papers | 10 compositions
- compositions: La0.6Sr0.4Co0.4Fe0.6O3 (4); La0.6Sr0.4Co0.6Fe0.4O3 (4); La1.2Sr0.8CoFeO6 (1); La1.4Sr0.6CoFeO6 (1); LaSrCoFeO6 (1); SrLaFeCoO6 (1)
- measured range: 297-1173 K (5th-95th pct of 22 curves; full span incl. outliers 199-1173 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Sr2La2FeCoO8 Amm2 (38) mp-1218706 [hull=0.031, PRIMARY]; Sr2La3Fe4CoO15 R3m (160) mp-1218784 [hull=0.028, PRIMARY]; Sr2La3FeCo4O15 R3m (160) mp-1218816 [hull=0.019, PRIMARY]; Sr3La2Fe4CoO15 R-3m (166) mp-1218604 [hull=0.004, PRIMARY]; Sr3La2FeCo4O15 R3m (160) mp-1218694 [hull=0.008, PRIMARY]
- papers: https://doi.org/10.1103/physrevb.99.174105 (Enhancement of thermoelectric power factor by inducing octahedral orde...) | https://doi.org/10.1088/1361-648x/aa5470 (Magnetic glass state and magnetoresistance in SrLaFeCoO<sub>6</sub>dou...) | https://doi.org/10.1016/j.jallcom.2016.07.289 (Decreasing the polarization resistance of LaSrCoO4 cathode by Fe subst...)

## Co-Fe-Sb-Ti
- rank 435 | 16 samples | 3 papers | 10 compositions
- compositions: TiFe0.29Co0.78Sb (5); TiFe0.665Co0.5Sb (2); TiFe0.4256Co0.68Sb0.875Sn0.125 (2); TiFe0.5Co0.5Sb (1); TiFe0.2Co0.8Sb (1); TiFe0.3Co0.7Sb (1)
- dopant candidates (<5% at.): Sn (5)
- measured range: 298-853 K (5th-95th pct of 78 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): TiFeCoSb F-43m (216) mp-998973 [hull=0.198, icsd=1, PRIMARY]
- papers: https://doi.org/10.1063/1.2809377 (Thermoelectric properties of p-type Fe-doped TiCoSb half-Heusler compo...) | https://doi.org/10.1016/j.jssc.2019.04.041 (Phase stability and thermoelectric properties of TiCoSb-TiM2Sn (M = Ni...) | https://doi.org/10.1039/c7dt03787b (The half Heusler system Ti<sub>1+x</sub>Fe<sub>1.33−x</sub>Sb–TiCoSb w...)

## Co-La-Mn-O
- rank 436 | 16 samples | 10 papers | 14 compositions
- compositions: La0.98Pb0.02Mn0.74Co0.25O3 (2); La2CoMnO6 (2); La0.95Sr0.05Co0.67Mn0.33O3 (1); (LaCoO3)0.50(La0.7Sr0.3MnO3)0.50 (1); La0.95Sr0.05Co0.33Mn0.67O3 (1); La0.95Sr0.05Co0.5Mn0.5O3 (1)
- dopant candidates (<5% at.): Sr (4), Mg (3), Pb (2), Fe (2)
- measured range: 10-1123 K (5th-95th pct of 25 curves; full span incl. outliers 10-1183 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): La2MnCoO6 P2_1/c (14) mp-19208 [hull=0.000, icsd=5, PRIMARY, AMBIGUOUS]; La2MnCoO6 C2/m (12) mp-1105414 [hull=0.007, icsd=6]
- papers: https://doi.org/10.1016/j.jallcom.2018.03.347 (Thermoelectric properties of (1-x)LaCoO3.xLa0.7Sr0.3MnO3 composite) | https://doi.org/10.1088/2053-1591/aad44c (Magnetothermopower, magnetoresistance and magnetothermal conductivity ...) | https://doi.org/10.1063/1.3054172 (Intrinsic phase separation in a single crystal of La0.98Pb0.02Mn0.74Co...)

## Co-La-O-Rh
- rank 437 | 16 samples | 1 papers | 5 compositions
- compositions: LaCo0.7Rh0.3O3 (4); LaCo0.6Rh0.4O3 (4); LaCo0.5Rh0.5O3 (4); LaCo0.3Rh0.7O3 (2); LaCo0.4Rh0.6O3 (2)
- solid-solution axis: Co/(Co+Rh) spans 0.30-0.70 (median 0.50) over 5 compositions
     ISOELECTRONIC SERIES: the parent compound depends on the composition, not on this host. Near either end the minor element is a dilute substituent; in the middle it is a genuine alloy. Record the axis, not one parent -- and note the 5% split used the whole formula, not the sublattice, so its cut lands at a different level on each site.
- measured range: 300-796 K (5th-95th pct of 16 curves)
- papers: https://doi.org/10.1016/j.jssc.2010.04.021 (Lattice crossover and mixed valency in the LaCo1−xRhxO3 solid solution)

## Cu-In-Se
- rank 438 | 16 samples | 5 papers | 13 compositions
- compositions: CuInSe2 (4); CuIn0.95Mn0.05Se2 (1); CuIn0.9Mn0.1Se2 (1); CuIn3Se4.9Te0.1 (1); CuIn3Se4.95Te0.05 (1); CuIn3Se4.8Te0.2 (1)
- dopant candidates (<5% at.): Zn (5), Te (3), Mn (2)
- measured range: 298-929 K (5th-95th pct of 63 curves; full span incl. outliers 98-933 K)
- [ref 1] TEDesignLab / ICSD: InCuSe2 I-42d (122) mp-22811 [hull=0.000, icsd=41, PRIMARY]; InCuSe2 (1)
- [ref 2] MP, ranked by ICSD evidence: In9(CuSe4)4 P-43m (215) mp-21827 [hull=0.156, icsd=1, PRIMARY]; In2CuSe4 I-4 (82) mp-1078168 [hull=0.052, icsd=1, PRIMARY]; In3CuSe5 P1 (1) mp-1224175 [hull=0.002, PRIMARY]; In11Cu9Se20 I-4 (82) mp-677803 [hull=0.034, PRIMARY]; In8Cu7Se16 P1 (1) mp-675060 [hull=0.064, PRIMARY]
- papers: https://doi.org/10.1111/jace.13860 (CuCrSe2\n Ternary Chromium Chalcogenide: Facile Fabrication, Doping an...) | https://doi.org/10.1103/physrevb.84.075203 (Thermoelectric properties of p-type CuInSe2chalcopyrites enhanced by i...) | https://doi.org/10.3103/s1068375512050043 (The electric and thermoelectric properties of CuInSe2-based chalcopyrite)

## Cu-Nd-O-Sr
- rank 439 | 16 samples | 2 papers | 16 compositions
- compositions: (Ru0.5Cu0.5)(Sr1.67Nd0.33)(Nd1.34Ce0.66)Cu2O10 (1); (Ru0.5Cu0.5)(Sr1.47Ba0.2Nd0.33)(Nd1.34Ce0.66)Cu2O10 (1); (Ru0.5Cu0.5)(Sr1.34Ba0.33Nd0.33)(Nd1.34Ce0.66)Cu2O10 (1); (Ru0.5Cu0.5)(Sr1.17Ba0.5Nd0.33)(Nd1.34Ce0.66)Cu2O10 (1); (Ru0.5Cu0.5)(Sr1.57Ba0.1Nd0.33)(Nd1.34Ce0.66)Cu2O10 (1); Nd1.38Ce0.22Sr0.4CuO4 (1)
- dopant candidates (<5% at.): Ce (16), Ru (5), Ba (4)
- measured range: 11-300 K (5th-95th pct of 21 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Sr5CeNd3Cu4PbO18 Amm2 (38) mp-1218731 [hull=0.046, PRIMARY]; SrNd2(CuO3)2 I4/mmm (139) mp-1218190 [hull=0.060, PRIMARY]; SrNd2(CuO3)2 I4mm (107) mp-1218159 [hull=0.071]
- papers: https://doi.org/10.1007/s10948-010-0721-0 (Synthesis and Superconductivity in Ba-doped (Ru,Cu)(Sr,Nd)2(Nd,Ce)2Cu2...) | https://doi.org/10.1143/jpsj.71.538 (Transport and NQR Studies of Nd1.6-xCexSr0.4CuO4with T*Structure)

## Cu-O-Sm
- rank 440 | 16 samples | 4 papers | 12 compositions
- compositions: Sm2CuO4 (3); Sm1.85Ce0.15CuO4 (3); Sm1.95Ce0.05CuO4 (1); Sm1.98Ce0.02CuO4 (1); Sm1.9Ce0.1CuO4 (1); Sm1.89Ce0.11CuO4 (1)
- dopant candidates (<5% at.): Ce (13)
- measured range: 12-954 K (5th-95th pct of 24 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Sm2CuO4 I4/mmm (139) mp-4210 [hull=0.007, icsd=5, PRIMARY]; Sm(CuO2)2 I4_1/a (88) mp-9417 [hull=0.000, icsd=1, PRIMARY]; SmCuO2 R-3m (166) mp-13695 [hull=0.000, icsd=1, PRIMARY]; Sm2Cu2O5 Pna2_1 (33) mp-768866 [hull=0.057, PRIMARY]; SmCuO3 Pnma (62) mp-770767 [hull=0.000, PRIMARY]
- papers: https://doi.org/10.1002/ecj.10003 (Thermoelectric properties of RE2−xMxCuO4oxide sintering bulks) | https://doi.org/10.1016/s0925-8388(02)00917-9 (Thermoelectric properties of layered rare earth copper oxides) | https://doi.org/10.1016/j.physc.2003.12.012 (Anomalous thermopower of the electron-doped superconductor, Sm2−xCexCuO4)

## F-Li
- rank 441 | 16 samples | 3 papers | 1 compositions
- compositions: LiF (16)
- seed hypothesis (confirm): rocksalt
- measured range: 10-603 K (5th-95th pct of 16 curves; full span incl. outliers 10-800 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): LiF Fm-3m (225) mp-1138 [hull=0.000, icsd=8, PRIMARY]; LiF3 P6_3/mmc (194) mp-1185348 [hull=0.168, PRIMARY]; LiF Pm-3m (221) mp-1009009 [hull=0.273, icsd=1]; LiF P6_3mc (186) mp-1185301 [hull=0.008]
- papers: https://doi.org/10.1002/smll.202101693 (Good Solid‐State Electrolytes Have Low, Glass‐Like Thermal Conductivity) | https://doi.org/10.1103/physrev.156.975 (Effect of Boundaries and Isotopes on the Thermal Conductivity of LiF) | https://doi.org/10.1103/physrevb.94.174304 (Isotope scattering and phonon thermal conductivity in light atom compo...)

## Fe-La-O-Sr-Ti
- rank 442 | 16 samples | 5 papers | 10 compositions
- compositions: (La0.3Sr0.7)0.95Ti0.3Fe0.7O2.95 (2); (La0.3Sr0.7)0.93Ti0.3Fe0.7O2.93 (2); (La0.3Sr0.7)Ti0.3Fe0.7O3 (2); (La0.3Sr0.7)0.91Ti0.3Fe0.7O2.91 (2); (La0.3Sr0.7)0.97Ti0.3Fe0.7O2.97 (2); La0.5Sr0.5Fe0.5Ti0.5O3 (2)
- dopant candidates (<5% at.): Co (1)
- measured range: 373-1173 K (5th-95th pct of 16 curves; full span incl. outliers 373-1223 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): SrLaTiFeO6 F-43m (216) mp-1218147 [hull=0.034, PRIMARY]; SrLaTiFeO6 Fmm2 (42) mp-1218316 [hull=0.199]
- papers: https://doi.org/10.1021/acsaem.2c03142 (La<sub>0.3</sub>Sr<sub>0.7</sub>Ti<sub>0.3</sub>Fe<sub>0.7</sub>O<sub>...) | https://doi.org/10.1063/1.4798364 (Neutron structural characterization and transport properties of <i>oxi...) | https://doi.org/10.1016/j.jmat.2020.02.009 (Cobalt and Titanium substituted SrFeO3 based perovskite as efficient s...)

## Fe-Sb-Ta
- rank 443 | 16 samples | 4 papers | 8 compositions
- compositions: TaFeSb (8); Ta0.94Ti0.06FeSb (2); Ta0.92Ti0.08FeSb (1); Ta0.88Ti0.12FeSb (1); Ta0.98Ti0.02FeSb (1); Ta0.96Ti0.04FeSb (1)
- dopant candidates (<5% at.): Ti (8)
- seed hypothesis (confirm): half_heusler
- measured range: 15-972 K (5th-95th pct of 67 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): TaFeSb F-43m (216) mp-631267 [hull=0.777, PRIMARY]
- papers: https://doi.org/10.1021/ar400290f (Decoupling Interrelated Parameters for Designing High Performance Ther...) | https://doi.org/10.1038/s41467-018-08223-5 (Discovery of TaFeSb-based half-Heuslers with high thermoelectric perfo...) | https://doi.org/10.1002/smll.202102045 (High‐Pressure‐Sintering‐Induced Microstructural Engineering for an Ult...)

## Ga-Sb-Te
- rank 444 | 16 samples | 5 papers | 14 compositions
- compositions: (GaSb)2.25(Ga2Te3)0.25 (2); (GaSb)2.7(Ga2Te3)0.1 (2); Ga7Sb2Te10 (1); Ga12Sb2Te15 (1); GaSb5Te9 (1); Ga2Cu0.05Sb0.3Te2.65 (1)
- dopant candidates (<5% at.): Cu (1)
- measured range: 299-776 K (5th-95th pct of 62 curves)
- papers: https://doi.org/10.1021/cm404115k (Enhancing the Thermoelectric Properties of Germanium Antimony Tellurid...) | https://doi.org/10.1063/1.3079483 (Thermoelectric properties in nanostructured homologous series alloys G...) | https://doi.org/10.1007/s11664-012-2405-y (Nanostructuring and Thermoelectric Characterization of (GaSb)3(1−x)(Ga...)

## Ge-Mn-Te
- rank 445 | 16 samples | 3 papers | 16 compositions
- compositions: Ge0.86Mn0.1Bi0.04Te (1); Ge0.81Mn0.15Bi0.04Te (1); Ge0.76Mn0.2Bi0.04Te (1); Ge0.66Mn0.3Bi0.04Te (1); Ge0.7Na0.15Bi0.15MnTe2 (1); GeMnTe2 (1)
- dopant candidates (<5% at.): Bi (7), Sb (4), Na (3)
- seed hypothesis (confirm): gete_rhombohedral
- measured range: 299-827 K (5th-95th pct of 83 curves)
  !! MEASUREMENT CROSSES A TRANSITION: gete_rhombohedral -> rocksalt at ~700 K (R3m -> Fm-3m, ~700 K; shifts with Ge vacancy content and doping.)
     Record each phase with its own temperature range, not a single prototype.
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): MnGeTe2 P4/mmm (123) mp-1221610 [hull=0.070, PRIMARY]; MnGeTe2 R-3m (166) mp-1221803 [hull=0.451]
- papers: https://doi.org/10.1073/pnas.1802020115 (Phase-transition temperature suppression to achieve cubic GeTe and hig...) | https://doi.org/10.1039/d1cp02545g (Dramatically enhanced Seebeck coefficient in GeMnTe2–NaBiTe2 alloys by...) | https://doi.org/10.1021/jacs.7b13611 (Rhombohedral to Cubic Conversion of GeTe via MnTe Alloying Leads to Ul...)

## Ge-Se-Te
- rank 446 | 16 samples | 8 papers | 15 compositions
- compositions: GeTe0.5Se0.5 (2); GeTe0.9Se0.1 (1); GeTe0.8Se0.2 (1); GeTe0.7Se0.3 (1); GeTe0.6Se0.4 (1); (GeSe)0.95(Sb2Te3)0.05 (1)
- dopant candidates (<5% at.): Bi (5), Sb (4), Ag (3), Cu (1)
- solid-solution axis: Se/(Se+Te) spans 0.10-0.86 (median 0.20) over 15 compositions
     ISOELECTRONIC SERIES: the parent compound depends on the composition, not on this host. Near either end the minor element is a dilute substituent; in the middle it is a genuine alloy. Record the axis, not one parent -- and note the 5% split used the whole formula, not the sublattice, so its cut lands at a different level on each site.
- measured range: 295-796 K (5th-95th pct of 72 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ge2TeSe R-3m (166) mp-1224336 [hull=0.022, PRIMARY]; Ge3Te2Se P-3m1 (164) mp-1224326 [hull=0.033, PRIMARY]; Ge5Te4Se I4/mmm (139) mp-1224356 [hull=0.070, PRIMARY]
- papers: https://doi.org/10.1016/j.actamat.2014.04.036 (High thermoelectric performance of Ge1−xPbxSe0.5Te0.5 due to (Pb, Se) ...) | https://doi.org/10.1007/s11664-016-4770-4 (Influence of Se Substitution in GeTe on Phase and Thermoelectric Prope...) | https://doi.org/10.1016/j.jechem.2019.09.021 (Glass-like electronic and thermal transport in crystalline cubic germa...)

## La-O-V
- rank 447 | 16 samples | 2 papers | 7 compositions
- compositions: LaVO3 (4); La0.84Sr0.16VO3 (3); La0.9Sr0.1VO3 (3); La0.82Sr0.18VO3 (3); La0.88Sr0.12VO3 (1); La0.86Sr0.14VO3 (1)
- dopant candidates (<5% at.): Sr (12)
- seed hypothesis (confirm): perovskite
- measured range: 11-1245 K (5th-95th pct of 18 curves)
- [ref 1] TEDesignLab / ICSD: LaVO4 P2_1/c (14) mp-18989 [hull=0.036, icsd=5, PRIMARY]; LaVO4 I4_1/amd (141) mp-19162 [hull=0.000, icsd=1]
- [ref 2] MP, ranked by ICSD evidence: LaVO3 Pnma (62) mp-19350 [hull=0.000, icsd=8, PRIMARY]; KLa5V2O13 C2/m (12) mp-1195137 [hull=0.000, icsd=1, PRIMARY]; LaV3O9 P2_1/m (11) mp-32481 [hull=0.025, icsd=1, PRIMARY]; La7SmTiV7O20 P1 (1) mp-1076664 [hull=0.245, PRIMARY]; La11V12O36 P1 (1) mp-997527 [hull=0.023, PRIMARY]
- papers: https://doi.org/10.4028/www.scientific.net/amr.118-120.775 (Combinatorial Synthesis and Characterization of Thermoelectric Composi...) | https://doi.org/10.1103/physrevb.83.165127 (Thermoelectric response in the incoherent transport region near Mott t...)

## La-Rh-Sn
- rank 448 | 16 samples | 3 papers | 2 compositions
- compositions: Ca0.2La2.8Rh4Sn13 (13); LaRhSn (3)
- dopant candidates (<5% at.): Ca (13)
- measured range: 11-299 K (5th-95th pct of 5 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): La3Sn13Rh4 Pm-3n (223) mp-30513 [hull=0.000, icsd=5, PRIMARY]; LaSn2Rh Cmcm (63) mp-17370 [hull=0.000, icsd=1, PRIMARY]; La16Sn3Rh8 P4/mbm (127) mp-1197220 [hull=0.000, icsd=1, PRIMARY]; La(Sn2Rh)2 Pnma (62) mp-1193123 [hull=0.000, icsd=1, PRIMARY]; La2Sn5Rh3 Ibam (72) mp-30755 [hull=0.000, icsd=1, PRIMARY]
- papers: https://doi.org/10.1016/s0925-8388(00)01176-2 (Large thermoelectric power in several metallic compounds of cerium and...) | https://doi.org/10.1088/1367-2630/aae4a8 (The effective increase in atomic scale disorder by doping and supercon...) | https://doi.org/10.1143/jjap.42.6512 (Thermoelectric Properties of Single-Crystal CeRhSn with Valence Fluctu...)

## Mg-Sb-Zn
- rank 449 | 16 samples | 4 papers | 14 compositions
- compositions: (Mg0.9Zn0.1)3Sb2 (3); (Mg0.45Zn0.55)3Sb2 (1); (Mg0.8Zn0.2)3Sb2 (1); (Mg0.68Zn0.32)3Sb2 (1); (Mg0.55Zn0.45)3Sb2 (1); Mg2.36Zn0.64Sb2 (1)
- dopant candidates (<5% at.): Na (7), Yb (1)
- seed hypothesis (confirm): caal2si2_zintl
- measured range: 11-775 K (5th-95th pct of 58 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Mg(ZnSb)2 P-3m1 (164) mp-1210585 [hull=0.021, PRIMARY]; Mg14ZnSb P-6m2 (187) mp-1027899 [hull=0.042, PRIMARY]; Mg2ZnSb2 P3m1 (156) mp-1222152 [hull=0.023, PRIMARY]; Mg6ZnSb Amm2 (38) mp-1022642 [hull=0.093, PRIMARY]; Mg14ZnSb Amm2 (38) mp-1027913 [hull=0.055]
- papers: https://doi.org/10.1088/0022-3727/42/16/165403 (Thermoelectric properties of nanocrystalline (Mg1−xZnx)3Sb2isostructur...) | https://doi.org/10.1016/j.jssc.2007.06.011 (Structural and physical properties of Mg3−xZnxSb2 (x=0–1.34)) | https://doi.org/10.1016/j.actamat.2017.10.015 (Significantly enhanced thermoelectric properties of p-type Mg3Sb2 via ...)

## O-Si-Y
- rank 450 | 16 samples | 7 papers | 2 compositions
- compositions: Y2Si2O7 (11); Y2SiO5 (5)
- measured range: 293-1274 K (5th-95th pct of 16 curves)
- [ref 1] TEDesignLab / ICSD: Y2Si2O7 C2/m (12) mp-5652 [hull=0.000, icsd=2, PRIMARY, AMBIGUOUS]; Y2Si2O7 P2_1/c (14) mp-7999 [hull=0.003, icsd=2]; Y2Si2O7 (11)
- [ref 2] MP, ranked by ICSD evidence: Y2SiO5 C2/c (15) mp-3520 [hull=0.000, icsd=4, PRIMARY]; Y3Si3O11 P2_1/c (14) mp-1204527 [hull=0.059, icsd=1, PRIMARY]; BaY4Si5O17 P2_1/m (11) mp-1019546 [hull=0.000, icsd=1, PRIMARY]; NaY9(Si3O13)2 P3 (143) mp-1220819 [hull=0.017, PRIMARY]; LiY9(Si3O13)2 P3 (143) mp-1222506 [hull=0.026, PRIMARY]
- papers: https://doi.org/10.1111/jace.15504 (Thermophysical properties of rare earth barium aluminates) | https://doi.org/10.1007/s11666-016-0450-4 (Processing Parameter Effects and Thermal Properties of Y2Si2O7 Nanostr...) | https://doi.org/10.1016/j.actamat.2020.06.012 (Tailoring thermal properties of multi-component rare earth monosilicates)
