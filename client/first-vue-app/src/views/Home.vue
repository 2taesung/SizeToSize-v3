<template>
  <div class="home">
    <HelloWorld/>
  </div>
</template>

<script>
// @ is an alias to /src
import HelloWorld from '@/components/HelloWorld.vue'
import { getKakaoToken } from '@/services/login'

export default {
  name: 'Home',
  components: {
    HelloWorld
  },
  created() {
    if (this.$route.query.code) {
        this.setKakaoToken();
    }
  },
  methods: {
    async setKakaoToken () {
        console.log('카카오 인증 코드', this.$route.query.code);
        const { data } = await getKakaoToken(this.$route.query.code);
        if (data.error) {
            alert('카카오톡 로그인 오류입니다.');
            this.$router.replace('/login');
            return;
        }
        // window.Kakao.Auth.setAccessToken(data.access_token);
        // this.$cookies.set('access-token', data.access_token, '1d');
        // this.$cookies.set('refresh-token', data.refresh_token, '1d');
        // await this.setUserInfo();
        // this.$router.replace('/');
    },
  }
}

</script>
