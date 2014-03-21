App.Router.map(function() {

    this.resource('status');
    this.resource('faq');
    this.resource('privacy');

    // Matches Tree
    this.resource('matches');
    this.resource('match', { path: '/matches/:match_id' });

    // Users
    this.resource('players');
    this.resource('player', { path: '/players/:steam_id32' }, function() {
        this.resource('player.matches', { path: '/matches'});
        this.resource('player.heroes',  { path: '/heroes' });
        this.resource('player.records', { path: '/records'});
    });

    this.resource('heroes');

    this.route('missing', { path: '/*path' });

});

App.MissingRoute = Em.Route.extend({
    redirect: function() {
        this.transitionTo('index');
    }
});