############################################
# This is a reference script with basic R syntax,
# based partly on https://www.cyclismo.org/tutorial/R/
# and partly on course notes.
############################################

setwd('/users/david/documents/github/R')

##########################
### 1 Basic Data Types ###
##########################

a <- 3
b <- a^2+4
v <- c(1,1,2,3,5)
v+1 # a new vector with each element increased by 1
c <- "hello there"        	 	
A <- TRUE

typeof(a) # double
typeof(v) # double
typeof(c) # character
typeof(A) # logical

# more on logicals
B <- FALSE
!B
A||B
A&&B
xor(A,B) # true iff exactly one is true	


##############################
### 2 Input and indexing   ###
##############################

# vectors:
hello <- c(1,1,2,3,5)
goodbye <- c(7,6,8,9,NA)
goodnight <- seq(1,5,by=1)

# c() concatenates vectors (it doesn't make a vector of vectors)
hg <- c(hello,goodbye,goodnight)
hg

# Indexing with logicals
b <- c(TRUE,TRUE,FALSE,FALSE,TRUE)
hello[b]
sum(hello[b])

# Missing values: NA, na.rm (NA remove?), is.na()
sum(goodbye)            # returns NA
sum(goodbye,na.rm=TRUE) # remove NA's
is.na(goodbye)
sum(goodbye[!is.na(goodbye)])

# Indexing vectors with conditions
hello<2
hello[hello<2]

# matrices:
M <- matrix(c(4,3,2,5,7,6),ncol=3,byrow=TRUE) # byrow=TRUE useful if you don't know how many rows you'll need
M

# adding row and column names to matrices:
colnames(M) <- c("A","B","C")
rownames(M) <- c("1","2")

# cbind() and rbind() turn vectors into matrices
hgc=cbind(hello,goodbye,goodnight)
hgc

hgr=rbind(hello,goodbye,goodnight)
hgr

# selecting by index from a matrix

hgc[3,] # row 3, all columns
hgc[,2]

# data.frame() turns a matrix into a dataframe
hgd <- data.frame(hgc)
hgd

# alternatively, you can create a dataframe directly from vectors
h <- c(1,1,2,3,5)
g <- c(7,6,8,9,5)
gn <- c(1,2,3,4,5)

hgd <- data.frame(hello=h,goodbye=g,goodnight=gn)
hgd

# add a column (or row) to an existing dataframe either with cbind or with a column reference 
# new row with rbind()
hgd
newrow <- c(9,9,9)
hgd <- rbind(hgd,newrow)
hgd

# new column with column reference
newcol <- c(0,0,0,0,0,0) # throws an error if number of rows mismatched
hgd$newcol <- newcol
hgd

# new column with cbind
newnewcol <- c(10,10,10,10,10,10)
hgd <- cbind(hgd,newnewcol)
hgd


# selecting from a dataframe by index
hgd[,1] # all rows, first column
hgd[,1|2] # all rows, columns 1 and 2

# selecting columns from a dataframe by name
hgd[,"hello"] # returns a vector
hgd[,c("goodbye","hello")]

# selecting from a dataframe with indexing by conditions
# Note that this returns just vectors when a single column is specified
hgd
hgd[hello<=2,c("hello","goodbye")]


# subset() on a dataframe: selecting by condition
# Note that this returns a (smaller) dataframe when a single column is specified,
# rather than a vector as indexing does.
subset(hgd,select=goodbye,hello<=2) # column to select can be specified
subset(hgd,goodbye>6) # defaults to selecting all columns


# order() for dataframes
hgd[order(hgd$goodbye),] # returns a dataframe ordered by 'goodbye'
hgd[rev(order(hgd$hello)),1] # returns just a vector

# read.csv()
monsters <- read.csv(file='/Users/David/Documents/gitHub/R/monsters.csv'
                     ,header=TRUE,sep=',')
monsters

# more basic dataframe navigation
head(monsters,3) # top 3 rows of data
colnames(monsters) # column names
monsters$fangs
attributes(monsters) 
summary(monsters)

# Finally, having created some variables, it's helpful to be able to view them
ls()
ls()[2]
ls()[ls()!="monsters"]







##########################
### 3 Basic Operations ###
##########################

#you can perform operations on numbers and vectors in a straightforward way.
#useful operations: sqrt(),exp(),log()

# useful vector operations: 
# , min(),pmin(), sum(), mean(), median(), quantile(), min(), max(), var(), sd()
# and, finally, summary(), a generic function

