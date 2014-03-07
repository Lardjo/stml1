App.MatchIndexController = Ember.ArrayController.extend({
    needs: 'match',
    match: Ember.computed.alias("controllers.match")
});

App.MatchAbilitiesController = Ember.ArrayController.extend({
    needs: 'match',
    match: Ember.computed.alias("controllers.match")
});