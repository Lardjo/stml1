/**
 * Created by Konstantin on 24.03.14.
 */
App.MatchesRoute = Ember.Route.extend({
    model: function() {
        return this.store.find('match');
    }
});

App.MatchRoute = Ember.Route.extend({
    model: function(params) {
        return this.store.find('match', params.match_id);
    }
});

App.MatchSerializer = DS.RESTSerializer.extend({
    primaryKey: 'match_id'
});
