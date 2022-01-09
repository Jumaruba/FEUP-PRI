export const badSentimentQuery = (userInput) => {
    return `http://localhost:9000/solr/reviews/select?q=title:"${userInput}" rating:[0 TO 3]&q.op=AND&defType=edismax&indent=true&
      bf=if(termfreq(review_text,amazing),div(termfreq(review_text,disappointed),termfreq(review_text,amazing)),termfreq(review_text,disappointed))^20 div(1,sum(rating,1))^5
      &rows=16&wt=json`;
} 