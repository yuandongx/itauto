

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function postModalData(){

	 $.ajax({
                url : "/api/add-host",
                type : "POST",
                data : $(this).serialize(),
				headers: {
					"X-CSRFToken": getCookie("csrftoken") 
				},
                success : function(data) {
                    console.info(data);
					$('.modal .fade').modal("hide");
                },
                error : function(data) {
                    console.warn(data);
					$('.modal .fade').modal("hide");
                }
            });
	 
		$('#Modal1').modal('hide')
            return false;
}