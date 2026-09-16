# Host systems -- chunk 054 of 73

Ranks 2651-2700 by sample count. These 50 host systems cover 50 samples (0.10% of the TE set); cumulative through this chunk: 98.18%.

Assign each host system a structural prototype from `data/annotated/taxonomy/prototypes_seed_v3.json`, or propose a new one in `taxonomy/prototypes_proposed.jsonl` first. Append results to `data/annotated/annotations/family_assignments.jsonl`.

The hand-entered MaterialFamily labels are deliberately NOT shown here -- they are held out in `df_host_systems.parquet` to validate this classification later. Decide from the compositions.

A "seed hypothesis" line means the taxonomy already names this host under that prototype. Confirm it against the compositions rather than accepting it; two or more listed means the host is mixed and needs splitting per composition.

Evidence follows the project precedence. Your judgement about the thermoelectric chemistry decides the prototype. [ref 1] is TEDesignLab, ICSD-backed and thermoelectric-specific -- prefer it. [ref 2] is Materials Project. Within a formula, polymorphs are ranked by ICSD reference count and the top one is marked PRIMARY -- not by e_above_hull, which is unusable for layered chalcogenides in the 2019 dump (Sb2Te3 R-3m carries 26 ICSD refs at hull 1.02). A primary resting on fewer than 5 ICSD references is flagged weak; the ambient phase may simply be absent from the snapshot, as it is for Bi2Se3.

While you have the host in view, also record what each minor element DOES, in `dopant_roles` -- the role follows from the prototype and cannot be judged without it. A median host has 2 such elements. Not everything listed is a dopant: O, C, N and H are usually milling or pressing residue, and an element just under 5 at.% may be an alloying end member rather than dilute doping. The doping LEVEL is computed later from the parsed fractions -- do not work it out by hand here.

A polymorph list is NOT a thermal sequence. SnSe has three known structures but only Pnma -> Cmcm happens on heating; rocksalt SnSe is metastable (2 icsd refs against 32). Put thermally reached phases in `phases` with their transition temperatures, and everything else in `other_polymorphs` with an occurrence reason. hull and icsd counts are shown to help you tell them apart.

A host may need MORE THAN ONE prototype. Transport is measured across a wide window and many thermoelectrics transform inside it, so where a "MEASUREMENT CROSSES A TRANSITION" line appears, record each phase with its own temperature range in the `phases` field. Transition temperatures shown are approximate and composition-dependent.

Both references describe which phases EXIST in a chemistry, not which phase this paper made. Al-O-Zn is best attested as ZnAl2O4 spinel (227) while almost every sample in it is Al-doped wurtzite ZnO (186). Weigh them against the compositions; do not follow them blindly.

## Ba-Cu-Fe-O-Tb
- rank 2651 | 1 samples | 1 papers | 1 compositions
- compositions: TbBaCuFeO5 (1)
- measured range: 296-998 K (5th-95th pct of 3 curves; full span incl. outliers 296-1043 K)
- papers: https://doi.org/10.1134/s1063783409020073 (Thermoelectric properties of layered ferrocuprates LnBaCuFeO5 + δ (Ln=...)

## Ba-Cu-Fe-O-Tm
- rank 2652 | 1 samples | 1 papers | 1 compositions
- compositions: TmBaCuFeO5 (1)
- measured range: 303-1000 K (5th-95th pct of 3 curves; full span incl. outliers 303-1044 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): BaTmFeCuO5 P4mm (99) mp-1205946 [hull=0.006, PRIMARY]
- papers: https://doi.org/10.1134/s1063783409020073 (Thermoelectric properties of layered ferrocuprates LnBaCuFeO5 + δ (Ln=...)

## Ba-Cu-Fe-O-Yb
- rank 2653 | 1 samples | 1 papers | 1 compositions
- compositions: YbBaCuFeO5 (1)
- measured range: 291-998 K (5th-95th pct of 3 curves; full span incl. outliers 291-1042 K)
- papers: https://doi.org/10.1134/s1063783409020073 (Thermoelectric properties of layered ferrocuprates LnBaCuFeO5 + δ (Ln=...)

