#!/usr/bin/env python
"""Merge the v2 prototype seed with the v0.2 structure ontology.

Produces data/annotated/taxonomy/prototypes_seed_v3.json.

Two lineages are combined:
  data/annotated/taxonomy/prototypes_seed_v2.json          135 prototypes, wide
      coverage, derived by surveying the 700 largest host systems.
  data/lineage/thermoelectric_structure_ontology_v0.2.json   51 structures,
      drafted in discussion with ChatGPT, with stronger assignment epistemics
      (candidate vs confirmed) and a dozen prototypes v2 missed.

Both lineages are LLM-generated, so their agreement is a weak check: they can
share correlated errors from the same textbook conventions. The independent
evidence is the held-out curator labels and, later, the papers themselves.
(The maintainer's own hand-written family list lives in the starrydata-explorer
repository and is not an input here.)

v3 keeps v2's breadth, adopts v0.2's field vocabulary and principles, and adds
the prototypes only v0.2 had. The v0.2 `legacy_label_map` is NOT carried over --
it anchors assignments to the hand labels, which are held out for validation. It
is written to validation/legacy_label_map.json instead.

Run:  python scripts/merge_taxonomy_v3.py
"""

import json
import os

_P = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
V2 = os.path.join(_P, 'data', 'annotated', 'taxonomy', 'prototypes_seed_v2.json')
V02 = os.path.join(_P, 'data', 'lineage', 'thermoelectric_structure_ontology_v0.2.json')
OUT = os.path.join(_P, 'data', 'annotated', 'taxonomy', 'prototypes_seed_v3.json')
VAL_DIR = os.path.join(_P, 'data', 'annotated', 'validation')

# v0.2 structure id -> v2 prototype id, where they describe the same thing.
EQUIV = {
    'tetradymite_Bi2Te3_type': 'tetradymite', 'rocksalt_B1': 'rocksalt',
    'GeTe_rhombohedral': 'gete_rhombohedral', 'SnSe_Pnma': 'layered_ges',
    'antifluorite_Mg2X': 'antifluorite', 'diamond_A4': 'diamond_cubic',
    'half_Heusler_C1b': 'half_heusler', 'full_Heusler_L21': 'full_heusler',
    'skutterudite_CoAs3': 'skutterudite', 'clathrate_type_I': 'clathrate_i',
    'CaAl2Si2_type': 'caal2si2_zintl', 'Zintl_14_1_11': 'yb14mnsb11_zintl',
    'Zintl_5_2_6': 'zintl_5_2_6', 'Zintl_9_4_9': 'zintl_9_4_9',
    'Mo3Sb7_Ir3Ge7_type': 'ir3ge7', 'tetrahedrite_Cu12Sb4S13': 'tetrahedrite',
    'chalcopyrite_CuFeS2': 'chalcopyrite', 'stannite': 'stannite_kesterite',
    'argyrodite': 'argyrodite', 'BiCuSeO_ZrCuSiAs_type': 'zrcusias_1111',
    'perovskite_ABO3': 'perovskite', 'double_perovskite': 'double_perovskite',
    'inverse_perovskite': 'antiperovskite', 'spinel': 'spinel',
    'delafossite': 'delafossite', 'wurtzite_ZnO': 'wurtzite',
    'bixbyite': 'bixbyite', 'tetragonal_tungsten_bronze': 'tungsten_bronze',
    'misfit_cobaltite': 'misfit_cobaltite', 'layered_cobaltate': 'naxcoo2_layered',
    'B20_FeSi_type': 'b20_fesi', 'HMS_Nowotny_chimney_ladder': 'hms_chimney_ladder',
    'pyrite_C2': 'pyrite', 'graphite_graphene': 'graphite_layered',
    'SiC_polytype': 'sic_polytype', 'polymer_noncrystalline': 'organic_polymer',
    'quasicrystal': 'quasicrystal_approximant',
    'noncrystalline_or_unknown': 'unresolved',
}

