# Temperate phage analysis in-house scirpts
* bacterial_phylogenetic_analysis
	* extract_from_assembly_summary.v2.py: Script integrating the processes of bacterial phylogenetic analysis.
	* core_ope: the assembly-based SNV calling pipeline created by ZheminZhou.
	* multi-process.pl: Script to use multiple CPU processes.
	* fa_stat.pl/fq_stat.pl: Script to acquire the length of each sequence in a fasta/fastq file.
	* nj2phyml_format_v2.pl: Script to convert tree format to phyml format.
	* Repeat_filter.pl: Script to identify the repeat regions in a genome sequence.
	* repeat_to_gff.pl: Script to convert repeat raw formats to gff format.
	* snp_stat-wyr.pl: Script to acquire the final core-snp matrix after removing the snps in repeat regions.
* function_gene
  * Anti-CRIPSR: Scripts to find anti-CRISPR system.
  * Rebase: Scripts to find RM system.
  * ResFinder: Scripts to find antibiotic resistance genes.
  * VFDB: Scripts to find virulent factors.
* data_clustering: Clustering phages with the same or reverse complementary sequences.
  * get_length.py: First obtain the length of every sequence.
  * cluster_length.py: Then cluster the sequences with the same length.
  * cluster_reverse_complement.py: Then cluster the phages with the same sequence.
* add_taxonomy.py: Scripts to add taxonomy to hosts.
* antibiotic_resistance_gene.cys: file for Extended Data Figure 7.
* genomic_island.cys: file for Extended Data Figure 9.
* muliple_host.cys: file for Figure 3A.
* virulent_factor.cys: file for Extended Data Figure 8.