## Ba-Cu-Ga-P
- rank 2654 | 1 samples | 1 papers | 1 compositions
- compositions: BaCuGaP2 (1)
- measured range: 11-669 K (5th-95th pct of 4 curves)
- papers: https://doi.org/10.1039/d4ta01063a (BaCu<i>T</i>P<sub>2</sub> (<i>T</i> = Al, Ga, In): a semiconducting bl...)

## Ba-Cu-Ge-P
- rank 2655 | 1 samples | 1 papers | 1 compositions
- compositions: Ba8Cu14Ge6P26 (1)
- measured range: 11-400 K (5th-95th pct of 4 curves; full span incl. outliers 11-812 K)
- papers: https://doi.org/10.1021/acs.accounts.7b00469 (Unconventional Clathrates with Transition Metal–Phosphorus Frameworks)

## Ba-Cu-Ge-Se
- rank 2656 | 1 samples | 1 papers | 1 compositions
- compositions: BaCu2GeSe4 (1)
- measured range: 320-674 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): BaCu2GeSe4 P3_121 (152) mp-17252 [hull=0.000, icsd=1, PRIMARY]
- papers: https://doi.org/10.1039/c8ta09660k (Origins of ultralow thermal conductivity in 1-2-1-4 quaternary selenides)

## Ba-Cu-In-P
- rank 2657 | 1 samples | 1 papers | 1 compositions
- compositions: BaCuInP2 (1)
- measured range: 23-300 K (5th-95th pct of 1 curves)
- papers: https://doi.org/10.1039/d4ta01063a (BaCu<i>T</i>P<sub>2</sub> (<i>T</i> = Al, Ga, In): a semiconducting bl...)

## Ba-Cu-Mn-O-Y
- rank 2658 | 1 samples | 1 papers | 1 compositions
- compositions: YBa2Cu3La0.7Sr0.3MnO10 (1)
- dopant candidates (<5% at.): La (1), Sr (1)
- measured range: 15-297 K (5th-95th pct of 1 curves)
- papers: https://doi.org/10.1063/1.1991973 (Superconducting and transport properties of YBa2Cu3O7∕La0.7Sr0.3MnO3 b...)

