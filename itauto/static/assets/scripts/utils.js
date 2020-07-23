
function webChannel(rome, token){
	if ("WebSocket" in window)
		{
		   alert("您的浏览器支持 WebSocket!");

		   // 打开一个 web socket
		   var ws = new WebSocket("ws://" + window.location.host + rome + token + "/" );

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


function getCliHosts(){
    var id = $(this).attr("id");
    $.ajax({
        url: "/tasks/cli/get-hosts",
        type: "GET",
        data: "page=9",
        success: function (result) {
            //refresh_cli_hosts(result);
            $("#hosts-list-cli").html(result);
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