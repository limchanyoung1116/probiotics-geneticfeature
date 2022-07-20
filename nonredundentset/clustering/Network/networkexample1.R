library(igraph)
library(MCL)

IDEN <-read.table("C:\\Rdata\\lacto\\pyani\\pheatmap\\Lactococcus\\ANIb_percentage_identity.tab",sep="\t",header=T)
# first row become header

rownames(IDEN) = IDEN$X #(1,1) is empty. so x is automatically indexed

IDEN = IDEN[,-1] # -1 <- exclude column 1

AVIDEN <- IDEN

L = length(IDEN)

for(i in 1:L){
  for(j in 1:L){
    x = (AVIDEN[i,j]+AVIDEN[j,i])/2
    AVIDEN[i,j] = x
    AVIDEN[j,i] = x
  }
}


# average score diagonal

NAVIDEN <- AVIDEN

for(i in 1:L){
  for(j in 1:L){
    if(NAVIDEN[i,j]>=0.995){
      NAVIDEN[i,j]=1
    }
    else{
      NAVIDEN[i,j]=0
    }
  }
}

NEWIDEN <- NAVIDEN

for(i in 1:L){
  for(j in 1:L){
    if(i==j){
      NEWIDEN[i,j]=0
    }
  }
}

#MCL

m_NAVIDEN <- as.matrix(NAVIDEN)

g1 <- graph.adjacency(m_NAVIDEN, mode="undirected", weighted=NULL)
#plot(g1, layout=layout.fruchterman.reingold, vertex.size=4, edge.arrow.size=2, vertex.label.cex=0.01)

mcl(g1, addLoops = FALSE, expansion = 2, 
    inflation = 2, allow1 = TRUE,
    max.iter = 100, ESM = TRUE)



# Leiden, Louvain

m_NEWIDEN <- as.matrix(NEWIDEN)

g2 <- graph.adjacency(m_NEWIDEN, mode="undirected", weighted=NULL)
#plot(g2, layout=layout.fruchterman.reingold, vertex.size=4, edge.arrow.size=2, vertex.label.cex=0.01)

cluster_leiden(
  g2,
  objective_function = c("modularity"),
  weights = NULL,
  resolution_parameter = 1,
  beta = 0.01,
  initial_membership = NULL,
  n_iterations = 2,
  vertex_weights = NULL
)

cluster_louvain(
  g2,
  weights = NULL,
  resolution = 1
)


