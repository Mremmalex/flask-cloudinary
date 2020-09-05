const div = document.querySelector("#container")




fetch("http://localhost:5000/product")
.then(res => res.json())
.then(data => {
	let products = data.output
	products.forEach((product) => {
		// console.log(product);
		const ul = document.createElement('ul')
		const li = document.createElement('li')
		const img = document.createElement('img')
		img.src = product[2]

		const h2 = document.createElement('h2')
		h2.textContent = product[1]
		li.appendChild(img)
		li.appendChild(h2)
		ul.appendChild(li)
		div.appendChild(ul)
	})
})