## Ba-Cu-S-Te
- rank 2659 | 1 samples | 1 papers | 1 compositions
- compositions: BaCu5.9STe6 (1)
- measured range: 307-593 K (5th-95th pct of 5 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ba4Cu11(Te4S)2 Pm (6) mp-1228217 [hull=0.000, PRIMARY]; BaCu6Te6S P2 (3) mp-1228010 [hull=0.041, PRIMARY]
- papers: https://doi.org/10.1021/ic502055z (Thermoelectric Properties of the Quaternary Chalcogenides BaCu5.9STe6a...)

## Ba-Fe-Ga-Ni-O
- rank 2660 | 1 samples | 1 papers | 1 compositions
- compositions: GaBaFeNiO5 (1)
- measured range: 523-1123 K (5th-95th pct of 1 curves)
- papers: https://doi.org/10.1016/j.electacta.2015.09.146 (Cobalt-free double perovskite cathode GdBaFeNiO5+δ and electrochemical...)

## Ba-Fe-Ir-O
- rank 2661 | 1 samples | 1 papers | 1 compositions
- compositions: Ba3Fe1.56Ir1.44O9 (1)
- measured range: 12-298 K (5th-95th pct of 1 curves)
- papers: https://doi.org/10.1021/acs.inorgchem.8b01015 (Ba3Fe1.56Ir1.44O9: A Polar Semiconducting Triple Perovskite with Near ...)

## Ba-Fe-La-O-Sr
- rank 2662 | 1 samples | 1 papers | 1 compositions
- compositions: LaBa0.5Sr0.5Fe1.8Cu0.2O6 (1)
- dopant candidates (<5% at.): Cu (1)
- measured range: 303-1123 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ba5SrLa2Fe4O15 Cc (9) mp-698793 [hull=0.000, PRIMARY]
- papers: https://doi.org/10.1007/s11664-021-09110-4 (XRD, XANES, and Electrical Conductivity Analysis of La- and Zr-Doped B...)

## Ba-Fe-Mo-O
- rank 2663 | 1 samples | 1 papers | 1 compositions
- compositions: Ba2FeMoO6 (1)
- measured range: 32-310 K (5th-95th pct of 2 curves; full span incl. outliers 32-849 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ba2FeMoO6 Fm-3m (225) mp-18995 [hull=0.000, icsd=12, PRIMARY]
- papers: https://doi.org/10.1063/1.1728294 (Effect of alkaline-earth and transition metals on the electrical trans...)

## Ba-Fe-Ni-O
- rank 2664 | 1 samples | 1 papers | 1 compositions
- compositions: BaFe0.75Ni0.25O3 (1)
- measured range: 373-1023 K (5th-95th pct of 1 curves)
- papers: https://doi.org/10.1016/j.electacta.2018.09.096 (Ni-doped BaFeO3− perovskite oxide as highly active cathode electrocata...)

## Ba-Fe-Ni-Sb
- rank 2665 | 1 samples | 1 papers | 1 compositions
- compositions: Ba0.96Fe3.0Ni1.0Sb12 (1)
- measured range: 26-802 K (5th-95th pct of 4 curves)
- papers: https://doi.org/10.1016/j.jmst.2014.05.007 (Thermoelectric Transport Properties of RyFe3NiSb12 (R = Ba, Nd and Yb))

## Ba-Fe-O-Os
- rank 2666 | 1 samples | 1 papers | 1 compositions
- compositions: Ba2Fe1.12Os0.88O6 (1)
- measured range: 110-301 K (5th-95th pct of 1 curves)
- papers: https://doi.org/10.1021/acs.chemmater.6b04983 (High-Temperature Ferrimagnetism with Large Coercivity and Exchange Bia...)

## Ba-Fe-O-Sb-Sr
- rank 2667 | 1 samples | 1 papers | 1 compositions
- compositions: Ba0.5Sr0.5Fe0.5Sb0.5O3 (1)
- measured range: 673-1073 K (5th-95th pct of 1 curves)
- papers: https://doi.org/10.1016/j.jallcom.2016.01.122 (Antimony doped barium strontium ferrite perovskites as novel cathodes ...)

## Ba-Fe-O-Ti
- rank 2668 | 1 samples | 1 papers | 1 compositions
- compositions: BaFe0.7Ti0.3O3 (1)
- measured range: 629-1201 K (5th-95th pct of 2 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ba2Ti4Fe2O13 C2/m (12) mp-1214656 [hull=0.012, PRIMARY]; Ba2TiFeO6 P3m1 (156) mp-1228536 [hull=0.015, PRIMARY]; Ba3Ti(FeO4)2 Ama2 (40) mp-1228283 [hull=0.026, PRIMARY]; Ba3TiFe2O9 P6_3mc (186) mp-1228231 [hull=0.000, PRIMARY, AMBIGUOUS]; BaTi2Fe4O11 C2/c (15) mp-1227638 [hull=0.051, PRIMARY]
- papers: https://doi.org/10.2109/jcersj2.121.706 (High-temperature thermoelectric properties of BaFexTi1^|^minus;xO3^|^m...)

## Ba-Fe-O-Zn
- rank 2669 | 1 samples | 1 papers | 1 compositions
- compositions: BaFe0.6Zn0.3Nb0.1O3 (1)
- dopant candidates (<5% at.): Nb (1)
- measured range: 573-973 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): BaZnFe6O11 Cm (8) mp-1227632 [hull=0.196, PRIMARY]
- papers: https://doi.org/10.1021/acs.jpcc.3c01812 (Characterization of BaFe<sub>0.8</sub>Zn<sub>0.1</sub>Nb<sub>0.1</sub>...)

## Ba-Ga
- rank 2670 | 1 samples | 1 papers | 1 compositions
- compositions: BaGa4 (1)
- measured range: 16-284 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): BaGa4 I4/mmm (139) mp-335 [hull=0.000, icsd=4, PRIMARY]; BaGa2 P6/mmm (191) mp-1219 [hull=0.000, icsd=4, PRIMARY]; Ba10Ga Fd-3m (227) mp-30430 [hull=0.131, icsd=1, PRIMARY]; Ba8Ga7 P2_13 (198) mp-30429 [hull=0.000, icsd=1, PRIMARY]; Ba5Ga6 P6_3/m (176) mp-1228211 [hull=0.002, PRIMARY]
- papers: https://doi.org/10.1016/j.jallcom.2015.08.193 (Characteristic Fermi surfaces and charge density wave in SrAl4 and rel...)

## Ba-Ga-Ge-Na
- rank 2671 | 1 samples | 1 papers | 1 compositions
- compositions: Ba8Na2.97Ga3.94Ge38.91 (1)
- measured range: 302-848 K (5th-95th pct of 1 curves)
- papers: https://doi.org/10.1002/adfm.200901817 (On the Design of High-Efficiency Thermoelectric Clathrates through a S...)

## Ba-Ga-Ge-Ni
- rank 2672 | 1 samples | 1 papers | 1 compositions
- compositions: Ba8Ni2.97Ga3.94Ge39.09 (1)
- measured range: 296-902 K (5th-95th pct of 3 curves)
- papers: https://doi.org/10.1002/adfm.200901817 (On the Design of High-Efficiency Thermoelectric Clathrates through a S...)

## Ba-Ga-Ge-Pt
- rank 2673 | 1 samples | 1 papers | 1 compositions
- compositions: Ba8Pt3Ga4Ge39 (1)
- measured range: 312-883 K (5th-95th pct of 1 curves)
- papers: https://doi.org/10.1109/ict.2003.1287464 (Effect of transition element substitution on thermoelectric properties...)

## Ba-Gd-Ni-O
- rank 2674 | 1 samples | 1 papers | 1 compositions
- compositions: Gd2BaNiO5 (1)
- measured range: 75-285 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): BaGd2NiO5 Immm (71) mp-19332 [hull=0.000, icsd=4, PRIMARY]
- papers: https://doi.org/10.1063/1.4881531 (Multiferroicity and magneto-electric effect in Gd2BaNiO5)

