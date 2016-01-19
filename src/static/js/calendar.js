$(function(ready) {
    month(1);
});

function month(m) {
    $.ajax({
        url: "/month/"+m,
        success: function() {
            updateProgress(m);
            if (m < 12) {
                month(m+1)
            }
        }
    });
}

function updateProgress(m) {
    pct = (m*100)/12
    $("progress").attr("width", pct.toString());
}
