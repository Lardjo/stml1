App.StatusRoute = Ember.Route.extend({
    model: function() {
        return Ember.$.getJSON('status');
    }
});
