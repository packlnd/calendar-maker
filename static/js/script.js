$(function(ready) {
    function readURL(input, month) {
        if (input.files && input.files[0]) {
            var reader = new FileReader();

            reader.onload = function (e) {
                $('img#img-'+month).attr('src', e.target.result);
            }

            reader.readAsDataURL(input.files[0]);
        }
    }

    $("input[id^=browse]").change(function(){
        readURL(this, this.id.split("-")[1]);
    });
});
