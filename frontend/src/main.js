import Vue from 'vue'
import App from './App.vue'
import vuetify from './plugins/vuetify'

Vue.config.productionTip = false

new Vue({
  vuetify,
  render: h => h(App)
}).$mount('#app')


// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import { getAnalytics } from "firebase/analytics";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: "AIzaSyBqw-_4pLOOAMArM8k6Iqla37aWk1T3enY",
  authDomain: "flaskonheroku.firebaseapp.com",
  projectId: "flaskonheroku",
  storageBucket: "flaskonheroku.appspot.com",
  messagingSenderId: "644162721537",
  appId: "1:644162721537:web:ed2cfbd05bb5919e706d00",
  measurementId: "G-80ZC9Y9D9H",
  databaseURL : "https://post_text.asia-northeast3.firebaseio.com"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const analytics = getAnalytics(app);