CLASS_TO_DIM = {
    'layered van der Waals': 'layered', 'rocksalt-derived': '3D',
    'tetrahedral diamond-like': '3D', 'close-packed intermetallic': '3D',
    'cage compound': '3D_cage_framework', 'perovskite-derived': '3D',
    'misfit / incommensurate': 'composite_modulated',
    'chain / low-dimensional': 'chain_or_network', 'cluster compound': 'cluster_3D',
    'framework oxide': '3D_framework', 'Zintl polyanion': '3D',
    'disordered / non-crystalline': 'amorphous', 'molecular / organic': 'molecular_polymer',
}
DIM_OVERRIDE = {'post_perovskite': 'layered', 'ruddlesden_popper': 'layered',
                'ybco_cuprate': 'layered', 'bscco_cuprate': 'layered',
                'aurivillius': 'layered', 'layered_double_perovskite': 'layered',
                'a7_rhombohedral': 'layered', 'alpha_nafeo2_layered': 'layered',
                'high_entropy_alloy': '3D', 'metallic_glass': 'amorphous',
                'interstitial_hydride': '3D', 'composite_multiphase': 'composite_multiphase',
                'unresolved': None}

# Prototypes present only in v0.2, restated in the v3 field vocabulary.
NEW = [
    {"id": "inverse_heusler", "display_name": "Inverse Heusler (Hg2CuTi-type)", "prototype": "Hg2CuTi", "strukturbericht": "X_a", "exemplar": "Ti2NiSn", "formula_archetype": "X2YZ", "typical_space_group": "F-43m (216)", "dimensionality": "3D", "structural_class": "close-packed intermetallic", "representative_materials": ["Ti2NiSn", "Mn2CoAl"], "example_host_systems": [], "discriminate_from": {"full_heusler": "the two X atoms are inequivalent; F-43m rather than Fm-3m", "half_heusler": "X2YZ not XYZ"}, "notes": ["Spin-gapless semiconductors."]},
    {"id": "quaternary_heusler", "display_name": "Quaternary Heusler (LiMgAuSn-type)", "prototype": "LiMgAuSn", "exemplar": "CoFeMnSi", "formula_archetype": "XX'YZ", "typical_space_group": "F-43m (216)", "dimensionality": "3D", "structural_class": "close-packed intermetallic", "representative_materials": ["CoFeMnSi", "NiCoMnSb"], "example_host_systems": ["Fe-Ni-Sb-Ti", "Mn-Ni-Sb-Ti"], "discriminate_from": {"full_heusler": "four distinct elements in an ordered 1:1:1:1 arrangement", "half_heusler": "the vacant site is occupied by a fourth element"}, "notes": ["The Fe-Ni-Sb-Ti host contains Ti2FeNiSb2, which may be a quaternary Heusler or a half-Heusler solid solution."], "confidence_note": "Composition alone does not distinguish an ordered quaternary Heusler from a disordered half-Heusler alloy -- needs paper evidence."},
    {"id": "filled_skutterudite", "display_name": "Filled skutterudite", "prototype": "LaFe4P12", "exemplar": "Yb0.3Co4Sb12", "formula_archetype": "RyM4X12", "typical_space_group": "Im-3 (204)", "dimensionality": "3D_cage_framework", "structural_class": "cage compound", "representative_materials": ["Yb0.3Co4Sb12", "Ba0.3In0.2Co4Sb12", "CeFe4Sb12", "YbFe4Sb12"], "example_host_systems": ["Co-Sb", "Ce-Fe-Sb", "Fe-Sb-Yb", "Ca-Fe-Sb", "Fe-Ni-Sb", "Ce-Co-Fe-Sb"], "discriminate_from": {"skutterudite": "the icosahedral void is occupied by a rare-earth/alkaline-earth guest; y > 0 distinguishes it from binary MX3"}, "notes": ["Split from binary skutterudite because the filled and unfilled frameworks are different Materials Project entries.", "The filler fraction y is a compositional variable that sets the carrier count -- treat as filling level, never as a substitutional dopant."]},
    {"id": "clathrate_viii", "display_name": "Clathrate type VIII", "prototype": "Ba8Ga16Sn30 (type VIII)", "exemplar": "Ba8Ga16Sn30", "formula_archetype": "A8E46", "typical_space_group": "I-43m (217)", "dimensionality": "3D_cage_framework", "structural_class": "cage compound", "representative_materials": ["Ba8Ga16Sn30"], "example_host_systems": ["Ba-Ga-Sn"], "discriminate_from": {"clathrate_i": "a single cage type (distorted pentagonal dodecahedra) rather than the two cage types of type I; beta-Ba8Ga16Sn30 is type VIII while the alpha phase is type I"}, "notes": ["Corrects v2, which filed Ba-Ga-Sn under type I alone."], "confidence_note": "The Ba-Ga-Sn host contains both the type-I (alpha) and type-VIII (beta) polymorphs -- split per composition and per paper."},
    {"id": "zintl_3_1_3", "display_name": "Zintl 3-1-3 (Ca3AlSb3-type)", "prototype": "Ca3AlSb3", "exemplar": "Ca3AlSb3", "formula_archetype": "A3MPn3", "typical_space_group": "Pnma (62)", "dimensionality": "chain_or_network", "structural_class": "Zintl polyanion", "representative_materials": ["Ca3AlSb3", "Sr3GaSb3"], "example_host_systems": [], "discriminate_from": {"zintl_5_2_6": "isolated MPn3 chains rather than corner-sharing MPn4 double chains"}, "notes": []},
    {"id": "mn5si3_d88", "display_name": "Mn5Si3-type (D8_8)", "prototype": "Mn5Si3", "strukturbericht": "D8_8", "exemplar": "Mn5Si3", "formula_archetype": "A5B3", "typical_space_group": "P63/mcm (193)", "dimensionality": "3D", "structural_class": "close-packed intermetallic", "representative_materials": ["Mn5Si3", "Ti5Ga3"], "example_host_systems": [], "discriminate_from": {"hms_chimney_ladder": "A5B3 rather than MSi~1.75", "b20_fesi": "different stoichiometry"}, "notes": ["Can host interstitial atoms in the octahedral chain void."]},
    {"id": "chevrel", "display_name": "Chevrel phase", "prototype": "Mo6S8", "exemplar": "Mo6Se8", "formula_archetype": "AxMo6X8", "typical_space_group": "R-3 (148)", "dimensionality": "cluster_3D", "structural_class": "cluster compound", "representative_materials": ["Mo6Se8", "PbMo6S8", "Cu2Mo6S8"], "example_host_systems": [], "discriminate_from": {"ir3ge7": "Mo6 octahedral clusters with intercalated cations"}, "notes": ["Restored from v1; dropped in error from v2.", "The intercalated cation content x is the doping variable."]},
    {"id": "hollandite", "display_name": "Hollandite", "prototype": "BaMn8O16", "exemplar": "K2Cr8O16", "formula_archetype": "AxM8O16", "typical_space_group": "I4/m (87)", "dimensionality": "tunnel", "structural_class": "framework oxide", "representative_materials": ["K2Cr8O16", "BaMn8O16"], "example_host_systems": [], "discriminate_from": {"tungsten_bronze": "2x2 edge-sharing octahedral tunnels", "rutile": "the tunnel framework is built from rutile-like chains but is not rutile"}, "notes": ["Tunnel cation content sets the mixed valence."]},
    {"id": "fresnoite", "display_name": "Fresnoite", "prototype": "Ba2TiSi2O8", "exemplar": "Ba2TiSi2O8", "formula_archetype": "A2BC2O8", "typical_space_group": "P4bm (100)", "dimensionality": "layered", "structural_class": "framework oxide", "representative_materials": ["Ba2TiSi2O8", "Sr2TiSi2O8"], "example_host_systems": [], "discriminate_from": {"tungsten_bronze": "silicate framework, polar tetragonal"}, "notes": ["Polar piezoelectric oxide; enters via the dielectric/piezoelectric projects."]},
    {"id": "langasite", "display_name": "Langasite", "prototype": "La3Ga5SiO14", "exemplar": "La3Ga5SiO14", "formula_archetype": "A3BC3D2O14", "typical_space_group": "P321 (150)", "dimensionality": "3D_framework", "structural_class": "framework oxide", "representative_materials": ["La3Ga5SiO14", "Ca3Ga2Ge4O14"], "example_host_systems": [], "discriminate_from": {"langatate": "langatate is the Ta-substituted member La3Ga5.5Ta0.5O14", "fresnoite": "trigonal P321 framework with four distinct cation sites"}, "notes": ["Piezoelectric crystal family."]},
    {"id": "langatate", "display_name": "Langatate", "prototype": "La3Ga5.5Ta0.5O14", "exemplar": "La3Ga5.5Ta0.5O14", "formula_archetype": "langasite-related", "typical_space_group": "P321 (150)", "dimensionality": "3D_framework", "structural_class": "framework oxide", "representative_materials": ["La3Ga5.5Ta0.5O14", "La3Ga5.5Nb0.5O14"], "example_host_systems": [], "discriminate_from": {"langasite": "Ta/Nb on the tetrahedral site instead of Si"}, "notes": ["Kept separate from langasite because the substituted member is a distinct database entry."]},
    {"id": "amorphous_igzo", "display_name": "Amorphous In-Ga-Zn-O", "prototype": None, "exemplar": "a-InGaZnO", "formula_archetype": "In-Ga-Zn-O", "typical_space_group": None, "dimensionality": "amorphous", "structural_class": "disordered / non-crystalline", "representative_materials": ["a-IGZO"], "example_host_systems": [], "discriminate_from": {"homologous_inmo3_zno": "the crystalline homologous superlattice of the same chemistry -- only paper evidence separates them", "amorphous": "named separately because a-IGZO is a large, well-defined thin-film class"}, "notes": ["No MP assignment."], "confidence_note": "Composition cannot distinguish a-IGZO from crystalline InGaZnO4 -- requires paper evidence."},
    {"id": "cmcm_snse_ht", "display_name": "High-temperature Cmcm SnSe", "prototype": "SnSe (Cmcm, high-T)", "exemplar": "SnSe", "formula_archetype": "AB", "typical_space_group": "Cmcm (63)", "dimensionality": "layered", "structural_class": "layered van der Waals", "representative_materials": ["SnSe", "SnS"], "example_host_systems": ["Se-Sn", "S-Sn"], "discriminate_from": {"layered_ges": "the Pnma phase below the transition; same material, different phase"}, "notes": ["The phase in which SnSe's record ZT is reported. Reached above ~800 K, inside the measured range of most SnSe papers."]},
    {"id": "bcc_superionic", "display_name": "bcc superionic (alpha-Ag2Se type)", "prototype": "alpha-Ag2Se", "exemplar": "Ag2Se", "formula_archetype": "A2B", "typical_space_group": "Im-3m (229)", "dimensionality": "3D", "structural_class": "rocksalt-derived", "representative_materials": ["Ag2Se", "Ag2S", "Ag2Te"], "example_host_systems": ["Ag-Se", "Ag-Te"], "discriminate_from": {"ag2se_naumannite": "the ordered orthorhombic phase below ~406 K; same material, different phase"}, "notes": ["Liquid-like Ag sublattice. Most Ag2Se transport data spans the transition."]},
    {"id": "fulleride_a3c60", "display_name": "Alkali fulleride (A3C60)", "prototype": "K3C60", "exemplar": "Rb3C60", "formula_archetype": "A3C60", "typical_space_group": "Fm-3m (225)", "dimensionality": "molecular_3D", "structural_class": "molecular / organic", "representative_materials": ["K3C60", "Rb3C60", "Cs3C60"], "example_host_systems": ["C"], "discriminate_from": {"graphite_layered": "an fcc packing of C60 molecules with alkali metals in the octahedral and tetrahedral voids, not an extended sp2 sheet", "organic_polymer": "a crystalline molecular solid, not a polymer", "diamond_cubic": "molecular rather than a continuous sp3 network"}, "notes": ["Proposed during chunk-001 annotation and accepted: the C host contains Rb3C60 and K3C60, which share no structural feature with graphite.", "The alkali content is a filling level setting the t1u band occupancy, not dilute doping -- A3C60 is the half-filled metallic composition.", "Air-sensitive; transport data are usually on sealed or thin-film samples."]},
    {"id": "colusite", "display_name": "Colusite", "prototype": "Cu26V2Sn6S32", "exemplar": "Cu26V2Sn6S32", "formula_archetype": "Cu26A2B6S32", "typical_space_group": "P-43n (218)", "dimensionality": "3D_framework", "structural_class": "cluster compound", "representative_materials": ["Cu26V2Sn6S32", "Cu26V2Ge6S32", "Cu26Nb2Sn6S32", "Cu26Ta2Sn6S32"], "example_host_systems": ["Cu-S-Sn", "Cu-Ge-S"], "discriminate_from": {"tetrahedrite": "a different Cu-S sulfosalt: colusite has a larger cubic cell with a dedicated transition-metal framework site and no Sb lone pair", "cu2gese3": "Cu2SnS3 is the simple diamond-like ternary; colusite has a much larger cell", "stannite_kesterite": "not a diamond-like superstructure", "famatinite": "different framework and cation count"}, "notes": ["Proposed during chunk-002 annotation and accepted: Cu26V2Sn6S32 is the largest composition in the Cu-S-Sn host and had no taxonomy entry.", "Cu content and the V/Nb/Ta framework site are the carrier-tuning variables; the sulfur sublattice is a rigid tetrahedral framework.", "Sometimes described as a derivative of the sphalerite net, but the supercell ordering makes it a distinct prototype for structure lookup."]},
    {"id": "in4se3", "display_name": "In4Se3", "prototype": "In4Se3", "exemplar": "In4Se3", "formula_archetype": "A4B3", "typical_space_group": "Pnnm (58)", "dimensionality": "chain_or_network", "structural_class": "Zintl polyanion", "representative_materials": ["In4Se3", "In4Te3"], "example_host_systems": ["In-Se", "In-Te"], "discriminate_from": {"layered_in2se3": "In2Se3 and InSe are simple layered polytypes of divalent-like In; In4Se3 is a distinct mixed-valence phase built from (In3)5+ cluster chains plus In+ cations, and is not a member of that polytype family", "inte_tlse": "InTe is the TlSe-type mixed-valence chain compound; In4Te3 is the 4-3 phase and belongs here -- separate by stoichiometry", "sphalerite": "not a tetrahedral net"}, "notes": ["Filed as an independent structure at the user\'s direction: In4Se3-delta is one of the well-known high-ZT systems (ZT ~1.5 near 700 K), and filing it under layered_in2se3 misdescribes both the bonding and the transport anisotropy.", "Quasi-one-dimensional and strongly anisotropic; the reported figures of merit are direction-dependent, so the measurement axis matters when comparing samples.", "Se deficiency (In4Se3-delta) is the carrier-concentration variable, not an impurity."]},
    {"id": "unresolved_crystalline", "display_name": "Unresolved but crystalline", "prototype": None, "exemplar": None, "formula_archetype": "variable", "typical_space_group": None, "dimensionality": "3D", "structural_class": None, "representative_materials": [], "example_host_systems": [], "discriminate_from": {"unresolved": "use this when the sample is known to be crystalline but the prototype cannot be pinned down", "amorphous": "crystallinity is established here"}, "notes": ["Distinct from `unresolved`, which also covers malformed composition strings and unknown crystallinity."]},
]


