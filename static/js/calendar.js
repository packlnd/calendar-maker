$(function(ready) {
    $("#btn-download").hide();
    month(1);

    function month(m) {
        $.ajax({
            url: "/month/"+m,
            success: function() {
                updateProgress(m);
                if (m < 12) {
                    month(m+1)
                } else if (m == 12) {
                    stitch();
                }
            }
        });
    }

    function stitch() {
        $.ajax({
            url: "/stitch",
            success: function() {
                updateProgress(16);
                $("#btn-download").show();
            }
        });
    }

    function updateProgress(m) {
        pct = (m*100)/16;
        $("#progress").attr("style", "width:"+pct.toString()+"%;");
    }
});
