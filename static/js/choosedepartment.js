window.onload = function() {
	var a = document.querySelectorAll('dd');
	var b = document.querySelectorAll("dt");
	 a[0].style.backgroundColor = '#6da3a3';
	 for (let i = 0; i < a.length; i++) {
	 	a[i].onclick = function() {
	 		for (let j = 0; j < a.length; j++) {
	 			a[j].style.backgroundColor = '';
	 			b[j].style.display='none';
	 		}
	 		b[i].style.display='inline';
	 		this.style.backgroundColor = '#6da3a3';
	 	}
	 }

}
