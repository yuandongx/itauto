
function webChannel(rome, token){
	if ("WebSocket" in window)
		{
		   alert("您的浏览器支持 WebSocket!");

		   // 打开一个 web socket
		   var ws = new WebSocket("ws://" + window.location.host + rome + token + "/" );
		   ws.onopen = function (evt){
			   var data = {"type": "ansible.cli", "token": token, "message": "websocket connected."}
			   ws.send(JSON.stringify(data));
		   };
		   ws.onmessage = function (evt) 
		   { 
			  var received_msg = evt.data;
			  alert("数据已接收..." + received_msg);
		   };
			
		   ws.onclose = function()
		   { 
			  // 关闭 websocket
			  alert("连接已关闭..."); 
		   };
		}
		
		else
		{
		   // 浏览器不支持 WebSocket
		   alert("您的浏览器不支持 WebSocket!");
		}
}


function start_exec_cli(){

	var hosts = new Array();
	$("#hosts-list").children().each(function(){
		hosts.push($(this).attr("name"));
	});
    $("#cli-result-modal-dialog").modal("show");
	$.ajax({
        url: "/tasks/cli/exec",
		headers: {
			"X-CSRFToken": getCookie("csrftoken") 
		},
        type: "POST",
        data: hosts,
        success: function (result) {
            //refresh_cli_hosts(result);
            // $("#hosts-list-cli").html(result);
			webChannel("/ws/cli/", result.token);
			console.log(result.token);
        },
    });
}


function confirm_select_cli_host(){
    var rows = document.getElementById("cli-hosts-lists").rows;
    var hosts = document.getElementById("hosts-list");
    for(var i=1,l=rows.length; i<l;i++){
        var node = document.createElement("span");
        node.setAttribute("class", "label label-primary");
		node.setAttribute("id", "host-" + rows[i].cells[0].firstChild.id);
		node.setAttribute("name", rows[i].cells[0].firstChild.id);
        node.textContent = rows[i].cells[2].textContent + "(" + rows[i].cells[1].textContent+")";
        var ig = document.createElement("i");
        ig.setAttribute("class", "glyphicon glyphicon-remove");
        ig.addEventListener("click", function(){
			var id = $(this).parent().attr("id");
			document.getElementById("hosts-list").removeChild(document.getElementById(id));
		});
		node.appendChild(ig);
        hosts.appendChild(node);
    }
	$("#modalHostList").modal('hide');
}


function getCliHosts(target){

	var id = target.id;
	if (id == "btn-select-hosts") {
		$("#page-1").addClass("active");
	}
	var active_page = $("#page-item-1").text();
	if ($("#page-2").hasClass("active")){
		active_page = $("#page-item-2").text();
	} else if ($("#page-3").hasClass("active")){
		active_page = $("#page-item-3").text();
	}
	var num_active = Number(active_page);
	console.log("active: " + active_page);
	var page = {"page": "1"};
	if (id == "page-item-1" || id == "page-item-2" || id == "page-item-3") {
		page.page = $(target).text();
		console.log("1");
	} else if (id == "page-previous"){
		if (num_active > 1){
			page.page = (num_active - 1).toString();
		} else {
			return false;
		}
		console.log("2");
	} else if (id == "page-next"){
		//if ($("#page-next").prop("disable") == false){
		//	page.page = (num_active + 1).toString();
		//}
		page.page = (num_active + 1).toString();
		console.log("3");
	} else{
		console.log("4");
	}
	$("#page-1").removeClass("active");
	$("#page-2").removeClass("active");
	$("#page-3").removeClass("active");
	console.log(page);
	console.log("5");
    $.ajax({
        url: "/tasks/cli/get-hosts",
        type: "GET",
		data: page,
        success: function (result) {
			var num_pages = Number(result.num_pages);
			var current_number = Number(result.number);
			if (num_pages > 0) {
				$("#page-1").show();
			}
			if (num_pages > 1) {
				$("#page-2").show();
			}
			if (num_pages > 2) {
				$("#page-3").show();
			}
			if (current_number == 1){
				$("#page-item-1").text("1");
				$("#page-1").addClass("active");
			} else {
				if (num_pages == 2){
					$("#page-item-1").text("1");
					$("#page-item-2").text("2");
					if (current_number == 1) {
							$("#page-1").addClass("active");
							$("#page-previous").prop("disable", true);
						} else {
							$("#page-2").addClass("active");
							$("#page-previous").prop("disable", false);
						}
				} else if (num_pages > 2){
					if (current_number == num_pages){
						$("#page-item-3").text(current_number);
						$("#page-3").addClass("active");
						$("#page-item-2").text(current_number - 1);
						$("#page-item-1").text(current_number - 2);
						$("#page-next").prop("disable", true);
					} else {
						$("#page-item-3").text(current_number + 1);
						$("#page-2").addClass("active");
						$("#page-item-2").text(current_number);
						$("#page-item-1").text(current_number - 1);
						$("#page-next").prop("disable", false);
					}
				}
			}
            $("#hosts-list-cli").html(result.rows);

        },
    });
    return false;
}


function select_table_all_rows(){

    var all_checked = $("#select-all-hosts").prop("checked");
    $("#cli-hosts-lists").find("input").each(function(){
        if(all_checked){
            $(this).prop("checked", true);
        } else{
            $(this).prop("checked", false);
        }
    });
}

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
	 
		$('#Modal1').modal('hide');
            return false;
}

function submit_host_type(){
	
}