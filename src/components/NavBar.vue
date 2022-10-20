<template>
    <nav class="navbar" role="navigation" aria-label="main navigation">
  <div class="navbar-brand">
    <router-link to="/" class="navbar-item" href="../index.html">
      <img src="@/assets/RD_logo.png">
    </router-link>
    <a role="button" class="navbar-burger" aria-label="menu" aria-expanded="false" data-target="navbarBasicExample">
      <span aria-hidden="true"></span>
      <span aria-hidden="true"></span>
      <span aria-hidden="true"></span>
    </a>
  </div>
  <div id="navbarBasicExample" class="navbar-menu">
    <div class="navbar-start">
      <router-link to="/" class="navbar-item" href="../index.html">
        <p>
			메인
		  </p>
      </router-link>
      <router-link to="/introduce" class="navbar-item">
		  <p>
			소개
		  </p>
      </router-link>
      <router-link to="/personality-tests" class="navbar-item">
		  <p>
			심리테스트
		  </p>
      </router-link>
	  <router-link to="/chatbot" class="navbar-item">
        <p>
			챗봇 심리테스트	
		</p>
      </router-link>
    </div>
    <div class="navbar-end">
    </div>
  </div>
</nav>
</template>

<style lang="css" src="@/css/bulma.css" scoped>
</style>

<script>
document.addEventListener('DOMContentLoaded', () => {

// Get all "navbar-burger" elements
const $navbarBurgers = Array.prototype.slice.call(document.querySelectorAll('.navbar-burger'), 0);

// Add a click event on each of them
$navbarBurgers.forEach( el => {
  el.addEventListener('click', () => {

    // Get the target from the "data-target" attribute
    const target = el.dataset.target;
    const $target = document.getElementById(target);

    // Toggle the "is-active" class on both the "navbar-burger" and the "navbar-menu"
    el.classList.toggle('is-active');
    $target.classList.toggle('is-active');

  });
});

});
export default {
    name: 'NavBar',
}
</script>