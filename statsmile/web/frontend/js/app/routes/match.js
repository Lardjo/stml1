App.MatchRoute = Ember.Route.extend({

    /*Ember.$.set('[data-toggle="tooltip"]').tooltip();*/

    model: function(params) {
      return Ember.$.getJSON('/matches/' + params.match_id);
    }
});