## Ba-Ge-K-Zn
- rank 2675 | 1 samples | 1 papers | 1 compositions
- compositions: K4Ba4Zn6Ge40 (1)
- measured range: 99-1050 K (5th-95th pct of 5 curves)
- papers: https://doi.org/10.1063/1.4711100 (Crystal structure and thermoelectric properties of KxBa8−xZnyGe46−y cl...)

## Ba-Ge-Ni-Si
- rank 2676 | 1 samples | 1 papers | 1 compositions
- compositions: Ba8Ni3.4Si9.0Ge33.6 (1)
- measured range: 308-821 K (5th-95th pct of 5 curves)
- papers: https://doi.org/10.3390/ma11060946 (Crystal Chemistry and Thermoelectric Properties of Type-I Clathrate Ba...)

## Ba-Ge-Rh
- rank 2677 | 1 samples | 1 papers | 1 compositions
- compositions: BaRhGe3 (1)
- measured range: 20-296 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ba(GeRh)2 I4/mmm (139) mp-10698 [hull=0.000, icsd=1, PRIMARY]; Ba3(Ge4Rh)4 I4/mmm (139) mp-1192163 [hull=0.000, icsd=1, PRIMARY]; BaGe3Rh I4mm (107) mp-1070247 [hull=0.038, icsd=1, PRIMARY]
- papers: https://doi.org/10.1021/ic302139r (Cage-Forming Compounds in the Ba–Rh–Ge System: From Thermoelectrics to...)

## Ba-Ir-Mg-O
- rank 2678 | 1 samples | 1 papers | 1 compositions
- compositions: Ba3MgIr2O9 (1)
- measured range: 111-297 K (5th-95th pct of 1 curves)
- papers: https://doi.org/10.1103/physrevb.97.064408 (Ba3MIr2O9\n hexagonal perovskites in the light of spin-orbit coupling ...)

