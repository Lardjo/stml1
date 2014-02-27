App = Ember.Application.create();

App.Router.map(function() {
    this.resource('matches');
    this.resource('players');
    this.resource('heroes');
    this.resource('events');
});