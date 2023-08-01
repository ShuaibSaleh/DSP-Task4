// var image1 = document.getElementById("image1"); 
// image1.src = "/static/img/image1.jpg";  
// image1.classList.remove("hidden");
// var image2 = document.getElementById("image1"); 
// image2.src = "/static/img/image2.jpg";   
// image2.classList.remove("hidden");

const image_input_1 = document.querySelector("#file1");
const image_input_2 = document.querySelector("#file2");

var uploaded_img_1 = "";
var uploaded_img_2 = "";

image_input_1.addEventListener("change", function(){
    const reader = new FileReader();
    reader.addEventListener("load", () =>{
        uploaded_img_1 = reader.result;
        const img1= document.querySelector("#img1");
        img1.src = uploaded_img_1
    })
    reader.readAsDataURL(this.files[0]);
});

image_input_2.addEventListener("change", function(){
    const reader = new FileReader();
    reader.addEventListener("load", () =>{
        uploaded_img_2 = reader.result;
        const img2 = document.querySelector("#img2");
        img2.src = uploaded_img_2
    })
    reader.readAsDataURL(this.files[0]);
    console.log(this.files)

});

