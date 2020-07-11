
{% load static %}
<li><a href="/home" id="home" class=""><i class="lnr lnr-home"></i> <span>工作台</span></a></li>
<li><a href="/hosts" id="hosts"  class=""><i class="lnr lnr-code"></i> <span>主机管理</span></a></li>
<li>
	<a href="#subPages1" data-toggle="collapse" class="collapsed">
	<i class="lnr lnr-file-empty"></i>
	<span>批量执行</span> 
	<i class="icon-submenu lnr lnr-chevron-left"></i></a>
	<div id="subPages1" class="collapse ">
		<ul class="nav">
			<li><a href="/batch/execute"  class="">执行任务</a></li>
			<li><a href="/batch/template"  class="">模板管理</a></li>
		</ul>
	</div>
</li>
<li><a href="/apps"  class=""><i class="lnr lnr-cog"></i> <span>应用发布</span></a></li>
<li><a href="/schedule"  class=""><i class="lnr lnr-cog"></i> <span>任务计划</span></a></li>
<li>
	<a href="#subPages2" data-toggle="collapse" class="collapsed">
	<i class="lnr lnr-file-empty"></i>
	<span>配置中心</span> 
	<i class="icon-submenu lnr lnr-chevron-left"></i></a>
	<div id="subPages2" class="collapse ">
		<ul class="nav">
			<li><a href="/config/environ"  class="">环境管理</a></li>
			<li><a href="/config/service"  class="">服务配置</a></li>
			<li><a href="/config/apps"  class="">应用配置</a></li>
		</ul>
	</div>
</li>
<li><a href="monitor"  class=""><i class="lnr lnr-cog"></i> <span>监控中心</span></a></li>
<li>
	<a href="#subPages3" data-toggle="collapse" class="collapsed">
	<i class="lnr lnr-file-empty"></i>
	<span>告警中心</span> 
	<i class="icon-submenu lnr lnr-chevron-left"></i></a>
	<div id="subPages3" class="collapse ">
		<ul class="nav">
			<li><a href="notify/log"  class="">告警日志</a></li>
			<li><a href="notify/contacts"  class="">联系人</a></li>
			<li><a href="notify/group"  class="">联系组</a></li>
		</ul>
	</div>
</li>

<li>
	<a href="#subPages4" data-toggle="collapse" class="collapsed">
	<i class="lnr lnr-file-empty"></i>
	<span>系统管理</span> 
	<i class="icon-submenu lnr lnr-chevron-left"></i></a>
	<div id="subPages4" class="collapse ">
		<ul class="nav">
			<li><a href="/system/user"  class="">账户管理</a></li>
			<li><a href="/system/role"  class="">角色管理</a></li>
			<li><a href="/system/device"  class="">系统设备</a></li>
		</ul>
	</div>
</li>