## Ba-Ir-O-Sr
- rank 2679 | 1 samples | 1 papers | 1 compositions
- compositions: Ba3SrIr2O9 (1)
- measured range: 120-300 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ba2SrIrO6 Fm-3m (225) mp-9115 [hull=0.000, icsd=1, PRIMARY]; Ba2Sr(IrO3)3 P-6m2 (187) mp-1229074 [hull=0.078, PRIMARY]
- papers: https://doi.org/10.1103/physrevb.97.064408 (Ba3MIr2O9\n hexagonal perovskites in the light of spin-orbit coupling ...)

## Ba-K-O-Sb
- rank 2680 | 1 samples | 1 papers | 1 compositions
- compositions: Ba0.35K0.65SbO3 (1)
- measured range: 10-50 K (5th-95th pct of 1 curves)
- papers: https://doi.org/10.1038/s41563-022-01203-7 (Superconductivity in (Ba,K)SbO3)

## Ba-La-Ni-O-Os
- rank 2681 | 1 samples | 1 papers | 1 compositions
- compositions: BaLaNiOsO6 (1)
- measured range: 190-301 K (5th-95th pct of 1 curves)
- papers: https://doi.org/10.1016/j.ssc.2016.06.008 (Synthesis, crystal structures, and magnetic properties of double perov...)

## Ba-Mn-O-Y
- rank 2682 | 1 samples | 1 papers | 1 compositions
- compositions: Y0.5Ba0.5MnO3 (1)
- measured range: 166-399 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): BaYMn2O5 P4/mmm (123) mp-18850 [hull=0.000, icsd=5, PRIMARY]; Ba5Y8Mn4O21 I4/m (87) mp-1199104 [hull=0.004, icsd=1, PRIMARY]; Ba2Y2Mn4O11 Cmmm (65) mp-1214593 [hull=0.031, PRIMARY, AMBIGUOUS]; BaYMn2O6 P2/c (13) mp-18739 [hull=0.075, PRIMARY]; BaYMn2O5 P4/nmm (129) mp-1189786 [hull=0.000]
- papers: https://doi.org/10.1143/jpsj.73.2283 (<i>A</i>-site Randomness Effect on Structural and Physical Properties ...)

## Ba-Mo-O-Sr-Ti
- rank 2683 | 1 samples | 1 papers | 1 compositions
- compositions: BaSrTiMoO6 (1)
- measured range: 335-1237 K (5th-95th pct of 1 curves)
- papers: https://doi.org/10.1016/j.jallcom.2017.03.264 (Effect of Ba-doping on high temperature thermoelectric properties of S...)

## Ba-Mo-O-Ti
- rank 2684 | 1 samples | 1 papers | 1 compositions
- compositions: BaTiMoO6 (1)
- measured range: 335-1240 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ba3TiMoO8 R3m (160) mp-1228461 [hull=0.030, PRIMARY]; Ba5Ti4MoO15 Cmmm (65) mp-1228035 [hull=0.006, PRIMARY]
- papers: https://doi.org/10.1016/j.jallcom.2017.03.264 (Effect of Ba-doping on high temperature thermoelectric properties of S...)

## Ba-N-O-Os
- rank 2685 | 1 samples | 1 papers | 1 compositions
- compositions: (Ba6O)(OsN3)2 (1)
- measured range: 41-291 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ba5Os3NO18 P6_3cm (185) mp-628618 [hull=0.000, icsd=1, PRIMARY]; Ba6Os2N6O R-3 (148) mp-1104257 [hull=0.000, icsd=1, PRIMARY]
- papers: https://doi.org/10.1002/asia.200800232 (Synthesis, Crystal Structure, Bonding, and Properties of (Ba<sub>6</su...)

