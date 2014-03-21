App.PlayersRoute = Ember.Route.extend({
    model: function() {
        return this.store.find('player');
    }
});

App.PlayerSerializer = DS.RESTSerializer.extend({
    primaryKey: 'steam_id32'
});