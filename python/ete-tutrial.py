from ete3 import EvolTree


def main():
    tree = EvolTree(
        """((Hsa_Human: 0.02556, Hla_gibbon: 0.03889): 0.06798,
    ((Cgu/Can_colobus: 0.04379, Pne_langur: 0.05254) : 0.07637, Mmu_rhesus:
    0.02168): 0.04345, (Ssc_squirrelM: 0.04080, Cja_marmoset: 0.02392):
    0.12266);""",
        binpath="/usr/local/bin",
    )
    tree2 = EvolTree(
        """(Hsa_Human: 0.02556, Hla_gibbon: 0.03889,
    (((Cgu/Can_colobus: 0.04379, Pne_langur: 0.05254) : 0.07637, Mmu_rhesus:
    0.02168): 0.04345, (Ssc_squirrelM: 0.04080, Cja_marmoset: 0.02392):
    0.12266): 0.03782);""",
        binpath="/usr/local/bin",
    )
    tree2.set_outgroup("Mmu_rhesus")
    # print(tree.write())
    # tree.unroot()
    # tree = tree2
    fasta_txt = """
  >Hsa_Human
  AAGGTCTTTGAAAGGTGTGAGTTGGCCAGAACTCTGAAAAGATTGGGAATGGATGGCTAC
  AGGGGAATCAGCCTAGCAAACTGGATGTGTTTGGCCAAATGGGAGAGTGGTTACAACACA
  CGAGCTACAAACTACAATGCTGGAGACAGAAGCACTGATTATGGGATATTTCAGATCAAT
  AGCCGCTACTGGTGTAATGATGGCAAAACCCCAGGAGCAGTTAATGCCTGTCATTTATCC
  TGCAGTGCTTTGCTGCAAGATAACATCGCTGATGCTGTAGCTTGTGCAAAGAGGGTTGTC
  CGTGATCCACAAGGCATTAGAGCATGGGTGGCATGGAGAAATCGTTGTCAAAACAGAGAT
  GTCCGTCAGTATGTTCAAGGTTGTGGAGTG

  >Hla_gibbon
  AAGGTCTTTGAAAGGTGTGAGTTGGCCAGAACTCTGAAAAGATTGGGAATGGATGGCTAC
  AGGGGAATCAGCCTAGCAAACTGGATGTGTTTGGCCAAATGGGAGAGTGGTTATAACACA
  CGAGCTACAAACTACAATCCTGGAGACAGAAGCACTGATTATGGGATATTTCAGATCAAT
  AGCCGCTACTGGTGTAATGATGGCAAAACCCCAGGAGCAGTTAATGCCTGTCATTTATCC
  TGCAATGCTTTGCTGCAAGATAACATCGCCGATGCTGTAGCTTGTGCAAAGAGGGTTGTC
  CGCGATCCACAAGGCATTAGAGCATGGGTGGCATGGAGAAATCGTTGTCAAAACAGAGAT
  CTCCGTCAGTATATTCAAGGTTGTGGAGTA

  >Cgu/Can_colobus
  AAGATCTTTGAAAGGTGTGAGTTGGCCAGAACTCTGAAAAAATTGGGACTGGATGGCTAC
  AAGGGAGTCAGCCTAGCAAACTGGGTGTGTTTGGCCAAATGGGAGAGTGGTTATAACACA
  GACGCTACAAACTACAATCCTGGAGATGAAAGCACTGATTATGGGATATTTCAGATCAAT
  AGCCGCTACTGGTGTAATAATGGCAAAACCCCAGGAGCAGTTAATGCCTGTCATATATCC
  TGCAATGCTTTGCTGCAAAATAACATCGCTGATGCTGTAGCTTGTGCAAAGAGGGTTGTC
  AGTGATCCACAAGGCATTCGAGCATGGGTGGCATGGAAAAAGCACTGTCAAAACAGAGAT
  GTCAGTCAGTATGTTGAAGGTTGTGGAGTA

  >Pne_langur
  AAGATCTTTGAAAGGTGTGAGTTGGCCAGAACTCTGAAAAAATTGGGACTGGATGGCTAC
  AAGGGAGTCAGCCTAGCAAACTGGGTGTGTTTGGCCAAATGGGAGAGTGGTTATAACACA
  GAAGCTACAAACTACAATCCTGGAGACGAAAGCACTGATTATGGGATATTTCAGATCAAT
  AGCCGCTACTGGTGTAATAATGGCAAAACCCCAGGAGCAGTTGATGCCTGTCATATATCC
  TGCAGTGCTTTGCTGCAAAACAACATCGCTGATGCTGTAGCTTGTGCAAAGAGGGTTGTC
  AGTGATCCACAAGGCGTTCGAGCATGGGTGGCATGGAGAAATCACTGTCAAAACAAAGAT
  GTCAGTCAGTACGTTAAAGGTTGTGGAGTG

  >Mmu_rhesus
  AAGATCTTTGAAAGGTGTGAGTTGGCCAGAACTCTGAAAAGATTGGGACTGGATGGCTAC
  AGGGGAATCAGCCTAGCAAACTGGGTGTGTTTGGCCAAATGGGAGAGTAATTATAACACA
  CAAGCTACAAACTACAATCCTGGAGACCAAAGCACTGATTATGGGATATTTCAGATCAAT
  AGCCACTACTGGTGTAATAATGGCAAAACCCCAGGAGCAGTTAATGCCTGTCATATATCC
  TGCAATGCTTTGCTGCAAGATAACATCGCTGATGCTGTAACTTGTGCAAAGAGGGTTGTC
  AGTGATCCACAAGGCATTAGAGCATGGGTGGCATGGAGAAATCACTGTCAAAACAGAGAT
  GTCAGTCAGTATGTTCAAGGTTGTGGAGTG

  >Ssc_squirrelM
  AAGGTCTTCGAAAGGTGTGAGTTGGCCAGAACTCTGAAAAGGCTTGGAATGGATGGCTAC
  AGGGGAATCAGCCTAGCAAACTGGATGTGTTTGGCCAAATGGGAGAGTGACTATAACACA
  CGTGCTACAAACTACAATCCTGGAGACCAAAGCACTGATTATGGGATATTTCAGATCAAT
  AGCCACTATTGGTGTAATAATGGCAGAACCCCAGGAGCAGTTAATGCCTGTCATATATCC
  TGCAATGCTTTGCTGCAAGATGACATCACTCAAGCTGTGGCCTGTGCAAAGAGGGTTGTC
  CGTGATCCACAAGGCATTAGAGCATGGGTGGCATGGAAAGCTCATTGTCAAAACAGAGAT
  GTCAGTCAGTATGTTCAAGGTTGTGGAGTA

  >Cja_marmoset
  AAGGTCTTTGAAAGGTGTGAGTTGGCCAGAACTCTGAAAAGGTTTGGACTGGATGGCTAC
  AGGGGAATCAGCCTAGCAAACTGGATGTGTTTGGCCAAATGGGAGAGTGATTATAACACA
  CGTGCTACAAACTACAATCCTGGAGACCAAAGCACTGATTATGGGATATTTCAGATCAAT
  AGCCACTATTGGTGTAACAATGGCAGAACCCCAGGAGCAGTTAATGCCTGTCATATATCC
  TGCAATGCTTTGCTGCAAGATGACATCACTGAAGCTGTGGCCTGTGCAAAGAGGGTTGTC
  CGCGATCCACAAGGCATTAGGGCATGGGTGGCATGGAAAGCTCATTGTCAAAACAGAGAT
  GTCAGTCAGTATGTTCAAGGTTGTGGAGTA
  """

    tree.link_to_alignment(fasta_txt)

    for leaf in tree:
        print(leaf)
        print(leaf.name)
        print(leaf)
        print(leaf.sequence)
        print(leaf.node_id)

    # node_ids = get_node_ids(tree, ["Ssc_squirrelM"])
    node_ids = get_mrca_node_ids(tree, ["Cgu/Can_colobus", "Pne_langur"])
    print(node_ids)

    tree.mark_tree(node_ids, marks=["#1"] * len(node_ids))
    print(tree.write())

    run_branch_model(tree)


