const nlp = require('compromise');
const baseURL = "http://localhost:9000/solr";

export const badSentimentQuery = (userInput) => {
    return `${baseURL}/reviews/select?q=title:"${userInput}" rating:[0 TO 3]&q.op=AND&defType=edismax&indent=true&
      bf=if(termfreq(review_text,amazing),div(termfreq(review_text,disappointed),termfreq(review_text,amazing)),termfreq(review_text,disappointed))^20 div(1,sum(rating,1))^5
      &rows=16&wt=json`;
} 

export const goodSentimentQuery = (userInput) => {
    return `${baseURL}/reviews/select?q=title:"${userInput}" rating:[4 TO 5]&q.op=AND&defType=edismax&indent=true&
    bf=if(termfreq(review_text,disappointed),div(termfreq(review_text,amazing),termfreq(review_text,disappointed)),termfreq(review_text,amazing))^20 sum(rating,1)^5
    &rows=10&wt=json`
}

export const thematicSearch = (userInput) => {
    const filterUserInput = (input) => {
        let doc = nlp(input).tag(); 
        doc.nouns().toSingular();
        doc.verbs().toInfinitive(); 
        let filteredInput = joinResult(doc.nouns().data(), ""); 
        filteredInput = joinResult(doc.verbs().data(), filteredInput);
        filteredInput = joinResult(doc.adjectives().data(), filteredInput); 
        return filteredInput
    }
    userInput = filterUserInput(userInput);
    // TODO: delete console
    console.log(`Thematic Search: ${userInput}`);
    return `${baseURL}/books/query?q=description:${userInput}&q.op=OR&defType=edismax&indent=true&qf=description%5E2&ps=4&rows=40`
}

/**
 * Extracts the named entity from the text and gives a boost to this named entity.  
 * Case the program doesn't identify a named entity, the full user input is used to perform the query.
 * @param {String} userInput The input given by the user. 
 * @returns 
 */
export const namedEntitySearch = (userInput) => {
    const filterUserInput = (input) => {
        let doc = nlp(input).tag(); 
        let namedEntities = doc.topics().data();
        if (namedEntities.length === 0) return input; 
        let filteredInput = joinResult(namedEntities, "");
        return filteredInput
    }
    userInput = filterUserInput(userInput);
    // TODO: delete console
    console.log(`Named entity: ${userInput}`);
    return `${baseURL}/books/select?defType=edismax&q="${userInput}"~5^10&qf=description^1&rows=10`
}

export const scientificBooksSearch = (userInput) => {
    return `${baseURL}/books/select?q.op=AND&defType=edismax&q=science -genres:fiction -genres:\"historical-fiction\"&bq=genres:\"non-fiction\"^4&qf=description title`
}

export const authorSearch = (userInput) => {
    return `${baseURL}/books/select?q=authors-space:"${userInput}" authors:"${userInput}"&q.op=OR&indent=true&defType=edismax&qs=2&wt=json`
}

/**
 * Get's the elements from the nlp.data() and append the text of each instance in a string. 
 * @param {Array} result The nlp.data() array of dictionaries. 
 * @param {String} str The string to have the texts appended to. 
 * @returns {String}
 */
 const joinResult = (data, currStr) => {
    if (data.length === 0) return currStr;
    return data.reduce((acc, currResult) => {return acc + " " + currResult.text}, currStr);
  }
