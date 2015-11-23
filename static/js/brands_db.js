function make_visible(){
    $("tr#add_row").removeClass("hidden");
    $("button#add_row_btn").addClass("hidden");
}

function edit_fields(id){
    table = document.getElementById("table_" + id);
    
    table.cells[0].innerHTML = "<input form='edit_" + id + "' type='text' name='brand-name' maxlength='25' value='" + table.cells[0].innerHTML.trim() + "'>";
    table.cells[1].innerHTML = "<input form='edit_" + id + "' type='text' name='industry' maxlength='20' value='" + table.cells[1].innerHTML.trim() + "'>";
    table.cells[2].innerHTML = "<input form='edit_" + id + "' type='number' name='foundation' placeholder='Year' min='1800' max='2015' value='" + parseInt(table.cells[2].innerHTML) + "'>";
    table.cells[3].innerHTML = "<input form='edit_" + id + "' type='text' name='website' maxlength='25' value='" + table.cells[3].innerHTML.trim() + "'>";
    table.cells[4].innerHTML = "<input form='edit_" + id + "' type='text' name='imagelink' maxlength='50' value='" + table.cells[4].innerHTML.trim() + "'>";
    table.cells[5].innerHTML = "<input form='edit_" + id + "' type='text' name='description' maxlength='75' value='" + table.cells[5].innerHTML.trim() + "'>";
    
    $(document.getElementsByClassName("edit_delete_forms_" + id)).html("<button form='edit_" + id + "' class='edit_finalize_button green' name='edit' value='" +id+"' type='submit'>" +
	    "<span class='icon-checkmark'>Update</span>" +
	"</button>" +
    "</form>");
   
    
}
