App.MatchIndexView = Ember.View.extend({
    didInsertElement: function () {
        this.$('[data-toggle="tooltip"]').tooltip();
    }
});