# Tilt/distortion sequences for prototypes whose aristotype is never the phase
# actually measured. Unlike a phase_transition between two prototypes, these
# steps all sit INSIDE one prototype and differ only by space group, so they are
# recorded here rather than as separate taxonomy entries.
#
# Temperatures are approximate and shift with stoichiometry, grain size and
# strain -- oxygen-deficient WO3-x in particular suppresses or displaces them.
DISTORTION_SERIES = {
    'reo3_wo3': {
        'compound': 'WO3',
        'note': ('The cubic ReO3 aristotype is essentially never observed for WO3 at '
                 'ambient pressure below the melt; every measured tungsten trioxide is '
                 'a tilt-distorted variant. A transport run from room temperature to '
                 '1200 K passes through three of these steps.'),
        'steps': [
            {'label': 'epsilon', 'spacegroup_symbol': 'Pc', 'spacegroup_number': 7,
             't_min_K': None, 't_max_K': 230, 'note': 'Ferroelectric, monoclinic.'},
            {'label': 'delta', 'spacegroup_symbol': 'P-1', 'spacegroup_number': 2,
             't_min_K': 230, 't_max_K': 290, 'note': 'Triclinic.'},
            {'label': 'gamma', 'spacegroup_symbol': 'P2_1/n', 'spacegroup_number': 14,
             't_min_K': 290, 't_max_K': 603, 'mp_id': 'mp-619461',
             'note': 'The room-temperature phase; P2_1/n is a non-standard setting of P2_1/c.'},
            {'label': 'beta', 'spacegroup_symbol': 'Pbcn', 'spacegroup_number': 60,
             't_min_K': 603, 't_max_K': 1013, 'note': 'Orthorhombic.'},
            {'label': 'alpha', 'spacegroup_symbol': 'P4/ncc', 'spacegroup_number': 130,
             't_min_K': 1013, 't_max_K': 1170,
             'note': 'Tetragonal; P4/nmm is also reported in the literature.'},
            {'label': 'cubic', 'spacegroup_symbol': 'Pm-3m', 'spacegroup_number': 221,
             't_min_K': 1170, 't_max_K': None,
             'note': 'The ReO3 aristotype itself; approached only near the melt and rarely reported.'},
        ],
    },
}


