$(document).ready(function () {
  $("#follow_user_form").on("submit", function (e) {
    e.preventDefault();
    const form_data = $("#follow_user_form").serializeArray();
    $.ajax({
      type: "post",
      url: window.location + "follow/",
      data: form_data,
      success: function (response) {
        const username = $("#username").html();
        let followers_count = parseInt($("#followers-count").text());
        if (response["message"] === "success") {
          $("#messages").append(
            "<p class='success'>You are now following " + username + "</p>"
          );
          $("#follow_submit").val("Unfollow");
          $("#user_action").val("Unfollow");
          $("#followers-count").text((followers_count += 1));
        } else if (response["message"] === "info") {
          $("#messages").append(
            "<p class='info'>You have unfollowed " + username + "</p>"
          );
          $("#follow_submit").val("follow");
          $("#user_action").val("follow");
          $("#followers-count").text((followers_count -= 1));
        } else {
          $("#messages").append(
            "<p class='error'>Unable to follow user " + username + "</p>"
          );
        }
      },
    });
  });

  $(".like-form").on("submit", function (e) {
    e.preventDefault();

    let form_data = {};
    const form_elements = this.elements;
    for (let i = 0; i < form_elements.length - 1; i++) {
      form_data[form_elements[i].name] = form_elements[i].value;
    }
    console.log(form_data);
    console.log(window.location.origin);

    $.ajax({
      type: "post",
      url: window.location.origin + "/like/" + form_data["whisper_id"] + "/",
      data: form_data,
      success: function (response) {
        if (response["message"] === "success") {
          window.location.reload();
        }
      },
    });
  });
});
