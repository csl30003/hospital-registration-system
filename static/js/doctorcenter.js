window.onload = function() {
	var em = document.querySelector('em');
	var date = new Date();
	var h = date.getHours();
	if (h < 11) {
		em.innerHTML = '上午好：';
	} else if (h < 18) {
		em.innerHTML = '下午好：';
	} else {
		em.innerHTML = '晚上好：';
	}
}
