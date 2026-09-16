# Annotations that need a paper to settle

**How to use this file.** Each entry says what is uncertain, what to look for in the paper, and links the papers reporting the compositions in question. Fill in the ```finding``` block at the end of an entry and run `python scripts/apply_review_findings.py` to write it into the ledger. Entries you skip are left alone, so you can work through this a few at a time. Nothing is overwritten without a decision.

83 of 200 annotated host systems, 12670 samples. Ordered by sample count, so working top-down resolves the most data per paper read.

Every assignment here was made from composition and materials knowledge; none has been read out of a paper. The links below go to the specific papers reporting the compositions in question.

---

## Bi-Sb-Te — 1473 samples, chunk 1

**Assigned** `tetradymite` (high confidence)

**Needs checking because:**
- structure reference cannot separate two polymorphs

**What to look for:**
- Which polymorph was actually made. Look for the reported space group or lattice parameters in the experimental section. Record the space group number, or the mp_id if you have it.

> Bi0.5Sb1.5Te3 (348) and Bi0.4Sb1.6Te3 (164) are the commercial p-type alloys; the whole host is the (Bi,Sb)2Te3 quintuple-layer solid solution.

**`Bi0.5Sb1.5Te3`** — 348 samples, 144 papers
- [Melting and solidification of bismuth antimony telluride under a high magnetic field: A new rou...](https://doi.org/10.1016/j.nanoen.2015.05.032) (2015) — 14 samples
- [Correlation with the composition of the different parts of p-type Bi0.5Sb1.5Te3 sintered bulks ...](https://doi.org/10.1016/j.jallcom.2020.156114) (2020) — 9 samples
- [Significant Enhancement of Thermoelectric Figure of Merit in BiSbTe‐Based Composites by Incorpo...](https://doi.org/10.1002/adfm.202008851) (2021) — 8 samples

**`Bi0.4Sb1.6Te3`** — 164 samples, 61 papers
- [Effects of spark plasma sintering conditions on the anisotropic thermoelectric properties of bi...](https://doi.org/10.1039/c6ra06688g) (2016) — 26 samples
- [The Influence of Anisotropy and Nanoparticle Size Distribution on the Lattice Thermal Conductiv...](https://doi.org/10.1007/s11664-014-2988-6) (2014) — 6 samples
- [Preparation and Characterization of Bi0.4Sb1.6Te3 Bulk Thermoelectric Materials](https://doi.org/10.1007/s11664-014-3038-0) (2014) — 6 samples

**`Bi0.48Sb1.52Te3`** — 47 samples, 18 papers
- [Investigation of the sintering pressure and thermal conductivity anisotropy of melt-spun spark-...](https://doi.org/10.1557/jmr.2011.170) (2011) — 16 samples
- [Structural and Electrical Properties Characterization of Sb1.52Bi0.48Te3.0 Melt-Spun Ribbons](https://doi.org/10.3390/cryst7060172) (2017) — 5 samples
- [Cost-Efficient Preparation and Enhanced Thermoelectric Performance of Bi0.48Sb1.52Te3 Bulk Mate...](https://doi.org/10.1007/s11664-013-2857-8) (2013) — 4 samples

**`(Bi0.25Sb0.75)2Te3`** — 28 samples, 10 papers
- [Thermoelectric generators for wearable body heat harvesting: Material and device concurrent opt...](https://doi.org/10.1016/j.nanoen.2019.104265) (2020) — 6 samples
- [Interfacial Stability in Bi2Te3 Thermoelectric Joints](https://doi.org/10.1021/acsami.9b22853) (2020) — 6 samples
- [Effect of Spinning and Milling Time on Thermoelectric Properties of the p-type (Bi<SUB>0.25</SU...](https://doi.org/10.3724/sp.j.1077.2010.00588) (2010) — 5 samples

**Your finding** — fill in, then run `python scripts/apply_review_findings.py`:

```finding
host: Bi-Sb-Te
decision:        # confirm | change | split | unresolved
prototype:       # for change: the prototype id it should be
spacegroup:      # number the paper reports, e.g. 212
mp_id:           # if you have it
evidence:        # DOI you read this from
notes:
```

---

## O-Sr-Ti — 1338 samples, chunk 1

**Assigned** `perovskite` (high confidence)

**Needs checking because:**
- structure reference cannot separate two polymorphs

**What to look for:**
- Which polymorph was actually made. Look for the reported space group or lattice parameters in the experimental section. Record the space group number, or the mp_id if you have it.

> SrTiO3 (196) and Nb/La-doped SrTiO3 dominate. Sr3Ti2O7, Sr4Ti3O10 and Sr2TiO4 appear as Ruddlesden-Popper members.

**`SrTiO3`** — 196 samples, 52 papers
- [The effect of annealing in carbon powders on the anisotropy of the thermoelectric properties of...](https://doi.org/10.1039/d2ce00423b) (2022) — 50 samples
- [Effect of annealing temperature in carbon powder on thermoelectric properties of the SrTiO3−δ s...](https://doi.org/10.1016/j.ceramint.2022.03.166) (2022) — 21 samples
- [Metallicity without quasi-particles in room-temperature strontium titanate](https://doi.org/10.1038/s41535-017-0044-5) (2017) — 13 samples

**`SrTi0.8Nb0.2O3`** — 66 samples, 14 papers
- [Effect of mesoporous structure on the Seebeck coefficient and electrical properties of SrTi0.8N...](https://doi.org/10.1016/j.apsusc.2017.03.016) (2017) — 32 samples
- [Abnormal Grain Growth as a Method To Enhance the Thermoelectric Performance of Nb-Doped Stronti...](https://doi.org/10.1021/acssuschemeng.8b03875) (2018) — 12 samples
- [High thermoelectric performance of niobium-doped strontium titanate bulk material affected by a...](https://doi.org/10.1016/j.scriptamat.2014.11.018) (2015) — 10 samples

**`Sr0.95La0.05TiO3`** — 29 samples, 12 papers
- [Enhancement of thermoelectric efficiency in oxygen-deficient Sr1−xLaxTiO3−δ ceramics](https://doi.org/10.1063/1.3254219) (2009) — 6 samples
- [High-temperature thermoelectric response of double-dopedSrTiO3epitaxial films](https://doi.org/10.1103/physrevb.82.165126) (2010) — 5 samples
- [The influence of oxygen deficiency on the thermoelectric properties of strontium titanates](https://doi.org/10.1063/1.2890493) (2008) — 4 samples

**`Sr0.9La0.1TiO3`** — 29 samples, 17 papers
- [Self-Nanostructuring in SrTiO3: A Novel Strategy for Enhancement of Thermoelectric Response in ...](https://doi.org/10.1021/acsami.9b06483) (2019) — 6 samples
- [High-temperature thermoelectric response of double-dopedSrTiO3epitaxial films](https://doi.org/10.1103/physrevb.82.165126) (2010) — 5 samples
- [Thermoelectric Properties of Combustion-Synthesized Lanthanum-Doped Strontium Titanate](https://doi.org/10.2320/matertrans.48.1079) (2007) — 4 samples

**Your finding** — fill in, then run `python scripts/apply_review_findings.py`:

```finding
host: O-Sr-Ti
decision:        # confirm | change | split | unresolved
prototype:       # for change: the prototype id it should be
split:           # for split: one "composition -> prototype_id" per line
  # Ca3Co4O9 -> misfit_cobaltite
  # Ca3Co2O6 -> ca3co2o6_chain
spacegroup:      # number the paper reports, e.g. 212
mp_id:           # if you have it
evidence:        # DOI you read this from
notes:
```

---

## Bi-Se-Te — 634 samples, chunk 1

**Assigned** `tetradymite` (high confidence)

**Needs checking because:**
- structure reference cannot separate two polymorphs

**What to look for:**
- Which polymorph was actually made. Look for the reported space group or lattice parameters in the experimental section. Record the space group number, or the mp_id if you have it.

> Bi2Te2.7Se0.3 (132) is the standard n-type alloy; the host spans the whole Bi2(Te,Se)3 series.

**`Bi2Te2.7Se0.3`** — 132 samples, 68 papers
- [Thermoelectric Property Studies on Cu-Doped n-type CuxBi2Te2.7Se0.3 Nanocomposites](https://doi.org/10.1002/aenm.201100149) (2011) — 11 samples
- [Experimental Studies on Anisotropic Thermoelectric Properties and Structures of n-Type Bi2Te2.7...](https://doi.org/10.1021/nl101156v) (2010) — 8 samples
- [Thermoelectric and transport properties of n-type Bi2Te3 nanocomposites](https://doi.org/10.1063/1.2871923) (2008) — 6 samples

**`Bi2Te2.4Se0.6`** — 44 samples, 19 papers
- [Quantitative Texture Analysis of Spark Plasma Textured n-Bi2Te3](https://doi.org/10.1111/jace.12970) (2014) — 10 samples
- [Effect of melt-spun powder additions on the thermoelectric properties of bismuth and antimony c...](https://doi.org/10.1134/s0020168517010095) (2017) — 6 samples
- [Attaining ultrahigh thermoelectric performance of direction-solidified bulk n-type Bi2Te2.4Se0....](https://doi.org/10.1016/j.nanoen.2017.10.034) (2017) — 5 samples

**`Cu0.01Bi2Te2.7Se0.3`** — 20 samples, 7 papers
- [Thermoelectric Property Studies on Cu-Doped n-type CuxBi2Te2.7Se0.3 Nanocomposites](https://doi.org/10.1002/aenm.201100149) (2011) — 12 samples
- [Effects of doping on the positional uniformity of the thermoelectric properties of n-type Bi2Te...](https://doi.org/10.3938/jkps.68.17) (2016) — 3 samples
- [Doping effects on the thermoelectric properties of Cu-intercalated Bi2Te2.7Se0.3](https://doi.org/10.1016/j.cap.2014.12.006) (2015) — 1 samples

**`Bi2Te2Se`** — 13 samples, 8 papers
- [How to Measure Thermoelectric Properties Reliably](https://doi.org/10.1016/j.joule.2018.10.020) (2018) — 6 samples
- [Point Defect Engineering of High-Performance Bismuth-Telluride-Based Thermoelectric Materials](https://doi.org/10.1002/adfm.201400474) (2014) — 1 samples
- [Thermoelectric properties of Bi2Te3microwires](https://doi.org/10.1002/pssc.201300202) (2014) — 1 samples

**Your finding** — fill in, then run `python scripts/apply_review_findings.py`:

```finding
host: Bi-Se-Te
decision:        # confirm | change | split | unresolved
prototype:       # for change: the prototype id it should be
spacegroup:      # number the paper reports, e.g. 212
mp_id:           # if you have it
evidence:        # DOI you read this from
notes:
```

---

## Mg-Si — 453 samples, chunk 1

**Assigned** `antifluorite` (high confidence)

**Needs checking because:**
- structure reference cannot separate two polymorphs

**What to look for:**
- Which polymorph was actually made. Look for the reported space group or lattice parameters in the experimental section. Record the space group number, or the mp_id if you have it.

> Mg2Si (115) antifluorite with Sb, Bi and Ag dopants. mp-1367 Fm-3m, 17 ICSD references.

**`Mg2Si`** — 115 samples, 78 papers
- [Synthesis of Magnesium Silicide Compounds by a Liquid-solid Phase Reaction Method and their The...](https://doi.org/10.2497/jjspm.56.26) (2009) — 5 samples
- [Development of Thermoelectric Materials Fabricated by Spark Plasma Sintering Methods](https://doi.org/10.2497/jjspm.54.576) (2007) — 5 samples
- [Thermoelectric properties of magnesium silicide fabricated using vacuum plasma thermal spray](https://doi.org/10.1063/1.4825045) (2013) — 5 samples

**`Mg2Si0.9875Sb0.0125`** — 19 samples, 3 papers
- [Fabrication parameters for optimized thermoelectric Mg2Si](https://doi.org/10.1007/s10853-014-8023-8) (2014) — 15 samples
- [Microstructural effects on thermoelectric efficiency: A case study on magnesium silicide](https://doi.org/10.1016/j.actamat.2014.05.041) (2014) — 3 samples
- [Thermoelectric transport and microstructure of optimized Mg2Si0.8Sn0.2](https://doi.org/10.1039/c5tc01535a) (2015) — 1 samples

**`Mg2Si0.98Ag0.02`** — 17 samples, 2 papers
- [Reaction and diffusion phenomena in Ag-doped Mg 2 Si](https://doi.org/10.1016/j.jallcom.2015.10.174) (2016) — 16 samples
- [Thermoelectric Properties and Electronic Structure of Bi- and Ag-Doped Mg2Si1−x Ge x Compounds](https://doi.org/10.1007/s11664-009-0735-1) (2009) — 1 samples

**`Mg2Si0.98Bi0.02`** — 7 samples, 4 papers
- [Sb- and Bi-doped Mg2Si: location of the dopants, micro- and nanostructures, electronic structur...](https://doi.org/10.1039/c4dt01177e) (2014) — 4 samples
- [Thermoelectric Properties and Electronic Structure of Bi- and Ag-Doped Mg2Si1−x Ge x Compounds](https://doi.org/10.1007/s11664-009-0735-1) (2009) — 1 samples
- [Effect of Bi-doping and Mg-excess on the thermoelectric properties of Mg2Si materials](https://doi.org/10.1016/j.jpcs.2014.04.008) (2014) — 1 samples

**Your finding** — fill in, then run `python scripts/apply_review_findings.py`:

```finding
host: Mg-Si
decision:        # confirm | change | split | unresolved
prototype:       # for change: the prototype id it should be
spacegroup:      # number the paper reports, e.g. 212
mp_id:           # if you have it
evidence:        # DOI you read this from
notes:
```

---

## Ge-Te — 450 samples, chunk 1

**Assigned** `gete_rhombohedral` (high confidence)

**Needs checking because:**
- transition at ~700 K is a taxonomy default, not read from a paper

**What to look for:**
- Whether the paper reports a structural transition, and at what temperature. Look for DSC, high-temperature XRD, or a kink discussed in the text. Record the temperature, or "none" if the paper shows the sample staying in one phase across its range.

> GeTe (73) is rhombohedral R3m at room temperature and converts to cubic rocksalt near 700 K, inside the measured 10-884 K window. The (GeTe)n(Sb2Te3)m and TAGS compositions are homologues.

**`GeTe`** — 73 samples, 60 papers
- [Cobalt germanide precipitates indirectly improve the properties of thermoelectric germanium ant...](https://doi.org/10.1039/c9tc03410b) (2019) — 4 samples
- [Effect of excess Ge and Te on thermoelectric performance of GeTe](https://doi.org/10.1111/ijac.13750) (2021) — 4 samples
- [Realizing high figure of merit plateau in Ge Bi Te via enhanced Bi solution and Ge precipitation](https://doi.org/10.1016/j.jallcom.2019.07.120) (2019) — 3 samples

**`Ge20Te80`** — 9 samples, 2 papers
- [Preparation and thermoelectric properties of bulkin situnanocomposites with amorphous/nanocryst...](https://doi.org/10.1088/0022-3727/40/19/049) (2007) — 5 samples
- [Nanostructuring and thermoelectric properties of semiconductor tellurides](https://doi.org/10.1109/ict.2007.4569410) (2007) — 4 samples

**`Ge0.95Bi0.05Te1.025`** — 8 samples, 2 papers
- [High Thermoelectric Performance Achieved in GeTe–Bi2Te3 Pseudo‐Binary via Van der Waals Gap‐Ind...](https://doi.org/10.1002/adfm.201806613) (2019) — 6 samples
- [Step-Up Thermoelectric Performance Realized in Bi2Te3 Alloyed GeTe via Carrier Concentration an...](https://doi.org/10.1021/acsaem.9b00057) (2019) — 2 samples

**`(GeTe)0.95(Bi2Te3)0.05`** — 7 samples, 1 papers
- [Investigation of the Microstructural and Thermoelectric Properties of the(GeTe)0.95(Bi2Te3)0.05...](https://doi.org/10.1155/2014/284634) (2014) — 7 samples

**Your finding** — fill in, then run `python scripts/apply_review_findings.py`:

```finding
host: Ge-Te
decision:        # confirm | change | split | unresolved
prototype:       # for change: the prototype id it should be
split:           # for split: one "composition -> prototype_id" per line
  # Ca3Co4O9 -> misfit_cobaltite
  # Ca3Co2O6 -> ca3co2o6_chain
transition_K:    # temperature, or "none"
evidence:        # DOI you read this from
notes:
```

---

## La-Mn-O — 377 samples, chunk 1

**Assigned** `perovskite` (high confidence)

**Needs checking because:**
- structure reference cannot separate two polymorphs

**What to look for:**
- Which polymorph was actually made. Look for the reported space group or lattice parameters in the experimental section. Record the space group number, or the mp_id if you have it.

> LaMnO3 (16) and La1-xAxMnO3 manganites, orthorhombic Pnma. mp-629046 hull 0 with 23 ICSD references.

**`La0.8Sr0.2MnO3`** — 37 samples, 19 papers
- [Growing and characterization of La0.8Sr0.2MnO3 thin films on single crystal oxide substrate](https://doi.org/10.1016/s0921-5107(03)00186-7) (2003) — 8 samples
- [Evaluation of La0.8 Sr0·2MnO3 perovskite prepared by fast solution combustion](https://doi.org/10.1016/j.ceramint.2022.08.105) (2022) — 4 samples
- [Angular dependence of the Hall effect of La<mml:math xmlns:mml=\"http://www.w3.org/1998/Math/Ma...](https://doi.org/10.1103/physrevb.86.184402) (2012) — 3 samples

**`LaMnO3`** — 16 samples, 11 papers
- [Cross-plane thermoelectric transport in p-type La0.67Sr0.33MnO3/LaMnO3 oxide metal/semiconducto...](https://doi.org/10.1063/1.4804937) (2013) — 3 samples
- [Cross-plane electronic and thermal transport properties of p-type La0.67Sr0.33MnO3/LaMnO3 perov...](https://doi.org/10.1063/1.4754514) (2012) — 3 samples
- [Tuning Jahn–Teller distortion and electron localization of LaMnO<sub>3</sub> epitaxial films vi...](https://doi.org/10.1088/1361-6463/abead5) (2021) — 2 samples

**`La0.9Na0.1MnO3`** — 14 samples, 8 papers
- [The effect of annealing process on the physical properties of La1−xNaxMnOy](https://doi.org/10.1016/j.jmmm.2007.08.031) (2008) — 5 samples
- [Magnetoelectric behavior of sodium doped lanthanum manganites](https://doi.org/10.1063/1.3173285) (2009) — 2 samples
- [Influence of magnetic field on electrical and thermal transport in the hole doped ferromagnetic...](https://doi.org/10.1039/c8ra08694j) (2019) — 2 samples

**`La0.9Sr0.1MnO3`** — 13 samples, 6 papers
- [Strain effect on electronic transport and ferromagnetic transition temperature in<mml:math xmln...](https://doi.org/10.1103/physrevb.65.174402) (2002) — 5 samples
- [Epitaxial growth and transport property of La0.9Sr0.1MnO3 thin films deposited on MgO, LaAlO3 a...](https://doi.org/10.1016/j.jallcom.2016.09.268) (2017) — 3 samples
- [Heat conductivity of La1−xSrxMnO3 surface layers](https://doi.org/10.1016/s0921-4526(01)00618-4) (2001) — 2 samples

**Your finding** — fill in, then run `python scripts/apply_review_findings.py`:

```finding
host: La-Mn-O
decision:        # confirm | change | split | unresolved
prototype:       # for change: the prototype id it should be
spacegroup:      # number the paper reports, e.g. 212
mp_id:           # if you have it
evidence:        # DOI you read this from
notes:
```

---

## C — 369 samples, chunk 1

**Assigned** `graphite_layered` (medium confidence)

**Needs checking because:**
- medium confidence
- taxonomy issue recorded

**What to look for:**
- Any explicit structure statement -- space group, prototype name, or the reference structure the authors index against. Record confirm, or the prototype it should be.
- Whether the taxonomy entry itself is wrong or incomplete, rather than the assignment. Record what should change in the prototype.

> C (333) is graphite, graphene, CNT and amorphous carbon -- one prototype for the sp2 net, morphology recorded separately. Rb3C60 and K3C60 are alkali fullerides, a completely different structure, and TEDesignLab's only entry is diamond (Fd-3m, hull 0.134).

**`C`** — 333 samples, 75 papers
- [Thermoelectric power generation using doped MWCNTs](https://doi.org/10.1016/j.carbon.2008.10.043) (2009) — 21 samples
- [Flexible carbonaceous and graphitized films by pyrolytic chemical‐vapor‐deposition method from ...](https://doi.org/10.1063/1.343514) (1989) — 19 samples
- [STB Model and Transport Properties of Pyrolytic Graphites](https://doi.org/10.1063/1.1713135) (1964) — 19 samples

**`B0.04C`** — 13 samples, 2 papers
- [Thermoelectric power factors of nanocarbon ensembles as a function of temperature](https://doi.org/10.1063/1.3103244) (2009) — 10 samples
- [Induction annealing and subsequent quenching: Effect on the thermoelectric properties of boron-...](https://doi.org/10.1063/1.3378681) (2010) — 3 samples

**`Rb3C60`** — 3 samples, 2 papers
- [Absence of saturation in the normal-state resistivity of thin films of<mml:math xmlns:mml=\"htt...](https://doi.org/10.1103/physrevb.48.9945) (1993) — 2 samples
- [Phonon Drag and Carrier Diffusion Contributions in Thermoelectric Power of M3C60(M = K, Rb) Ful...](https://doi.org/10.12693/aphyspola.123.752) (2013) — 1 samples

**`B0.0005C`** — 2 samples, 1 papers
- [Pyrolytic Graphites: Their Description as Semimetallic Molecular Solids](https://doi.org/10.1063/1.1931167) (1962) — 2 samples

**Your finding** — fill in, then run `python scripts/apply_review_findings.py`:

```finding
host: C
decision:        # confirm | change | split | unresolved
prototype:       # for change: the prototype id it should be
split:           # for split: one "composition -> prototype_id" per line
  # Ca3Co4O9 -> misfit_cobaltite
  # Ca3Co2O6 -> ca3co2o6_chain
evidence:        # DOI you read this from
notes:
```

---

## O-Ti — 367 samples, chunk 1

**Assigned** `rutile` (low confidence)

**Needs checking because:**
- low confidence

**What to look for:**
- Any explicit structure statement -- space group, prototype name, or the reference structure the authors index against. Record confirm, or the prototype it should be.

> Genuinely four or more structures: TiO2 (119) as rutile and anatase, TiO (31) rocksalt, Ti2O3 (26) corundum, and Ti4O7/Ti3O5 Magneli shear phases. No single prototype is defensible; must be split per composition.

**`TiO2`** — 119 samples, 39 papers
- [Effect of Thermal Treatment on Thermoelectric Properties of Extruded TiO<sub>2</sub> Ceramics](https://doi.org/10.4028/www.scientific.net/kem.604.249) (2014) — 24 samples
- [Thermoelectric Performance Enhancement of Magnéli Phase TinO2n−1 Compacts by In Situ Reduction ...](https://doi.org/10.1007/s11664-022-09942-8) (2022) — 9 samples
- [Pressure dependence of the large-polaron transport in anatase TiO2single crystals](https://doi.org/10.1209/0295-5075/99/57005) (2012) — 7 samples

**`TiO`** — 31 samples, 8 papers
- [Influence of TiO2 layer's nanostructure on its thermoelectric power factor](https://doi.org/10.1016/j.apsusc.2019.143736) (2019) — 12 samples
- [Superconducting Phase of $\\mathrm{Ti_xO_y}$ Thin Films Grown by Molecular Beam Epitaxy](https://doi.org/10.48550/ARXIV.2203.01405) (2022) — 5 samples
- [Effects of phase fraction on superconductivity of low-valence eutectic titanate films](https://doi.org/10.1063/1.4997443) (2017) — 4 samples

**`Ti2O3`** — 26 samples, 11 papers
- [Thermoelectric Effects in Pure and V-DopedTi2O3Single Crystals](https://doi.org/10.1103/physrevb.8.1364) (1973) — 6 samples
- [Large anisotropy in conductivity of Ti<sub>2</sub>O<sub>3</sub> films](https://doi.org/10.1063/1.5050823) (2018) — 5 samples
- [Pressure-temperature phase diagram of Ti2O3and physical properties in the golden Th2S3-type phase](https://doi.org/10.1103/physrevb.86.024106) (2012) — 4 samples

**`Sr0.1Ti0.9O3`** — 13 samples, 1 papers
- [Effect of nanostructure on the thermal conductivity of La-doped SrTiO3 ceramics](https://doi.org/10.1016/j.jeurceramsoc.2013.08.009) (2014) — 13 samples

**Your finding** — fill in, then run `python scripts/apply_review_findings.py`:

```finding
host: O-Ti
decision:        # confirm | change | split | unresolved
prototype:       # for change: the prototype id it should be
split:           # for split: one "composition -> prototype_id" per line
  # Ca3Co4O9 -> misfit_cobaltite
  # Ca3Co2O6 -> ca3co2o6_chain
evidence:        # DOI you read this from
notes:
```

---

## Co-Na-O — 342 samples, chunk 1

**Assigned** `naxcoo2_layered` (medium confidence)

**Needs checking because:**
- medium confidence

**What to look for:**
- Any explicit structure statement -- space group, prototype name, or the reference structure the authors index against. Record confirm, or the prototype it should be.

> NaCo2O4 (44) is Na0.5CoO2; the whole host is the P2-type gamma-NaxCoO2 layered cobaltate. x is the compositional knob, not doping.

**`NaCo2O4`** — 44 samples, 28 papers
- [Property-processing relations in developing thermoelectric ceramics: Na1−x Co2O4](https://doi.org/10.1007/s10853-010-5039-6) (2010) — 7 samples
- [Power generation performance of π-structure thermoelectric device using NaCo2O4 and Mg2Si elements](https://doi.org/10.1557/opl.2013.53) (2013) — 3 samples
- [The spin entropy suppression induced by Fe3+ in NaCo2O4](https://doi.org/10.1063/1.3409112) (2010) — 3 samples

**`Na0.7CoO2`** — 23 samples, 9 papers
- [Exfoliation Route to Nanostructured Cobalt Oxide with Enhanced Thermoelectric Performance](https://doi.org/10.1143/apex.4.065201) (2011) — 7 samples
- [Enhancing Thermoelectric Figure-of-Merit of Polycrystalline Na\n                y\n            ...](https://doi.org/10.1007/s11664-018-6186-9) (2018) — 5 samples
- [Anisotropic carrier transport properties in layered cobaltate epitaxial films grown by reactive...](https://doi.org/10.1063/1.3119631) (2009) — 3 samples

**`Na0.75CoO2`** — 15 samples, 8 papers
- [Fabrication of p- and n-type Thermoelectric Cobalt Oxides through the Powder-In-Tube Method](https://doi.org/10.1109/ict.2006.331371) (2006) — 4 samples
- [Improved environmental stability of thermoelectric ceramics based on intergrowths of Ca3Co4O9–N...](https://doi.org/10.1016/j.ceramint.2021.01.008) (2021) — 3 samples
- [Unconventional electronic transition in NaxCoO2 with a precisely controlled Na nonstoichiometry](https://doi.org/10.1016/s0921-4526(02)02599-1) (2003) — 2 samples

**`NaCoO2`** — 9 samples, 6 papers
- [Thermal conductivity of the thermoelectric layered cobalt oxides measured by the Harman method](https://doi.org/10.1063/1.1753070) (2004) — 4 samples
- [Enhanced Thermoelectric Power Factor of NaxCoO2Thin Films by Structural Engineering](https://doi.org/10.1002/aenm.201301927) (2014) — 1 samples
- [Laser-induced voltage effects in c-axis inclined NaxCoO2 thin films](https://doi.org/10.1016/j.apsusc.2012.03.186) (2012) — 1 samples

**Your finding** — fill in, then run `python scripts/apply_review_findings.py`:

```finding
host: Co-Na-O
decision:        # confirm | change | split | unresolved
prototype:       # for change: the prototype id it should be
evidence:        # DOI you read this from
notes:
```

---

## Co-La-O — 327 samples, chunk 1

**Assigned** `perovskite` (high confidence)

**Needs checking because:**
- structure reference cannot separate two polymorphs

**What to look for:**
- Which polymorph was actually made. Look for the reported space group or lattice parameters in the experimental section. Record the space group number, or the mp_id if you have it.

> LaCoO3 (64) rhombohedral R-3c perovskite with Sr A-site and Ni/Fe B-site substitution.

**`LaCoO3`** — 64 samples, 40 papers
- [Sintering behavior and thermoelectric properties of LaCoO3 ceramics with Bi2O3–B2O3–SiO2 as a s...](https://doi.org/10.1039/c4ra06735e) (2014) — 7 samples
- [Lattice crossover and mixed valency in the LaCo1−xRhxO3 solid solution](https://doi.org/10.1016/j.jssc.2010.04.021) (2010) — 4 samples
- [Thermoelectric properties of p-type perovskite compounds LaCoO3systems containing the A-site va...](https://doi.org/10.1088/1757-899x/18/14/142005) (2011) — 4 samples

**`La0.9Sr0.1CoO3`** — 18 samples, 13 papers
- [Thermoelectric properties of p-type perovskite compounds LaCoO3systems containing the A-site va...](https://doi.org/10.1088/1757-899x/18/14/142005) (2011) — 5 samples
- [Fabrication and thermoelectric properties of perovskite-type oxide La1−xSrxCoO3 (x=0, 0.1)](https://doi.org/10.1016/j.jallcom.2005.12.127) (2008) — 2 samples
- [Thermoelectric properties of perovskite oxides La1−x Sr x CoO3 prepared by polymerlized complex...](https://doi.org/10.1007/s10853-007-2365-4) (2008) — 1 samples

**`La0.8Sr0.2CoO3`** — 14 samples, 12 papers
- [Exploring the thermoelectric behavior of intrinsic and defect induced LaCoO3 with selected alka...](https://doi.org/10.1016/j.jallcom.2020.157507) (2021) — 3 samples
- [Thermoelectric properties of perovskite oxides La1−x Sr x CoO3 prepared by polymerlized complex...](https://doi.org/10.1007/s10853-007-2365-4) (2008) — 1 samples
- [Properties of oxides for high temperature solid electrolyte fuel cell](https://doi.org/10.1016/0167-2738(83)90122-4) (1983) — 1 samples

**`La0.95Sr0.05CoO3`** — 9 samples, 7 papers
- [Simple chemical solution deposition and thermoelectric properties of epitaxial La0.95Sr0.05CoO3...](https://doi.org/10.1016/j.matlet.2011.03.014) (2011) — 3 samples
- [Thermoelectric properties of perovskite oxides La1−x Sr x CoO3 prepared by polymerlized complex...](https://doi.org/10.1007/s10853-007-2365-4) (2008) — 1 samples
- [Synthesis, sintering, and thermoelectric properties of the solid solution La1–xSrxCoO3±δ (0 ≤ x...](https://doi.org/10.1007/s40145-018-0267-3) (2018) — 1 samples

**Your finding** — fill in, then run `python scripts/apply_review_findings.py`:

```finding
host: Co-La-O
decision:        # confirm | change | split | unresolved
prototype:       # for change: the prototype id it should be
spacegroup:      # number the paper reports, e.g. 212
mp_id:           # if you have it
evidence:        # DOI you read this from
notes:
```

---

## Se-Sn — 287 samples, chunk 1

**Assigned** `layered_ges` (high confidence)

**Needs checking because:**
- transition at ~800 K is a taxonomy default, not read from a paper
- structure reference cannot separate two polymorphs

**What to look for:**
- Whether the paper reports a structural transition, and at what temperature. Look for DSC, high-temperature XRD, or a kink discussed in the text. Record the temperature, or "none" if the paper shows the sample staying in one phase across its range.
- Which polymorph was actually made. Look for the reported space group or lattice parameters in the experimental section. Record the space group number, or the mp_id if you have it.

> SnSe (108) is orthorhombic Pnma and converts to Cmcm near 800 K, inside the measured window and where the record ZT is reported. SnSe2 (5) is a 1T dichalcogenide, a different compound.

**`SnSe`** — 108 samples, 49 papers
- [Understanding of the Extremely Low Thermal Conductivity in High-Performance Polycrystalline SnS...](https://doi.org/10.1002/adfm.201602652) (2016) — 7 samples
- [Ultrahigh power factor and thermoelectric performance in hole-doped single-crystal SnSe](https://doi.org/10.1126/science.aad3749) (2015) — 6 samples
- [Realizing High Figure of Merit in Phase-Separated Polycrystalline Sn1–xPbxSe](https://doi.org/10.1021/jacs.6b07010) (2016) — 5 samples

**`Na0.03Sn0.965Se`** — 12 samples, 1 papers
- [Polycrystalline SnSe with a thermoelectric figure of merit greater than the single crystal](https://doi.org/10.1038/s41563-021-01064-6) (2021) — 12 samples

**`Ag0.01Sn0.99Se`** — 7 samples, 2 papers
- [Thermoelectric properties of p-type polycrystalline SnSe doped with Ag](https://doi.org/10.1039/c4ta01643b) (2014) — 6 samples
- [Realizing High Figure of Merit in Phase-Separated Polycrystalline Sn1–xPbxSe](https://doi.org/10.1021/jacs.6b07010) (2016) — 1 samples

**`SnSe2`** — 5 samples, 4 papers
- [Interface tuning charge transport and enhanced thermoelectric properties in flower-like SnSe2 h...](https://doi.org/10.1016/j.apsusc.2020.145478) (2020) — 2 samples
- [Cu Intercalation and Br Doping to Thermoelectric SnSe\n            2\n            Lead to Ultra...](https://doi.org/10.1002/adfm.201908405) (2019) — 1 samples
- [Phase structure, phase transition and thermoelectric properties of pristine and Br doped SnSe2](https://doi.org/10.1016/j.jssc.2020.121468) (2020) — 1 samples

**Your finding** — fill in, then run `python scripts/apply_review_findings.py`:

```finding
host: Se-Sn
decision:        # confirm | change | split | unresolved
prototype:       # for change: the prototype id it should be
split:           # for split: one "composition -> prototype_id" per line
  # Ca3Co4O9 -> misfit_cobaltite
  # Ca3Co2O6 -> ca3co2o6_chain
spacegroup:      # number the paper reports, e.g. 212
mp_id:           # if you have it
transition_K:    # temperature, or "none"
evidence:        # DOI you read this from
notes:
```

---

## Cu-Se — 277 samples, chunk 1

**Assigned** `cu2se_superionic` (high confidence)

**Needs checking because:**
- transition at ~400 K is a taxonomy default, not read from a paper
- structure reference cannot separate two polymorphs

**What to look for:**
- Whether the paper reports a structural transition, and at what temperature. Look for DSC, high-temperature XRD, or a kink discussed in the text. Record the temperature, or "none" if the paper shows the sample staying in one phase across its range.
- Which polymorph was actually made. Look for the reported space group or lattice parameters in the experimental section. Record the space group number, or the mp_id if you have it.

> Cu2-xSe (75) superionic conductor. The ordered low-temperature superstructure converts to the cubic superionic phase near 400 K, inside the measured window. Cu deficiency, not a foreign element, is the carrier knob.

**`Cu2Se`** — 75 samples, 47 papers
- [The unstable thermoelectric effect in non-stoichiometric Cu2Se during the non-equilibrium phase...](https://doi.org/10.1007/s10853-021-06170-z) (2021) — 11 samples
- [Enhanced thermoelectric and mechanical properties in hierarchical tubular porous cuprous selenide](https://doi.org/10.1016/j.scriptamat.2019.09.009) (2020) — 6 samples
- [Thermoelectric performance of Cu2Se bulk materials by high-temperature and high-pressure synthesis](https://doi.org/10.1016/j.jmat.2018.12.002) (2019) — 5 samples

**`Cu1.98Se`** — 15 samples, 7 papers
- [Effects of Pb doping on the electrical transport performance of Cu1.98Se](https://doi.org/10.1007/s10853-019-04242-9) (2019) — 5 samples
- [Conventional sintered Cu2-Se thermoelectric material](https://doi.org/10.1016/j.jmat.2019.06.005) (2019) — 3 samples
- [Copper ion liquid-like thermoelectrics](https://doi.org/10.1038/nmat3273) (2012) — 2 samples

**`Cu1.97Se`** — 11 samples, 4 papers
- [Thermal stability study of Cu1.97Se superionic thermoelectric materials](https://doi.org/10.1039/d0tc01085e) (2020) — 6 samples
- [Conventional sintered Cu2-Se thermoelectric material](https://doi.org/10.1016/j.jmat.2019.06.005) (2019) — 3 samples
- [Off-stoichiometry effects on the thermoelectric properties of Cu2+δSe (−0.1 ≤ δ ≤ 0.05) compoun...](https://doi.org/10.1039/c9ce01651a) (2020) — 1 samples

**`Cu2Se1.01`** — 8 samples, 2 papers
- [Thermoelectric properties of copper selenide with ordered selenium layer and disordered copper ...](https://doi.org/10.1016/j.nanoen.2012.02.010) (2012) — 4 samples
- [A review on the enhancement of figure of merit from bulk to nano-thermoelectric materials](https://doi.org/10.1016/j.nanoen.2012.10.005) (2013) — 4 samples

**Your finding** — fill in, then run `python scripts/apply_review_findings.py`:

```finding
host: Cu-Se
decision:        # confirm | change | split | unresolved
prototype:       # for change: the prototype id it should be
spacegroup:      # number the paper reports, e.g. 212
mp_id:           # if you have it
transition_K:    # temperature, or "none"
evidence:        # DOI you read this from
notes:
```

---

## Co-O-Sr — 246 samples, chunk 1

**Assigned** `perovskite` (medium confidence)

**Needs checking because:**
- medium confidence

**What to look for:**
- Any explicit structure statement -- space group, prototype name, or the reference structure the authors index against. Record confirm, or the prototype it should be.

> SrCoO3-delta (20) perovskite with heavy oxygen non-stoichiometry. Sr6Co5O15 (10) is a 1D chain phase of the Ca3Co2O6 family, and oxygen-poor members order into brownmillerite.

**`SrCoO3`** — 20 samples, 17 papers
- [Anomalous Hall effect and spin fluctuations in ionic liquid gated \n<mml:math xmlns:mml=\"http:...](https://doi.org/10.1103/physrevb.97.184433) (2018) — 3 samples
- [Relationship between transport properties and phase transformations in mixed-conducting oxides](https://doi.org/10.1016/j.jssc.2005.10.027) (2006) — 2 samples
- [Phosphorus‐Doped Perovskite Oxide as Highly Efficient Water Oxidation Electrocatalyst in Alkali...](https://doi.org/10.1002/adfm.201601902) (2016) — 1 samples

**`SrCo0.9Nb0.1O3`** — 13 samples, 8 papers
- [Bulk Properties of the Oxygen Reduction Catalyst SrCo<sub>0.9</sub>Nb<sub>0.1</sub>O<sub>3−δ</sub>](https://doi.org/10.1021/acs.chemmater.5b04783) (2016) — 5 samples
- [Systematic investigation on new SrCo1−yNbyO3−δ ceramic membranes with high oxygen semi-permeabi...](https://doi.org/10.1016/j.memsci.2008.07.002) (2008) — 2 samples
- [Suppression of multiple magnetic ordering induced by Nb and Ru substitution in SrCoO3-δ systems](https://doi.org/10.1016/j.jallcom.2021.159261) (2021) — 1 samples

**`SrCo0.8Fe0.2O3`** — 11 samples, 8 papers
- [Phase equilibrium and electrical conductivity of SrCo0.8Fe0.2O3−δ](https://doi.org/10.1016/j.jssc.2004.03.026) (2004) — 3 samples
- [Effect of La3+ doping on the perovskite-to-brownmillerite transformation in Sr1−xLaxCo0.8Fe0.2O...](https://doi.org/10.1016/j.ssi.2003.12.006) (2004) — 2 samples
- [Electrical conductivity and structural stability of SrCo1−xFexO3−δ](https://doi.org/10.1016/j.jpcs.2010.10.084) (2011) — 1 samples

**`Sr6Co5O15`** — 10 samples, 4 papers
- [Controlling independently the electric and thermal properties by shrinking the particle size do...](https://doi.org/10.1103/physrevb.82.085110) (2010) — 6 samples
- [Electrical resistivity and Seebeck coefficient of Sr6Co5O15](https://doi.org/10.1016/j.jallcom.2004.01.060) (2004) — 2 samples
- [A new thermoelectric misfit cobaltite: [Sr2CoO3][CoO2]1.8](https://doi.org/10.1016/j.solidstatesciences.2003.12.004) (2004) — 1 samples

**Your finding** — fill in, then run `python scripts/apply_review_findings.py`:

```finding
host: Co-O-Sr
decision:        # confirm | change | split | unresolved
prototype:       # for change: the prototype id it should be
split:           # for split: one "composition -> prototype_id" per line
  # Ca3Co4O9 -> misfit_cobaltite
  # Ca3Co2O6 -> ca3co2o6_chain
evidence:        # DOI you read this from
notes:
```

---

## Ag-Sb-Te — 206 samples, chunk 1

**Assigned** `rocksalt` (medium confidence)

**Needs checking because:**
- medium confidence

**What to look for:**
- Any explicit structure statement -- space group, prototype name, or the reference structure the authors index against. Record confirm, or the prototype it should be.

> AgSbTe2 (41) is a cation-disordered rocksalt: Ag and Sb share the cation site at random. Every ordered MP ternary sits above hull 0.65, which is the expected signature of a disordered phase rather than evidence against rocksalt.

**`AgSbTe2`** — 41 samples, 28 papers
- [Optimized thermoelectric properties of AgSbTe2 through adjustment of fabrication parameters](https://doi.org/10.1007/s13391-014-4152-0) (2015) — 6 samples
- [Analysis of the Influence of Thermal Treatment on the Stability of Ag1−xSb1+xTe2+x and Se-Doped...](https://doi.org/10.1007/s11664-015-4102-0) (2015) — 3 samples
- [Doping Effects on the Thermoelectric Properties of AgSbTe2](https://doi.org/10.1007/s11664-009-0669-7) (2009) — 3 samples

**`Ag0.366Sb0.56Te`** — 12 samples, 1 papers
- [Off-stoichiometric silver antimony telluride: An experimental study of transport properties wit...](https://doi.org/10.1063/1.4916217) (2015) — 12 samples

**`Ag0.9Sb1.1Te2.1`** — 9 samples, 2 papers
- [Thermal Stability and Tuning of Thermoelectric Properties of Ag1−xSb1+xTe2+x (0 ≤ x ≤ 0.4) Alloys](https://doi.org/10.3390/app8010052) (2018) — 8 samples
- [Improved thermoelectric properties of AgSbTe2 based compounds with nanoscale Ag2Te in situ prec...](https://doi.org/10.1016/j.jallcom.2010.03.170) (2010) — 1 samples

**`Ag0.81Sb1.19Te2.19`** — 4 samples, 2 papers
- [Thermal Stability and Tuning of Thermoelectric Properties of Ag1−xSb1+xTe2+x (0 ≤ x ≤ 0.4) Alloys](https://doi.org/10.3390/app8010052) (2018) — 3 samples
- [Improved thermoelectric properties of AgSbTe2 based compounds with nanoscale Ag2Te in situ prec...](https://doi.org/10.1016/j.jallcom.2010.03.170) (2010) — 1 samples

**Your finding** — fill in, then run `python scripts/apply_review_findings.py`:

```finding
host: Ag-Sb-Te
decision:        # confirm | change | split | unresolved
prototype:       # for change: the prototype id it should be
evidence:        # DOI you read this from
notes:
```

---

## Bi-Se — 202 samples, chunk 1

**Assigned** `tetradymite` (medium confidence)

**Needs checking because:**
- medium confidence

**What to look for:**
- Any explicit structure statement -- space group, prototype name, or the reference structure the authors index against. Record confirm, or the prototype it should be.

> Bi2Se3 (99) tetradymite R-3m. BiSe (7) is a member of the (Bi2)m(Bi2Se3)n homologous series. Note the MP dump ranks Pnma (mp-23164) lowest -- the same van der Waals artefact seen for Sb2Te3.

**`Bi2Se3`** — 99 samples, 43 papers
- [Thermoelectric power of n-type Bi2Se8 in strong transverse magnetic fields](https://doi.org/10.1002/pssb.2220570120) (1973) — 16 samples
- [Ambipolar Surface State Thermoelectric Power of Topological Insulator Bi2Se3](https://doi.org/10.1021/nl4032154) (2014) — 9 samples
- [Peculiarities of the electronic transport in topological materials of Bi<sub>2</sub>Se<sub>3</s...](https://doi.org/10.1088/1742-6596/1410/1/012199) (2019) — 7 samples

**`(Bi0.95Sb0.05)2Se3`** — 17 samples, 1 papers
- [Effect of heat treatment on the electrical and thermoelectric properties of Sb doped Bi2Se3](https://doi.org/10.1088/0031-8949/90/4/045802) (2015) — 17 samples

**`BiSe`** — 7 samples, 3 papers
- [Localized Vibrations of Bi Bilayer Leading to Ultralow Lattice Thermal Conductivity and High Th...](https://doi.org/10.1021/jacs.8b02691) (2018) — 3 samples
- [Bi8Se7: Delocalized Interlayer π-Bond Interactions Enhancing Carrier Mobility and Thermoelectri...](https://doi.org/10.1021/jacs.0c05904) (2020) — 2 samples
- [Enhanced thermoelectric performance of BiSe by Sn doping and ball milling](https://doi.org/10.1016/j.ceramint.2021.06.048) (2021) — 2 samples

**`(Bi2Se3)0.9(TiO2)0.1`** — 4 samples, 1 papers
- [Enhanced thermoelectric performance of Bi2Se3/TiO2 composite](https://doi.org/10.1007/s12598-020-01414-4) (2020) — 4 samples

**Your finding** — fill in, then run `python scripts/apply_review_findings.py`:

```finding
host: Bi-Se
decision:        # confirm | change | split | unresolved
prototype:       # for change: the prototype id it should be
split:           # for split: one "composition -> prototype_id" per line
  # Ca3Co4O9 -> misfit_cobaltite
  # Ca3Co2O6 -> ca3co2o6_chain
evidence:        # DOI you read this from
notes:
```

---

## O-V — 186 samples, chunk 1

**Assigned** `vo2_monoclinic` (low confidence)

**Needs checking because:**
- low confidence
- transition at ~340 K is a taxonomy default, not read from a paper
- structure reference cannot separate two polymorphs

**What to look for:**
- Any explicit structure statement -- space group, prototype name, or the reference structure the authors index against. Record confirm, or the prototype it should be.
- Whether the paper reports a structural transition, and at what temperature. Look for DSC, high-temperature XRD, or a kink discussed in the text. Record the temperature, or "none" if the paper shows the sample staying in one phase across its range.
- Which polymorph was actually made. Look for the reported space group or lattice parameters in the experimental section. Record the space group number, or the mp_id if you have it.

> Four or more structures: VO2 (86) monoclinic M1 converting to rutile at ~340 K, V2O3 (10) corundum, V7O13/V8O15/V6O11 Magneli shear phases, and SrV6O15 a vanadium bronze. Not resolvable as one prototype.

**`VO2`** — 86 samples, 30 papers
- [Optimization of the semiconductor-metal transition in VO<sub>2</sub> epitaxial thin films as a ...](https://doi.org/10.1063/1.4866806) (2014) — 7 samples
- [Tuning the properties of VO2 thin films through growth temperature for infrared and terahertz m...](https://doi.org/10.1063/1.4821846) (2013) — 7 samples
- [Terahertz transmission characteristics across the phase transition in VO2 films deposited on Si...](https://doi.org/10.1063/1.4746701) (2012) — 6 samples

**`V7O13`** — 13 samples, 2 papers
- [Physical properties ofV7O13single crystals](https://doi.org/10.1103/physrevb.25.1703) (1982) — 7 samples
- [Charge transport near pressure-induced antiferromagnetic quantum critical point in Magnéli-phas...](https://doi.org/10.1016/s0038-1098(02)00716-0) (2003) — 6 samples

**`V2O3`** — 10 samples, 4 papers
- [Thickness dependence of the electronic properties in V2O3 thin films](https://doi.org/10.1063/1.2824465) (2007) — 4 samples
- [Critical Pressure for the Metal-Semiconductor Transition in<mml:math xmlns:mml=\"http://www.w3....](https://doi.org/10.1103/physrevlett.22.887) (1969) — 3 samples
- [Magnetic anisotropy in the SDW state of metallic V2−yO3 observed by magnetotransport measuremen...](https://doi.org/10.1016/s0921-4526(96)00779-x) (1997) — 2 samples

**`V8O15`** — 8 samples, 1 papers
- [Charge transport near pressure-induced antiferromagnetic quantum critical point in Magnéli-phas...](https://doi.org/10.1016/s0038-1098(02)00716-0) (2003) — 8 samples

**Your finding** — fill in, then run `python scripts/apply_review_findings.py`:

```finding
host: O-V
decision:        # confirm | change | split | unresolved
prototype:       # for change: the prototype id it should be
split:           # for split: one "composition -> prototype_id" per line
  # Ca3Co4O9 -> misfit_cobaltite
  # Ca3Co2O6 -> ca3co2o6_chain
spacegroup:      # number the paper reports, e.g. 212
mp_id:           # if you have it
transition_K:    # temperature, or "none"
evidence:        # DOI you read this from
notes:
```

---

## Ca-La-Mn-O — 180 samples, chunk 1

**Assigned** `perovskite` (medium confidence)

**Needs checking because:**
- medium confidence

**What to look for:**
- Any explicit structure statement -- space group, prototype name, or the reference structure the authors index against. Record confirm, or the prototype it should be.

> La1-xCaxMnO3 (39) manganite perovskite, orthorhombic Pnma. The x=0.3 CMR composition dominates.

**`La0.7Ca0.3MnO3`** — 39 samples, 16 papers
- [Tailoring transport properties of phase-separated manganite films with ordered magnetic nanostr...](https://doi.org/10.1103/physrevb.94.064404) (2016) — 17 samples
- [La<sub>0.7</sub>Ca<sub>0.3</sub>MnO<sub>3</sub> / Mn<sub>3</sub>O<sub>4</sub> composites: Does ...](https://doi.org/10.1063/1.3694664) (2012) — 5 samples
- [Critical behavior of magnetoresistance near the metal–insulator transition of La0.7Ca0.3MnO3](https://doi.org/10.1016/s0304-8853(01)00847-2) (2002) — 2 samples

**`La0.67Ca0.33MnO3`** — 10 samples, 9 papers
- [Magnetization dynamics in La<sub>0.67</sub>Ca<sub>0.33</sub>MnO<sub>3</sub> epitaxial films pro...](https://doi.org/10.1063/1.4905262) (2015) — 2 samples
- [Charge-carrier density collapse in and epitaxial thin films](https://doi.org/10.1007/s100510051059) (2000) — 1 samples
- [Effects of V doping in La0.67Ca0.33MnO3: Resistivity, magnetization, thermoelectric power and t...](https://doi.org/10.1016/j.jallcom.2009.04.068) (2009) — 1 samples

**`La0.5Ca0.5MnO3`** — 9 samples, 7 papers
- [Influence of Te doping on the perovskite manganite La0.5Ca0.5MnO3](https://doi.org/10.1016/j.ssc.2006.04.021) (2006) — 3 samples
- [B-site bismuth doping effect on structural, magnetic and magnetotransport properties of La0.5Ca...](https://doi.org/10.1016/j.ceramint.2014.10.163) (2015) — 1 samples
- [Microstructural and magnetotransport properties of La1−xCaxMnO3 (0.45≤x≤0.60) thin films](https://doi.org/10.1016/j.jallcom.2012.03.111) (2012) — 1 samples

**`La0.625Ca0.375MnO3`** — 6 samples, 3 papers
- [Thermal and Electronic Transport Properties and Two-Phase Mixtures inLa5/8−xPrxCa3/8MnO3](https://doi.org/10.1103/physrevlett.84.2961) (2000) — 4 samples
- [Large temperature coefficient of resistivity (TCR) of La1-Ca MnO3 films prepared by spin-coatin...](https://doi.org/10.1016/j.jallcom.2021.161788) (2022) — 1 samples
- [Competition between coexisting phases in (La,Pr)CaMnO3 manganites](https://doi.org/10.1063/1.2786570) (2007) — 1 samples

**Your finding** — fill in, then run `python scripts/apply_review_findings.py`:

```finding
host: Ca-La-Mn-O
decision:        # confirm | change | split | unresolved
prototype:       # for change: the prototype id it should be
evidence:        # DOI you read this from
notes:
```

---

## Pb-Sn-Te — 176 samples, chunk 1

**Assigned** `rocksalt` (high confidence)

**Needs checking because:**
- structure reference cannot separate two polymorphs

**What to look for:**
- Which polymorph was actually made. Look for the reported space group or lattice parameters in the experimental section. Record the space group number, or the mp_id if you have it.

> Pb1-xSnxTe across the full range, rocksalt throughout. The band inversion near x=0.35-0.4 is electronic, not structural, so the prototype is unchanged across the series.

**`(Pb0.5Sn0.5Te)0.4955Te0.5045`** — 12 samples, 1 papers
- [High temperature thermoelectric properties evolution of Pb 1-x Sn x Te based alloys](https://doi.org/10.1016/j.jallcom.2017.06.075) (2017) — 12 samples

**`Pb0.6Sn0.4Te`** — 9 samples, 3 papers
- [Pressure-induced band cross-over in Pb1−x Sn x Te](https://doi.org/10.1007/bf02744293) (1987) — 7 samples
- [Tailoring of Electronic Structure and Thermoelectric Properties of a Topological Crystalline In...](https://doi.org/10.1002/anie.201508492) (2015) — 1 samples
- [Electronic structure modulation of Pb0.6Sn0.4Te via zinc doping and its effect on the thermoele...](https://doi.org/10.1016/j.jallcom.2021.159681) (2021) — 1 samples

**`Pb0.73Sn0.27Te`** — 6 samples, 1 papers
- [Increase in the thermoelectric power produced by mechanically alloyed Pb1−x Snx Te due to the p...](https://doi.org/10.1063/1.3651173) (2011) — 6 samples

**`Sn0.70Pb0.30Te`** — 5 samples, 1 papers
- [An enhanced Seebeck coefficient and high thermoelectric performance in p-type In and Mg co-dope...](https://doi.org/10.1039/c7tc00009j) (2017) — 5 samples

**Your finding** — fill in, then run `python scripts/apply_review_findings.py`:

```finding
host: Pb-Sn-Te
decision:        # confirm | change | split | unresolved
prototype:       # for change: the prototype id it should be
spacegroup:      # number the paper reports, e.g. 212
mp_id:           # if you have it
evidence:        # DOI you read this from
notes:
```

---

## Ba-Ga-Ge — 173 samples, chunk 2

**Assigned** `clathrate_i` (medium confidence)

**Needs checking because:**
- medium confidence

**What to look for:**
- Any explicit structure statement -- space group, prototype name, or the reference structure the authors index against. Record confirm, or the prototype it should be.

> Ba8Ga16Ge30 (82) type-I clathrate. Ga/Ge ratio on the framework sets the electron count and is not doping.

**`Ba8Ga16Ge30`** — 82 samples, 23 papers
- [Optimization of the thermoelectric properties of Ba8Ga16Ge30](https://doi.org/10.1063/1.2939438) (2008) — 18 samples
- [Estimating carrier relaxation times in the Ba8Ga16Ge30 clathrate in the extrinsic regime](https://doi.org/10.1039/c6cp08026j) (2017) — 11 samples
- [Large thermoelectric figure of merit at high temperature in Czochralski-grown clathrate Ba8Ga16...](https://doi.org/10.1063/1.2163979) (2006) — 9 samples

**`Ba24Ga12Ge88`** — 3 samples, 2 papers
- [High thermoelectric performance of type-III clathrate compounds of the Ba–Ge–Ga system](https://doi.org/10.1016/j.actamat.2005.12.032) (2006) — 2 samples
- [Thermoelectric properties and crystal structure of type-III clathrate compounds in the Ba–Al–Ge...](https://doi.org/10.1063/1.2768040) (2007) — 1 samples

**`Ba8Ga16Ge20`** — 3 samples, 1 papers
- [High temperature thermoelectric properties of Czochralski-pulled Ba8Ga16Ge30](https://doi.org/10.1109/ict.2006.331265) (2006) — 3 samples

**`Ba24Ga15Ge85`** — 2 samples, 1 papers
- [High thermoelectric performance of type-III clathrate compounds of the Ba–Ge–Ga system](https://doi.org/10.1016/j.actamat.2005.12.032) (2006) — 2 samples

**Your finding** — fill in, then run `python scripts/apply_review_findings.py`:

```finding
host: Ba-Ga-Ge
decision:        # confirm | change | split | unresolved
prototype:       # for change: the prototype id it should be
evidence:        # DOI you read this from
notes:
```

---

## Ge-Sb-Te — 173 samples, chunk 2

**Assigned** `gst_homologous` (high confidence)

**Needs checking because:**
- transition at ~420 K is a taxonomy default, not read from a paper

**What to look for:**
- Whether the paper reports a structural transition, and at what temperature. Look for DSC, high-temperature XRD, or a kink discussed in the text. Record the temperature, or "none" if the paper shows the sample staying in one phase across its range.

> Ge2Sb2Te5 (19) and the (GeTe)n(Sb2Te3)m series. The stable phase is layered; the quenched phase is a vacancy-ordered cubic rocksalt, and transport is often measured across that crystallisation.

**`Ge2Sb2Te5`** — 19 samples, 6 papers
- [Phase purity and the thermoelectric properties of Ge2Sb2Te5 films down to 25 nm thickness](https://doi.org/10.1063/1.4731252) (2012) — 8 samples
- [Electronic Properties of Amorphous and Crystalline Ge2Sb2Te5Films](https://doi.org/10.1143/jjap.44.7340) (2005) — 6 samples
- [Microstructures and thermoelectric properties of GeSbTe based layered compounds](https://doi.org/10.1007/s00339-007-4006-9) (2007) — 2 samples

**`(CoGe2)0.15(GeTe)12Sb2Te3`** — 6 samples, 2 papers
- [Cobalt germanide precipitates indirectly improve the properties of thermoelectric germanium ant...](https://doi.org/10.1039/c9tc03410b) (2019) — 4 samples
- [High Thermoelectric Figure of Merit Values of Germanium Antimony Tellurides with Kinetically St...](https://doi.org/10.1021/jacs.5b07856) (2015) — 2 samples

**`(CoGe2)0.2(GeTe)17Sb2Te3`** — 6 samples, 2 papers
- [Cobalt germanide precipitates indirectly improve the properties of thermoelectric germanium ant...](https://doi.org/10.1039/c9tc03410b) (2019) — 4 samples
- [High Thermoelectric Figure of Merit Values of Germanium Antimony Tellurides with Kinetically St...](https://doi.org/10.1021/jacs.5b07856) (2015) — 2 samples

**`(GeTe)12Sb2Te3`** — 6 samples, 2 papers
- [Cobalt germanide precipitates indirectly improve the properties of thermoelectric germanium ant...](https://doi.org/10.1039/c9tc03410b) (2019) — 4 samples
- [High Thermoelectric Figure of Merit Values of Germanium Antimony Tellurides with Kinetically St...](https://doi.org/10.1021/jacs.5b07856) (2015) — 2 samples

**Your finding** — fill in, then run `python scripts/apply_review_findings.py`:

```finding
host: Ge-Sb-Te
decision:        # confirm | change | split | unresolved
prototype:       # for change: the prototype id it should be
transition_K:    # temperature, or "none"
evidence:        # DOI you read this from
notes:
```

---

## In-O-Zn — 153 samples, chunk 2

**Assigned** `homologous_inmo3_zno` (medium confidence)

**Needs checking because:**
- medium confidence
- structure reference cannot separate two polymorphs

**What to look for:**
- Any explicit structure statement -- space group, prototype name, or the reference structure the authors index against. Record confirm, or the prototype it should be.
- Which polymorph was actually made. Look for the reported space group or lattice parameters in the experimental section. Record the space group number, or the mp_id if you have it.

> In2O3(ZnO)n natural superlattices, n set by the In:Zn ratio. Not a doped ZnO and not bixbyite In2O3.

**`(ZnO)5In2O3`** — 15 samples, 7 papers
- [Thermoelectric Properties of Homologous Compounds in the ZnO-In2O3 System](https://doi.org/10.1111/j.1151-2916.1996.tb08958.x) (1996) — 3 samples
- [Single crystal growth of homologous compounds in the ZnO-In/sub 2/O/sub 3/ system and thermoele...](https://doi.org/10.1109/ict.2003.1287475) — 3 samples
- [Development of thick-film thermoelectric microgenerators based on p-type Ca3Co4O9 and n-type (Z...](https://doi.org/10.1016/j.ceramint.2015.07.097) (2015) — 3 samples

**`In2O3(ZnO)5`** — 14 samples, 4 papers
- [Ni metal coating boosting the thermoelectric performance of In2O3(ZnO)5 ceramics](https://doi.org/10.1016/j.scriptamat.2019.01.039) (2019) — 5 samples
- [Enhanced thermoelectric properties of In<sub>2</sub>O<sub>3</sub>(ZnO)<sub>5</sub> intrinsic su...](https://doi.org/10.1039/c7ra06267b) (2017) — 4 samples
- [Formation of homologous In2O3(ZnO)m thin films and its thermoelectric properties](https://doi.org/10.1116/1.4953032) (2016) — 4 samples

**`(In2O3)70.99(ZnO)29.01`** — 13 samples, 1 papers
- [Electron-phonon scattering in amorphous In2O3–ZnO films](https://doi.org/10.1063/1.2936316) (2008) — 13 samples

**`(ZnO)7In2O3`** — 8 samples, 3 papers
- [A study of electrodes for thermoelectric oxides](https://doi.org/10.1007/s13391-013-0025-1) (2013) — 4 samples
- [Thermoelectric Properties of Homologous Compounds in the ZnO-In2O3 System](https://doi.org/10.1111/j.1151-2916.1996.tb08958.x) (1996) — 3 samples
- [Improvement in thermoelectric properties of (ZnO)5In2O3 through partial substitution of yttrium...](https://doi.org/10.1557/jmr.1998.0067) (1998) — 1 samples

**Your finding** — fill in, then run `python scripts/apply_review_findings.py`:

```finding
host: In-O-Zn
decision:        # confirm | change | split | unresolved
prototype:       # for change: the prototype id it should be
spacegroup:      # number the paper reports, e.g. 212
mp_id:           # if you have it
evidence:        # DOI you read this from
notes:
```

---

## In-Se — 145 samples, chunk 2

**Assigned** `in4se3` (high confidence)

**Needs checking because:**
- taxonomy issue recorded

**What to look for:**
- Whether the taxonomy entry itself is wrong or incomplete, rather than the assignment. Record what should change in the prototype.

> In4Se3 (29) dominates the host and is a distinct mixed-valence phase built from (In3)5+ cluster chains, not a layered In2Se3 polytype. InSe (5) and In2Se3 (3) are the layered members.

**`In4Se3`** — 29 samples, 15 papers
- [Preparation and Thermoelectric Transport of Polycrystalline In$lt;inf$gt;4$lt;/inf$gt;Se$lt;inf...](https://doi.org/10.15541/jim20140396) (2015) — 7 samples
- [Microstructures and Thermoelectric Properties of Spark Plasma Sintered In4Se3](https://doi.org/10.3365/eml.2010.09.117) (2010) — 4 samples
- [Effect of Forming Process on Microstructure and Thermoelectric Properties of In4se3 Compound](https://doi.org/10.1016/j.proeng.2011.12.439) (2012) — 3 samples

**`In4Se2.35`** — 7 samples, 5 papers
- [Peierls distortion as a route to high thermoelectric performance in In4Se3-δ crystals](https://doi.org/10.1038/nature08088) (2009) — 3 samples
- [Thermoelectric Properties of Indium-Selenium Nanocomposites Prepared by Mechanical Alloying and...](https://doi.org/10.1007/s11664-012-1940-x) (2012) — 1 samples
- [Preparation and Thermoelectric Properties of Polycrystalline In4Sn3−x by Mechanical Alloying an...](https://doi.org/10.1007/s11664-012-1948-2) (2012) — 1 samples

**`InSe`** — 5 samples, 4 papers
- [Enhanced thermoelectric transport properties of n-type InSe due to the emergence of the flat ba...](https://doi.org/10.1039/c9qi00210c) (2019) — 2 samples
- [Optical and low-temperature thermoelectric properties of phase-pure p-type InSe thin films](https://doi.org/10.1007/s00339-015-9237-6) (2015) — 1 samples
- [Thermoelectric Properties of Indium-Selenium Nanocomposites Prepared by Mechanical Alloying and...](https://doi.org/10.1007/s11664-012-1940-x) (2012) — 1 samples

**`In4Se2.5`** — 4 samples, 4 papers
- [Enhancement of the Thermoelectric Performance of Polycrystalline In4Se2.5by Copper Intercalatio...](https://doi.org/10.1002/aenm.201300599) (2013) — 1 samples
- [Multiple heteroatom induced carrier engineering and hierarchical nanostructures for high thermo...](https://doi.org/10.1039/c4ta05508j) (2015) — 1 samples
- [Thermoelectric properties and anisotropic electronic band structure on the In4Se3−x compounds](https://doi.org/10.1063/1.3266579) (2009) — 1 samples

**Your finding** — fill in, then run `python scripts/apply_review_findings.py`:

```finding
host: In-Se
decision:        # confirm | change | split | unresolved
prototype:       # for change: the prototype id it should be
split:           # for split: one "composition -> prototype_id" per line
  # Ca3Co4O9 -> misfit_cobaltite
  # Ca3Co2O6 -> ca3co2o6_chain
evidence:        # DOI you read this from
notes:
```

---

## Bi-Mg-Sb — 140 samples, chunk 2

**Assigned** `caal2si2_zintl` (high confidence)

**Needs checking because:**
- structure reference cannot separate two polymorphs

**What to look for:**
- Which polymorph was actually made. Look for the reported space group or lattice parameters in the experimental section. Record the space group number, or the mp_id if you have it.

> Mg3(Sb,Bi)2 CaAl2Si2-type Zintl, mp-2646. Te on the anion site and excess Mg are the n-type routes.

**`Mg3.2Sb1.5Bi0.49Te0.01`** — 13 samples, 6 papers
- [Defect Engineering for Realizing High Thermoelectric Performance in n-Type Mg3Sb2-Based Materials](https://doi.org/10.1021/acsenergylett.7b00742) (2017) — 5 samples
- [Tuning the carrier scattering mechanism to effectively improve the thermoelectric properties](https://doi.org/10.1039/c7ee00098g) (2017) — 3 samples
- [Enhancement of average thermoelectric figure of merit by increasing the grain-size of Mg3.2Sb1....](https://doi.org/10.1063/1.5016488) (2018) — 2 samples

**`Mg3.032Y0.018SbBi`** — 4 samples, 1 papers
- [Extraordinary n‐Type Mg\n            3\n            SbBi Thermoelectrics Enabled by Yttrium Doping](https://doi.org/10.1002/adma.201903387) (2019) — 4 samples

**`Mg3.047Y0.003SbBi`** — 4 samples, 1 papers
- [Extraordinary n‐Type Mg\n            3\n            SbBi Thermoelectrics Enabled by Yttrium Doping](https://doi.org/10.1002/adma.201903387) (2019) — 4 samples

**`Mg3.1Sb1.5Bi0.49Te0.01`** — 4 samples, 1 papers
- [Scalable synthesis of n-type Mg3Sb2-xBix for thermoelectric applications](https://doi.org/10.1016/j.mtphys.2020.100336) (2021) — 4 samples

**Your finding** — fill in, then run `python scripts/apply_review_findings.py`:

```finding
host: Bi-Mg-Sb
decision:        # confirm | change | split | unresolved
prototype:       # for change: the prototype id it should be
spacegroup:      # number the paper reports, e.g. 212
mp_id:           # if you have it
evidence:        # DOI you read this from
notes:
```

---

## Fe-O — 129 samples, chunk 2

**Assigned** `spinel` (high confidence)

**Needs checking because:**
- reference disagreement recorded

**What to look for:**
- Which polymorph was actually made. Look for the reported space group or lattice parameters in the experimental section. Record the space group number, or the mp_id if you have it.

> Fe3O4 (48) magnetite is spinel Fd-3m; Fe2O3 (15) hematite is corundum R-3c. Two distinct oxides sharing a host.

**`Fe3O4`** — 48 samples, 14 papers
- [Thermoelectric property of Fe3O4 thin films grown onto the SiO2 (250nm)/Si and c-Al2O3 (0001) s...](https://doi.org/10.1016/j.snb.2014.08.005) (2014) — 29 samples
- [Thermal Conductivity of MgO,Al2O3, MgAl2O4, andFe3O4Crystals from 3° to 300°K](https://doi.org/10.1103/physrev.126.427) (1962) — 5 samples
- [Anomalous Nernst effect ofFe3O4single crystal](https://doi.org/10.1103/physrevb.90.054422) (2014) — 2 samples

**`Fe2O3`** — 15 samples, 9 papers
- [Thermoelectric properties of magnetite at the Verwey transition](https://doi.org/10.1103/physrevb.14.1401) (1976) — 5 samples
- [High-pressure cycling of hematiteα-Fe2O3: Nanostructuring,in situelectronic transport, and poss...](https://doi.org/10.1103/physrevb.86.205131) (2012) — 2 samples
- [Thermoelectric properties of P-doped and V-doped Fe2O3for renewable energy conversion](https://doi.org/10.1002/er.3052) (2013) — 2 samples

**`(Fe0.97Ti0.03)2O3`** — 1 samples, 1 papers
- [Thermoelectric properties of Ti- and Sn-doped α-Fe2O3](https://doi.org/10.1016/s0925-8388(01)01804-7) (2002) — 1 samples

**`(Fe0.98Sn0.02)2O3`** — 1 samples, 1 papers
- [Thermoelectric properties of Ti- and Sn-doped α-Fe2O3](https://doi.org/10.1016/s0925-8388(01)01804-7) (2002) — 1 samples

**Your finding** — fill in, then run `python scripts/apply_review_findings.py`:

```finding
host: Fe-O
decision:        # confirm | change | split | unresolved
prototype:       # for change: the prototype id it should be
split:           # for split: one "composition -> prototype_id" per line
  # Ca3Co4O9 -> misfit_cobaltite
  # Ca3Co2O6 -> ca3co2o6_chain
spacegroup:      # number the paper reports, e.g. 212
mp_id:           # if you have it
evidence:        # DOI you read this from
notes:
```

---

## B — 124 samples, chunk 2

**Assigned** `boron_carbide` (medium confidence)

**Needs checking because:**
- medium confidence

**What to look for:**
- Any explicit structure statement -- space group, prototype name, or the reference structure the authors index against. Record confirm, or the prototype it should be.

> Mixed boron-rich solids: beta-rhombohedral boron (B, B105), metal-doped B105 (V1.5B105, Co1.0B105) and YB66 (13), which is a distinct cubic Fm-3c structure with B12 icosahedra, not the B4C type.

**`YB66`** — 13 samples, 7 papers
- [Effect of transition metal doping and carbon doping on thermoelectric properties of YB66 single...](https://doi.org/10.1016/j.jssc.2006.01.064) (2006) — 4 samples
- [Specific heat and thermal conductivity of amorphous boron](https://doi.org/10.1063/1.40852) (1991) — 3 samples
- [Thermal Conductivity of Boron and Some Boron Compounds](https://doi.org/10.1103/physrevb.4.1714) (1971) — 2 samples

**`B`** — 11 samples, 8 papers
- [Thermoelectric Properties of Boron and Boron Phosphide CVD Wafers](https://doi.org/10.1006/jssc.1997.7493) (1997) — 2 samples
- [Seebeck Coefficient and Power Factor of Single-Crystalline Boron Nanobelts](https://doi.org/10.1143/apex.4.041201) (2011) — 2 samples
- [Effects of Metal Doping on Thermoelectric Properties of Arc-Melted and Hot-Pressed &beta;-Rhomb...](https://doi.org/10.2320/matertrans.e-mra2007890) (2008) — 2 samples

**`V1.5B105`** — 4 samples, 2 papers
- [Effects of Metal Doping on Thermoelectric Properties of Arc-Melted and Hot-Pressed &beta;-Rhomb...](https://doi.org/10.2320/matertrans.e-mra2007890) (2008) — 2 samples
- [Thermoelectric properties from 353K to 1073K for metal-doped β-rhombohedral boron](https://doi.org/10.1109/ict.2003.1287514) — 2 samples

**`B105`** — 3 samples, 2 papers
- [Thermoelectric properties from 353K to 1073K for metal-doped β-rhombohedral boron](https://doi.org/10.1109/ict.2003.1287514) — 2 samples
- [Structure and electronic properties of Mg-dopedβ-rhombohedral boron constructed from icosahedra...](https://doi.org/10.1103/physrevb.77.024515) (2008) — 1 samples

**Your finding** — fill in, then run `python scripts/apply_review_findings.py`:

```finding
host: B
decision:        # confirm | change | split | unresolved
prototype:       # for change: the prototype id it should be
split:           # for split: one "composition -> prototype_id" per line
  # Ca3Co4O9 -> misfit_cobaltite
  # Ca3Co2O6 -> ca3co2o6_chain
evidence:        # DOI you read this from
notes:
```

---

## Fe-La-O-Sr — 122 samples, chunk 2

**Assigned** `perovskite` (high confidence)

**Needs checking because:**
- structure reference cannot separate two polymorphs

**What to look for:**
- Which polymorph was actually made. Look for the reported space group or lattice parameters in the experimental section. Record the space group number, or the mp_id if you have it.

> La0.6Sr0.4Co0.2Fe0.8O3 (LSCF, 26) and La1-xSrxFeO3 perovskites with heavy oxygen non-stoichiometry.

**`La0.6Sr0.4Co0.2Fe0.8O3`** — 26 samples, 16 papers
- [Electrical Property, Crystal Structure and Oxygen Nonstoichiometry of La&lt;sub&gt;1-&lt;/sub&g...](https://doi.org/10.5796/electrochemistry.68.515) (2000) — 5 samples
- [Significant effects of sintering temperature on the performance of La0.6Sr0.4Co0.2Fe0.8O3−δ oxy...](https://doi.org/10.1016/j.memsci.2007.06.047) (2007) — 4 samples
- [Synthesis and Characterization of La[sub 0.6]Sr[sub 0.4]Co[sub 0.2]Fe[sub 0.8]O[sub 3−δ] and Ba...](https://doi.org/10.1149/1.2960873) (2008) — 2 samples

**`La0.6Sr0.4FeO3`** — 12 samples, 10 papers
- [Electrical Properties of La<sub>0.6</sub>Sr<sub>0.4</sub>Co<sub>1–<i>y</i></sub>Fe<sub><i>y</i>...](https://doi.org/10.1021/acs.jpcc.5b09696) (2015) — 2 samples
- [Doping Effects of Pentavalent Metal Ions (Nb<sup>5+</sup> or Ta<sup>5+</sup>) on the Redox Stab...](https://doi.org/10.1002/bkcs.12068) (2020) — 2 samples
- [Structure and mixed electronic-ionic conducting properties of La0.6Sr0.4Co1−y Fe y O3(y=0−1.0) ...](https://doi.org/10.1007/s11595-006-1080-3) (2008) — 1 samples

**`La0.5Sr0.5Al0.2Fe0.8O3`** — 11 samples, 3 papers
- [Grain size dependent electrical conductivity, chemical surface exchange and bulk diffusion coef...](https://doi.org/10.1016/j.jallcom.2019.152831) (2020) — 8 samples
- [Effect of B-site substitution on the crystal structure, electrical conductivity and oxygen tran...](https://doi.org/10.1016/j.jssc.2020.121237) (2020) — 2 samples
- [Electrical transport behavior of La0.5Sr0.5Co0.2-xAlxFe0.8O3-δ (x = 0–0.2) perovskite oxides](https://doi.org/10.1007/s11581-021-04168-w) (2021) — 1 samples

**`La0.4Sr0.6Co0.2Fe0.8O3`** — 4 samples, 3 papers
- [Structural and electrical properties of selected La1−xSrxCo0.2Fe0.8O3 and La0.6Sr0.4Co0.2Fe0.6N...](https://doi.org/10.1016/j.jpowsour.2007.05.052) (2007) — 2 samples
- [Electrochemical Properties of Mixed Conducting Perovskites La1 − x  M  x Co1 − y Fe y  O 3 − δ ...](https://doi.org/10.1149/1.1837098) (1996) — 1 samples
- [Electrical Property, Crystal Structure and Oxygen Nonstoichiometry of La&lt;sub&gt;1-&lt;/sub&g...](https://doi.org/10.5796/electrochemistry.68.515) (2000) — 1 samples

**Your finding** — fill in, then run `python scripts/apply_review_findings.py`:

```finding
host: Fe-La-O-Sr
decision:        # confirm | change | split | unresolved
prototype:       # for change: the prototype id it should be
spacegroup:      # number the paper reports, e.g. 212
mp_id:           # if you have it
evidence:        # DOI you read this from
notes:
```

---

## Bi-O-Se — 108 samples, chunk 2

**Assigned** `bi2o2se_layered` (medium confidence)

**Needs checking because:**
- medium confidence

**What to look for:**
- Any explicit structure statement -- space group, prototype name, or the reference structure the authors index against. Record confirm, or the prototype it should be.

> Bi2O2Se (37). Bi2O2 fluorite-like layers alternating with Se; distinct from the ZrCuSiAs type, which has an additional metal layer.

**`Bi2O2Se`** — 37 samples, 17 papers
- [Boosting the thermoelectric performance of Bi\n            2\n            O\n            2\n   ...](https://doi.org/10.1111/jace.15720) (2018) — 5 samples
- [Enhanced Thermoelectric Performance in n-Type Bi2O2Se by an Exquisite Grain Boundary Engineerin...](https://doi.org/10.1021/acsaem.1c02219) (2021) — 5 samples
- [Optimization of the thermoelectric properties of Bi2O2Se ceramics by altering the temperature o...](https://doi.org/10.1007/s10832-016-0038-x) (2016) — 5 samples

**`Bi1.92La0.08O2Se`** — 5 samples, 1 papers
- [Boosting the thermoelectric performance of Bi\n            2\n            O\n            2\n   ...](https://doi.org/10.1111/jace.15720) (2018) — 5 samples

**`Bi1.94La0.06O2Se`** — 5 samples, 1 papers
- [Boosting the thermoelectric performance of Bi\n            2\n            O\n            2\n   ...](https://doi.org/10.1111/jace.15720) (2018) — 5 samples

**`Bi1.96La0.04O2Se`** — 5 samples, 1 papers
- [Boosting the thermoelectric performance of Bi\n            2\n            O\n            2\n   ...](https://doi.org/10.1111/jace.15720) (2018) — 5 samples

**Your finding** — fill in, then run `python scripts/apply_review_findings.py`:

```finding
host: Bi-O-Se
decision:        # confirm | change | split | unresolved
prototype:       # for change: the prototype id it should be
evidence:        # DOI you read this from
notes:
```

---

## Co-La-O-Sr — 107 samples, chunk 2

**Assigned** `perovskite` (medium confidence)

**Needs checking because:**
- medium confidence

**What to look for:**
- Any explicit structure statement -- space group, prototype name, or the reference structure the authors index against. Record confirm, or the prototype it should be.

> La1-xSrxCoO3 (22) rhombohedral perovskite; the Sr content at x=0.4 is alloying-level A-site substitution.

**`La0.6Sr0.4CoO3`** — 22 samples, 13 papers
- [Deposition and Electrical and Structural Properties of La0.6Sr0.4CoO3 Thin Films for Applicatio...](https://doi.org/10.1007/s11664-019-07372-7) (2019) — 7 samples
- [Electrical and electrochemical characteristics of La0.6Sr0.4CoO3-δ cathode materials synthesize...](https://doi.org/10.1007/s10971-018-4675-1) (2018) — 3 samples
- [Synthesis and properties of La0.6Sr0.4CoO3−δ nanopowder](https://doi.org/10.1016/j.jpowsour.2008.09.021) (2008) — 2 samples

**`La0.6Sr0.4Co0.8Fe0.2O3`** — 19 samples, 8 papers
- [Citrate method synthesis, characterization and mixed electronic–ionic conduction properties of ...](https://doi.org/10.1016/j.scriptamat.2003.09.008) (2004) — 7 samples
- [Influence of sintering temperature on microstructure and mixed electronic–ionic conduction prop...](https://doi.org/10.1016/s0272-8842(03)00127-5) (2004) — 4 samples
- [Electrical Properties of La<sub>0.6</sub>Sr<sub>0.4</sub>Co<sub>1–<i>y</i></sub>Fe<sub><i>y</i>...](https://doi.org/10.1021/acs.jpcc.5b09696) (2015) — 2 samples

**`La0.7Sr0.3CoO3`** — 18 samples, 9 papers
- [Determining the Oxygen Stoichiometry of Cobaltite Thin Films](https://doi.org/10.1021/acs.chemmater.1c03338) (2022) — 7 samples
- [Thermoelectric and magnetic properties of nanocrystalline La0.7Sr0.3CoO3](https://doi.org/10.1063/1.3699038) (2012) — 3 samples
- [Transport and Magnetic Properties of R1-xAxCoO3(R = La, Pr and Nd; A = Ba, Sr and Ca)](https://doi.org/10.1143/jpsj.72.873) (2003) — 2 samples

**`La0.5Sr0.5CoO3`** — 9 samples, 8 papers
- [Transport and Magnetic Properties of R1-xAxCoO3(R = La, Pr and Nd; A = Ba, Sr and Ca)](https://doi.org/10.1143/jpsj.72.873) (2003) — 2 samples
- [Properties of oxides for high temperature solid electrolyte fuel cell](https://doi.org/10.1016/0167-2738(83)90122-4) (1983) — 1 samples
- [Doping- and Strain-Dependent Electrolyte-Gate-Induced Perovskite to Brownmillerite Transformati...](https://doi.org/10.1021/acsami.1c13828) (2021) — 1 samples

**Your finding** — fill in, then run `python scripts/apply_review_findings.py`:

```finding
host: Co-La-O-Sr
decision:        # confirm | change | split | unresolved
prototype:       # for change: the prototype id it should be
evidence:        # DOI you read this from
notes:
```

---

## O-W — 103 samples, chunk 2

**Assigned** `reo3_wo3` (high confidence)

**Needs checking because:**
- transition at ~290 K is a taxonomy default, not read from a paper
- taxonomy issue recorded

**What to look for:**
- Whether the paper reports a structural transition, and at what temperature. Look for DSC, high-temperature XRD, or a kink discussed in the text. Record the temperature, or "none" if the paper shows the sample staying in one phase across its range.
- Whether the taxonomy entry itself is wrong or incomplete, rather than the assignment. Record what should change in the prototype.

> WO3 (15) plus oxygen-deficient WO3-x. The measured 49-1100 K range crosses three steps of the WO3 tilt-distortion series, so no single space group describes these samples: gamma P2_1/n at room temperature, beta Pbcn above ~603 K, alpha P4/ncc above ~1013 K.

**`WO3`** — 15 samples, 12 papers
- [Thermoelectric properties of Bi2O3-added WO3 ceramics](https://doi.org/10.1016/j.ceramint.2018.09.151) (2019) — 3 samples
- [Photo-controllable thermoelectric properties with reversibility and photo-thermoelectric effect...](https://doi.org/10.1063/1.4900852) (2014) — 2 samples
- [Thermoelectric properties of WO3-based ceramics doped with Co2O3](https://doi.org/10.1007/s10854-011-0574-8) (2011) — 1 samples

**`WO2.90`** — 11 samples, 4 papers
- [SPS-assisted preparation of the Magnéli phase WO2.90 for thermoelectric applications](https://doi.org/10.1039/c3ta12145c) (2013) — 7 samples
- [Towards higher zT in early transition metal oxides: optimizing the charge carrier concentration...](https://doi.org/10.1016/j.matpr.2017.12.271) (2018) — 2 samples
- [Using crystallographic shear to reduce lattice thermal conductivity: high temperature thermoele...](https://doi.org/10.1039/c3cp52361f) (2013) — 1 samples

**`W0.95Ti0.05O3`** — 6 samples, 1 papers
- [The disordering effect of Ti observed in the microstructure and electrical properties of W0.95T...](https://doi.org/10.1063/1.3496473) (2010) — 6 samples

**`WO2.9`** — 5 samples, 3 papers
- [Unconventional Transport Properties of Reduced Tungsten Oxide WO2.9](https://doi.org/10.3390/condmat5040063) (2020) — 4 samples
- [Spark Plasma Sintering of Tungsten Oxides WOx (2.50 ≤ x ≤ 3): Phase Analysis and Thermoelectric...](https://doi.org/10.3390/cryst7090271) (2017) — 1 samples

**Your finding** — fill in, then run `python scripts/apply_review_findings.py`:

```finding
host: O-W
decision:        # confirm | change | split | unresolved
prototype:       # for change: the prototype id it should be
transition_K:    # temperature, or "none"
evidence:        # DOI you read this from
notes:
```

---

## Cu-S — 102 samples, chunk 2

**Assigned** `cu2se_superionic` (high confidence)

**Needs checking because:**
- transition at ~376 K is a taxonomy default, not read from a paper

**What to look for:**
- Whether the paper reports a structural transition, and at what temperature. Look for DSC, high-temperature XRD, or a kink discussed in the text. Record the temperature, or "none" if the paper shows the sample staying in one phase across its range.

> Cu2-xS (Cu2S, Cu1.97S, Cu1.8S) -- the sulfur analogue of Cu2Se, superionic above ~376 K. Cu deficiency spans chalcocite to digenite and is the carrier knob.

**`Cu1.8S`** — 13 samples, 9 papers
- [Synthesis and transport property of Cu1.8S as a promising thermoelectric compound](https://doi.org/10.1039/c1cc16368j) (2011) — 5 samples
- [Size effect of SiO2on enhancing thermoelectric properties of Cu1.8S](https://doi.org/10.1002/pssa.201330185) (2013) — 1 samples
- [Enhanced thermoelectric properties of Cu1.8Se1−xSx alloys prepared by mechanical alloying and s...](https://doi.org/10.1016/j.jallcom.2016.04.140) (2016) — 1 samples

**`Cu1.97S`** — 12 samples, 3 papers
- [High thermoelectric and mechanical performance in highly dense Cu2−xS bulks prepared by a melt-...](https://doi.org/10.1039/c5ta01667c) (2015) — 10 samples
- [High Thermoelectric Performance in Non-Toxic Earth-Abundant Copper Sulfide](https://doi.org/10.1002/adma.201400515) (2014) — 1 samples
- [Research Update: Cu–S based synthetic minerals as efficient thermoelectric materials at medium ...](https://doi.org/10.1063/1.4955398) (2016) — 1 samples

**`Cu2S`** — 12 samples, 5 papers
- [High thermoelectric and mechanical performance in highly dense Cu2−xS bulks prepared by a melt-...](https://doi.org/10.1039/c5ta01667c) (2015) — 8 samples
- [High Thermoelectric Performance in Non-Toxic Earth-Abundant Copper Sulfide](https://doi.org/10.1002/adma.201400515) (2014) — 1 samples
- [Electrical and thermoelectric properties of Cu2Se and Cu2S](https://doi.org/10.1016/0025-5408(81)90119-7) (1981) — 1 samples

**`(Cu2S)0.90(Cu5FeS4)0.10`** — 5 samples, 1 papers
- [Structural, thermoelectric and stability studies of Fe-doped copper sulfide](https://doi.org/10.1016/j.ssi.2020.115322) (2020) — 5 samples

**Your finding** — fill in, then run `python scripts/apply_review_findings.py`:

```finding
host: Cu-S
decision:        # confirm | change | split | unresolved
prototype:       # for change: the prototype id it should be
transition_K:    # temperature, or "none"
evidence:        # DOI you read this from
notes:
```

---

## Nb-O-Sr — 102 samples, chunk 2

**Assigned** `tungsten_bronze` (medium confidence)

**Needs checking because:**
- medium confidence
- structure reference cannot separate two polymorphs

**What to look for:**
- Any explicit structure statement -- space group, prototype name, or the reference structure the authors index against. Record confirm, or the prototype it should be.
- Which polymorph was actually made. Look for the reported space group or lattice parameters in the experimental section. Record the space group number, or the mp_id if you have it.

> Sr0.61Ba0.39Nb2O6 (26) is the SBN tetragonal tungsten bronze, not a perovskite. SrNbO3 (6) is a genuine perovskite and Sr2Nb2O7 a layered niobate -- three structures in one host.

**`Sr0.61Ba0.39Nb2O6`** — 26 samples, 4 papers
- [Effects of Oxygen-Reduction on Thermoelectric Properties of Sr<sub>0.61</sub>Ba<sub>0.39</sub>N...](https://doi.org/10.4028/www.scientific.net/msf.787.210) (2014) — 15 samples
- [SrxBa1−xNb2O6−δ Ferroelectric-thermoelectrics: Crystal anisotropy, conduction mechanism, and po...](https://doi.org/10.1063/1.3291563) (2010) — 6 samples
- [Thermoelectric power factor enhancement of textured ferroelectric Sr xBa1– x Nb2O6–δ ceramics](https://doi.org/10.1557/jmr.2010.78) (2011) — 4 samples

**`Sr5Nb5O17`** — 6 samples, 3 papers
- [Large anisotropic thermoelectricity in perovskite related layered structure: SrnNbnO3n+2 (n=4,5)](https://doi.org/10.1063/1.3510585) (2010) — 3 samples
- [Thermoelectric Responses in Layered Strontium-Niobates Via Two Ways of Charge Carrier Control T...](https://doi.org/10.1111/j.1551-2916.2012.05169.x) (2012) — 2 samples
- [Semiconducting large bandgap oxides as potential thermoelectric materials for high-temperature ...](https://doi.org/10.1007/s00339-014-8515-z) (2014) — 1 samples

**`SrNbO3`** — 6 samples, 2 papers
- [Electron transport and visible light absorption in a plasmonic photocatalyst based on strontium...](https://doi.org/10.1038/ncomms15070) (2017) — 5 samples
- [Intrinsic high electrical conductivity of stoichiometric<mml:math xmlns:mml=\"http://www.w3.org...](https://doi.org/10.1103/physrevb.92.205102) (2015) — 1 samples

**`Sr1.8La0.2Nb2O7`** — 5 samples, 3 papers
- [Large anisotropic thermoelectricity in perovskite related layered structure: SrnNbnO3n+2 (n=4,5)](https://doi.org/10.1063/1.3510585) (2010) — 3 samples
- [Semiconducting large bandgap oxides as potential thermoelectric materials for high-temperature ...](https://doi.org/10.1007/s00339-014-8515-z) (2014) — 1 samples
- [Thermoelectric Responses in Layered Strontium-Niobates Via Two Ways of Charge Carrier Control T...](https://doi.org/10.1111/j.1551-2916.2012.05169.x) (2012) — 1 samples

**Your finding** — fill in, then run `python scripts/apply_review_findings.py`:

```finding
host: Nb-O-Sr
decision:        # confirm | change | split | unresolved
prototype:       # for change: the prototype id it should be
split:           # for split: one "composition -> prototype_id" per line
  # Ca3Co4O9 -> misfit_cobaltite
  # Ca3Co2O6 -> ca3co2o6_chain
spacegroup:      # number the paper reports, e.g. 212
mp_id:           # if you have it
evidence:        # DOI you read this from
notes:
```

---

## Al-Cu-O — 99 samples, chunk 2

**Assigned** `delafossite` (high confidence)

**Needs checking because:**
- structure reference cannot separate two polymorphs

**What to look for:**
- Which polymorph was actually made. Look for the reported space group or lattice parameters in the experimental section. Record the space group number, or the mp_id if you have it.

> CuAlO2 (33) delafossite R-3m, the archetypal transparent p-type oxide. The Ca/Sr additions are at sub-percent level.

**`CuAlO2`** — 33 samples, 16 papers
- [Synergetic improvement strategy on thermoelectric performance of CuAlO2 compacts](https://doi.org/10.1016/j.ceramint.2018.12.004) (2019) — 6 samples
- [Fabrication of thermoelectric CuAlO2  and performance enhancement by high density](https://doi.org/10.1016/j.jallcom.2015.08.013) (2015) — 5 samples
- [Effect of calcination temperature on structure and thermoelectric properties of CuAlO2 powders](https://doi.org/10.1007/s10853-017-1602-8) (2017) — 4 samples

**`CuAl0.9Fe0.1O2`** — 11 samples, 4 papers
- [Figures of Merit of Low-Cost CuAl<sub>0.9</sub>Fe<sub>0.1</sub>O<sub>2</sub> Thermoelectric Mat...](https://doi.org/10.4028/www.scientific.net/kem.659.185) (2015) — 8 samples
- [Effects of mechanical milling on preparation and properties of CuAl1−xFexO2 thermoelectric cera...](https://doi.org/10.1016/j.ceramint.2011.12.079) (2012) — 1 samples
- [Improvement in thermoelectric properties of CuAlO2 by adding Fe2O3](https://doi.org/10.1016/j.jallcom.2006.07.067) (2007) — 1 samples

**`Ca(CuAlO2)99`** — 5 samples, 1 papers
- [Synergetic improvement strategy on thermoelectric performance of CuAlO2 compacts](https://doi.org/10.1016/j.ceramint.2018.12.004) (2019) — 5 samples

**`Ca2(CuAlO2)98`** — 5 samples, 1 papers
- [Synergetic improvement strategy on thermoelectric performance of CuAlO2 compacts](https://doi.org/10.1016/j.ceramint.2018.12.004) (2019) — 5 samples

**Your finding** — fill in, then run `python scripts/apply_review_findings.py`:

```finding
host: Al-Cu-O
decision:        # confirm | change | split | unresolved
prototype:       # for change: the prototype id it should be
spacegroup:      # number the paper reports, e.g. 212
mp_id:           # if you have it
evidence:        # DOI you read this from
notes:
```

---

## Cu-Fe-S — 99 samples, chunk 2

**Assigned** `chalcopyrite` (high confidence)

**Needs checking because:**
- structure reference cannot separate two polymorphs

**What to look for:**
- Which polymorph was actually made. Look for the reported space group or lattice parameters in the experimental section. Record the space group number, or the mp_id if you have it.

> CuFeS2 (20) chalcopyrite; Cu5FeS4 (7) is bornite, a different sulfosalt in the same host.

**`CuFeS2`** — 20 samples, 11 papers
- [Synthesis and property evaluation of CuFeS2−x as earth-abundant and environmentally-friendly th...](https://doi.org/10.1016/j.jallcom.2012.09.067) (2013) — 6 samples
- [Synthesis and Thermoelectric Properties of Carrier-Doped CuFeS2 Sintered Samples](https://doi.org/10.2497/jjspm.61.18) (2014) — 3 samples
- [Enhanced thermoelectric performance of chalcopyrite nanocomposite via co-milling of synthetic a...](https://doi.org/10.1016/j.matlet.2020.128107) (2020) — 3 samples

**`Zn0.03Cu0.97FeS2`** — 9 samples, 4 papers
- [Effect of Nanostructuring and High-Pressure Torsion Process on Thermal Conductivity of Carrier-...](https://doi.org/10.1007/s11664-015-4147-0) (2015) — 4 samples
- [Effect of microstructure on lattice thermal conductivity of thermoelectric chalcopyrite CuFeS2:...](https://doi.org/10.35848/1882-0786/ac1231) (2021) — 3 samples
- [Phase Stability and Thermoelectric Properties of CuFeS2-Based Magnetic Semiconductor](https://doi.org/10.1007/s11664-014-3072-y) (2014) — 1 samples

**`Cu5FeS4`** — 7 samples, 3 papers
- [Ball milling as an effective route for the preparation of doped bornite: synthesis, stability a...](https://doi.org/10.1039/c5tc01704a) (2015) — 4 samples
- [Sulfide bornite thermoelectric material: a natural mineral with ultralow thermal conductivity](https://doi.org/10.1039/c4ee02428a) (2014) — 2 samples
- [High Thermoelectric Performance of Bornite through Control of the Cu(II) Content and Vacancy Co...](https://doi.org/10.1021/acs.chemmater.7b04436) (2018) — 1 samples

**`Cu0.95Fe1.05S2`** — 4 samples, 4 papers
- [Possible Enhancement of Thermoelectric Properties by Use of a Magnetic Semiconductor: Carrier-D...](https://doi.org/10.1007/s11664-013-2485-3) (2013) — 1 samples
- [Thermoelectric transport properties of diamond-like Cu1−xFe1+xS2 tetrahedral compounds](https://doi.org/10.1063/1.4902849) (2014) — 1 samples
- [Research Update: Cu–S based synthetic minerals as efficient thermoelectric materials at medium ...](https://doi.org/10.1063/1.4955398) (2016) — 1 samples

**Your finding** — fill in, then run `python scripts/apply_review_findings.py`:

```finding
host: Cu-Fe-S
decision:        # confirm | change | split | unresolved
prototype:       # for change: the prototype id it should be
split:           # for split: one "composition -> prototype_id" per line
  # Ca3Co4O9 -> misfit_cobaltite
  # Ca3Co2O6 -> ca3co2o6_chain
spacegroup:      # number the paper reports, e.g. 212
mp_id:           # if you have it
evidence:        # DOI you read this from
notes:
```

---

## Ir-O-Sr — 96 samples, chunk 2

**Assigned** `perovskite` (medium confidence)

**Needs checking because:**
- medium confidence

**What to look for:**
- Any explicit structure statement -- space group, prototype name, or the reference structure the authors index against. Record confirm, or the prototype it should be.

> SrIrO3 (35) and Sr2IrO4 (21). SrIrO3 is the monoclinic distorted perovskite (a 6H hexagonal polymorph also exists) and Sr2IrO4 is the n=1 Ruddlesden-Popper spin-orbit Mott insulator.

**`SrIrO3`** — 35 samples, 10 papers
- [Anomalous pressure dependence of the electronic transport and anisotropy in SrIrO3 films](https://doi.org/10.1088/1361-648x/ab8a9e) (2020) — 17 samples
- [Metal insulator transitions in perovskite SrIrO3 thin films](https://doi.org/10.1063/1.4903314) (2014) — 5 samples
- [Anisotropy and interaction effects of strongly strained SrIrO<sub>3</sub> thin films](https://doi.org/10.1063/1.4960700) (2016) — 5 samples

**`Sr2IrO4`** — 21 samples, 10 papers
- [Crossover of conduction mechanism in Sr<sub>2</sub>IrO<sub>4</sub> epitaxial thin films](https://doi.org/10.1063/1.4894465) (2014) — 6 samples
- [Quest for quantum states via field-altering technology](https://doi.org/10.1038/s41535-020-00286-2) (2020) — 4 samples
- [Decoupling of magnetism and electric transport in single-crystal (Sr<sub>1−<i>x</i> </sub>A<sub...](https://doi.org/10.1088/1361-648x/aac23d) (2018) — 2 samples

**`Sr1.95La0.05IrO4`** — 3 samples, 2 papers
- [Insight on the electronic state of Sr2IrO4revealed by cationic substitutions](https://doi.org/10.1088/0953-8984/20/29/295201) (2008) — 2 samples
- [Transport Properties and Cationic Substitutions in Sr2IrO4](https://doi.org/10.1007/s11664-008-0642-x) (2009) — 1 samples

**`Sr2Ir0.9Rh0.1O4`** — 3 samples, 2 papers
- [Insight on the electronic state of Sr2IrO4revealed by cationic substitutions](https://doi.org/10.1088/0953-8984/20/29/295201) (2008) — 2 samples
- [Transport Properties and Cationic Substitutions in Sr2IrO4](https://doi.org/10.1007/s11664-008-0642-x) (2009) — 1 samples

**Your finding** — fill in, then run `python scripts/apply_review_findings.py`:

```finding
host: Ir-O-Sr
decision:        # confirm | change | split | unresolved
prototype:       # for change: the prototype id it should be
split:           # for split: one "composition -> prototype_id" per line
  # Ca3Co4O9 -> misfit_cobaltite
  # Ca3Co2O6 -> ca3co2o6_chain
evidence:        # DOI you read this from
notes:
```

---

## Sb-Yb — 93 samples, chunk 2

**Assigned** `yb14mnsb11_zintl` (medium confidence)

**Needs checking because:**
- medium confidence
- structure reference cannot separate two polymorphs

**What to look for:**
- Any explicit structure statement -- space group, prototype name, or the reference structure the authors index against. Record confirm, or the prototype it should be.
- Which polymorph was actually made. Look for the reported space group or lattice parameters in the experimental section. Record the space group number, or the mp_id if you have it.

> Yb14MnSb11 (18) and Yb14MgSb11 -- the 14-1-11 Zintl, the highest-performing p-type high-temperature thermoelectric. Yb11GaSb9 and Yb4Sb3 are separate phases in this host.

**`Yb14MnSb11`** — 18 samples, 14 papers
- [High Temperature Thermoelectric Properties of Yb14MnSb11Prepared from Reaction of MnSb with the...](https://doi.org/10.1021/acs.chemmater.5b02446) (2015) — 5 samples
- [Traversing the Metal-Insulator Transition in a Zintl Phase: Rational Enhancement of Thermoelect...](https://doi.org/10.1002/adfm.200800298) (2008) — 1 samples
- [Achieving zT > 1 in Inexpensive Zintl Phase Ca9\nZn4+\n                        \n              ...](https://doi.org/10.1002/adfm.201606361) (2017) — 1 samples

**`Yb14MgSb11`** — 7 samples, 3 papers
- [Yb14MgSb11and Ca14MgSb11—New Mg-Containing Zintl Compounds and Their Structures, Bonding, and T...](https://doi.org/10.1021/cm504059t) (2015) — 5 samples
- [Improved Power Factor and Mechanical Properties of Composites of Yb14MgSb11 with Iron](https://doi.org/10.1021/acsaem.9b02168) (2020) — 1 samples
- [Discovery of multivalley Fermi surface responsible for the high thermoelectric performance in Y...](https://doi.org/10.1126/sciadv.abe9439) (2021) — 1 samples

**`Yb14Mn1.05Sb11`** — 4 samples, 3 papers
- [High Temperature Thermoelectric Properties of Yb14MnSb11Prepared from Reaction of MnSb with the...](https://doi.org/10.1021/acs.chemmater.5b02446) (2015) — 2 samples
- [Preparation and thermoelectric properties of polycrystalline nonstoichiometric Yb14MnSb11 Zintl...](https://doi.org/10.1002/pssr.201004193) (2010) — 1 samples
- [Improved Thermoelectric Properties in Lu-doped Yb$_{14}$MnSb$_{11}$ Zintl Compounds](https://doi.org/10.1143/apex.5.031801) (2012) — 1 samples

**`Yb11GaSb9`** — 3 samples, 1 papers
- [High-Temperature Transport Properties of the Zintl Phases Yb11GaSb9and Yb11InSb9†](https://doi.org/10.1021/cm901824c) (2010) — 3 samples

**Your finding** — fill in, then run `python scripts/apply_review_findings.py`:

```finding
host: Sb-Yb
decision:        # confirm | change | split | unresolved
prototype:       # for change: the prototype id it should be
split:           # for split: one "composition -> prototype_id" per line
  # Ca3Co4O9 -> misfit_cobaltite
  # Ca3Co2O6 -> ca3co2o6_chain
spacegroup:      # number the paper reports, e.g. 212
mp_id:           # if you have it
evidence:        # DOI you read this from
notes:
```

---

## Te — 92 samples, chunk 2

**Assigned** `trigonal_te` (high confidence)

**Needs checking because:**
- transition at ~723 K is a taxonomy default, not read from a paper

**What to look for:**
- Whether the paper reports a structural transition, and at what temperature. Look for DSC, high-temperature XRD, or a kink discussed in the text. Record the temperature, or "none" if the paper shows the sample staying in one phase across its range.

> Elemental Te (33), helical chains P3_121, mp-19 with 20 ICSD references. Te melts at ~723 K, inside many high-temperature runs.

**`Te`** — 33 samples, 10 papers
- [Tellurium as a high-performance elemental thermoelectric](https://doi.org/10.1038/ncomms10287) (2016) — 15 samples
- [Thermoelectric properties of electrodeposited tellurium films and the sodium lignosulfonate effect](https://doi.org/10.1016/j.electacta.2015.04.063) (2015) — 6 samples
- [Thermoelectric Properties of Films and Monocrystalline Whiskers of Tellurium](https://doi.org/10.1109/ict.2006.331387) (2006) — 3 samples

**`Te0.98As0.02`** — 8 samples, 2 papers
- [Enhancing the average thermoelectric figure of merit of elemental Te by suppressing grain bound...](https://doi.org/10.1039/d0ta02660c) (2020) — 7 samples
- [Sb induces both doping and precipitation for improving the thermoelectric performance of elemen...](https://doi.org/10.1039/c7qi00138j) (2017) — 1 samples

**`SnSeTe30`** — 4 samples, 1 papers
- [Anion-exchanged porous SnTe nanosheets for ultra-low thermal conductivity and high-performance ...](https://doi.org/10.1016/j.cej.2020.126274) (2020) — 4 samples

**`Te97Se3`** — 2 samples, 1 papers
- [Effect of selenium on the thermoelectric properties of tellurium](https://doi.org/10.1007/bf00891150) (1975) — 2 samples

**Your finding** — fill in, then run `python scripts/apply_review_findings.py`:

```finding
host: Te
decision:        # confirm | change | split | unresolved
prototype:       # for change: the prototype id it should be
transition_K:    # temperature, or "none"
evidence:        # DOI you read this from
notes:
```

---

## Ge-Pb-Te — 91 samples, chunk 2

**Assigned** `gete_rhombohedral` (high confidence)

**Needs checking because:**
- transition at ~700 K is a taxonomy default, not read from a paper

**What to look for:**
- Whether the paper reports a structural transition, and at what temperature. Look for DSC, high-temperature XRD, or a kink discussed in the text. Record the temperature, or "none" if the paper shows the sample staying in one phase across its range.

> Ge1-xPbxTe alloys, Ge-rich (median Ge/(Ge+Pb)=0.82). Rhombohedral at room temperature, converting to rocksalt near 700 K; Pb content lowers the transition temperature.

**`Ge0.87Pb0.13Te`** — 10 samples, 4 papers
- [Controlling Metallurgical Phase Separation Reactions of the Ge0.87Pb0.13Te Alloy for High Therm...](https://doi.org/10.1002/aenm.201200970) (2013) — 7 samples
- [A Comparison Between the Mechanical and Thermoelectric Properties of Three Highly Efficient p-T...](https://doi.org/10.1007/s11664-012-2316-y) (2012) — 1 samples
- [Stacking Fault-Induced Minimized Lattice Thermal Conductivity in the High-Performance GeTe-Base...](https://doi.org/10.1021/acsami.9b04984) (2019) — 1 samples

**`Ge0.76Sb0.08Pb0.12Te`** — 8 samples, 1 papers
- [Vacancy Manipulation for Thermoelectric Enhancements in GeTe Alloys](https://doi.org/10.1021/jacs.8b09375) (2018) — 8 samples

**`Ge0.86Pb0.1Bi0.04Te`** — 6 samples, 1 papers
- [Low-Symmetry Rhombohedral GeTe Thermoelectrics](https://doi.org/10.1016/j.joule.2018.02.016) (2018) — 6 samples

**`Ge0.4Pb0.6Te`** — 2 samples, 1 papers
- [Near-room-temperature rhombohedral Ge1-Pb Te thermoelectrics](https://doi.org/10.1016/j.mtphys.2020.100260) (2020) — 2 samples

**Your finding** — fill in, then run `python scripts/apply_review_findings.py`:

```finding
host: Ge-Pb-Te
decision:        # confirm | change | split | unresolved
prototype:       # for change: the prototype id it should be
transition_K:    # temperature, or "none"
evidence:        # DOI you read this from
notes:
```

---

## Cu-O — 89 samples, chunk 2

**Assigned** `tenorite` (high confidence)

**Needs checking because:**
- structure reference cannot separate two polymorphs

**What to look for:**
- Which polymorph was actually made. Look for the reported space group or lattice parameters in the experimental section. Record the space group number, or the mp_id if you have it.

> CuO (9) monoclinic tenorite and Cu2O cuprite in the same host; separated by copper oxidation state.

**`CuO`** — 9 samples, 4 papers
- [Controlled nanostructuring via aluminum doping in CuO nanosheets for enhanced thermoelectric pe...](https://doi.org/10.1016/j.jallcom.2021.159370) (2021) — 5 samples
- [Thermoelectric properties of Li-doped Cu0.95-x M0.05Li x O (M=Mn, Ni, Zn)](https://doi.org/10.1557/opl.2012.1571) (2012) — 2 samples
- [Nanocomposites of CuO/SWCNT: Promising thermoelectric materials for mid-temperature thermoelect...](https://doi.org/10.1016/j.jeurceramsoc.2019.04.036) (2019) — 1 samples

**`Cu0.94Ni0.05Li0.01O`** — 7 samples, 1 papers
- [Thermoelectric properties of Li-doped Cu0.95-x M0.05Li x O (M=Mn, Ni, Zn)](https://doi.org/10.1557/opl.2012.1571) (2012) — 7 samples

**`Al0.005(CuO)0.995`** — 5 samples, 1 papers
- [Controlled nanostructuring via aluminum doping in CuO nanosheets for enhanced thermoelectric pe...](https://doi.org/10.1016/j.jallcom.2021.159370) (2021) — 5 samples

**`Al0.01(CuO)0.99`** — 5 samples, 1 papers
- [Controlled nanostructuring via aluminum doping in CuO nanosheets for enhanced thermoelectric pe...](https://doi.org/10.1016/j.jallcom.2021.159370) (2021) — 5 samples

**Your finding** — fill in, then run `python scripts/apply_review_findings.py`:

```finding
host: Cu-O
decision:        # confirm | change | split | unresolved
prototype:       # for change: the prototype id it should be
split:           # for split: one "composition -> prototype_id" per line
  # Ca3Co4O9 -> misfit_cobaltite
  # Ca3Co2O6 -> ca3co2o6_chain
spacegroup:      # number the paper reports, e.g. 212
mp_id:           # if you have it
evidence:        # DOI you read this from
notes:
```

---

## Ag-Se — 86 samples, chunk 2

**Assigned** `ag2se_naumannite` (medium confidence)

**Needs checking because:**
- medium confidence
- transition at ~406 K is a taxonomy default, not read from a paper

**What to look for:**
- Any explicit structure statement -- space group, prototype name, or the reference structure the authors index against. Record confirm, or the prototype it should be.
- Whether the paper reports a structural transition, and at what temperature. Look for DSC, high-temperature XRD, or a kink discussed in the text. Record the temperature, or "none" if the paper shows the sample staying in one phase across its range.

> Ag2Se (46) orthorhombic below ~406 K, converting to the bcc superionic phase above it -- inside the measured window.

**`Ag2Se`** — 46 samples, 19 papers
- [Thermoelectric power of annealed β‐Ag2Se alloy thin films: Temperature and size effects—possibi...](https://doi.org/10.1063/1.345747) (1990) — 12 samples
- [Non-epitaxial pulsed laser deposition of Ag 2 Se thermoelectric thin films for near-room temper...](https://doi.org/10.1016/j.ceramint.2016.05.037) (2016) — 5 samples
- [Hierarchical Structures Advance Thermoelectric Properties of Porous n-type β-Ag2Se](https://doi.org/10.1021/acsami.0c15341) (2020) — 5 samples

**`Ag2.001Se1.01`** — 5 samples, 1 papers
- [Thermoelectric figure of merit of Ag2Se with Ag and Se excess](https://doi.org/10.1134/s1063782609080028) (2009) — 5 samples

**`Ag2.0006Se`** — 2 samples, 1 papers
- [Evaluating the potential for high thermoelectric efficiency of silver selenide](https://doi.org/10.1039/c3tc31810a) (2013) — 2 samples

**`Ag2.0027Se`** — 2 samples, 1 papers
- [Evaluating the potential for high thermoelectric efficiency of silver selenide](https://doi.org/10.1039/c3tc31810a) (2013) — 2 samples

**Your finding** — fill in, then run `python scripts/apply_review_findings.py`:

```finding
host: Ag-Se
decision:        # confirm | change | split | unresolved
prototype:       # for change: the prototype id it should be
transition_K:    # temperature, or "none"
evidence:        # DOI you read this from
notes:
```

---

## Cu-S-Sn — 84 samples, chunk 2

**Assigned** `colusite` (medium confidence)

**Needs checking because:**
- medium confidence
- taxonomy issue recorded

**What to look for:**
- Any explicit structure statement -- space group, prototype name, or the reference structure the authors index against. Record confirm, or the prototype it should be.
- Whether the taxonomy entry itself is wrong or incomplete, rather than the assignment. Record what should change in the prototype.

> Cu26V2Sn6S32 (18) is colusite, a distinct sulfosalt with a cubic P-43n framework; Cu2SnS3 (11) is the diamond-like ternary and Cu4Sn7S16 a third phase. Colusite has no entry in the taxonomy.

**`Cu26V2Sn6S32`** — 18 samples, 7 papers
- [Issues and opportunities from Peltier effect in functionally-graded colusites: From SPS tempera...](https://doi.org/10.1016/j.apmt.2021.100948) (2021) — 6 samples
- [A scalable synthesis route for multiscale defect engineering in the sustainable thermoelectric ...](https://doi.org/10.1016/j.actamat.2020.05.039) (2020) — 4 samples
- [Promoted crystallisation and cationic ordering in thermoelectric Cu26V2Sn6S32 colusite by eccen...](https://doi.org/10.1039/d0dt03368e) (2020) — 4 samples

**`Cu2SnS3`** — 11 samples, 7 papers
- [Ultra-low thermal conductivity and improved thermoelectric performance in disordered nanostruct...](https://doi.org/10.1016/j.jallcom.2020.154604) (2020) — 4 samples
- [Experimental and Ab Initio Study of Cu2SnS3 (CTS) Polymorphs for Thermoelectric Applications](https://doi.org/10.1021/acs.jpcc.0c09139) (2020) — 2 samples
- [The Enhanced Electrical Transport Properties of Fe3+ Doped Cu2SnS3](https://doi.org/10.1007/s13391-021-00309-5) (2021) — 1 samples

**`Cu4Sn7S16`** — 6 samples, 4 papers
- [Low thermal conductivity in ternary Cu4Sn7S16 compound](https://doi.org/10.1016/j.actamat.2015.06.046) (2015) — 3 samples
- [Crystal structure, electronic structure and thermoelectric properties of Cu4Sn7S16](https://doi.org/10.1016/j.jallcom.2005.09.030) (2006) — 1 samples
- [Improved thermoelectric performance of solid solution Cu4Sn7.5S16 through isoelectronic substit...](https://doi.org/10.1038/s41598-018-26362-z) (2018) — 1 samples

**`Cu24Zn2V2Sn6S32`** — 2 samples, 2 papers
- [Tunable electronic properties and low thermal conductivity in synthetic colusites Cu26−xZnxV2M6...](https://doi.org/10.1063/1.4892593) (2014) — 1 samples
- [Tuning the charge carrier density in the thermoelectric colusite](https://doi.org/10.1063/1.4948475) (2016) — 1 samples

**Your finding** — fill in, then run `python scripts/apply_review_findings.py`:

```finding
host: Cu-S-Sn
decision:        # confirm | change | split | unresolved
prototype:       # for change: the prototype id it should be
split:           # for split: one "composition -> prototype_id" per line
  # Ca3Co4O9 -> misfit_cobaltite
  # Ca3Co2O6 -> ca3co2o6_chain
evidence:        # DOI you read this from
notes:
```

---

*43 further hosts are in `needs_review.parquet`; re-run with `--top` to include them.*
