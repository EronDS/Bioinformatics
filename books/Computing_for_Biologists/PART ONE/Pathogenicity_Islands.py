import geneticfunctions as genf

# Finding Abnormal values for GCcontent (Pathogenicity Islands)
# pathogenicity island – a part of a bacterial genome containing genes involved in infections and diseases 


genf.GCcontent('CGAA')
genf.Transcription('TCGA')

genf.CCAAT_boxes('CCAATGCTA')
genf.multi_CCAAT_boxes(['CCAATGCT', 'CG', 'GCCAATGCCAAT'])