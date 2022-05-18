window.onload = function() {
	var a = document.querySelectorAll('dd');
	var b = document.querySelectorAll("dt");
	// a[0].style.backgroundColor = '#6da3a3';
	// for (var i = 0; i < a.length; i++) {
	// 	a[i].onclick = function() {
	// 		for (var i = 0; i < a.length; i++) {
	// 			a[i].style.backgroundColor = '';
	// 			b[i].style.display='none';
	// 		}
	// 		b[i].style.display='inline';
	// 		this.style.backgroundColor = '#6da3a3';
	// 	}
	// }
	for(var i = 0; i<a.length;i++){
	    a[i].onclick=function(){
		for(var j = 0; j < a.length; j++){
			    a[j].style.backgroundColor = '';
			    b[j].style.display='none';
		    }
		    this.style.backgroundColor = '#8ea4f8';
		    b[i].style.display='inline';
	    }
	}

	a[0].onclick=function(){
		for(var i = 0; i < a.length; i++){
			a[i].style.backgroundColor = '';
			b[i].style.display='none';
		}
		this.style.backgroundColor = '#8ea4f8';
		b[0].style.display='inline';
	}
	a[1].onclick=function(){
		for(var i = 0; i < a.length; i++){
			a[i].style.backgroundColor = '';
			b[i].style.display='none';
		}
		this.style.backgroundColor = '#8ea4f8';
		b[1].style.display='inline';
	}
	a[2].onclick=function(){
		for(var i = 0; i < a.length; i++){
			a[i].style.backgroundColor = '';
			b[i].style.display='none';
		}
		this.style.backgroundColor = '#8ea4f8';
		b[2].style.display='inline';
	}
	a[3].onclick=function(){
		for(var i = 0; i < a.length; i++){
			a[i].style.backgroundColor = '';
			b[i].style.display='none';
		}
		this.style.backgroundColor = '#8ea4f8';
		b[3].style.display='inline';
	}
	a[4].onclick=function(){
		for(var i = 0; i < a.length; i++){
			a[i].style.backgroundColor = '';
			b[i].style.display='none';
		}
		this.style.backgroundColor = '#8ea4f8';
		b[4].style.display='inline';
	}
	a[5].onclick=function(){
		for(var i = 0; i < a.length; i++){
			a[i].style.backgroundColor = '';
			b[i].style.display='none';
		}
		this.style.backgroundColor = '#8ea4f8';
		b[5].style.display='inline';
	}
	a[6].onclick=function(){
		for(var i = 0; i < a.length; i++){
			a[i].style.backgroundColor = '';
			b[i].style.display='none';
		}
		this.style.backgroundColor = '#8ea4f8';
		b[6].style.display='inline';
	}
	a[7].onclick=function(){
		for(var i = 0; i < a.length; i++){
			a[i].style.backgroundColor = '';
			b[i].style.display='none';
		}
		this.style.backgroundColor = '#8ea4f8';
		b[7].style.display='inline';
	}
	a[8].onclick=function(){
		for(var i = 0; i < a.length; i++){
			a[i].style.backgroundColor = '';
			b[i].style.display='none';
		}
		this.style.backgroundColor = '#8ea4f8';
		b[8].style.display='inline';
	}
}