a <- c(1,-2,3,-4)
b <- c(-1,2,-3,4)

sd(a)              # Standard deviation: 3.109126
sqrt(var(a))       # 3.109126
quantile(a)

min(a,b)					#Returns the minimum of all the numbers
pmin(a,b)					#Returns a vector with minimum for each place

# sort() for simple vector sorting
c <- sort(a,decreasing=TRUE)
c

# summary()
summary(a) # For a vector, the summary() function just gives quantiles, mean, min, and max.
summary(monsters) # For a dataframe, summary() gives similar information for each column


# adding to an existing dataframe:
monsters$is_mammal <- NA
monsters
monsters$is_mammal <- c(0,1,0,1)

# correctly treating columns as factors:
summary(monsters$is_mammal) # notice that R treats this as a vector
monsters$is_mammal <- factor(monsters$is_mammal)
summary(monsters$is_mammal) # This is a more useful summary


# tables
# table(): create a simple table with factor frequencies
summary(a)            # a is treated as a vector
table(a)              # a is treated as a factor

t <- factor(c("A","A","B","A","B","B","C","A","C"))
results <- table(t)			# Create a simple table with factor frequencies
results

# attributes(): viewing attributes of objects
attributes(results)
attributes(monsters)


# as.table(): creating a table from a matrix:
M <- matrix(c(4,3,2,5,7,6),nrow=2,ncol=3,byrow=TRUE)
colnames(M)<-c("A","B","C")
rownames(M)=c("1","2")
T <- as.table(M)
# P <- as.table(monsters[c("fangs","spots")]) # throws an error: cannot coerce

M
T              # They look almost identical, but they're treated quite differently
summary(M) 
summary(T)     # Summary() on a table counts cases, factors, and checks for independence


# two-way table:
a <- c("Sometimes","Sometimes","Never","Always","Always","Sometimes","Sometimes","Never")
b <- c("Maybe","Maybe","Yes","Maybe","Maybe","No","Yes","No")
results <- table(a,b)
results


# Now, a slightly more complex dataframe:
# The Trees91 dataset, from http://cdiac.ornl.gov/ftp/ndp061a/trees91.wk1,
# as described at https://www.cyclismo.org/tutorial/R/input.html

tr <- read.csv('trees91.csv')
names(tr)
head(tr)

# correctly treating columns as factors
tr$CHBR
summary(tr$CHBR) #Automatically and correctly treats this column as a factor, so a summary returns a tally of the number of observations having that factor
tr$C
summary(tr$C)		#R automatically treats this as a vector, but it's really a factor

tr$C <- factor(tr$C) #Tell R to treat this column as a factor
summary(tr$C)




#########################################
### 4 Basic probability Distributions ###
#########################################

## d(ensity)
# p(robability up to x)
# q('s and inverse probabilities)
# r(andom)

dnorm(0)  # value of the unit normal density function at 0					
dnorm(0)*sqrt(2*pi) # =1
dnorm(0,mean=1,sd=2)

# vectorization with probability distribution functions:
v <- c(0,1,2,3) 
dnorm(v)

# plot of the unit normal
x <- seq(-5,5,by=.1)			
y <- dnorm(x)
plot(x,y)
plot(x,y,type='h', col='3')      # Other type options: (p)oints, (b)oth, (s)tep, (l)ines.  

# plot of the unit normal cumulative density
x <- seq(-5,5,by=.1)  	
y <- pnorm(x,sd=2,mean=-2)
plot(x,y,type='h',col='5')

# tail probabilities as follows:
pnorm(3)                    # defaults to lower.tail=FALSE
pnorm(3,lower.tail=FALSE)   # that is, upper tail probability at 3 standard deviations
pnorm(3,lower.tail=FALSE)+pnorm(3)   # =1
pnorm(3,mean=10,sd=10)      # shifting the distribution

# qnorm(): inverse of pnorm, probability -> z-score
qnorm(.5)            # z-score of 0 is the mean of the unshifted normal
qnorm(.5,mean=2)     # 2

# rnorm(): random numbers generated according to a normal distribution
rnorm(2, mean=1,sd=3)

y <- rnorm(200)
hist(y)


# Intro to the t-distribution
# t-distribution vs normal:
x <- seq(-5,5,by=.1)
n <- dnorm(x)
t <- dt(x,df=1)
y <- dnorm(x)-dt(x,df=1)

