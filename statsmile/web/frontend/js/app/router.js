App.Router.map(function() {

    this.resource('status');
    this.resource('faq');
    this.resource('privacy');

    // Matches Tree
    this.resource('matches');
    this.resource('match', { path: '/matches/:match_id' });

    this.resource('heroes');

    this.route('missing', { path: '/*path' });

});

App.MissingRoute = Em.Route.extend({
    redirect: function() {
        this.transitionTo('index');
    }
});