## Ba-Ni-O-Ta
- rank 2686 | 1 samples | 1 papers | 1 compositions
- compositions: Ba3NiTa2O9 (1)
- measured range: 475-1473 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ba3Ta2NiO9 P-3m1 (164) mp-32310 [hull=0.000, icsd=1, PRIMARY]; Ba4Ta10NiO30 Imm2 (44) mp-1228660 [hull=0.006, PRIMARY]
- papers: https://doi.org/10.1007/s11666-018-0796-x (High-Temperature Thermal Properties of Ba(Ni1/3Ta2/3)O3 Ceramic and Ch...)

## Ba-Ni-P
- rank 2687 | 1 samples | 1 papers | 1 compositions
- compositions: BaNi2P4 (1)
- measured range: 10-297 K (5th-95th pct of 3 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): BaNi9P5 P6_3/mmc (194) mp-3202 [hull=0.000, icsd=2, PRIMARY]; Ba(Ni5P3)2 Cmce (64) mp-14765 [hull=0.007, icsd=1, PRIMARY]; Ba(NiP)2 I4/mmm (139) mp-9473 [hull=0.000, icsd=1, PRIMARY]; Ba(NiP2)2 I4/mmm (139) mp-28927 [hull=0.000, icsd=1, PRIMARY]
- papers: https://doi.org/10.1021/acs.chemmater.5b01592 (Twisted Kelvin Cells and Truncated Octahedral Cages in the Crystal Str...)

## Ba-O-Rh
- rank 2688 | 1 samples | 1 papers | 1 compositions
- compositions: Ba2RhO4 (1)
- measured range: 17-297 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): BaRhO3 P6_3/mmc (194) mp-7685 [hull=0.019, icsd=1, PRIMARY]; Ba3(RhO2)14 P-1 (2) mp-758025 [hull=0.000, PRIMARY]; Ba9Rh8O27 P1 (1) mp-772389 [hull=0.000, PRIMARY]; BaRhO3 Pm-3m (221) mp-1016850 [hull=0.112]
- papers: https://doi.org/10.1103/physrevmaterials.5.015001 (High-pressure synthesis of \n<mml:math xmlns:mml=\"http://www.w3.org/1...)

## Ba-O-Sb-Sr
- rank 2689 | 1 samples | 1 papers | 1 compositions
- compositions: Ba0.5Sr0.5SbO3 (1)
- measured range: 673-1073 K (5th-95th pct of 1 curves)
- papers: https://doi.org/10.1016/j.jallcom.2016.01.122 (Antimony doped barium strontium ferrite perovskites as novel cathodes ...)

## Ba-P-Si
- rank 2690 | 1 samples | 1 papers | 1 compositions
- compositions: Ba2Si3P6 (1)
- measured range: 11-299 K (5th-95th pct of 4 curves)
- [ref 1] TEDesignLab / ICSD: Ba3(Si2P3)2 P2_1/m (11) mp-27887 [hull=0.000, icsd=1, PRIMARY]
- [ref 2] MP, ranked by ICSD evidence: Ba4SiP4 P-43n (218) mp-14214 [hull=0.000, icsd=1, PRIMARY]
- papers: https://doi.org/10.1021/jacs.9b04653 (Ba2Si3P6: 1D Nonlinear Optical Material with Thermal Barrier Chains)

## Ba-Pt-Si
- rank 2691 | 1 samples | 1 papers | 1 compositions
- compositions: Ba8Pt5Si41 (1)
- measured range: 306-1057 K (5th-95th pct of 2 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): BaSi3Pt I4mm (107) mp-1069809 [hull=0.000, icsd=1, PRIMARY]; BaSiPt P2_13 (198) mp-1101912 [hull=0.000, icsd=1, PRIMARY]; BaSi12Pt5 C2/m (12) mp-1214345 [hull=0.000, PRIMARY]
- papers: https://doi.org/10.1007/s11664-015-4238-y (High-Temperature Thermoelectric Properties of Polycrystalline Silicon ...)