plot(x,n)      # normal density plot
plot(x,t)      # plot of t with one degree of freedom
plot(x,y)      # Here's how the t-distribution with one degree of freedom deviates from the normal

x <- c(-3,-4,-2,-1)
pt(x,df=10)
pt((x-mean(x))/sd(x),df=10) # Here the values of x have been standardized

# binomial distribution:
# dbinom
dbinom(1,2,.5)  # probability of 1 head in two flips of a fair coin
dbinom(0,4,.5)  # 1/16

# plot of a binomial distribution
x <- seq(0,50,by=1)
y <- dbinom(x,50,.2)  # that is, for each value of x, the probability of attaining it in 50 trials with .2 probability of success
plot(x,y)  # This plots P(X=x) for x from 1 to 50 for a binomial with parameters n=50, p=2

# qbinom: given a probability, return # successes
qbinom(.5,2,.5)   # the number of successes with probability of .5 is 1

# rbinom
rbinom(5,10,.9)    # counting successes in five instances of a 10-flip trial of a biased coin

# chisq:
# plotting chisq: dchisq:
x <- seq(0,20,by=.5)
y <- dchisq(x,df=5)
plot(x,y)







########################
### 5 Basic Plotting ###
########################

w1 <- read.csv(file="w1.csv",sep=",",head=TRUE) # the default values
head(w1)
plot(w1) # defaults to a stripchart for one-dimensional data

# stripchart():
stripchart(w1$vals)
stripchart(w1$vals,method="stack") # repeated values are stacked
stripchart(w1$vals,method="jitter") # repeated values are jittered
stripchart(w1$vals
           ,method="stack"
           ,vertical=TRUE)
stripchart(w1$vals
           ,method="stack"
           ,vertical=FALSE
           #,xlim=c(0,5)
           ,ylim=c(-2,3))

# adding labels:
stripchart(w1$vals
           ,method="stack"
           ,vertical=TRUE
           ,main="Leaf Biomass in High CO2"
           ,xlab="Leaf Biomass")

# adding a grid
grid(nx=NA,ny=NULL,lty=3,lwd=3)


# boxplots
boxplot(w1$vals,main="nifty boxplot"
        ,horizontal=TRUE # Displays with main axis (y) horizontal
        ,ylim=c(-1,3)) # Changing the main (y) axis

# histograms
hist(w1$vals)
hist(w1$vals,breaks=12)  # changes width of intervals

# setting axis length
hist(w1$vals)
hist(w1$vals,xlim=c(0,3))
hist(w1$vals,ylim=c(0,30))

# Adding multiple graphs to the same plot with the 'add' option
hist(w1$vals
     ,main='Leaf BioMass in High CO2 Environment'
     ,col=3
     ,xlab='BioMass of Leaves'
     ,ylim=c(0,20))
boxplot(w1$vals
        ,horizontal=TRUE
        ,col=5
        ,at=15.5
        ,add=TRUE
        ,axes=FALSE)
stripchart(w1$vals,add=TRUE,at=17.5,col=6) # Note that if the stripchart is to be displayed above the default histogram range, a higher y-limit needs to be specified.


#########################
### 6 More plotting   ###
#########################

# par() for arranging plots
par(mfrow=c(1,2)) # Now the next two plots will be displayed in a 1x2 matrix,
# filling by rows.

# points(): adding points (or lines) to an existing plot
x <- seq(-5,5,.01)
y <- dnorm(x)
plot(x,y,type='l')
points(x,y+.1,type='l',col='2')
points(x,y+.2,type='l',col='3')
points(x,y+.3,type='l',col='4')
points(x,y+.4,type='l',col='5')

# points(): Superimpose two scatterplots with a legend 
x <- rnorm(10,sd=5,mean=20)
y <- 2.5*x-1+rnorm(10,sd=9,mean=0)
plot(x,y
     ,xlab="Independent"
     ,ylab="Dependent"
     ,main="Normal and uniform"
     ,col=10
     ,pch=1
     ,xlim=c(0,30)
     ,ylim=c(0,80))

x1 <- runif(8,15,25)
y1 <- 2.5*x1+runif(8,-6,6)
points(x1,y1
       ,col=5
       ,pch=2)

legend(0,75               # upper left corner position
       ,c("Normal","Uniform")
       ,col=c(10,5)
       ,pch=c(1,2))

# See also: using the dev.new() command to open multiple graphics windows.

