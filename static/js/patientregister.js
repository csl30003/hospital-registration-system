function checkUname() {
	//获取用户获得用户名信息
	var uname=document.getElementById("uname").value;

	//创建校验规则,用户名2-4个
	var reg=/^[\u4e00-\u9fa5]{2,4}$/;
	//获取span对象
	var unameSpan=document.getElementById("unameSpan");

	//开始交验
	if (unameSpan==""|| unameSpan==null) {
		//输入校验结果
		unameSpan.innerHTML="<p style='margin-left: 275px;'>*用户名不能为空</p>";
		unameSpan.style.color="red";
		return false;
	}

	else if (reg.test(uname)) {
		//输入校验结果
		unameSpan.innerHTML="<p style='margin-left: 300px;'>*用户名通过</p>";
		unameSpan.style.color="green";
		return true;
	}

	else {
		//输入校验结果
		unameSpan.innerHTML="<p style='margin-left: 275px;'>*用户名格式不符</p>"
		unameSpan.style.color="red";
		return false;
	}

}

function checkPwd() {
	//获取用户获得用户名信息
	var upwd=document.getElementById("pwd").value;

	//创建校验规则,密码要求6-8位，首位为字母，后面5-7位是数字
	var reg=/^[0-9a-zA-Z_]{1,}$/;
	//获取span对象
	var span=document.getElementById("pwdSpan");

	//开始交验
	if (span==""|| span==null) {
		//输入校验结果
		span.innerHTML="<p style='margin-left: 235px; font-size: 10px;'>*密码不能为空</p>";
		span.style.color="red";
		return false;
	}

	else if (reg.test(upwd)) {
		//输入校验结果
		span.innerHTML="<p style='margin-left: 310px; font-size: 10px;'>*密码通过</p>";
		span.style.color="green";
		return true;
	}

	else {
		//输入校验结果
		span.innerHTML="<p style='margin-left: 290px; font-size: 10px;'>*密码格式不符</p>"
		span.style.color="red";
		return false;
	}

	//第一次密码为a123456，第二次密码为a1234567，则修改的第一次密码，确认密码也会重新校验
	checkPwd2();
}

function checkPwd2() {
	//获取第一次校验密码
	var pwd=document.getElementById("pwd").value;
	//获取确认密码
	var pwd2=document.getElementById("pwd2").value;
	//获取span对象
	var span=document.getElementById("pwd2Span");

	//比较前两次密码是否相同
	if (pwd2==""|| pwd2==null) {
		//输入校验结果
		span.innerHTML="<p style='margin-left: 290px; font-size: 10px;'>*密码不能为空</p>";
		span.style.color="red";
		return false;
	}

	else if (pwd===pwd2) {
		//输入校验结果
		span.innerHTML="<p style='margin-left: 310px; font-size: 10px;'>*密码通过</p>";
		span.style.color="green";
		return true;
	}

	else {
		//输入校验结果
		span.innerHTML="<p style='margin-left: 235px; font-size: 10px;'>*密码不同，请重新输入</p>"
		span.style.color="red";
		return false;
	}
}

function checkPhone() {
	var phone=document.getElementById('phone').value;
	var phoneSpan=document.getElementById('phoneSpan');

	var reg=/^1[34578]\d{9}$/;

	if (phoneSpan==""|| phoneSpan==null) {
		phoneSpan.innerHTML="<p style='margin-left: 275px;'>*手机号不能为空</p>"
		phoneSpan.style.color="red";
		return false;
	}

	else if (reg.test(phone)) {
		phoneSpan.innerHTML="<p style='margin-left: 275px;'>*手机号输入正确</p>"
		phoneSpan.style.color="green";
		return true;
	}

	else {
		phoneSpan.innerHTML="<p style='margin-left: 275px;'>*手机号格式不同</p>"
		phoneSpan.style.color="red";
		return false;
	}
}

function checkage() {
	var age=document.getElementById('age').value;
	var ageSpan=document.getElementById("ageSpan");
	var reg=/^(0|[1-9][0-9]*)$/;

	if (ageSpan==""|| ageSpan==null) {
		ageSpan.innerHTML="<p style='margin-left: 300px;'>*年龄不可为空</p>"
		ageSpan.style.color="red";
		return false;
	}

	else if (reg.test(age)) {
		ageSpan.innerHTML="<p style='margin-left: 310px;'>*年龄正确</p>"
		ageSpan.style.color="green";
		return true;
	}

	else {
		ageSpan.innerHTML="<p style='margin-left: 285px;'>*年龄格式不同</p>"
		ageSpan.style.color="red";
		return false;
	}

}

function checkSub() {
	if (checkUname() && checkPwd() && checkPwd2() && checkPhone() && checkage()) {
		return true;
	}

	else {
		alert("提交失败");
		return false;
	}
}
