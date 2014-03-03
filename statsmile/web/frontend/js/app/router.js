App.Router.map(function() {
    this.resource('matches');
    this.resource('match', { path: '/matches/:match_id' }, function() {
        this.route('abilities');
    });
});