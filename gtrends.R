entries <- read.csv("~/R/entries.csv", header=FALSE, stringsAsFactors=FALSE)
country.codes<-read.csv("~/R/codes.csv", header=FALSE, stringsAsFactors=FALSE)
#install gtrendsR
#turn this into a list

#ch<-gconnect(usr='zanynumbers@gmail.com',psw='pipypony')

#split the entries list up into each competition year, add variables later??
for( i in 2013:2016){
  
  x<-subset(entries,V4==i)
  sd<-print(paste0(i,"-03-01"))
  ed<-print(paste0(i,"-05-29"))
  terms<-x[,2]
  
  for(j in 1:nrow(x)){
      country.name<-x[j,1]
      country<-list()
      country[j]<-country.codes[which(country.codes$V1==country.name),]
      output <- lapply(country, function(y){ 
        y <- gsub("\\s+", "\\+", gsub("[-,]", " ", y))
        terms<- gsub("\\s+", "\\+", gsub("[-,]", " ", terms))
        out<- cbind.data.frame(gtrends(query=terms, geo=y, ch, start_date = as.Date(sd),
                                                 end_date = as.Date(ed)))
        out
      })
      results.list<-list()
      results.list[[i]][j]<-out
}}