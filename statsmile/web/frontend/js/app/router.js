App.Router.map(function() {
    this.resource('status');
    this.resource('faq');
    this.resource('privacy');

    // Matches Tree
    this.resource('matches');
    this.resource('match', {path: '/matches/:match_id'});

    // Heroes Tree
    this.resource('heroes', function() {
        this.route('popular');
        this.route('gold');
    });

    this.resource('hero');

});