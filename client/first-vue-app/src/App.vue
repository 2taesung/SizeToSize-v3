<template>
  <div id="app">
    <div id="nav">
      <router-link to="/signup">signup</router-link>
    </div>
    <img src="@/assets/logo.png" alt="">
    <br>
    <router-view/>
    <button v-on:click="kakaoLogin"><img src="http://gi.esmplus.com/buybye1/page/kakao-login.png" style="height:60px;width:auto;"></button>
  </div>
</template>

<script src="https://developers.kakao.com/sdk/js/kakao.js"></script>
<script>
// import axios from 'axios'
import HelloWorld from './components/HelloWorld.vue'

export default {
  name: 'App',
  component: {
    HelloWorld,
  },
  methods: {
    kakaoLogin() {
      const params = {
        redirectUri:'http://localhost:8080/home',
      }
      window.Kakao.Auth.authorize(params)
      
    }
  },

}

</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}
</style>
