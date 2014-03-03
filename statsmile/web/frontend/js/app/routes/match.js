App.MatchRoute = Ember.Route.extend({
    model: function(params) {
      return Ember.$.getJSON('/matches/' + params.match_id);
    }
});
