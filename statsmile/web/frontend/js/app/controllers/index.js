toastr.options = {
    positionClass: "toast-bottom-left"
};

App.IndexController = Ember.ObjectController.extend({

  name: '',

  actions: {
    select: function(id) {
      if ("WebSocket" in window) {
        var ws = new WebSocket('ws://'+document.location.host+'/ws?id='+id);
          ws.onopen = function() {
            ws.send(id);
          };
          ws.onmessage = function (evt) {
            toastr.success(evt.data);
            $('#notify')[0].play();
          };
          ws.onclose = function() {
            toastr.warning("Connection is closed...");
          };
      } else {
        toastr.error("WebSocket NOT supported by your Browser!");
      }
    }
  }
});
