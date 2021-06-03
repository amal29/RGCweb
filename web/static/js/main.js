$(document).ready(function () {
  $("#formid").submit(function () {
    // catch the form's submit event
    console.log("hai form");

    $.ajax({
      // create an AJAX call...
      data: $(this).serialize(), // get the form data
      type: $(this).attr("method"), // GET or POST
      url: "snt",

      success: function (response) {
        if (response == "Success") {
          $(".contactform").find(".output_message").addClass("success");
          $(".output_message").text("Message Sent!");
          $("#out").delay(500000).fadeOut();

          window.location.reload();
        } else {
          $(".contactform").find(".output_message").addClass("error");
          $(".output_message").text("Error Sending!");
          $("#out").delay(500000).fadeOut();

          window.location.reload();
        }
      },
    });

    return false;
  });
});
