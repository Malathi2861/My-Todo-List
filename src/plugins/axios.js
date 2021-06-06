import Vue from 'vue';
import axios from 'axios';
import VueAxios from 'vue-axios';
import VueProgressBar from 'vue-progressbar';
// import router from '../router';

const options = {
    color: '#00cc00',
    failedColor: '#ff3300',
    thickness: '5px',
    transition: {
        speed: '0.2s',
        opacity: '0.6s',
        termination: 300,
    },
    autoRevert: true,
    location: 'top',
    inverse: false
};


Vue.use(VueAxios, axios);
Vue.use(VueProgressBar, options);
Vue.axios.defaults.baseURL = `${process.env.VUE_APP_DEV}`;
console.log(process.env.VUE_APP_DEV);
// Vue.router = router;

axios.interceptors.request.use((config) => {
    // router.app.$Progress.start();
    return config;
}, (error) => {
    // router.app.$Progress.fail();
    return Promise.reject(error);
});
axios.interceptors.response.use((response) => {
    // router.app.$Progress.finish();
    return response;
}, (error) => {
    // router.app.$Progress.fail();
    return Promise.reject(error);
});

