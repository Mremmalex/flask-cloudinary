const form = document.querySelector("form");


form.addEventListener("submit", (e) => {
	e.preventDefault();
	const formdata = new FormData(form);

	// using ajax to send in forma data


	// let request = new XMLHttpRequest();
	// request.onload = function (){
	// 	if(this.status === 200) {
	// 		let response = this.response
	// 		console.log(response);
	// 	}
	// }
	// request.open('POST',"http://localhost:5000/product", true);
	// request.send(formdata)
	// console.log(request.response);


	//using the fetch api for sending in data 
	fetch("http://localhost:5000/product", {
		method:"POST",
		mode: "no-cors",
		body: formdata
	})
	.then(res =>res.Text)
	.then(data => data)

});