 $(document).ready(function () {
    toggleFields(); 
    $("#deposit").change(function () {
        toggleFields();
    });

});
// this toggles the visibility of other server
function toggleFields() {
    if ($("#deposit").val() === "fixed")
        $("#fixedamount").show();
    else
        $("#fixedamount").hide();
}