// const productImages = document.querySelectorAll(".product-images img");
// const productImageSlide = document.querySelector(".image-slider");

// let activeImageSlide = 0;

// productImages.forEach((item, i) => {
//   item.addEventListener("click", () => {
//     productImages[activeImageSlide].classList.remove("active");
//     item.classList.add("active");
//     activeImageSlide = i;
//     productImageSlide.style.backgroundImage = `url("${item.src}")`;
//   });
// });

// // size selection part
// const sizeBtns = document.querySelectorAll(".size-radio-btn");
// let checkedBtn = 0;
// sizeBtns.forEach((item, i) => {
//   item.addEventListener("click", () => {
//     sizeBtns[checkedBtn].classList.remove("check");
//     item.classList.add("check");
//     checkedBtn = i;
//   });
// });

const activeImg = document.querySelector(".active-img")
const smallImgArray = document.querySelectorAll(".small-img")

smallImgArray.forEach(item => {
  item.addEventListener("click", () => {
    activeImg.srt = item.src
  })
})
