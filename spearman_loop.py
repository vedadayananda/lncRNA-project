# gene x lncRNA

all_genes = ['a', 'b', 'c']

all_lncRNAs = ['x', 'y', 'z']

all_spearman = np.array([]) # []

for gene in all_genes:
#     print(gene)
    
    samples_gene = get_sample_vals_for_gene(gene)
    
    # vector of GEX values for all samples
    
    for lncRNA in all_lncRNAs:
#         print(lncRNA)
        
        samples_lncRNA = get_sample_vals_for_lncRNA(lncRNA)
        
        # vector of LEX values for all samples
        
        # run spearman
        spearman_corr = sp.spearman(samples_gene, samples_lncRNA)
        
        all_spearman = np.append(all_spearman, spearman_corr)
