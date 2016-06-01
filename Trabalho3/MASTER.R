Needed <- c("tm", "SnowballCC", "RColorBrewer", "ggplot2", "wordcloud", "biclust", "cluster", "igraph", "fpc")   
install.packages(Needed, dependencies=TRUE)   

install.packages("Rcampdf", repos = "http://datacube.wu.ac.at/", type = "source")    

library(tm) 

# sampling some txts (size of sample = 15)

texts <- file.path(getwd(), "sample")

docs <- Corpus(DirSource(texts))   

summary(docs) 


inspect(docs[2])


docs <- tm_map(docs, removePunctuation)   

docs <- tm_map(docs, removeNumbers)   


docs <- tm_map(docs, tolower)   


docs <- tm_map(docs, removeWords, stopwords("english"))   

library(SnowballC)   
docs <- tm_map(docs, stemDocument) 

docs <- tm_map(docs, stripWhitespace)  

docs <- tm_map(docs, PlainTextDocument)   

dtm <- DocumentTermMatrix(docs)   
dtm   

tdm <- TermDocumentMatrix(docs)   
tdm   

freq <- colSums(as.matrix(dtm))   
length(freq)


dtms <- removeSparseTerms(dtm, 0.1) # This makes a matrix that is 10% empty space, maximum.   
inspect(dtms)  

View(sort(freq))
