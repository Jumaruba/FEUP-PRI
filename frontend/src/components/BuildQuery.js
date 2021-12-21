const BuildThematicSearchQuery = (search) => {
    const options = {
        "description:" : search,
        "q.op:": "OR",
        "defType:": "edismax",
        "qf:": "description%5E2",
        "ps:": "4",
    }

    let full_query = 'http://localhost:80/solr/books/select?q=';
    for (let option in options)
        full_query += option + options[option] + '&';

    return full_query + 'wt=json';
}

export default BuildThematicSearchQuery;