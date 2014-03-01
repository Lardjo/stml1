App.MatchesRoute = Ember.Route.extend({
    model: function() {
        return Ember.$.getJSON('matches');
    }
});