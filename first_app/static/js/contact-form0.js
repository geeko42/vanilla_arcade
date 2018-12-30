/* ---------------------------------------------
 Contact form
 --------------------------------------------- */
$(document).ready(function(){
    $("#submit_btn").click(function(){

        //get input field values
        var user_email = $('input[name=email]').val();

        //simple validation at client's end
        //we simply change border color to red if empty field using .css()
        var proceed = true;
        if (user_email == "") {
            $('input[name=email]').css('border-color', '#e41919');
            proceed = false;
        }

        //everything looks good! proceed...
        if (proceed) {
            //data to be sent to server
            post_data = {
                'userEmail': user_email,
            };

            //Ajax post data to server
            $.post('contact_me.php', post_data, function(response){

                //load json data from server and output message
                if (response.type == 'error') {
                    output = '<div class="error">' + response.text + '</div>';
                }
                else {

                    output = '<div class="success">' + response.text + '</div>';

                    //reset values in all input fields
                    $('#contact_form0 input').val('');
                    $('#contact_form0 textarea').val('');
                }

                $("#result").hide().html(output).slideDown();
            }, 'json');

        }

        return false;
    });

    //reset previously set border colors and hide all message on .keyup()
    $("#contact_form0 input, #contact_form0 textarea").keyup(function(){
        $("#contact_form0 input, #contact_form0 textarea").css('border-color', '');
        $("#result").slideUp();
    });

});
