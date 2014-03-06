App.Router.map(function() {
    this.resource('status');
    this.resource('faq');
    this.resource('privacy');
    this.resource('matches');
    this.resource('match', { path: '/matches/:match_id' }, function() {
        this.resource('match.abilities', { path: '/abilities' });
    });
});