def findGene(gene):
    final = ""
    genep = gene.split("ATG")
    for part in genep:
        for chr in part:
            for i in range(0, len(chr)):
                if genePool(chr[i:i + 3]) == 1:
                    break
                else:
                    final += (chr[i+i + 3] + "\n")
    return final

def genePool(part):
    g1 = "ATG"
    g2 = "TAG"
    g3 = "TAA"
    g4 = "TGA"
    if (part.count(g1) != 0) or (part.count(g2) != 0) or (part.count(g3) != 0) or (part.count(g4) != 0):
        return 1

def main():
    geneinput = input("Enter a genome string: ")
    string =



if __name__ == "__main__":
    main()