# Entries that originate in v3 itself rather than in either source draft.
V3_ORIGIN = {
    'cmcm_snse_ht': 'v3 (high-temperature phase, added as a transition target)',
    'bcc_superionic': 'v3 (high-temperature phase, added as a transition target)',
    'in4se3': 'v3 (added during chunk-002 annotation, accepted by the user)',
    'fulleride_a3c60': 'v3 (proposed in chunk 001, accepted by the user)',
    'colusite': 'v3 (proposed in chunk 002, accepted by the user)',
}

# v3 id -> the v0.2 structure key it comes from (these exist only in v0.2).
# Structural transitions that fall inside the measured temperature window.
# Transport data here is typically taken from ~300 K to ~740 K (median), and
# 58% of curves exceed 700 K, so a single prototype per host is wrong wherever
# a transition sits in that range. Temperatures are approximate and flagged for
# confirmation against the paper -- they vary with composition and doping.
PHASE_TRANSITIONS = {
    'layered_ges': [{'to': 'cmcm_snse_ht', 'T_K': 800, 'exemplar': 'SnSe',
                     'note': 'Pnma -> Cmcm, ~800 K for SnSe and ~880 K for SnS; the high-ZT regime.'}],
    'gete_rhombohedral': [{'to': 'rocksalt', 'T_K': 700, 'exemplar': 'GeTe',
                           'note': 'R3m -> Fm-3m, ~700 K; shifts with Ge vacancy content and doping.'}],
    'cu2se_superionic': [{'to': 'cu2se_superionic', 'T_K': 400, 'exemplar': 'Cu2Se',
                          'note': 'Ordered low-T superstructure -> cubic superionic, ~400 K. Cu2S transforms near ~376 K.'}],
    'ag2se_naumannite': [{'to': 'bcc_superionic', 'T_K': 406, 'exemplar': 'Ag2Se',
                          'note': 'P212121 -> bcc superionic, ~406 K. Ag2Te transforms near ~418 K.'}],
    'vo2_monoclinic': [{'to': 'rutile', 'T_K': 340, 'exemplar': 'VO2',
                        'note': 'M1 -> rutile metal-insulator transition, ~340 K.'}],
    'gst_homologous': [{'to': 'rocksalt', 'T_K': 420, 'exemplar': 'Ge2Sb2Te5',
                        'note': 'Amorphous -> metastable cubic, ~420 K; cubic -> stable layered above ~500 K.'}],
    'argyrodite': [{'to': 'argyrodite', 'T_K': 330, 'exemplar': 'Ag8GeSe6',
                    'note': 'Order-disorder transition to the cubic superionic phase, ~320-350 K.'}],
    'alpha_nafeo2_layered': [{'to': 'alpha_nafeo2_layered', 'T_K': None, 'exemplar': 'LiCoO2',
                              'note': 'Order-disorder on the Li sublattice depends on Li content, not temperature alone.'}],
    'reo3_wo3': [
        {'to': 'reo3_wo3', 'T_K': 603, 'exemplar': 'WO3',
         'note': 'gamma (P2_1/n) -> beta (Pbcn), ~603 K. First step of the WO3 distortion series inside a typical measurement window.'},
        {'to': 'reo3_wo3', 'T_K': 1013, 'exemplar': 'WO3',
         'note': 'beta (Pbcn) -> alpha (P4/ncc), ~1013 K.'},
        {'to': 'reo3_wo3', 'T_K': 290, 'exemplar': 'WO3',
         'note': 'delta (P-1) -> gamma (P2_1/n), ~290 K; relevant only to runs starting near or below room temperature.'}],
    'perovskite': [{'to': 'perovskite', 'T_K': 393, 'compound_specific': True, 'exemplar': 'BaTiO3',
                    'note': 'Ferroelectric tilt/polarisation transitions are compound-specific: BaTiO3 tetragonal -> cubic ~393 K; SrTiO3 antiferrodistortive ~105 K, below the measured range.'}],
    'trigonal_te': [{'to': None, 'T_K': 723, 'exemplar': 'Te',
                     'note': 'Melts at ~723 K, inside the range of many high-T runs.'}],
    'a7_rhombohedral': [{'to': None, 'T_K': 544, 'exemplar': 'Bi',
                         'note': 'Bi melts at ~544 K; Bi-Sb alloys melt higher.'}],
}


