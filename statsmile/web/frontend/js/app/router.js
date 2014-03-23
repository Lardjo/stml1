App.Router.map(function() {

    this.resource('status');
    this.resource('faq');
    this.resource('privacy');
    this.resource('matches');
    this.resource('heroes');
    this.resource('match', { path: '/matches/:match_id' });
    this.resource('players');

    this.resource('player', { path: '/players/:steam_id32' }, function() {
        this.resource('player.matches', { path: '/matches'});
        this.resource('player.heroes',  { path: '/heroes' });
        this.resource('player.records', { path: '/records'});
    });
});