## Ba-Sb-Se
- rank 2692 | 1 samples | 1 papers | 1 compositions
- compositions: Ba2Sb2Se5 (1)
- measured range: 11-400 K (5th-95th pct of 2 curves; full span incl. outliers 11-772 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ba(SbSe2)2 P2_1/c (14) mp-4727 [hull=0.000, icsd=1, PRIMARY]; Ba3Sb2Se7 C2/c (15) mp-1194583 [hull=0.000, icsd=1, PRIMARY]; Ba4Sb4Se11 Pnnm (58) mp-28238 [hull=0.000, icsd=1, PRIMARY]
- papers: https://doi.org/10.1039/c5tc01721a (Synthesis, crystal structure, and thermoelectric properties of two new...)

## Ba-Sc-Te
- rank 2693 | 1 samples | 1 papers | 1 compositions
- compositions: BaSc2Te4 (1)
- measured range: 161-295 K (5th-95th pct of 2 curves; full span incl. outliers 161-545 K)
- [ref 1] TEDesignLab / ICSD: Ba(ScTe2)2 Pnma (62) mp-17501 [hull=0.002, icsd=1, PRIMARY]
- papers: https://doi.org/10.1016/j.intermet.2006.08.006 (Thermoelectric properties of the new tellurides SrSc2Te4 and BaSc2Te4 ...)

## Ba-Si-Sr
- rank 2694 | 1 samples | 1 papers | 1 compositions
- compositions: Sr0.81Ba0.19Si2 (1)
- measured range: 10-387 K (5th-95th pct of 5 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): BaSrSi4 C222_1 (20) mp-1227347 [hull=0.012, PRIMARY]; BaSrSi4 Pnma (62) mp-1227506 [hull=0.050]
- papers: https://doi.org/10.1016/j.intermet.2020.106981 (Thermoelectric properties of cubic Ba-substituted strontium disilicide...)

## Ba-Sn-Te
- rank 2695 | 1 samples | 1 papers | 1 compositions
- compositions: Ba2SnTe5 (1)
- measured range: 180-295 K (5th-95th pct of 1 curves)
- papers: https://doi.org/10.1109/ict.2005.1519948 (Exploratory synthesis of new heavy main group chalcogenides)

## Ba-Te-Y
- rank 2696 | 1 samples | 1 papers | 1 compositions
- compositions: BaY2Te4 (1)
- measured range: 185-297 K (5th-95th pct of 2 curves; full span incl. outliers 185-550 K)
- [ref 1] TEDesignLab / ICSD: Ba(YTe2)2 Pnma (62) mp-17872 [hull=0.000, icsd=1, PRIMARY]
- papers: https://doi.org/10.1016/j.intermet.2006.08.006 (Thermoelectric properties of the new tellurides SrSc2Te4 and BaSc2Te4 ...)

## Be-Ce
- rank 2697 | 1 samples | 1 papers | 1 compositions
- compositions: CeBe2 (1)
- measured range: 10-91 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): CeBe13 Fm-3c (226) mp-457 [hull=0.000, icsd=6, PRIMARY]
- papers: https://doi.org/10.1063/1.2355360 (Zirconium Copper — a New Material for Use at Low Temperatures?)

## Be-Ce-Pd
- rank 2698 | 1 samples | 1 papers | 1 compositions
- compositions: CePd3Be0.4 (1)
- measured range: 13-348 K (5th-95th pct of 3 curves)
- papers: https://doi.org/10.1088/0953-8984/28/16/165603 (Kondo effect and thermoelectric transport in CePd3Bex)

## Be-Th
- rank 2699 | 1 samples | 1 papers | 1 compositions
- compositions: ThBe13 (1)
- measured range: 21-347 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): ThBe13 Fm-3c (226) mp-1562 [hull=0.000, icsd=7, PRIMARY]; Th3Be Pm-3m (221) mp-979009 [hull=0.338, PRIMARY]
- papers: https://doi.org/10.1016/0304-8853(87)90605-6 (Seebeck coefficient of heavy fermion compounds)

## Be-V
- rank 2700 | 1 samples | 1 papers | 1 compositions
- compositions: VBe12 (1)
- measured range: 298-774 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Be2V P6_3/mmc (194) mp-11281 [hull=0.000, icsd=1, PRIMARY]
- papers: https://doi.org/10.1109/fusion.2009.5226458 (Beryllides for fusion reactors)