V02_SOURCE = {'inverse_heusler': 'inverse_Heusler', 'quaternary_heusler': 'quaternary_Heusler', 'filled_skutterudite': 'filled_skutterudite', 'clathrate_viii': 'clathrate_type_VIII', 'zintl_3_1_3': 'Zintl_3_1_3', 'mn5si3_d88': 'Mn5Si3_D88', 'chevrel': 'chevrel', 'hollandite': 'hollandite', 'fresnoite': 'fresnoite', 'langasite': 'langasite', 'langatate': 'langatate', 'amorphous_igzo': 'amorphous_IGZO', 'unresolved_crystalline': 'unresolved_crystalline'}


def main():
    v2 = json.load(open(V2))
    v02 = json.load(open(V02))
    old = {p['id']: p for p in v2['prototypes']}
    ustruct = v02['structures']
    rev = {}
    for uk, mk in EQUIV.items():
        rev.setdefault(mk, []).append(uk)

    out = []
    for p in v2['prototypes']:
        u = ustruct.get(rev.get(p['id'], [None])[0]) if p['id'] in rev else None
        dim = (u or {}).get('dimensionality')
        if p['id'] in DIM_OVERRIDE:
            dim = DIM_OVERRIDE[p['id']]
        elif not dim:
            dim = CLASS_TO_DIM.get(p.get('structural_class'))
        notes = [n for n in [p.get('notes')] if n]
        for n in (u or {}).get('notes', []):
            if n not in notes:
                notes.append(n)
        e = {
            'id': p['id'],
            'display_name': (u or {}).get('display_name') or p.get('prototype') or p['id'],
            'prototype': p.get('prototype'),
            'exemplar': p.get('exemplar'),
            'formula_archetype': p.get('stoichiometry'),
            'typical_space_group': p.get('space_group'),
            'dimensionality': dim,
            'structural_class': p.get('structural_class'),
            'representative_materials': (u or {}).get('representative_materials', []),
            'example_host_systems': p.get('example_host_systems', []),
            'discriminate_from': p.get('discriminate_from', {}),
            'structure_database_candidates': [],
            'notes': notes,
        }
        if (u or {}).get('strukturbericht'):
            e['strukturbericht'] = u['strukturbericht']
        if p.get('confidence_note'):
            e['confidence_note'] = p['confidence_note']
        if p['id'] in PHASE_TRANSITIONS:
            e['phase_transitions'] = PHASE_TRANSITIONS[p['id']]
        if p['id'] in DISTORTION_SERIES:
            e['distortion_series'] = DISTORTION_SERIES[p['id']]
        e['merged_from'] = (['v2:' + p['id']]
                            + ['v0.2:' + k for k in rev.get(p['id'], [])])
        out.append(e)

    for n in NEW:
        e = dict(n)
        if e['id'] in PHASE_TRANSITIONS:
            e['phase_transitions'] = PHASE_TRANSITIONS[e['id']]
        e.setdefault('structure_database_candidates', [])
        e['notes'] = list(e.get('notes', []))
        src = V02_SOURCE.get(e['id'])
        e['merged_from'] = ['v0.2:' + src] if src else [V3_ORIGIN.get(
            e['id'], 'v3 (added in v3)')]
        out.append(e)

    # Correction: Ba-Ga-Sn moves to the type-VIII entry as a co-citation.
    for e in out:
        if e['id'] == 'clathrate_i':
            e['discriminate_from']['clathrate_viii'] = (
                'beta-Ba8Ga16Sn30 is type VIII; the Ba-Ga-Sn host holds both polymorphs')
            e['notes'].append(
                'v2 filed Ba-Ga-Sn under type I alone; v3 co-cites it with clathrate_viii.')

    v3 = {
        'version': 'v3',
        'created': '2026-09-16',
        'supersedes': ['prototypes_seed_v2.json (135 prototypes)',
                       'data/dict/thermoelectric_structure_ontology_v0.2.json (51 structures)'],
        'axis': 'crystal structure prototype',
        'scope': v02.get('scope'),
        'principles': v02['principles'] + [
            'The hand-entered MaterialFamily labels are held out, not used as an '
            'assignment basis. They are kept in validation/legacy_label_map.json '
            'and in df_host_systems.parquet solely to validate the finished '
            'classification.',
            'Every label names a structure prototype, never a chemical class '
            '(Oxide, Telluride) and never a specific compound (Bi2Te3, PbTe).',
        ],
        'sample_structure_assignment_schema': v02['sample_structure_assignment_schema'],
        'composition_refinement_rules': v02.get('composition_refinement_rules', []),
        'dopant_threshold': v2.get('dopant_threshold'),
        'structural_classes': v2.get('structural_classes'),
        'phase_policy': (
            'A host system may need more than one prototype: transport is measured '
            'across a wide temperature window (median 302-740 K; 58% of curves pass '
            '700 K) and many thermoelectrics transform inside it. Where a prototype '
            'carries phase_transitions, record every phase the measurement spans, '
            'each with its temperature range, rather than one label. Transition '
            'temperatures here are approximate and composition-dependent -- confirm '
            'against the paper.'),
        'mp_id_policy': ('structure_database_candidates stays empty until resolved '
                         'against Materials Project / AFLOW / ICSD in stage 2. '
                         'Never fill it in from memory.'),
        'prototypes': out,
    }
    with open(OUT, 'w') as f:
        json.dump(v3, f, indent=1)
    print(f'-> {OUT}  ({len(out)} prototypes)')

    os.makedirs(VAL_DIR, exist_ok=True)
    val = os.path.join(VAL_DIR, 'legacy_label_map.json')
    with open(val, 'w') as f:
        json.dump({
            'purpose': ('Hand-entered MaterialFamily labels mapped to structure '
                        'candidates, lifted out of thermoelectric_structure_ontology_v0.2.json. '
                        'HELD OUT: not an annotation input. Use only to validate '
                        'the finished stage-1 classification.'),
            'source': 'data/dict/thermoelectric_structure_ontology_v0.2.json',
            'legacy_label_map': v02.get('legacy_label_map', {}),
        }, f, indent=1)
    print(f'-> {val}  ({len(v02.get("legacy_label_map", {}))} legacy labels, held out)')


if __name__ == '__main__':
    main()
