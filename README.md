<b><h2>Inferring the relative contributions of evolutionary processes shaping X chromosome dynamics in the common marmoset (Callithrix jacchus) in the presence of twinning and hematopoietic chimerism</b></h2>  

<b>Vivak Soni, Cyril J. Versoza, Devangana Shah, Susanne P. Pfeifer, and Jeffrey D. Jensen.</b>

Data and code to perform analysis: 

<b>scripts/marm_X.slim</b> - SLiM script to run simulations of marmoset X chromosome demographic model under neutrality.<br>
<b>scripts/marm_X_null.slim</b> - SLiM script to run simulations of marmoset X chromosome demographic model, incorporating a DFE to model purifying and background selection.<br>
<b>scripts/get_samples_X.slim</b> - python script to get chimieric samples from simulated vcf.<br>
<b>scripts/get_summary_stats_X.slim</b> - python script to estimate summary statistics from chmimeric vcf.<br>
<b>scripts/marmosetX_generate_maps.ipynb</b> - jupyter script for generating mutation and recombination maps for simulations, as well as genomic segments for null threshold simulations.<br>
<b>scripts/marmosetX_plot_results.ipynb</b> - jupyter script to generate figures in manuscript.
<br>
<br>

<b>100kb_divergence.bed</b> - X chromosome divergence between <i>C. jacchus</i> and humans, calculated across 100kb windows, with a 50kb step size.
<br>
<br>

<b>demog.tar.gz:</b>

<b>demog/10ind.X.non-PAR.demog.vcf.gz</b> - vcf file containing variation data for 10 individuals sampled for this study, from non-functional, unlinked regions.<br>
<b>demog/demog_stats.txt</b> - summary statistics for empirical data, calculated over 10kb windows with a 5kb step size.<br>
<b>demog/*.stats</b> - summary statistics for simulations performed under the marmoset demographic model under neutrality for a range of sex ratios, with 100 replicates performed per sex ratio (file naming convention is {sex_ratio}_rep{replicate}_chimeric.stats).
<br>
<br>

<b>recombination.tar.gz</b>:

<b>recombination/empirical/10ind.X.snps.phased.seg.recode.females.vcf.gz</b> - variation data for recombination rate analysis.<br>
<b>recombination/empirical/*.bed</b> - results of empirical recombination rate inference with LDhat and pyrho, with rates averaged across 100kb windows.<br>
<b>recombination/simulation/</b> - folders containing recombination rate inference on simulations run for benchmarking with LDhat and pyrho.
<br>
<br>

<b>genome_scans.tar.gz</b>:

<b>genome_scans/10ind.X.non-PAR.selection.vcf.gz</b> - variation data for performing genome scans.<br>
<b>genome_scans/1mb_gene.counts.bed</b> - counts of genes across 1mb genomic windows.<br>
<b>genome_scans/X_BM.aff</b> - input file for B_0MAF scans for balancing selection.<br>
<b>genome_scans/X_SF2.aff</b> - input file for SweepFinder2 scans for selective sweeps.<br>
<b>genome_scans/X_SF2.grid</b> - input file for SweepFinder2, listing positions at which to perform inference.<br>
<b>genome_scans/BM.out</b> - results of balancing selection scans using B_0MAF.<br>
<b>genome_scans/BM_genes.out</b> - candidate genes from balancing selection scans using B_0MAF.<br>
<b>genomes_scans/SF2.out</b> - results of scans for selective sweeps using SweepFinder2.<br>
<b>genomes_scans/SF2_genes.out</b> - candidate genes from scans for selective sweeps using SweepFinder2.<br>
<b>genome_scans/segments_by_exon_X.bed</b> - bed file containing coordinates for each genomic segment to simulate for null thresholds.
