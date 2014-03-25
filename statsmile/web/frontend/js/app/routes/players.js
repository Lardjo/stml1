/**
 * Created by Konstantin on 23.03.14.
 */
App.PlayersRoute = Ember.Route.extend({
    model: function() {
        return this.store.find('player');
    },
    setupController: function(controller, model) {
        controller.set('model', model);
    }
});

App.PlayerRoute = Ember.Route.extend({
    model: function(params) {
        return this.store.find('player', params.steam_id32);
    }
});

App.PlayerMatchesRoute = Ember.Route.extend({
    model: function() {
        var user_id = this.modelFor("player");
        return this.store.find('match', { account_id: user_id.id });
    }
});

App.PlayerSerializer = DS.RESTSerializer.extend({
    primaryKey: 'steam_id32'
});