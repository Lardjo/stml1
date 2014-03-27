/**
 * Created by Konstantin on 23.03.14.
 */
App.PlayersRoute = Ember.Route.extend({
    model: function() {
        return this.store.find('player');
    }
});

App.PlayerRoute = Ember.Route.extend({
    model: function(params) {
        console.log('test');
        return this.store.find('player', params.steam_id32);
    }
});

App.PlayersIndexRoute = Em.Route.extend({
    model: function() {
        return this.modelFor('player');
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

App.FavoriteSerializer = DS.RESTSerializer.extend({
    primaryKey: '_id'
});