def site_model(tree):
    return 0


def run_branch_model(tree):
    tree.run_model("M0")
    tree.run_model("b_free")
    tree.run_model("b_neut")

    m0 = tree.get_evol_model("M0")
    b_free = tree.get_evol_model("b_free")
    b_neut = tree.get_evol_model("b_neut")

    print(b_free.branches.values())

    p_free_m0 = tree.get_most_likely("b_free", "M0")
    p_free_neut = tree.get_most_likely("b_free", "b_neut")

    print("{:.7g}".format(p_free_m0))
    print("{:.7g}".format(p_free_neut))


def run_branch_site_model(tree):
    tree.run_model("M0")
    tree.run_model("bsA")
    tree.run_model("bsA1")

    m0 = tree.get_evol_model("M0")
    bsA = tree.get_evol_model("bsA")
    bsA1 = tree.get_evol_model("bsA1")

    # print(bsA.sites["BEB"])

    for site, aa in enumerate(bsA.sites["BEB"]["aa"]):
        prob = bsA.sites["BEB"]["p2"][site]
        if prob > 0.95:
            print(
                "Positively selected site %s at position: %s, with probability: %s"
                % (aa, site, prob)
            )

    p_bsA_bsA1 = tree.get_most_likely("bsA", "bsA1")
    p_bsA1_m0 = tree.get_most_likely("bsA1", "M0")

    print(p_bsA_bsA1)
    print(p_bsA1_m0)


def get_node(tree, node):
    res = tree.search_nodes(name=node)
    if len(res) > 1:
        exit("ERROR: more than 1 node with name: %s" % node)
    elif len(res) < 1:
        try:
            res = tree.search_nodes(node_id=int(node))
        except ValueError:
            exit("ERROR: node %s not found" % node)
        if len(res) < 1:
            exit("ERROR: node %s not found" % node)
    return res[0]


def get_node_ids(tree, names: list[str]) -> list[int]:
    node_ids = [leaf.node_id for leaf in tree if leaf.name in names]
    return node_ids


def get_mrca_node_ids(tree, names: list[str]) -> list[int]:
    node_ids = [get_node(tree, name) for name in names]
    anc = tree.get_common_ancestor(node_ids)
    return [anc.node_id]


if __name__ == "__main__":
    main()
