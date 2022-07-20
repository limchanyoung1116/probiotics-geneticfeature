IDEN <-read.table("C:\\Rdata\\lacto\\pyani\\pheatmap\\Lacticasei\\ANIb_percentage_identity.tab",sep="\t",header=T)
#header=T means first row become header

rownames(IDEN) = IDEN$X # 1row 1column is empty. so x is automatically indexed. names exist on colx 

library(pheatmap)

IDEN = IDEN[,-1] # -1 means exclude column 1

IDEN[1:5, 1:5]

# splitting start

L = length(IDEN)

AVIDEN <- IDEN
# IDEN diagonal average
  
for(i in 1:L){
  for(j in 1:L){
    x = (AVIDEN[i,j]+AVIDEN[j,i])/2
    AVIDEN[i,j] = x
    AVIDEN[j,i] = x
  }
}

# score > 0.95

pheatmap(AVIDEN)
SOR <- pheatmap(AVIDEN)

ro <- SOR$tree_row$order
co <- SOR$tree_col$order

NEW <- AVIDEN[,ro]
NEWIDEN <- NEW[co,]

# score 0.95

v <- 0
a <- 1
i <- 1
x <- 0
j <- 0
k <- 0

while(i < L){
  for(j in a:L){
    for(k in a:j){
      if(NEWIDEN[j,i]<0.95){
        x = j
        v = c(v,x)
        break
      }
    }
    if(x==j){
      break
    }
  }
  a = x+1
  i = a+1
  if(j==L){
    break
  }
}

print(v)

# score > 0.98

v1 <- 0
a1 <- 1
i1 <- 1
x1 <- 0
j1 <- 0
k1 <- 0

while(i1 < L){
  for(j1 in a1:L){
    for(k1 in a1:j1){
      if(NEWIDEN[j1,i1]<0.98){
        x1 = j1
        v1 = c(v1,x1)
        break
      }
    }
    if(x1==j1){
      break
    }
  }
  a1 = x1+1
  i1 = a1+1
  if(j1 == L){
    break
  }
}
v1 = c(v1,L)
print(v1)

# score > 0.99

# group length

ii = 1
jj = 1

l = length(v1-1)
le = NULL

for(ii in 1:l){
  kk = v[ii+1]-v[ii]
  le = c(le,kk)
}

le3 = length(le)
le = le[1:le3-1]
le2 = sum(le)
le[le3] = L - le2

print(le)

# group compare

csta = NULL
cend = NULL
rsta = NULL
rend = NULL

ii1 = 0
jj1 = 0

for(ii0 in 1:l){
  for(jj0 in 1:l){
    xx = 0
    if(ii0 != jj0){
      for(ii1 in v1[ii0]:v1[ii0+1]-1){
        for(jj1 in v1[jj0]:v1[jj0+1]-1){
          if(NEWIDEN[ii1,jj1] >= 0.98){
            substitute(xx <- xx+1)
          }
      }
      if(xx == (v1[ii0+1]-1-v1[ii0])*v1[jj0+1]-1-v1[jj0]){
        rsta = c(rsta,v1[ii0])
        rend = c(rsta,v1[ii0+1]-1)
        csta = c(csta,v1[jj0])
        cend = c(cend,vi[jj0+1]-1)
      }
      }
    }
  }
}

AVIDEN[227:230, 227:230]