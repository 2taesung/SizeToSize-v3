import axios from 'axios'
import VueCookies from 'vue-cookies'


const kakaoHeader = {
    'Authorization': 'ddb282e9e9a5e2bb7d96c93b41bf21a4',
    'Content-type': 'application/x-www-form-urlencoded;charset=utf-8',
};

const getKakaoToken = async (code) => {
    console.log('loginWithKakao');
    try {
        const data = {
            grant_type: 'authorization_code',
            client_id: '7f388f87a53c908f562ab8cf34456a7e',
            redirect_uri: 'http://localhost:8080/home',
            code: code,
        };
        const queryString = Object.keys(data)
            .map(k => encodeURIComponent(k) + '=' + encodeURIComponent(data[k]))
            .join('&');

        console.log(queryString)
        console.log(('https://kauth.kakao.com/oauth/token', queryString, { headers: kakaoHeader }))
        const result = await axios.post(`https://kauth.kakao.com/oauth/token`, queryString, { headers: kakaoHeader });
        // const result = await axios.post(`https://kauth.kakao.com/oauth/token?grant_type=authorization_code&client_id=${data.client_id}&redirect_uri=${data.redirect_uri}&code=${data.code}`);
        console.log('카카오 토큰', queryString);
        console.log(result)
        return result;
    } catch (e) {
        return e;
    }
};

const refreshToken = async () => {
    try {
        const { result } = (await axios.get('/refreshToken')).data;
        VueCookies.set('access-token', result.access_token);
        console.log('Refresh API 성공', result);
        return result;
    } catch (e) {
        console.log(e);
    }
}

export {
    getKakaoToken,
    refreshToken,
};