(function($) {

	'use strict';

	$(function() {

	var runInput = $('.run-input');		// ECS 검색 입력박스

	$('.second-card > .btn-check').on('click', function(){
		runInput.focus();
	})

	// 검색버튼클릭 또는 엔터키
	runInput.on("keydown", function(event) {
		if (event.keycode == 13) {
			getEcsList()
		}
	});
	$('.run-btn').on("click", function(event) {
		getEcsList()
	});

	$('.empty-btn').on("click", function(event) {
		// ecsListItem.empty();
		runInput.val('');
		runInput.focus();
	});

	// ECS 클러스터 리스트 조회
	function getEcsList() {
		var profile = $(".second-card > .btn-check:checked").val();
		var clusterName = runInput.val();

		$.post("/ecs",
			{
				profile: profile,
				clusterName: clusterName
			},
			function(items) {
				addEcs(items)
			}
		);
	}

	var addEcs = function(item) {		// ➎ 항목 추가 함수
		ecsListItem.empty();
		item.Clusters.forEach(e=>{
			ecsListItem.append("<li class='p-0 m-0'><div class='m-0 p-0 form-check'><label class='m-0 p-0 form-check-label'><input class='checkbox' type='checkbox' /><span class='list-group-item-light list-group-item-action clusterItem' id='"+ e.ClusterArn+ "'>" + e.ClusterName + "</span><div></div><i class='input-helper'></i></label></div></li>");
		});
	};

	// 리스트 클릭이벤트 정의
	ecsListItem.on('click', '.clusterItem', function() {
		var profile = $(".second-card > .btn-check:checked").val();
		var clusterArn = $(this).attr('id')

		$.ajax({
			url: "/ecsdetail",
			type: "POST",
			data: {
				profile: profile,
				clusterArn: clusterArn
			},
			context: $(this).next(),
			success: function(items) {
				var ul = document.createElement('ul');
				items.CLusters

				// ECS Cluster 디테일
				if (!!items.Clusters) {
					var cluster = items.Clusters[0];
					// console.log(cluster)
					var li1 = document.createElement('li');
					li1.className="p-0 m-0";

					//var small = document.createElement('small');
					//small.innerHTML = cluster.ClusterArn;
					//li1.appendChild(small)
					//ul.appendChild(li1)

					var li1 = document.createElement('li');
					li1.className="p-0 m-0";
					li1.setAttribute("class", "clusterName");
					li1.setAttribute("id", cluster.ClusterName);


					var small = document.createElement('small');
					small.setAttribute("style", "color:blue");
					small.innerHTML = "&nbsp;&nbsp;➟ <b>Service</b> ✔️: " +	cluster.ActiveServicesCount+"개";
					li1.appendChild(small)

					var small = document.createElement('small');
					small.setAttribute("style", "color:blue");
					small.innerHTML = "&nbsp;&nbsp;&nbsp; <b>Task</b> ✔️: " + cluster.RunningTasksCount + "개, ⌛ : " + cluster.PendingTasksCount+"개";
					li1.appendChild(small)
					ul.appendChild(li1)
					items.ServiceArns.forEach(e=>{
					var li = document.createElement('li');
					li.className="p-0 m-0";
						var parts = e.split('/');
						var svcName = parts.pop();
						li.innerHTML = "&nbsp;&nbsp;&nbsp;&nbsp;<small>" + svcName + "</small>"
						ul.appendChild(li)
					});
				}
				$(this).replaceWith(ul)
			},
		});
	});





	var svcListItem = $('.svc-list');			 // ECS 서비스 리스트
	var svcListInput = $('.svc-list-input');		// ECS 서비스 검색 입력박스

	$('.third-card > .btn-check').on('click', function(){
		svcListItem.empty();
		svcListInput.focus();
	})
	// 검색버튼클릭 또는 엔터키
	svcListInput.on("keydown", function(event) {
		if (event.keyCode == 13) {
			getSvcList()
		}
	});
	$('.svc-list-add-btn').on("click", function(event) {
		getSvcList()
	});

	$('.svc-list-empty-btn').on("click", function(event) {
		svcListItem.empty();
		svcListInput.focus();
	});

	// ECS 서비스 리스트 조회
	function getSvcList() {
		var profile = $(".third-card > .btn-check:checked").val();
		var svcName = svcListInput.val();

		$.post("/svc",
			{
				profile	: profile,
				svcName: svcName
			},
			function(items) {
				addSvc(items)
			}
		);
	}
	var addSvc = function(item) {		// ➎ 항목 추가 함수
		svcListItem.empty();
		item.ServiceArns.forEach(e=>{
			var parts = e.split('/');
			var svcName = parts.pop();

			svcListItem.append("<li class='p-0 m-0'><div class='m-0 p-0 form-check'><label class='m-0 p-0 form-check-label'><input class='checkbox' type='checkbox' /><span class='list-group-item-light list-group-item-action' data-toggle='modal' data-target='#gridSystemModal' class='svcItem' id='"+ e+ "'>" + svcName + "</span><div></div><i class='input-helper'></i></label></div></li>");
		});
	};

	$('.modal-dialog').draggable({
		handle: ".modal-header"
	});
	$('#gridSystemModal').on('shown.bs.modal', function (e) {
		$('.modal-backdrop').remove();
		var profile = $(".third-card > .btn-check:checked").val();
		var row = e.relatedTarget;
		var svcArn = row.id;

		$.ajax({
			url: "/svcdetail",
			type: "POST",
			data: {
				profile: profile,
				svcArn: svcArn
			},
			// context: $(this).next(),
			context: $(this),
			success: function(items) {
				$('.first-row > .first-col').empty();
				$('.first-row > .second-col').empty();
				$('.second-row').empty();
				// $('.third-row').empty();
				// $('.fourth-row').empty();

				// ECS Svc 디테일
				if (!!items.Services) {
					var service = items.Services[0];
					var taskDefinition = items.TaskDefinition;

					var str = "<b>Service</b> : " + service.ServiceName
						+ "<br>&emsp;	ARN : "+ service.ServiceArn
						+ "<br>&emsp;	SG : "+ service.NetworkConfiguration.AwsvpcConfiguration.SecurityGroups
						+ "<br>&emsp;	Subnets :";
					var subnets = service.NetworkConfiguration.AwsvpcConfiguration.Subnets;
					subnets.forEach(subnet=>{
						str += "<br>&emsp;" + subnet
					});
					var div = document.createElement('div');
					div.innerHTML = "<small>" + str +"</small>"
					$('.first-row > .first-col').append(div);

					var str = "<br><b>Task</b> : " + taskDefinition.Family + ":" + taskDefinition.Revision
						+ "<br>&emsp;	ARN : " + taskDefinition.TaskDefinitionArn
						+ "<br>&emsp;	Desired : " + service.DesiredCount + " Running : " + service.RunningCount
						+ "<br>&emsp;	Status : " + taskDefinition.Status
						+ "<br>&emsp;	Cpu : " + taskDefinition.Cpu + " Memory : " + taskDefinition.Memory

					// Running Tasks IP!!!Name
					var tasks = items.Tasks;
					str += "<br>&emsp; <b>Private IPs </b>: "
					tasks.forEach(task=>{
						task.Containers.forEach(container=>{
							// if (container.Name != "log_router" && container.Name != "datadog-agent") {
							// https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-lifecycle.html
							//var lastStatus = "";
							//switch(container.LastStatus) {
								//case "RUNNING":
									//lastStatus = "✔️ ";
									//break;
								//case "STOPPED":
									//lastStatus = "❌ ";
									//break;
								//default:
									//lastStatus = container.LastStatus;
									//break;
							//}
							if (container.Name.includes("ecn")) {
								container.NetworkInterfaces.forEach(network=>{
									str += "<br>&emsp;&emsp; <small>" + container.Name + "&emsp;&emsp;" + network.PrivateIpv4Address + "&emsp;&emsp;" + container.LastStatus + "</small>"
								})
							}
						})
					})
					var div = document.createElement('div');
					div.innerHTML = "<small>" + str +"</small>"
					$('.first-row > .second-col').append(div);

					var str = "<br><b>Containers</b>"
					var containers = taskDefinition.ContainerDefinitions;
					containers.forEach(e=>{
						str += "<br>&emsp;	Name : " + e.Name
							+ "<br>&emsp;	Cpu : " + e.Cpu
							+ "<br>&emsp;	MemoryLimit : " + e.MemoryReservation
							+ "<br>&emsp;	Image : " + e.Image
						var envs = e.Environment;
						str += "<br>&emsp;	Envs : "
						envs.forEach(e=>{
							str +="<br>&emsp;&emsp;	"+ e.Name + "=" + e.Value
						})
						var ports = e.PortMappings;
						str += "<br>&emsp;	Ports : "
						ports.forEach(p=>{
							str += "<br>&emsp;&emsp;		ContainerPort : " + p.ContainerPort
								+ "<br>&emsp;&emsp;		HostPort : " + p.HostPort
								+ "<br>&emsp;&emsp;			Protocol : " + p.Protocol
						})
						str += "<br>&emsp;	LogDriver : " + e.LogConfiguration.LogDriver
						// e.LogConfiguration.Options
						// Options map[string]*string `locationName:"options" type:"map"`
						$.each(e.LogConfiguration.Options, function (key, val) {
							str += "<br>&emsp;&emsp;	 " + key + " : " + val
						})

						str += "<br><hr>"
					})
					var div = document.createElement('div');
					div.innerHTML = "<small>" + str +"</small>"
					$('.second-row').append(div);

				}
				// $(this).replaceWith(ul)
				// $(this).append(ul);
			},
		});
	})

	
	});
})(jQuery);
