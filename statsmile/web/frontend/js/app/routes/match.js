App.MatchRoute = Ember.Route.extend({
    model: function(params) {
        return this.store.find('match', params.match_id);
    },
    actions: {
        goBack: function(){
            this.transitionTo('matches');
        }
    }
});
