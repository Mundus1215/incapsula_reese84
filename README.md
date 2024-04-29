incapsula_reese84破解由JavaScript和HTML5编译
安装nodejs:https://nodejs.org/en/download
安装python：https://www.python.org/downloads/windows/
python模块:
pip install flask
如何去引用Reese84.js:
const reeseReturnSuccess = (data) => {
        console.log(JSON.stringify(data))
        var div=document.getElementById("reese_84_id");
        div.innerText=JSON.stringify(data)
        //通过flask提供接口把生成的p值参数保存（有什么好方法可以联系）
        $.ajax({
		url: "http://127.0.0.1:12184/get_seese84",
		type: "POST",
		data: {"data":JSON.stringify(data)},
		success: function(res) {
			console.log(res)
		}
	})
        //console.log('Data above is payload.')
    };
    const reeseReturnError = (data) => {
        console.log(data)
        console.log('Data above is from error.')
    };
    var uH_=function(){
        new window.reese84interrogator().interrogate(reeseReturnSuccess,reeseReturnError);

    };
  setInterval(uH_, 1000);
