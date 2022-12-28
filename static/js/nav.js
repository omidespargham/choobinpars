// const createNav = () => {
//   let nav = document.querySelector(".navbar");

//   nav.innerHTML = `
//   <div class="nav">
//     <img src="img/dark-logo.png" class="brand-logo" alt="logo">
//     <div class="nav-items">
//       <div class="search">
//         <input type="text" class="search-box" placeholder="search brand, product">
//         <button class="search-btn">search</button>
//       </div>
//       <a href="#"><img src="img/user.png" alt=""></a>
//       <a href="#"><img src="img/cart.png" alt=""></a>
//     </div>
//   </div>
//   <ul class="links-container">
//     <li class="link-item"><a href="#" class="link">home</a></li>
//     <li class="link-item"><a href="#" class="link">women</a></li>
//     <li class="link-item"><a href="#" class="link">men</a></li>
//     <li class="link-item"><a href="#" class="link">kids</a></li>
//     <li class="link-item"><a href="#" class="link">accessories</a></li>
//   </ul>
//   `;
// };

// createNav();


// document.getElementById("user-logo").addEventListener("click", async () => {
//   const { value: email } = await Swal.fire({
//     title: "شماره موبایل تان را وارد کنید",
//     input: "text",
//     inputPlaceholder: "09127095028",
//   });

//   if (email) {
//     Swal.fire(`شماره موبایل شما: ${email}`);
//   }
// });


document.querySelector(".hamburger-icon").addEventListener("click", () => {
    document.querySelector(".menu").classList.toggle("responsive")
})
  
// modal part here
const modal = document.querySelector(".modal");
const trigger = document.querySelector(".trigger");
const closeButton = document.querySelector(".close-button");

function toggleModal() {
  modal.classList.toggle("show-modal");
}

function windowOnClick(event) {
    if (event.target === modal) {
        toggleModal();
    }
}

trigger.addEventListener("click", toggleModal);
closeButton.addEventListener("click", toggleModal);
window.addEventListener("click", windowOnClick);
