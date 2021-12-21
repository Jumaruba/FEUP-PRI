function BuildQuery(search) {
    if (search === "romantic") {

    }

    return 'http://localhost:80/solr/books/select?q=description:' + search + '&wt=json';
}

export default BuildQuery;